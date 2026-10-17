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
    "contact_label":   "Kirim Email",
    "alamat":          "Balai Kelurahan Podorejo, Kec. Ngaliyan, Kota Semarang",
    "email":           "ppkosglpgsdunnes@gmail.com",
    "instagram_url":   "https://instagram.com/ppko_sglpgsdunnes",
    "youtube_url":     "",
    "last_updated":    "17 Oktober 2026",
    "logo_unnes_url":  "/static/images/logo-unnes.svg",
    "logo_pgsd_url":   "/static/images/logo-pgsd.svg",
    "logo_kelurahan_url": "/static/images/logo-kelurahan.svg",
    "smtp_host":       "",
    "smtp_port":       "587",
    "smtp_username":   "",
    "smtp_password":   "",
    "smtp_use_tls":    "true",
    "email_to":        "",
    "gmap_embed_url":  "https://www.google.com/maps?q=Balai+Kelurahan+Podorejo+Semarang&output=embed",
}

# Label untuk form admin settings
SETTING_KEYS = [
    ("nama_site",       "Nama Website"),
    ("tagline_site",    "Tagline / Slogan"),
    ("contact_label",   "Label Tombol Kontak"),
    ("alamat",          "Alamat Lokasi"),
    ("email",           "Email Kontak Utama"),
    ("instagram_url",   "Link Instagram"),
    ("youtube_url",     "Link YouTube Program"),
    ("last_updated",    "Pembaruan Terakhir (teks)"),
    ("logo_unnes_url",  "URL Logo UNNES"),
    ("logo_pgsd_url",   "URL Logo PGSD"),
    ("logo_kelurahan_url", "URL Logo Kelurahan"),
    ("smtp_host",       "SMTP Host"),
    ("smtp_port",       "SMTP Port"),
    ("smtp_username",   "SMTP Username / Email Pengirim"),
    ("smtp_password",   "SMTP Password / App Password"),
    ("smtp_use_tls",    "SMTP Use TLS (true/false)"),
    ("email_to",        "Email Tujuan Form Kontak (opsional)"),
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
            row = db.query(models.SiteSettings).filter(models.SiteSettings.key == key).first()
            if not row:
                db.add(models.SiteSettings(key=key, value=value))
                continue

            # Normalize legacy placeholders so contact and map remain usable
            # on older databases that were seeded before defaults changed.
            if key == "email" and not (row.value or "").strip():
                row.value = value
            if key == "gmap_embed_url" and "0x0%3A0x0" in (row.value or ""):
                row.value = value
        db.commit()
    finally:
        db.close()
