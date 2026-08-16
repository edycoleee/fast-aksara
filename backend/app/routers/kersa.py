from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Artikel
from app.jinja import templates

router = APIRouter()


@router.get("/pojok-literasi/kersa", name="kersa")
def kersa_page(request: Request, db: Session = Depends(get_db)):
    artikel_kesehatan = db.query(Artikel).filter(Artikel.kategori == "artikel-kersa-kesehatan").all()
    artikel_keterampilan = db.query(Artikel).filter(Artikel.kategori == "artikel-kersa-keterampilan").all()
    return templates.TemplateResponse(request, "kersa.html", {
        "artikel_kesehatan": artikel_kesehatan,
        "artikel_keterampilan": artikel_keterampilan,
    })
