from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Dokumentasi
from app.jinja import templates

router = APIRouter()


@router.get("/pojok-literasi/karya", name="karya")
def karya_page(request: Request, db: Session = Depends(get_db)):
    karya_digital = db.query(Dokumentasi).filter(Dokumentasi.kategori == "karya-digital").all()
    karya_sosmed = db.query(Dokumentasi).filter(Dokumentasi.kategori == "karya-media-sosial").all()
    carousel = db.query(Dokumentasi).filter(Dokumentasi.kategori == "gambar-carosel").all()
    return templates.TemplateResponse(request, "karya.html", {
        "karya_digital": karya_digital,
        "karya_sosmed": karya_sosmed,
        "carousel": carousel,
    })
