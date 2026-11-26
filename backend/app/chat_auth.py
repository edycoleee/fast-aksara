from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException, Request, status
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import ChatUser
from app.security import ALGORITHM, SECRET_KEY, pwd_context

CHAT_TOKEN_COOKIE = "chat_token"
CHAT_TOKEN_EXPIRE_HOURS = 8


def create_chat_token(username: str) -> str:
    expire = datetime.utcnow() + timedelta(hours=CHAT_TOKEN_EXPIRE_HOURS)
    return jwt.encode(
        {"sub": username, "scope": "chat", "exp": expire},
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def get_chat_username(request: Request) -> Optional[str]:
    token = request.cookies.get(CHAT_TOKEN_COOKIE)
    if not token:
        return None
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return None
    if payload.get("scope") != "chat":
        return None
    return payload.get("sub")


def get_current_chat_user(
    request: Request,
    db: Session = Depends(get_db),
) -> Optional[ChatUser]:
    username = get_chat_username(request)
    if not username:
        return None
    return (
        db.query(ChatUser)
        .filter(ChatUser.username == username, ChatUser.is_active.is_(True))
        .first()
    )


def require_chat_user(
    user: Optional[ChatUser] = Depends(get_current_chat_user),
) -> ChatUser:
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Silakan login untuk membuka chat.",
        )
    return user


def authenticate_chat_user(db: Session, username: str, password: str) -> Optional[ChatUser]:
    user = (
        db.query(ChatUser)
        .filter(ChatUser.username == username, ChatUser.is_active.is_(True))
        .first()
    )
    if not user or not pwd_context.verify(password, user.hashed_password):
        return None
    return user
