from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text, UniqueConstraint
from app.database import Base


class ELibrary(Base):
    __tablename__ = "elibrary"

    id = Column(Integer, primary_key=True, index=True)
    # modul-pembelajaran | ebook | buku-cerita | buku-literasi-digital | buku-keterampilan
    kategori = Column(String(50), nullable=False, index=True)
    judul = Column(String(255), nullable=False)
    deskripsi = Column(Text, nullable=True)
    link = Column(String(500), nullable=True)
    # external = URL YouTube/web | internal = path file lokal
    link_type = Column(String(10), nullable=False, default="external")
    gambar = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Dokumentasi(Base):
    __tablename__ = "dokumentasi"

    id = Column(Integer, primary_key=True, index=True)
    # dokumentasi-tunas | karya-digital | karya-media-sosial | gambar-carosel
    kategori = Column(String(50), nullable=False, index=True)
    judul = Column(String(255), nullable=False)
    deskripsi = Column(Text, nullable=True)
    link_gambar = Column(String(500), nullable=True)
    link_video = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Artikel(Base):
    __tablename__ = "artikel"

    id = Column(Integer, primary_key=True, index=True)
    # artikel-tunas | artikel-cakra | artikel-kersa-kesehatan | artikel-kersa-keterampilan
    kategori = Column(String(50), nullable=False, index=True)
    judul = Column(String(255), nullable=False)
    deskripsi = Column(Text, nullable=True)
    link_pdf = Column(String(500), nullable=True)
    gambar = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class AdminUser(Base):
    __tablename__ = "admin_user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)


class SiteSettings(Base):
    __tablename__ = "site_settings"

    key = Column(String(100), primary_key=True)
    value = Column(Text, nullable=True, default="")


class ChatUser(Base):
    __tablename__ = "chat_user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    display_name = Column(String(100), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    last_seen_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)


class ChatConversation(Base):
    __tablename__ = "chat_conversation"
    __table_args__ = (
        UniqueConstraint(
            "participant_one_id",
            "participant_two_id",
            name="uq_chat_conversation_participants",
        ),
    )

    id = Column(Integer, primary_key=True, index=True)
    participant_one_id = Column(Integer, ForeignKey("chat_user.id"), nullable=False, index=True)
    participant_two_id = Column(Integer, ForeignKey("chat_user.id"), nullable=False, index=True)
    message_version = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)


class ChatMessage(Base):
    __tablename__ = "chat_message"

    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(
        Integer, ForeignKey("chat_conversation.id"), nullable=False, index=True
    )
    sender_id = Column(Integer, ForeignKey("chat_user.id"), nullable=False, index=True)
    content = Column(Text, nullable=False, default="")
    attachment_path = Column(String(500), nullable=True)
    attachment_thumbnail_path = Column(String(500), nullable=True)
    attachment_name = Column(String(255), nullable=True)
    attachment_type = Column(String(50), nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow, index=True)
