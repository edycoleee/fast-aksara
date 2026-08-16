from fastapi import APIRouter, Request
from app.jinja import templates

router = APIRouter()


@router.get("/profil/kelurahan-podorejo", name="profil_kelurahan")
def profil_kelurahan_page(request: Request):
    return templates.TemplateResponse(request, "profil_kelurahan.html")
