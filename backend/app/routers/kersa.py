from math import ceil

from fastapi import APIRouter, Request, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Artikel
from app.jinja import templates

router = APIRouter()

ITEMS_PER_PAGE = 10


def paginate_query(query, page: int):
    total_items = query.count()
    total_pages = max(1, ceil(total_items / ITEMS_PER_PAGE))
    current_page = min(page, total_pages)
    items = query.offset((current_page - 1) * ITEMS_PER_PAGE).limit(ITEMS_PER_PAGE).all()
    return items, total_items, current_page, total_pages


@router.get("/pojok-literasi/kersa", name="kersa")
def kersa_page(
    request: Request,
    db: Session = Depends(get_db),
    kesehatan_page: int = Query(1, ge=1),
    keterampilan_page: int = Query(1, ge=1),
):
    kesehatan_query = db.query(Artikel).filter(Artikel.kategori == "artikel-kersa-kesehatan")
    keterampilan_query = db.query(Artikel).filter(Artikel.kategori == "artikel-kersa-keterampilan")
    artikel_kesehatan, artikel_kesehatan_total, artikel_kesehatan_current, artikel_kesehatan_total_pages = paginate_query(kesehatan_query, kesehatan_page)
    artikel_keterampilan, artikel_keterampilan_total, artikel_keterampilan_current, artikel_keterampilan_total_pages = paginate_query(keterampilan_query, keterampilan_page)
    return templates.TemplateResponse(request, "kersa.html", {
        "artikel_kesehatan": artikel_kesehatan,
        "artikel_kesehatan_total": artikel_kesehatan_total,
        "artikel_kesehatan_current": artikel_kesehatan_current,
        "artikel_kesehatan_total_pages": artikel_kesehatan_total_pages,
        "artikel_keterampilan": artikel_keterampilan,
        "artikel_keterampilan_total": artikel_keterampilan_total,
        "artikel_keterampilan_current": artikel_keterampilan_current,
        "artikel_keterampilan_total_pages": artikel_keterampilan_total_pages,
    })


@router.get("/pojok-literasi/kersa/kesehatan/{item_id}", name="kersa_detail_kesehatan")
def kersa_detail_kesehatan(request: Request, item_id: int, db: Session = Depends(get_db)):
    item = db.query(Artikel).filter(Artikel.id == item_id, Artikel.kategori == "artikel-kersa-kesehatan").first()
    if not item:
        raise HTTPException(status_code=404, detail="Artikel tidak ditemukan")
    return templates.TemplateResponse(request, "program_detail.html", {
        "page_title": "Detail Artikel Kesehatan Kersa Ngrembaka",
        "back_url": "/pojok-literasi/kersa",
        "section_label": "Kersa Ngrembaka",
        "detail_label": "Artikel Kesehatan",
        "item": item,
        "media_type": "artikel",
    })


@router.get("/pojok-literasi/kersa/keterampilan/{item_id}", name="kersa_detail_keterampilan")
def kersa_detail_keterampilan(request: Request, item_id: int, db: Session = Depends(get_db)):
    item = db.query(Artikel).filter(Artikel.id == item_id, Artikel.kategori == "artikel-kersa-keterampilan").first()
    if not item:
        raise HTTPException(status_code=404, detail="Artikel tidak ditemukan")
    return templates.TemplateResponse(request, "program_detail.html", {
        "page_title": "Detail Artikel Keterampilan Kersa Ngrembaka",
        "back_url": "/pojok-literasi/kersa",
        "section_label": "Kersa Ngrembaka",
        "detail_label": "Artikel Keterampilan",
        "item": item,
        "media_type": "artikel",
    })
