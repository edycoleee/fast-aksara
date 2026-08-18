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


@router.get("/pojok-literasi/cakra", name="cakra")
def cakra_page(request: Request, db: Session = Depends(get_db), artikel_page: int = Query(1, ge=1)):
    artikel_query = db.query(Artikel).filter(Artikel.kategori == "artikel-cakra")
    artikel, artikel_total, artikel_current, artikel_total_pages = paginate_query(artikel_query, artikel_page)
    return templates.TemplateResponse(request, "cakra.html", {
        "artikel": artikel,
        "artikel_total": artikel_total,
        "artikel_current": artikel_current,
        "artikel_total_pages": artikel_total_pages,
    })


@router.get("/pojok-literasi/cakra/artikel/{item_id}", name="cakra_detail_artikel")
def cakra_detail_artikel(request: Request, item_id: int, db: Session = Depends(get_db)):
    item = db.query(Artikel).filter(Artikel.id == item_id, Artikel.kategori == "artikel-cakra").first()
    if not item:
        raise HTTPException(status_code=404, detail="Artikel tidak ditemukan")
    return templates.TemplateResponse(request, "program_detail.html", {
        "page_title": "Detail Artikel Cakra Ngrembaka",
        "back_url": "/pojok-literasi/cakra",
        "section_label": "Cakra Ngrembaka",
        "detail_label": "Artikel",
        "item": item,
        "media_type": "artikel",
    })
