from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import Response
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


@app.get("/robots.txt")
def robots_txt():
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "Sitemap: https://aksara.fun/sitemap.xml\n"
    )
    return Response(content=content, media_type="text/plain; charset=utf-8")


@app.get("/sitemap.xml")
def sitemap_xml():
    urls = [
        "https://aksara.fun/",
        "https://aksara.fun/beranda",
        "https://aksara.fun/profil/ngrembaka-aksara",
        "https://aksara.fun/profil/kelurahan-podorejo",
        "https://aksara.fun/elibrary",
        "https://aksara.fun/pojok-literasi/tunas",
        "https://aksara.fun/pojok-literasi/karya",
        "https://aksara.fun/pojok-literasi/cakra",
        "https://aksara.fun/pojok-literasi/kersa",
    ]
    url_entries = "\n".join(
        f"  <url><loc>{url}</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>"
        for url in urls
    )
    xml = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">
{url_entries}
</urlset>
"""
    return Response(content=xml, media_type="application/xml")


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
