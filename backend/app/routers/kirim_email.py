import os
import smtplib
from email.message import EmailMessage

from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse

from app.jinja import templates
from app.settings import get_setting

router = APIRouter()


SMTP_ERROR_MSG = (
    "Layanan email belum dikonfigurasi. "
    "Silakan hubungi admin untuk mengaktifkan SMTP server."
)


def _smtp_config() -> dict:
    host = (get_setting("smtp_host", "") or os.getenv("SMTP_HOST", "")).strip()
    username = (get_setting("smtp_username", "") or os.getenv("SMTP_USERNAME", "")).strip()
    password = (get_setting("smtp_password", "") or os.getenv("SMTP_PASSWORD", "")).strip()

    raw_port = (get_setting("smtp_port", "") or os.getenv("SMTP_PORT", "587")).strip()
    try:
        port = int(raw_port)
    except ValueError:
        port = 587

    raw_tls = (get_setting("smtp_use_tls", "") or os.getenv("SMTP_USE_TLS", "true")).strip().lower()
    use_tls = raw_tls in {"1", "true", "yes", "on"}

    return {
        "host": host,
        "port": port,
        "username": username,
        "password": password,
        "use_tls": use_tls,
    }


def _build_form_state(
    nama: str = "",
    email_pengirim: str = "",
    telepon: str = "",
    instansi: str = "",
    subjek: str = "",
    pesan: str = "",
) -> dict:
    return {
        "nama": nama,
        "email_pengirim": email_pengirim,
        "telepon": telepon,
        "instansi": instansi,
        "subjek": subjek,
        "pesan": pesan,
    }


@router.get("/kirim-email", name="kirim_email")
def kirim_email_page(request: Request):
    sent = request.query_params.get("sent") == "1"
    return templates.TemplateResponse(
        request,
        "kirim_email.html",
        {
            "sent": sent,
            "error": None,
            "form": _build_form_state(),
        },
    )


@router.post("/kirim-email", name="kirim_email_submit")
def kirim_email_submit(
    request: Request,
    nama: str = Form(...),
    email_pengirim: str = Form(...),
    telepon: str = Form(""),
    instansi: str = Form(""),
    subjek: str = Form(...),
    pesan: str = Form(...),
):
    form = _build_form_state(nama, email_pengirim, telepon, instansi, subjek, pesan)

    smtp = _smtp_config()
    if not smtp["host"] or not smtp["username"] or not smtp["password"]:
        return templates.TemplateResponse(
            request,
            "kirim_email.html",
            {
                "sent": False,
                "error": SMTP_ERROR_MSG,
                "form": form,
            },
            status_code=400,
        )

    target_email = (
        (get_setting("email_to", "") or "").strip()
        or os.getenv("EMAIL_TO", "").strip()
        or (get_setting("email", "").strip())
    )
    if not target_email:
        return templates.TemplateResponse(
            request,
            "kirim_email.html",
            {
                "sent": False,
                "error": "Email tujuan belum tersedia di pengaturan website.",
                "form": form,
            },
            status_code=400,
        )

    message = EmailMessage()
    message["Subject"] = f"[Kontak Website] {subjek.strip()}"
    message["From"] = smtp["username"]
    message["To"] = target_email

    body = (
        "Pesan baru dari halaman Kirim Email website Ngrembaka Aksara\n\n"
        f"Nama: {nama.strip()}\n"
        f"Email: {email_pengirim.strip()}\n"
        f"No. HP/WhatsApp: {telepon.strip() or '-'}\n"
        f"Instansi/Komunitas: {instansi.strip() or '-'}\n"
        f"Subjek: {subjek.strip()}\n\n"
        "Isi pesan:\n"
        f"{pesan.strip()}\n"
    )
    message.set_content(body)
    message.add_alternative(
        f"""
        <h3>Pesan Baru dari Form Website</h3>
        <p><strong>Nama:</strong> {nama.strip()}</p>
        <p><strong>Email:</strong> {email_pengirim.strip()}</p>
        <p><strong>No. HP/WhatsApp:</strong> {telepon.strip() or '-'}</p>
        <p><strong>Instansi/Komunitas:</strong> {instansi.strip() or '-'}</p>
        <p><strong>Subjek:</strong> {subjek.strip()}</p>
        <hr />
        <p><strong>Isi pesan:</strong></p>
        <p>{pesan.strip().replace(chr(10), '<br/>')}</p>
        """,
        subtype="html",
    )

    try:
        with smtplib.SMTP(smtp["host"], smtp["port"], timeout=30) as server:
            if smtp["use_tls"]:
                server.starttls()
            server.login(smtp["username"], smtp["password"])
            server.send_message(message)
    except Exception:
        return templates.TemplateResponse(
            request,
            "kirim_email.html",
            {
                "sent": False,
                "error": "Pengiriman gagal. Periksa konfigurasi SMTP atau coba beberapa saat lagi.",
                "form": form,
            },
            status_code=502,
        )

    return RedirectResponse("/kirim-email?sent=1", status_code=303)
