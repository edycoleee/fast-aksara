import logging
from datetime import datetime, timedelta
from pathlib import Path

from fastapi import APIRouter, Depends, File, Form, HTTPException, Query, Request, UploadFile
from fastapi.responses import FileResponse, RedirectResponse
from pydantic import BaseModel, Field
from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.chat_auth import (
    CHAT_TOKEN_COOKIE,
    authenticate_chat_user,
    create_chat_token,
    get_current_chat_user,
    require_chat_user,
)
from app.database import get_db
from app.jinja import templates
from app.models import ChatConversation, ChatMessage, ChatUser
from app.upload import resolve_private_file, save_chat_attachment

router = APIRouter(prefix="/chat", tags=["chat"])
logger = logging.getLogger(__name__)
ONLINE_WINDOW = timedelta(seconds=30)


class MessageInput(BaseModel):
    content: str = Field(max_length=4000)


class ConversationInput(BaseModel):
    partner_id: int


def participant_ids(conversation: ChatConversation) -> set[int]:
    return {conversation.participant_one_id, conversation.participant_two_id}


def require_conversation(
    db: Session, conversation_id: int, user: ChatUser
) -> ChatConversation:
    conversation = db.query(ChatConversation).filter(
        ChatConversation.id == conversation_id
    ).first()
    if not conversation:
        raise HTTPException(404, "Percakapan tidak ditemukan")
    if user.id not in participant_ids(conversation):
        raise HTTPException(403, "Anda bukan peserta percakapan ini")
    return conversation


def partner_for(db: Session, conversation: ChatConversation, user: ChatUser) -> ChatUser:
    partner_id = (
        conversation.participant_two_id
        if conversation.participant_one_id == user.id
        else conversation.participant_one_id
    )
    partner = db.query(ChatUser).filter(ChatUser.id == partner_id).first()
    if not partner:
        raise HTTPException(404, "Pengguna percakapan tidak ditemukan")
    return partner


def iso_utc(value: datetime | None) -> str | None:
    if value is None:
        return None
    return value.isoformat(timespec="seconds") + "Z"


def is_online(user: ChatUser) -> bool:
    return bool(
        user.last_seen_at
        and datetime.utcnow() - user.last_seen_at <= ONLINE_WINDOW
    )


def message_payload(message: ChatMessage) -> dict:
    attachment = None
    if message.attachment_path:
        attachment = {
            "name": message.attachment_name,
            "type": message.attachment_type,
            "url": f"/chat/api/messages/{message.id}/attachment",
            "preview_url": (
                f"/chat/api/messages/{message.id}/attachment?preview=1"
                if message.attachment_type == "image"
                else None
            ),
        }
    return {
        "id": message.id,
        "sender_id": message.sender_id,
        "content": message.content,
        "attachment": attachment,
        "created_at": iso_utc(message.created_at),
    }


@router.get("/login", name="chat_login")
def login_page(
    request: Request,
    user: ChatUser | None = Depends(get_current_chat_user),
):
    if user:
        return RedirectResponse("/chat", status_code=302)
    return templates.TemplateResponse(request, "chat_login.html", {"error": None})


@router.post("/login")
def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    username = username.strip()
    user = authenticate_chat_user(db, username, password)
    if not user:
        return templates.TemplateResponse(
            request,
            "chat_login.html",
            {"error": "Username atau password salah."},
            status_code=401,
        )
    user.last_seen_at = datetime.utcnow()
    db.commit()
    response = RedirectResponse("/chat", status_code=302)
    response.set_cookie(
        CHAT_TOKEN_COOKIE,
        create_chat_token(user.username),
        httponly=True,
        samesite="lax",
        secure=request.url.scheme == "https",
        max_age=8 * 60 * 60,
    )
    return response


@router.get("/logout")
def logout():
    response = RedirectResponse("/chat/login", status_code=302)
    response.delete_cookie(CHAT_TOKEN_COOKIE)
    return response


@router.get("", name="chat_page")
@router.get("/")
def chat_page(
    request: Request,
    user: ChatUser | None = Depends(get_current_chat_user),
):
    if not user:
        return RedirectResponse("/chat/login", status_code=302)
    return templates.TemplateResponse(
        request,
        "chat.html",
        {"current_user": user},
    )


@router.get("/api/users")
def list_users(
    db: Session = Depends(get_db),
    user: ChatUser = Depends(require_chat_user),
):
    users = (
        db.query(ChatUser)
        .filter(ChatUser.id != user.id, ChatUser.is_active.is_(True))
        .order_by(ChatUser.display_name)
        .all()
    )
    return [
        {
            "id": other.id,
            "display_name": other.display_name,
            "is_online": is_online(other),
        }
        for other in users
    ]


@router.get("/api/conversations")
def list_conversations(
    db: Session = Depends(get_db),
    user: ChatUser = Depends(require_chat_user),
):
    conversations = (
        db.query(ChatConversation)
        .filter(
            or_(
                ChatConversation.participant_one_id == user.id,
                ChatConversation.participant_two_id == user.id,
            )
        )
        .all()
    )
    result = []
    for conversation in conversations:
        partner = partner_for(db, conversation, user)
        last_message = (
            db.query(ChatMessage)
            .filter(ChatMessage.conversation_id == conversation.id)
            .order_by(ChatMessage.id.desc())
            .first()
        )
        result.append({
            "id": conversation.id,
            "partner_id": partner.id,
            "partner_name": partner.display_name,
            "last_message": (
                last_message.content
                if last_message and last_message.content
                else "Lampiran"
                if last_message
                else ""
            ),
            "last_message_at": iso_utc(
                last_message.created_at if last_message else None
            ),
            "is_online": is_online(partner),
            "message_version": conversation.message_version,
        })
    return sorted(
        result,
        key=lambda item: item["last_message_at"] or "",
        reverse=True,
    )


@router.post("/api/conversations", status_code=201)
def create_conversation(
    payload: ConversationInput,
    db: Session = Depends(get_db),
    user: ChatUser = Depends(require_chat_user),
):
    if payload.partner_id == user.id:
        raise HTTPException(400, "Tidak dapat membuat percakapan dengan diri sendiri")
    partner = (
        db.query(ChatUser)
        .filter(ChatUser.id == payload.partner_id, ChatUser.is_active.is_(True))
        .first()
    )
    if not partner:
        raise HTTPException(404, "Pengguna tidak ditemukan")

    first_id, second_id = sorted((user.id, partner.id))
    conversation = (
        db.query(ChatConversation)
        .filter(
            ChatConversation.participant_one_id == first_id,
            ChatConversation.participant_two_id == second_id,
        )
        .first()
    )
    if not conversation:
        conversation = ChatConversation(
            participant_one_id=first_id,
            participant_two_id=second_id,
        )
        db.add(conversation)
        db.commit()
        db.refresh(conversation)
    return {
        "id": conversation.id,
        "partner_id": partner.id,
        "partner_name": partner.display_name,
        "is_online": is_online(partner),
        "message_version": conversation.message_version,
    }


@router.get("/api/conversations/{conversation_id}/messages")
def get_messages(
    conversation_id: int,
    after_id: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: Session = Depends(get_db),
    user: ChatUser = Depends(require_chat_user),
):
    conversation = require_conversation(db, conversation_id, user)
    user.last_seen_at = datetime.utcnow()
    query = db.query(ChatMessage).filter(
        ChatMessage.conversation_id == conversation.id
    )
    messages = (
        query.filter(ChatMessage.id > after_id)
        .order_by(ChatMessage.id.asc())
        .limit(limit)
        .all()
    )
    if not after_id:
        messages = (
            query.order_by(ChatMessage.id.desc())
            .limit(limit)
            .all()
        )[::-1]
    db.commit()
    latest_message = query.order_by(ChatMessage.id.desc()).first()
    return {
        "messages": [message_payload(message) for message in messages],
        "last_message_id": messages[-1].id if messages else latest_message.id if latest_message else 0,
        "message_version": conversation.message_version,
        "server_time": iso_utc(datetime.utcnow()),
    }


@router.post("/api/conversations/{conversation_id}/messages", status_code=201)
def send_message(
    conversation_id: int,
    payload: MessageInput,
    db: Session = Depends(get_db),
    user: ChatUser = Depends(require_chat_user),
):
    conversation = require_conversation(db, conversation_id, user)
    content = payload.content.strip()
    if not content:
        raise HTTPException(400, "Pesan tidak boleh kosong")
    message = ChatMessage(
        conversation_id=conversation.id,
        sender_id=user.id,
        content=content,
    )
    user.last_seen_at = datetime.utcnow()
    db.add(message)
    db.commit()
    db.refresh(message)
    return message_payload(message)


@router.post("/api/conversations/{conversation_id}/attachments", status_code=201)
async def send_attachment(
    conversation_id: int,
    file: UploadFile = File(...),
    content: str = Form(""),
    db: Session = Depends(get_db),
    user: ChatUser = Depends(require_chat_user),
):
    conversation = require_conversation(db, conversation_id, user)
    stored_path, thumbnail_path, attachment_type, _ = await save_chat_attachment(file)
    message = ChatMessage(
        conversation_id=conversation.id,
        sender_id=user.id,
        content=content.strip()[:4000],
        attachment_path=stored_path,
        attachment_thumbnail_path=thumbnail_path,
        attachment_name=Path(file.filename or "lampiran").name,
        attachment_type=attachment_type,
    )
    user.last_seen_at = datetime.utcnow()
    try:
        db.add(message)
        db.commit()
        db.refresh(message)
    except Exception:
        db.rollback()
        for path in (stored_path, thumbnail_path):
            if path:
                try:
                    resolve_private_file(path).unlink()
                except (HTTPException, OSError):
                    logger.exception("Gagal membersihkan lampiran setelah penyimpanan pesan gagal")
        raise
    return message_payload(message)


@router.delete("/api/conversations/{conversation_id}/messages")
def clear_messages(
    conversation_id: int,
    db: Session = Depends(get_db),
    user: ChatUser = Depends(require_chat_user),
):
    conversation = require_conversation(db, conversation_id, user)
    messages = (
        db.query(ChatMessage)
        .filter(ChatMessage.conversation_id == conversation.id)
        .all()
    )
    file_paths = [
        path
        for message in messages
        for path in (
            message.attachment_path,
            message.attachment_thumbnail_path,
        )
        if path
    ]
    for message in messages:
        db.delete(message)
    conversation.message_version += 1
    db.commit()
    for path in file_paths:
        try:
            resolve_private_file(path).unlink()
        except OSError:
            logger.exception("Gagal menghapus lampiran chat")
            raise HTTPException(500, "Riwayat terhapus, tetapi lampiran gagal dibersihkan")
    return {"cleared": True, "conversation_id": conversation.id}


@router.get("/api/messages/{message_id}/attachment")
def get_attachment(
    message_id: int,
    preview: bool = False,
    db: Session = Depends(get_db),
    user: ChatUser = Depends(require_chat_user),
):
    message = db.query(ChatMessage).filter(ChatMessage.id == message_id).first()
    if not message:
        raise HTTPException(404, "Lampiran tidak ditemukan")
    require_conversation(db, message.conversation_id, user)
    if not message.attachment_path:
        raise HTTPException(404, "Pesan ini tidak memiliki lampiran")
    if preview and message.attachment_type != "image":
        raise HTTPException(400, "Preview hanya tersedia untuk gambar")
    path = (
        message.attachment_thumbnail_path
        if preview and message.attachment_thumbnail_path
        else message.attachment_path
    )
    file_path = resolve_private_file(path)
    media_type = (
        "image/webp"
        if preview and message.attachment_thumbnail_path
        else None
    )
    return FileResponse(
        file_path,
        media_type=media_type,
        filename=(
            message.attachment_name
            if not preview and message.attachment_type == "pdf"
            else None
        ),
    )


@router.post("/api/heartbeat")
def heartbeat(
    db: Session = Depends(get_db),
    user: ChatUser = Depends(require_chat_user),
):
    user.last_seen_at = datetime.utcnow()
    db.commit()
    return {"ok": True, "server_time": iso_utc(user.last_seen_at)}
