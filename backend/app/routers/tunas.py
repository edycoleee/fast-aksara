from math import ceil

from fastapi import APIRouter, Request, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Dokumentasi, Artikel
from app.jinja import templates

router = APIRouter()

ITEMS_PER_PAGE = 10


def paginate_query(query, page: int):
    total_items = query.count()
    total_pages = max(1, ceil(total_items / ITEMS_PER_PAGE))
    current_page = min(page, total_pages)
    items = query.offset((current_page - 1) * ITEMS_PER_PAGE).limit(ITEMS_PER_PAGE).all()
    return items, total_items, current_page, total_pages


@router.get("/pojok-literasi/tunas", name="tunas")
def tunas_page(
    request: Request,
    db: Session = Depends(get_db),
    dokumentasi_page: int = Query(1, ge=1),
    artikel_page: int = Query(1, ge=1),
):
    dokumentasi_query = db.query(Dokumentasi).filter(Dokumentasi.kategori == "dokumentasi-tunas")
    artikel_query = db.query(Artikel).filter(Artikel.kategori == "artikel-tunas")
    dokumentasi, dokumentasi_total, dokumentasi_current, dokumentasi_total_pages = paginate_query(dokumentasi_query, dokumentasi_page)
    artikel, artikel_total, artikel_current, artikel_total_pages = paginate_query(artikel_query, artikel_page)
    return templates.TemplateResponse(request, "tunas.html", {
        "dokumentasi": dokumentasi,
        "dokumentasi_total": dokumentasi_total,
        "dokumentasi_current": dokumentasi_current,
        "dokumentasi_total_pages": dokumentasi_total_pages,
        "artikel": artikel,
        "artikel_total": artikel_total,
        "artikel_current": artikel_current,
        "artikel_total_pages": artikel_total_pages,
    })


@router.get("/pojok-literasi/tunas/dokumentasi/{item_id}", name="tunas_detail_dokumentasi")
def tunas_detail_dokumentasi(request: Request, item_id: int, db: Session = Depends(get_db)):
    item = db.query(Dokumentasi).filter(Dokumentasi.id == item_id, Dokumentasi.kategori == "dokumentasi-tunas").first()
    if not item:
        raise HTTPException(status_code=404, detail="Dokumentasi tidak ditemukan")
    return templates.TemplateResponse(request, "program_detail.html", {
        "page_title": "Detail Dokumentasi Tunas Ngrembaka",
        "back_url": "/pojok-literasi/tunas",
        "section_label": "Tunas Ngrembaka",
        "detail_label": "Dokumentasi",
        "item": item,
        "media_type": "dokumentasi",
    })


@router.get("/pojok-literasi/tunas/artikel/{item_id}", name="tunas_detail_artikel")
def tunas_detail_artikel(request: Request, item_id: int, db: Session = Depends(get_db)):
    item = db.query(Artikel).filter(Artikel.id == item_id, Artikel.kategori == "artikel-tunas").first()
    if not item:
        raise HTTPException(status_code=404, detail="Artikel tidak ditemukan")
    return templates.TemplateResponse(request, "program_detail.html", {
        "page_title": "Detail Artikel Tunas Ngrembaka",
        "back_url": "/pojok-literasi/tunas",
        "section_label": "Tunas Ngrembaka",
        "detail_label": "Artikel",
        "item": item,
        "media_type": "artikel",
    })
