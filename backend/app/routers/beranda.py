from fastapi import APIRouter, Request
from app.jinja import templates

router = APIRouter()


@router.get("/beranda", name="beranda")
def beranda_page(request: Request):
    return templates.TemplateResponse(request, "beranda.html")
