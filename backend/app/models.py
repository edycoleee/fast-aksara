from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
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
