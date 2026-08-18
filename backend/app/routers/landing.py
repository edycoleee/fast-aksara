from fastapi import APIRouter, Request, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Artikel, Dokumentasi, ELibrary
from app.jinja import templates

router = APIRouter()


@router.get("/", name="landing")
def landing_page(request: Request, db: Session = Depends(get_db)):
    elibrary_categories = [
        ("modul-pembelajaran", "Modul Pembelajaran"),
        ("ebook", "E-Book"),
        ("buku-cerita", "Buku Cerita"),
        ("buku-literasi-digital", "Literasi Digital"),
        ("buku-keterampilan", "Life Skills"),
    ]
    pojok_categories = [
        ("tunas", "Tunas Ngrembaka"),
        ("karya", "Karya Ngrembaka"),
        ("cakra", "Cakra Ngrembaka"),
        ("kersa", "Kersa Ngrembaka"),
    ]

    def count_items(model, kategori: str) -> int:
        return db.query(func.count(model.id)).filter(model.kategori == kategori).scalar() or 0

    elibrary_counts = {slug: count_items(ELibrary, slug) for slug, _label in elibrary_categories}
    pojok_counts = {
        "tunas": count_items(Dokumentasi, "dokumentasi-tunas") + count_items(Artikel, "artikel-tunas"),
        "karya": (
            count_items(Dokumentasi, "karya-digital")
            + count_items(Dokumentasi, "karya-media-sosial")
            + count_items(Dokumentasi, "gambar-carosel")
        ),
        "cakra": count_items(Artikel, "artikel-cakra"),
        "kersa": count_items(Artikel, "artikel-kersa-kesehatan") + count_items(Artikel, "artikel-kersa-keterampilan"),
    }

    context = {
        "elibrary_counts": elibrary_counts,
        "elibrary_total": sum(elibrary_counts.values()),
        "pojok_counts": pojok_counts,
        "pojok_total": sum(pojok_counts.values()),
    }
    return templates.TemplateResponse(request, "landing.html", context)
