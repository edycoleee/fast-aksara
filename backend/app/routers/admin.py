from fastapi import APIRouter, Request, Depends, Form, File, UploadFile
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.jinja import templates
from app.models import AdminUser, ELibrary, Dokumentasi, Artikel, SiteSettings
from app.security import create_token, get_current_admin, require_admin, pwd_context
from app.settings import SETTING_KEYS
from app.upload import save_image, save_pdf, delete_file

router = APIRouter(prefix="/admin", tags=["admin"])


# ===== AUTH =====

@router.get("/login", name="admin_login")
def login_page(request: Request):
    if get_current_admin(request):
        return RedirectResponse("/admin", status_code=302)
    return templates.TemplateResponse(request, "admin/login.html", {"error": None})


@router.post("/login")
def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    user = db.query(AdminUser).filter(AdminUser.username == username).first()
    if not user or not pwd_context.verify(password, user.hashed_password):
        return templates.TemplateResponse(request, "admin/login.html", {"error": "Username atau password salah."})
    response = RedirectResponse("/admin", status_code=302)
    response.set_cookie("admin_token", create_token(username), httponly=True, samesite="lax")
    return response


@router.get("/logout")
def logout():
    response = RedirectResponse("/admin/login", status_code=302)
    response.delete_cookie("admin_token")
    return response


# ===== DASHBOARD =====

@router.get("", name="admin_dashboard")
@router.get("/")
def dashboard(request: Request, db: Session = Depends(get_db), admin=Depends(require_admin)):
    return templates.TemplateResponse(request, "admin/dashboard.html", {
        "total_elibrary":    db.query(ELibrary).count(),
        "total_dokumentasi": db.query(Dokumentasi).count(),
        "total_artikel":     db.query(Artikel).count(),
        "admin_user":        admin,
    })


# ===== E-LIBRARY =====

@router.get("/elibrary", name="admin_elibrary")
def elibrary_list(request: Request, db: Session = Depends(get_db), admin=Depends(require_admin)):
    items = db.query(ELibrary).order_by(ELibrary.created_at.desc()).all()
    return templates.TemplateResponse(request, "admin/elibrary_form.html", {"items": items})


@router.post("/elibrary/tambah")
async def elibrary_tambah(
    judul: str = Form(...), kategori: str = Form(...),
    deskripsi: str = Form(""), link: str = Form(""), link_type: str = Form("external"),
    gambar_file: UploadFile = File(None), pdf_file: UploadFile = File(None),
    db: Session = Depends(get_db), admin=Depends(require_admin),
):
    gambar_path = await save_image(gambar_file) if gambar_file and gambar_file.filename else ""
    pdf_path = await save_pdf(pdf_file) if pdf_file and pdf_file.filename else ""
    db.add(ELibrary(
        judul=judul, kategori=kategori, deskripsi=deskripsi,
        link=pdf_path or link,
        link_type="internal" if pdf_path else link_type,
        gambar=gambar_path,
    ))
    db.commit()
    return RedirectResponse("/admin/elibrary", status_code=302)


@router.post("/elibrary/hapus/{item_id}")
def elibrary_hapus(item_id: int, db: Session = Depends(get_db), admin=Depends(require_admin)):
    item = db.query(ELibrary).filter(ELibrary.id == item_id).first()
    if item:
        delete_file(item.gambar)
        delete_file(item.link if item.link_type == "internal" else "")
        db.delete(item)
        db.commit()
    return RedirectResponse("/admin/elibrary", status_code=302)


# ===== DOKUMENTASI =====

@router.get("/dokumentasi", name="admin_dokumentasi")
def dokumentasi_list(request: Request, db: Session = Depends(get_db), admin=Depends(require_admin)):
    items = db.query(Dokumentasi).order_by(Dokumentasi.created_at.desc()).all()
    return templates.TemplateResponse(request, "admin/dokumentasi_form.html", {"items": items})


@router.post("/dokumentasi/tambah")
async def dokumentasi_tambah(
    judul: str = Form(...), kategori: str = Form(...),
    deskripsi: str = Form(""), link_video: str = Form(""),
    gambar_file: UploadFile = File(None),
    db: Session = Depends(get_db), admin=Depends(require_admin),
):
    gambar_path = await save_image(gambar_file) if gambar_file and gambar_file.filename else ""
    db.add(Dokumentasi(judul=judul, kategori=kategori, deskripsi=deskripsi,
                       link_gambar=gambar_path, link_video=link_video))
    db.commit()
    return RedirectResponse("/admin/dokumentasi", status_code=302)


@router.post("/dokumentasi/hapus/{item_id}")
def dokumentasi_hapus(item_id: int, db: Session = Depends(get_db), admin=Depends(require_admin)):
    item = db.query(Dokumentasi).filter(Dokumentasi.id == item_id).first()
    if item:
        delete_file(item.link_gambar)
        db.delete(item)
        db.commit()
    return RedirectResponse("/admin/dokumentasi", status_code=302)


# ===== ARTIKEL =====

@router.get("/artikel", name="admin_artikel")
def artikel_list(request: Request, db: Session = Depends(get_db), admin=Depends(require_admin)):
    items = db.query(Artikel).order_by(Artikel.created_at.desc()).all()
    return templates.TemplateResponse(request, "admin/artikel_form.html", {"items": items})


@router.post("/artikel/tambah")
async def artikel_tambah(
    judul: str = Form(...), kategori: str = Form(...),
    deskripsi: str = Form(""),
    gambar_file: UploadFile = File(None), pdf_file: UploadFile = File(None),
    db: Session = Depends(get_db), admin=Depends(require_admin),
):
    gambar_path = await save_image(gambar_file) if gambar_file and gambar_file.filename else ""
    pdf_path = await save_pdf(pdf_file) if pdf_file and pdf_file.filename else ""
    db.add(Artikel(judul=judul, kategori=kategori, deskripsi=deskripsi,
                   link_pdf=pdf_path, gambar=gambar_path))
    db.commit()
    return RedirectResponse("/admin/artikel", status_code=302)


@router.post("/artikel/hapus/{item_id}")
def artikel_hapus(item_id: int, db: Session = Depends(get_db), admin=Depends(require_admin)):
    item = db.query(Artikel).filter(Artikel.id == item_id).first()
    if item:
        delete_file(item.gambar)
        delete_file(item.link_pdf)
        db.delete(item)
        db.commit()
    return RedirectResponse("/admin/artikel", status_code=302)


# ===== SETTINGS =====

@router.get("/settings", name="admin_settings")
def settings_page(request: Request, db: Session = Depends(get_db), admin=Depends(require_admin)):
    current = {row.key: row.value for row in db.query(SiteSettings).all()}
    return templates.TemplateResponse(request, "admin/settings.html", {
        "settings": current,
        "setting_keys": SETTING_KEYS,
    })


@router.post("/settings/save")
async def settings_save(request: Request, db: Session = Depends(get_db), admin=Depends(require_admin)):
    form = await request.form()
    for key, _ in SETTING_KEYS:
        value = form.get(key, "")
        row = db.query(SiteSettings).filter(SiteSettings.key == key).first()
        if row:
            row.value = value
        else:
            db.add(SiteSettings(key=key, value=value))
    db.commit()
    return RedirectResponse("/admin/settings?saved=1", status_code=302)



# ===== LOGIN =====

@router.get("/login", name="admin_login")
def admin_login_page(request: Request):
    if get_current_admin(request):
        return RedirectResponse("/admin", status_code=302)
    return templates.TemplateResponse(request, "admin/login.html", {"error": None})


@router.post("/login")
def admin_login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    user = db.query(AdminUser).filter(AdminUser.username == username).first()
    if not user or not pwd_context.verify(password, user.hashed_password):
        return templates.TemplateResponse(request, "admin/login.html", {"error": "Username atau password salah."})
    response = RedirectResponse("/admin", status_code=302)
    response.set_cookie("admin_token", create_token(username), httponly=True, samesite="lax")
    return response


@router.get("/logout")
def admin_logout():
    response = RedirectResponse("/admin/login", status_code=302)
    response.delete_cookie("admin_token")
    return response


# ===== DASHBOARD =====

@router.get("", name="admin_dashboard")
@router.get("/")
def admin_dashboard(request: Request, db: Session = Depends(get_db), admin=Depends(require_admin)):
    return templates.TemplateResponse(request, "admin/dashboard.html", {
        "total_elibrary":    db.query(ELibrary).count(),
        "total_dokumentasi": db.query(Dokumentasi).count(),
        "total_artikel":     db.query(Artikel).count(),
        "admin_user":        admin,
    })


# ===== CRUD E-LIBRARY =====

@router.get("/elibrary", name="admin_elibrary")
def admin_elibrary(request: Request, db: Session = Depends(get_db), admin=Depends(require_admin)):
    items = db.query(ELibrary).order_by(ELibrary.created_at.desc()).all()
    return templates.TemplateResponse(request, "admin/elibrary_form.html", {"items": items})


@router.post("/elibrary/tambah")
async def admin_elibrary_tambah(
    request: Request,
    judul: str = Form(...), kategori: str = Form(...),
    deskripsi: str = Form(""), link: str = Form(""),
    link_type: str = Form("external"),
    gambar_file: UploadFile = File(None),
    pdf_file: UploadFile = File(None),
    db: Session = Depends(get_db), admin=Depends(require_admin),
):
    gambar_path = await save_image(gambar_file) if gambar_file and gambar_file.filename else ""
    pdf_path = await save_pdf(pdf_file) if pdf_file and pdf_file.filename else ""
    # pdf upload menggantikan link teks jika ada
    final_link = pdf_path or link
    final_type = "internal" if pdf_path else link_type
    db.add(ELibrary(judul=judul, kategori=kategori, deskripsi=deskripsi,
                    link=final_link, link_type=final_type, gambar=gambar_path))
    db.commit()
    return RedirectResponse("/admin/elibrary", status_code=302)


@router.post("/elibrary/hapus/{item_id}")
def admin_elibrary_hapus(item_id: int, db: Session = Depends(get_db), admin=Depends(require_admin)):
    item = db.query(ELibrary).filter(ELibrary.id == item_id).first()
    if item:
        delete_file(item.gambar)
        delete_file(item.link if item.link_type == "internal" else "")
        db.delete(item)
        db.commit()
    return RedirectResponse("/admin/elibrary", status_code=302)


# ===== CRUD DOKUMENTASI =====

@router.get("/dokumentasi", name="admin_dokumentasi")
def admin_dokumentasi(request: Request, db: Session = Depends(get_db), admin=Depends(require_admin)):
    items = db.query(Dokumentasi).order_by(Dokumentasi.created_at.desc()).all()
    return templates.TemplateResponse(request, "admin/dokumentasi_form.html", {"items": items})


@router.post("/dokumentasi/tambah")
async def admin_dokumentasi_tambah(
    request: Request,
    judul: str = Form(...), kategori: str = Form(...),
    deskripsi: str = Form(""), link_video: str = Form(""),
    gambar_file: UploadFile = File(None),
    db: Session = Depends(get_db), admin=Depends(require_admin),
):
    gambar_path = await save_image(gambar_file) if gambar_file and gambar_file.filename else ""
    db.add(Dokumentasi(judul=judul, kategori=kategori, deskripsi=deskripsi,
                       link_gambar=gambar_path, link_video=link_video))
    db.commit()
    return RedirectResponse("/admin/dokumentasi", status_code=302)


@router.post("/dokumentasi/hapus/{item_id}")
def admin_dokumentasi_hapus(item_id: int, db: Session = Depends(get_db), admin=Depends(require_admin)):
    item = db.query(Dokumentasi).filter(Dokumentasi.id == item_id).first()
    if item:
        delete_file(item.link_gambar)
        db.delete(item)
        db.commit()
    return RedirectResponse("/admin/dokumentasi", status_code=302)


# ===== CRUD ARTIKEL =====

@router.get("/artikel", name="admin_artikel")
def admin_artikel(request: Request, db: Session = Depends(get_db), admin=Depends(require_admin)):
    items = db.query(Artikel).order_by(Artikel.created_at.desc()).all()
    return templates.TemplateResponse(request, "admin/artikel_form.html", {"items": items})


@router.post("/artikel/tambah")
async def admin_artikel_tambah(
    request: Request,
    judul: str = Form(...), kategori: str = Form(...),
    deskripsi: str = Form(""),
    gambar_file: UploadFile = File(None),
    pdf_file: UploadFile = File(None),
    db: Session = Depends(get_db), admin=Depends(require_admin),
):
    gambar_path = await save_image(gambar_file) if gambar_file and gambar_file.filename else ""
    pdf_path = await save_pdf(pdf_file) if pdf_file and pdf_file.filename else ""
    db.add(Artikel(judul=judul, kategori=kategori, deskripsi=deskripsi,
                   link_pdf=pdf_path, gambar=gambar_path))
    db.commit()
    return RedirectResponse("/admin/artikel", status_code=302)


@router.post("/artikel/hapus/{item_id}")
def admin_artikel_hapus(item_id: int, db: Session = Depends(get_db), admin=Depends(require_admin)):
    item = db.query(Artikel).filter(Artikel.id == item_id).first()
    if item:
        delete_file(item.gambar)
        delete_file(item.link_pdf)
        db.delete(item)
        db.commit()
    return RedirectResponse("/admin/artikel", status_code=302)


# ===== SETTINGS =====

SETTING_KEYS = [
    ("nama_site",       "Nama Website"),
    ("tagline_site",    "Tagline / Slogan"),
    ("whatsapp_number", "Nomor WhatsApp (format: 628xxx)"),
    ("whatsapp_label",  "Label Tombol WhatsApp"),
    ("alamat",          "Alamat Lokasi"),
    ("email",           "Email Kontak"),
    ("gmap_embed_url",  "URL Embed Google Maps"),
]


@router.get("/settings", name="admin_settings")
def admin_settings(request: Request, db: Session = Depends(get_db), admin=Depends(require_admin)):
    settings = {row.key: row.value for row in db.query(SiteSettings).all()}
    return templates.TemplateResponse(request, "admin/settings.html", {
        "settings": settings,
        "setting_keys": SETTING_KEYS,
    })


@router.post("/settings")
def admin_settings_save(request: Request, db: Session = Depends(get_db), admin=Depends(require_admin), **kwargs):
    return RedirectResponse("/admin/settings?saved=1", status_code=302)


@router.post("/settings/save")
async def admin_settings_save_post(request: Request, db: Session = Depends(get_db), admin=Depends(require_admin)):
    form = await request.form()
    for key, _ in SETTING_KEYS:
        value = form.get(key, "")
        row = db.query(SiteSettings).filter(SiteSettings.key == key).first()
        if row:
            row.value = value
        else:
            db.add(SiteSettings(key=key, value=value))
    db.commit()
    return RedirectResponse("/admin/settings?saved=1", status_code=302)
