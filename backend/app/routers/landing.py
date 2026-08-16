from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.jinja import templates

router = APIRouter()


@router.get("/", name="landing")
def landing_page(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse(request, "landing.html")
