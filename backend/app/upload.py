import os
import uuid
from pathlib import Path

from fastapi import HTTPException, UploadFile

UPLOAD_DIR = Path("app/static/uploads")
IMAGE_DIR = UPLOAD_DIR / "images"
PDF_DIR = UPLOAD_DIR / "pdf"

ALLOWED_IMAGE_MIME = {"image/jpeg", "image/png", "image/webp"}
ALLOWED_PDF_MIME = {"application/pdf"}

MAX_IMAGE_MB = int(os.getenv("MAX_UPLOAD_IMAGE_MB", "2"))
MAX_PDF_MB = int(os.getenv("MAX_UPLOAD_PDF_MB", "20"))


def _ext_from_mime(mime: str) -> str:
    return {"image/jpeg": ".jpg", "image/png": ".png", "image/webp": ".webp",
            "application/pdf": ".pdf"}.get(mime, "")


async def _read_and_validate(file: UploadFile, allowed: set, max_mb: int) -> bytes:
    data = await file.read()
    if len(data) > max_mb * 1024 * 1024:
        raise HTTPException(400, f"Ukuran file melebihi {max_mb} MB")

    # Deteksi MIME dari magic bytes (4 byte pertama)
    sig = data[:4]
    mime = file.content_type or ""

    # Fallback deteksi manual via magic bytes jika content_type tidak dipercaya
    if sig[:3] == b"\xff\xd8\xff":
        mime = "image/jpeg"
    elif sig[:4] == b"\x89PNG":
        mime = "image/png"
    elif sig[:4] == b"RIFF" and data[8:12] == b"WEBP":
        mime = "image/webp"
    elif sig[:4] == b"%PDF":
        mime = "application/pdf"

    if mime not in allowed:
        raise HTTPException(400, f"Tipe file tidak diizinkan: {mime}")
    return data, mime


async def save_image(file: UploadFile) -> str:
    """Simpan gambar ke uploads/images/, return path relatif untuk disimpan di DB."""
    if not file or not file.filename:
        return ""
    data, mime = await _read_and_validate(file, ALLOWED_IMAGE_MIME, MAX_IMAGE_MB)
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    filename = uuid.uuid4().hex + _ext_from_mime(mime)
    (IMAGE_DIR / filename).write_bytes(data)
    return f"/static/uploads/images/{filename}"


async def save_pdf(file: UploadFile) -> str:
    """Simpan PDF ke uploads/pdf/, return path relatif untuk disimpan di DB."""
    if not file or not file.filename:
        return ""
    data, mime = await _read_and_validate(file, ALLOWED_PDF_MIME, MAX_PDF_MB)
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    filename = uuid.uuid4().hex + ".pdf"
    (PDF_DIR / filename).write_bytes(data)
    return f"/static/uploads/pdf/{filename}"


def delete_file(path: str) -> None:
    """Hapus file lokal dari disk jika path internal (bukan URL eksternal)."""
    if not path or path.startswith("http"):
        return
    full = Path("app") / path.lstrip("/")
    if full.exists():
        full.unlink()
