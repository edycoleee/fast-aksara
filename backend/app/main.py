from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database import Base, engine
from app import models  # noqa: F401
from app.jinja import templates
from app.settings import seed_admin, seed_settings, get_setting
from app.routers import (
    landing, beranda, profil_aksara, profil_kelurahan,
    elibrary, tunas, karya, cakra, kersa, admin,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    seed_admin()
    seed_settings()
    templates.env.globals["site"] = get_setting
    yield


app = FastAPI(title="Ngrembaka Aksara", version="1.0.0", lifespan=lifespan)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(landing.router)
app.include_router(beranda.router)
app.include_router(profil_aksara.router)
app.include_router(profil_kelurahan.router)
app.include_router(elibrary.router)
app.include_router(tunas.router)
app.include_router(karya.router)
app.include_router(cakra.router)
app.include_router(kersa.router)
app.include_router(admin.router)
