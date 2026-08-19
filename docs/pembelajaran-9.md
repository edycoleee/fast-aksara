# Pembelajaran 9 - Auth, Role, dan Keamanan Upload

Pembelajaran ini melanjutkan Pembelajaran 8.
Jika siswa sudah paham skema database dan CRUD dasar, tahap berikutnya adalah menjaga akses admin tetap aman.

## A. Tujuan

- Siswa memahami autentikasi login admin.
- Siswa memahami otorisasi berbasis role (hak akses).
- Siswa memahami prinsip keamanan upload file.
- Siswa dapat menerapkan proteksi route admin.

## B. Hasil Akhir

Di akhir pembelajaran, siswa mampu:

1. Membuat alur login dan logout.
2. Menjaga halaman admin agar hanya bisa diakses user login.
3. Membedakan role `admin` dan `editor`.
4. Menerapkan validasi upload file (ukuran, tipe, nama aman).

## C. Estimasi Waktu

- 3 sampai 5 pertemuan (270-450 menit).

## D. Tahap Belajar

### Tahap 1 - Konsep Auth dan Role (30-45 menit)

Aktivitas:
- Bedakan autentikasi vs otorisasi.
- Jelaskan risiko jika route admin tidak diproteksi.

Output:
- Siswa paham kenapa login dan role wajib ada.

### Tahap 2 - Login Session Dasar (60-90 menit)

Aktivitas:
- Buat route login GET/POST.
- Simpan status login ke session.

Output:
- User bisa login dan logout.

### Tahap 3 - Proteksi Route Admin (45-60 menit)

Aktivitas:
- Buat helper `require_login`.
- Terapkan ke route admin penting.

Output:
- Route admin menolak akses user belum login.

### Tahap 4 - Otorisasi Role (45-60 menit)

Aktivitas:
- Buat helper `require_role`.
- Batasi aksi sensitif (misalnya delete) untuk role admin.

Output:
- Hak akses antar role jelas.

### Tahap 5 - Keamanan Upload File (60-90 menit)

Aktivitas:
- Validasi MIME type dan ekstensi file.
- Batasi ukuran file.
- Gunakan nama file aman (UUID), bukan nama asli user.

Output:
- Upload gambar/PDF lebih aman untuk produksi ringan.

## E. Struktur File yang Dipakai

```text
backend/app/
|-- routers/
|   |-- admin.py
|-- security.py
|-- upload.py
|-- templates/admin/
|   |-- login.html
```

## F. Kunci Konsep: Auth vs Role

1. Auth (autentikasi): "siapa kamu?"
2. Role (otorisasi): "apa yang boleh kamu lakukan?"

Contoh:
- `editor` boleh tambah/edit artikel.
- `admin` boleh tambah/edit/hapus semua modul + settings.

## G. Contoh Alur Login Session

### 1) Login Form (GET)

```python
@router.get("/admin/login")
def login_page(request: Request):
	return templates.TemplateResponse("admin/login.html", {"request": request, "error": None})
```

### 2) Proses Login (POST)

```python
@router.post("/admin/login")
def login_submit(request: Request, username: str = Form(...), password: str = Form(...)):
	if username == "admin" and password == "admin123":
		request.session["user"] = {
			"username": username,
			"role": "admin",
		}
		return RedirectResponse(url="/admin", status_code=303)

	return templates.TemplateResponse(
		"admin/login.html",
		{"request": request, "error": "Username/password salah."},
		status_code=401,
	)
```

### 3) Logout

```python
@router.get("/admin/logout")
def logout(request: Request):
	request.session.clear()
	return RedirectResponse(url="/admin/login", status_code=303)
```

## H. Contoh Proteksi Route

Buat helper sederhana:

```python
from fastapi import Request
from fastapi.responses import RedirectResponse


def require_login(request: Request):
	user = request.session.get("user")
	if not user:
		return RedirectResponse(url="/admin/login", status_code=303)
	return None
```

Pemakaian di route:

```python
@router.get("/admin")
def admin_dashboard(request: Request):
	blocked = require_login(request)
	if blocked:
		return blocked

	return templates.TemplateResponse("admin/dashboard.html", {"request": request})
```

## I. Contoh Proteksi Role

```python
from fastapi import HTTPException


def require_role(request: Request, allowed_roles: list[str]):
	user = request.session.get("user")
	if not user:
		raise HTTPException(status_code=401, detail="Belum login")
	if user.get("role") not in allowed_roles:
		raise HTTPException(status_code=403, detail="Akses ditolak")
```

Pemakaian contoh (hapus data hanya admin):

```python
@router.post("/admin/artikel/delete/{item_id}")
def artikel_delete(item_id: int, request: Request, db: Session = Depends(get_db)):
	require_role(request, ["admin"])
	...
```

## J. Keamanan Upload File (Best Practice Dasar)

Prinsip minimal:

1. Batasi jenis file.
2. Batasi ukuran file.
3. Simpan file dengan nama acak aman.
4. Jangan percaya ekstensi file saja.

Contoh helper upload aman:

```python
import os
import uuid
from pathlib import Path

MAX_FILE_SIZE = 2 * 1024 * 1024  # 2MB
ALLOWED_IMAGE = {"image/jpeg", "image/png", "image/webp"}
ALLOWED_PDF = {"application/pdf"}


def secure_filename(original_name: str) -> str:
	ext = Path(original_name).suffix.lower()
	return f"{uuid.uuid4().hex}{ext}"
```

Contoh validasi upload image:

```python
def validate_upload(file: UploadFile, allowed_types: set[str]):
	if file.content_type not in allowed_types:
		raise ValueError("Tipe file tidak diizinkan")
```

Catatan pengajaran:
- `content_type` bisa dimanipulasi, jadi validasi berlapis lebih baik.
- Untuk proyek sekolah, validasi dasar + batas ukuran sudah cukup bagus.

## K. Template Login Minimal

```html
{% extends "base.html" %}
{% block content %}
<h1>Login Admin</h1>

{% if error %}
  <p style="color: #b91c1c;">{{ error }}</p>
{% endif %}

<form method="post" action="/admin/login">
  <label>Username</label>
  <input type="text" name="username" required />

  <label>Password</label>
  <input type="password" name="password" required />

  <button type="submit">Masuk</button>
</form>
{% endblock %}
```

## L. Checklist Praktik Siswa

1. Login benar -> masuk dashboard.
2. Login salah -> muncul pesan error.
3. Belum login -> route admin redirect ke login.
4. Role editor tidak bisa akses aksi delete.
5. Upload file tidak valid -> ditolak.
6. Upload file valid -> tersimpan dengan nama aman.

## M. Rubrik Penilaian

Skor 1-4 per aspek:

1. Implementasi login/logout.
2. Proteksi route admin.
3. Otorisasi berbasis role.
4. Validasi upload file.
5. Konsistensi UX error/sukses.

Nilai akhir = rata-rata 5 aspek.

## N. Tugas Lanjutan

1. Tambahkan user `editor` dan `admin` dari database, bukan hardcoded.
2. Hash password dengan `passlib`.
3. Tambahkan log aktivitas: siapa mengubah data apa.
4. Tambahkan rate-limit sederhana pada endpoint login.

## O. Penutup

Setelah Pembelajaran 9:

- Siswa paham fondasi keamanan aplikasi web berbasis session.
- Siswa siap lanjut ke Pembelajaran 10: audit log, backup data, dan hardening aplikasi.
