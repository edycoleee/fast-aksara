"""
Jalankan sekali (atau kapanpun ingin reset password):
  python seed.py
"""
import os
from dotenv import load_dotenv
from passlib.context import CryptContext
from app.database import SessionLocal, engine, Base
from app import models  # noqa: F401

load_dotenv()

Base.metadata.create_all(bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")

if not ADMIN_PASSWORD:
    print("ERROR: ADMIN_PASSWORD tidak ditemukan di .env")
    exit(1)

db = SessionLocal()

existing = db.query(models.AdminUser).filter(models.AdminUser.username == ADMIN_USERNAME).first()
if existing:
    existing.hashed_password = pwd_context.hash(ADMIN_PASSWORD)
    db.commit()
    print(f"Password akun '{ADMIN_USERNAME}' diperbarui dari .env")
else:
    db.add(models.AdminUser(
        username=ADMIN_USERNAME,
        hashed_password=pwd_context.hash(ADMIN_PASSWORD),
    ))
    db.commit()
    print(f"Akun admin dibuat: username='{ADMIN_USERNAME}'")

db.close()
