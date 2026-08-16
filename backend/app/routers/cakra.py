from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Artikel
from app.jinja import templates

router = APIRouter()


@router.get("/pojok-literasi/cakra", name="cakra")
def cakra_page(request: Request, db: Session = Depends(get_db)):
    artikel = db.query(Artikel).filter(Artikel.kategori == "artikel-cakra").all()
    return templates.TemplateResponse(request, "cakra.html", {"artikel": artikel})
