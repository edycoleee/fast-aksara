import os
import uuid
from io import BytesIO
from pathlib import Path

from fastapi import HTTPException, UploadFile
from PIL import Image, ImageOps

UPLOAD_DIR = Path("app/static/uploads")
IMAGE_DIR = UPLOAD_DIR / "images"
PDF_DIR = UPLOAD_DIR / "pdf"
CHAT_UPLOAD_DIR = Path("app/private_uploads/chat")

ALLOWED_IMAGE_MIME = {"image/jpeg", "image/png", "image/webp"}
ALLOWED_PDF_MIME = {"application/pdf"}

MAX_IMAGE_MB = int(os.getenv("MAX_UPLOAD_IMAGE_MB", "2"))
MAX_PDF_MB = int(os.getenv("MAX_UPLOAD_PDF_MB", "20"))
MAX_CHAT_IMAGE_MB = 5
MAX_CHAT_PDF_MB = 10


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


async def save_image_resized(file: UploadFile, width: int, height: int) -> str:
    """Simpan gambar yang di-resize agar dimensinya konsisten."""
    if not file or not file.filename:
        return ""

    data, _ = await _read_and_validate(file, ALLOWED_IMAGE_MIME, MAX_IMAGE_MB)

    try:
        image = Image.open(BytesIO(data))
        image = ImageOps.exif_transpose(image)
    except Exception as exc:
        raise HTTPException(400, f"File gambar tidak valid: {exc}") from exc

    # Keep aspect ratio and place image at center on transparent canvas.
    image = image.convert("RGBA")
    resized = ImageOps.contain(image, (width, height), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    offset_x = (width - resized.width) // 2
    offset_y = (height - resized.height) // 2
    canvas.paste(resized, (offset_x, offset_y), resized)

    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    filename = uuid.uuid4().hex + ".png"
    output_path = IMAGE_DIR / filename
    canvas.save(output_path, format="PNG", optimize=True)
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


async def save_chat_attachment(
    file: UploadFile,
) -> tuple[str, str, str, str | None]:
    if not file or not file.filename:
        raise HTTPException(400, "File lampiran wajib dipilih")

    data = await file.read()
    if len(data) > MAX_CHAT_PDF_MB * 1024 * 1024:
        raise HTTPException(400, f"Ukuran file melebihi {MAX_CHAT_PDF_MB} MB")

    mime = ""
    if data.startswith(b"\xff\xd8\xff"):
        mime = "image/jpeg"
    elif data.startswith(b"\x89PNG"):
        mime = "image/png"
    elif data.startswith(b"RIFF") and len(data) >= 12 and data[8:12] == b"WEBP":
        mime = "image/webp"
    elif data.startswith(b"%PDF"):
        mime = "application/pdf"

    if mime not in ALLOWED_IMAGE_MIME | ALLOWED_PDF_MIME:
        raise HTTPException(400, "Lampiran harus berupa JPG, PNG, WebP, atau PDF")

    if mime in ALLOWED_IMAGE_MIME and len(data) > MAX_CHAT_IMAGE_MB * 1024 * 1024:
        raise HTTPException(400, f"Ukuran gambar melebihi {MAX_CHAT_IMAGE_MB} MB")

    CHAT_UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    extension = _ext_from_mime(mime)
    identifier = uuid.uuid4().hex
    stored_path = CHAT_UPLOAD_DIR / f"{identifier}{extension}"
    thumbnail_path = None

    if mime in ALLOWED_IMAGE_MIME:
        try:
            image = Image.open(BytesIO(data))
            image.verify()
            image = Image.open(BytesIO(data))
            image = ImageOps.exif_transpose(image)
            image.thumbnail((560, 560), Image.Resampling.LANCZOS)
            thumb_file = CHAT_UPLOAD_DIR / f"{identifier}_thumb.webp"
            image.convert("RGB").save(thumb_file, format="WEBP", quality=82)
            thumbnail_path = str(thumb_file)
        except Exception as exc:
            raise HTTPException(400, "File gambar tidak valid") from exc
    elif not data.rstrip().endswith(b"%%EOF"):
        raise HTTPException(400, "File PDF tidak valid")

    stored_path.write_bytes(data)
    attachment_type = "image" if mime in ALLOWED_IMAGE_MIME else "pdf"
    return str(stored_path), thumbnail_path, attachment_type, mime


def resolve_private_file(path: str) -> Path:
    base = CHAT_UPLOAD_DIR.resolve()
    file_path = Path(path).resolve()
    if not file_path.is_relative_to(base):
        raise HTTPException(400, "Path lampiran tidak valid")
    if not file_path.is_file():
        raise HTTPException(404, "Lampiran tidak ditemukan")
    return file_path


def delete_file(path: str) -> None:
    """Hapus file lokal dari disk jika path internal (bukan URL eksternal)."""
    if not path or path.startswith("http"):
        return
    full = Path("app") / path.lstrip("/")
    if full.exists():
        full.unlink()
