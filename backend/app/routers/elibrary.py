from math import ceil
from urllib.parse import urlencode

from fastapi import APIRouter, Request, Depends, Query
from fastapi.responses import RedirectResponse
from sqlalchemy import or_
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import ELibrary
from app.jinja import templates

router = APIRouter()

KATEGORI_VALID = {
    "modul-pembelajaran", "ebook", "buku-cerita",
    "buku-literasi-digital", "keterampilan-hidup", "buku-keterampilan",
}

KATEGORI_LABEL = {
    "modul-pembelajaran": "Modul Pembelajaran",
    "ebook": "E-Book",
    "buku-cerita": "Buku Cerita",
    "buku-literasi-digital": "Literasi Digital",
    "keterampilan-hidup": "Keterampilan Hidup",
    "buku-keterampilan": "Keterampilan Hidup",
}

ITEMS_PER_PAGE = 10

AUDIENCE_MAP = {
    "semua": [],
    "anak": ["modul-pembelajaran", "buku-cerita"],
    "remaja": ["ebook", "buku-literasi-digital"],
    "keluarga": ["modul-pembelajaran", "keterampilan-hidup"],
    "umum": [
        "modul-pembelajaran",
        "ebook",
        "buku-cerita",
        "buku-literasi-digital",
        "keterampilan-hidup",
    ],
}


def paginate_query(query, page: int):
    total_items = query.count()
    total_pages = max(1, ceil(total_items / ITEMS_PER_PAGE))
    current_page = min(page, total_pages)
    offset = (current_page - 1) * ITEMS_PER_PAGE
    page_items = query.offset(offset).limit(ITEMS_PER_PAGE).all()
    return page_items, total_items, current_page, total_pages


def canonical_kategori(kategori: str) -> str:
    if kategori == "buku-keterampilan":
        return "keterampilan-hidup"
    return kategori


def kategori_filter_values(kategori: str) -> list[str]:
    if kategori == "keterampilan-hidup":
        return ["keterampilan-hidup", "buku-keterampilan"]
    return [kategori]


def normalize_audience(audience: str) -> str:
    return audience if audience in AUDIENCE_MAP else "semua"


def apply_elibrary_filters(query, q: str, audience: str):
    q = (q or "").strip()
    if q:
        pattern = f"%{q}%"
        query = query.filter(
            or_(
                ELibrary.judul.ilike(pattern),
                ELibrary.deskripsi.ilike(pattern),
            )
        )

    audience = normalize_audience(audience)
    audience_kategori = AUDIENCE_MAP[audience]
    if audience_kategori:
        expanded = []
        for kategori in audience_kategori:
            expanded.extend(kategori_filter_values(kategori))
        query = query.filter(ELibrary.kategori.in_(expanded))

    return query


def build_filter_query(q: str, audience: str) -> tuple[str, str]:
    params = {}
    if (q or "").strip():
        params["q"] = q.strip()
    if audience and audience != "semua":
        params["audience"] = audience
    filter_query = urlencode(params)
    query_suffix = f"&{filter_query}" if filter_query else ""
    return filter_query, query_suffix


@router.get("/elibrary", name="elibrary")
def elibrary_page(
    request: Request,
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    q: str = Query(""),
    audience: str = Query("semua"),
):
    audience = normalize_audience(audience)
    query = db.query(ELibrary)
    query = apply_elibrary_filters(query, q, audience)
    query = query.order_by(ELibrary.created_at.desc())
    items, total_items, current_page, total_pages = paginate_query(query, page)
    filter_query, query_suffix = build_filter_query(q, audience)
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
            "search_q": q,
            "audience": audience,
            "filter_query": filter_query,
            "query_suffix": query_suffix,
        },
    )


@router.get("/elibrary/{kategori}", name="elibrary_kategori")
def elibrary_kategori_page(
    request: Request,
    kategori: str,
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    q: str = Query(""),
    audience: str = Query("semua"),
):
    audience = normalize_audience(audience)
    raw_kategori = kategori
    kategori = canonical_kategori(kategori)

    if raw_kategori == "buku-keterampilan":
        filter_query, _query_suffix = build_filter_query(q, audience)
        target = "/elibrary/keterampilan-hidup"
        if filter_query:
            target = f"{target}?{filter_query}"
        return RedirectResponse(target, status_code=302)

    if kategori not in KATEGORI_VALID:
        return RedirectResponse("/elibrary", status_code=302)

    query = db.query(ELibrary).filter(ELibrary.kategori.in_(kategori_filter_values(kategori)))
    query = apply_elibrary_filters(query, q, audience)
    query = query.order_by(ELibrary.created_at.desc())

    items, total_items, current_page, total_pages = paginate_query(query, page)
    filter_query, query_suffix = build_filter_query(q, audience)
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
            "search_q": q,
            "audience": audience,
            "filter_query": filter_query,
            "query_suffix": query_suffix,
        },
    )
