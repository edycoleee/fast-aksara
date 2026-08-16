from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import ELibrary
from app.jinja import templates

router = APIRouter()

KATEGORI_VALID = {
    "modul-pembelajaran", "ebook", "buku-cerita",
    "buku-literasi-digital", "buku-keterampilan",
}


@router.get("/elibrary", name="elibrary")
def elibrary_page(request: Request, db: Session = Depends(get_db)):
    items = db.query(ELibrary).order_by(ELibrary.created_at.desc()).all()
    return templates.TemplateResponse(request, "elibrary.html", {"items": items})


@router.get("/elibrary/{kategori}", name="elibrary_kategori")
def elibrary_kategori_page(request: Request, kategori: str, db: Session = Depends(get_db)):
    items = db.query(ELibrary).filter(ELibrary.kategori == kategori).order_by(ELibrary.created_at.desc()).all()
    return templates.TemplateResponse(request, "elibrary.html", {"items": items, "aktif_kategori": kategori})
