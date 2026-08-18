from math import ceil

from fastapi import APIRouter, Request, Depends, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import ELibrary
from app.jinja import templates

router = APIRouter()

KATEGORI_VALID = {
    "modul-pembelajaran", "ebook", "buku-cerita",
    "buku-literasi-digital", "buku-keterampilan",
}

KATEGORI_LABEL = {
    "modul-pembelajaran": "Modul Pembelajaran",
    "ebook": "E-Book",
    "buku-cerita": "Buku Cerita",
    "buku-literasi-digital": "Literasi Digital",
    "buku-keterampilan": "Life Skills",
}

ITEMS_PER_PAGE = 10


def paginate_query(query, page: int):
    total_items = query.count()
    total_pages = max(1, ceil(total_items / ITEMS_PER_PAGE))
    current_page = min(page, total_pages)
    offset = (current_page - 1) * ITEMS_PER_PAGE
    page_items = query.offset(offset).limit(ITEMS_PER_PAGE).all()
    return page_items, total_items, current_page, total_pages


@router.get("/elibrary", name="elibrary")
def elibrary_page(request: Request, db: Session = Depends(get_db), page: int = Query(1, ge=1)):
    query = db.query(ELibrary).order_by(ELibrary.created_at.desc())
    items, total_items, current_page, total_pages = paginate_query(query, page)
    return templates.TemplateResponse(
        request,
        "elibrary.html",
        {
            "items": items,
            "total_items": total_items,
            "current_page": current_page,
            "total_pages": total_pages,
            "base_path": "/elibrary",
            "page_label": "Semua Koleksi",
        },
    )


@router.get("/elibrary/{kategori}", name="elibrary_kategori")
def elibrary_kategori_page(
    request: Request,
    kategori: str,
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
):
    query = db.query(ELibrary).filter(ELibrary.kategori == kategori).order_by(ELibrary.created_at.desc())
    items, total_items, current_page, total_pages = paginate_query(query, page)
    return templates.TemplateResponse(
        request,
        "elibrary.html",
        {
            "items": items,
            "total_items": total_items,
            "current_page": current_page,
            "total_pages": total_pages,
            "base_path": f"/elibrary/{kategori}",
            "aktif_kategori": kategori,
            "page_label": KATEGORI_LABEL.get(kategori, kategori.replace("-", " ").title()),
        },
    )
