from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Dokumentasi, Artikel
from app.jinja import templates

router = APIRouter()


@router.get("/pojok-literasi/tunas", name="tunas")
def tunas_page(request: Request, db: Session = Depends(get_db)):
    dokumentasi = db.query(Dokumentasi).filter(Dokumentasi.kategori == "dokumentasi-tunas").all()
    artikel = db.query(Artikel).filter(Artikel.kategori == "artikel-tunas").all()
    return templates.TemplateResponse(request, "tunas.html", {
        "dokumentasi": dokumentasi, "artikel": artikel,
    })
