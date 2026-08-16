import os
from dotenv import load_dotenv
from passlib.context import CryptContext
from app.database import SessionLocal
from app import models

load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

DEFAULT_SETTINGS = {
    "nama_site":       "Ngrembaka Aksara",
    "tagline_site":    "Tumbuh dan berkembangnya ilmu pengetahuan",
    "whatsapp_number": "6281234567890",
    "whatsapp_label":  "Hubungi Kami",
    "alamat":          "Balai Kelurahan Podorejo, Kec. Ngaliyan, Kota Semarang",
    "email":           "",
    "gmap_embed_url":  (
        "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3959.8"
        "!2d110.33!3d-7.01!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1"
        "!3m3!1m2!1s0x0%3A0x0!2zKi4uKg!5e0!3m2!1sid!2sid!4v1"
    ),
}

# Label untuk form admin settings
SETTING_KEYS = [
    ("nama_site",       "Nama Website"),
    ("tagline_site",    "Tagline / Slogan"),
    ("whatsapp_number", "Nomor WhatsApp (format: 628xxx)"),
    ("whatsapp_label",  "Label Tombol WhatsApp"),
    ("alamat",          "Alamat Lokasi"),
    ("email",           "Email Kontak"),
    ("gmap_embed_url",  "URL Embed Google Maps"),
]


def get_setting(key: str, default: str = "") -> str:
    db = SessionLocal()
    try:
        row = db.query(models.SiteSettings).filter(models.SiteSettings.key == key).first()
        return row.value if row else default
    finally:
        db.close()


def seed_admin() -> None:
    username = os.getenv("ADMIN_USERNAME", "admin")
    password = os.getenv("ADMIN_PASSWORD", "")
    if not password:
        return
    db = SessionLocal()
    try:
        exists = db.query(models.AdminUser).filter(models.AdminUser.username == username).first()
        if not exists:
            db.add(models.AdminUser(
                username=username,
                hashed_password=pwd_context.hash(password),
            ))
            db.commit()
    finally:
        db.close()


def seed_settings() -> None:
    db = SessionLocal()
    try:
        for key, value in DEFAULT_SETTINGS.items():
            if not db.query(models.SiteSettings).filter(models.SiteSettings.key == key).first():
                db.add(models.SiteSettings(key=key, value=value))
        db.commit()
    finally:
        db.close()
