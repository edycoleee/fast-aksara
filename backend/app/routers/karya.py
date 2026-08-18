from math import ceil

from fastapi import APIRouter, Request, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Dokumentasi
from app.jinja import templates

router = APIRouter()

ITEMS_PER_PAGE = 10


def paginate_query(query, page: int):
    total_items = query.count()
    total_pages = max(1, ceil(total_items / ITEMS_PER_PAGE))
    current_page = min(page, total_pages)
    items = query.offset((current_page - 1) * ITEMS_PER_PAGE).limit(ITEMS_PER_PAGE).all()
    return items, total_items, current_page, total_pages


@router.get("/pojok-literasi/karya", name="karya")
def karya_page(
    request: Request,
    db: Session = Depends(get_db),
    digital_page: int = Query(1, ge=1),
    sosmed_page: int = Query(1, ge=1),
    carousel_page: int = Query(1, ge=1),
):
    karya_digital_query = db.query(Dokumentasi).filter(Dokumentasi.kategori == "karya-digital")
    karya_sosmed_query = db.query(Dokumentasi).filter(Dokumentasi.kategori == "karya-media-sosial")
    carousel_query = db.query(Dokumentasi).filter(Dokumentasi.kategori == "gambar-carosel")
    karya_digital, karya_digital_total, karya_digital_current, karya_digital_total_pages = paginate_query(karya_digital_query, digital_page)
    karya_sosmed, karya_sosmed_total, karya_sosmed_current, karya_sosmed_total_pages = paginate_query(karya_sosmed_query, sosmed_page)
    carousel, carousel_total, carousel_current, carousel_total_pages = paginate_query(carousel_query, carousel_page)
    return templates.TemplateResponse(request, "karya.html", {
        "karya_digital": karya_digital,
        "karya_digital_total": karya_digital_total,
        "karya_digital_current": karya_digital_current,
        "karya_digital_total_pages": karya_digital_total_pages,
        "karya_sosmed": karya_sosmed,
        "karya_sosmed_total": karya_sosmed_total,
        "karya_sosmed_current": karya_sosmed_current,
        "karya_sosmed_total_pages": karya_sosmed_total_pages,
        "carousel": carousel,
        "carousel_total": carousel_total,
        "carousel_current": carousel_current,
        "carousel_total_pages": carousel_total_pages,
    })


@router.get("/pojok-literasi/karya/digital/{item_id}", name="karya_detail_digital")
def karya_detail_digital(request: Request, item_id: int, db: Session = Depends(get_db)):
    item = db.query(Dokumentasi).filter(Dokumentasi.id == item_id, Dokumentasi.kategori == "karya-digital").first()
    if not item:
        raise HTTPException(status_code=404, detail="Dokumentasi tidak ditemukan")
    return templates.TemplateResponse(request, "program_detail.html", {
        "page_title": "Detail Karya Digital",
        "back_url": "/pojok-literasi/karya",
        "section_label": "Karya Ngrembaka",
        "detail_label": "Karya Digital",
        "item": item,
        "media_type": "dokumentasi",
    })


@router.get("/pojok-literasi/karya/sosmed/{item_id}", name="karya_detail_sosmed")
def karya_detail_sosmed(request: Request, item_id: int, db: Session = Depends(get_db)):
    item = db.query(Dokumentasi).filter(Dokumentasi.id == item_id, Dokumentasi.kategori == "karya-media-sosial").first()
    if not item:
        raise HTTPException(status_code=404, detail="Dokumentasi tidak ditemukan")
    return templates.TemplateResponse(request, "program_detail.html", {
        "page_title": "Detail Karya Media Sosial",
        "back_url": "/pojok-literasi/karya",
        "section_label": "Karya Ngrembaka",
        "detail_label": "Karya Media Sosial",
        "item": item,
        "media_type": "dokumentasi",
    })


@router.get("/pojok-literasi/karya/carousel/{item_id}", name="karya_detail_carousel")
def karya_detail_carousel(request: Request, item_id: int, db: Session = Depends(get_db)):
    item = db.query(Dokumentasi).filter(Dokumentasi.id == item_id, Dokumentasi.kategori == "gambar-carosel").first()
    if not item:
        raise HTTPException(status_code=404, detail="Dokumentasi tidak ditemukan")
    return templates.TemplateResponse(request, "program_detail.html", {
        "page_title": "Detail Carousel Hosting Library",
        "back_url": "/pojok-literasi/karya",
        "section_label": "Karya Ngrembaka",
        "detail_label": "Hosting Library",
        "item": item,
        "media_type": "dokumentasi",
    })
