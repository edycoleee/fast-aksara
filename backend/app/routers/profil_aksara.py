from fastapi import APIRouter, Request
from app.jinja import templates

router = APIRouter()


@router.get("/profil/ngrembaka-aksara", name="profil_aksara")
def profil_aksara_page(request: Request):
    return templates.TemplateResponse(request, "profil_aksara.html")
