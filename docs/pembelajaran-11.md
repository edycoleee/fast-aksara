# Pembelajaran 11 - Menghubungkan HTML dengan CRUD End-to-End

Pembelajaran ini melanjutkan Pembelajaran 10.
Setelah siswa sudah paham database, auth, dan testing dasar, tahap berikutnya adalah menghubungkan seluruh alur: admin input -> database -> halaman publik.

## A. Tujuan

- Siswa memahami alur penuh aplikasi web dinamis.
- Siswa dapat menghubungkan form HTML ke backend FastAPI.
- Siswa dapat menyimpan data ke database dan menampilkannya lewat Jinja2.
- Siswa dapat membuktikan hasil CRUD berjalan dari admin ke tampilan publik.

## B. Hasil Akhir

Di akhir pembelajaran, siswa mampu:

1. Membuat form admin untuk tambah/edit data.
2. Menangkap data dari form HTML ke route FastAPI.
3. Menyimpan data ke database SQLite.
4. Menampilkan data ke halaman publik dengan Jinja2.
5. Menghapus dan memperbarui data dengan alur yang aman.

## C. Estimasi Waktu

- 2 sampai 3 pertemuan (180-270 menit).

## D. Konsep Inti

Aplikasi web yang bagus bukan hanya tampil halaman statis.
Sistem yang dinamis memiliki alur seperti ini:

1. Admin membuka form.
2. Form dikirim ke route backend.
3. Backend validasi data.
4. Data disimpan ke database.
5. Database dipanggil lagi saat halaman dibuka.
6. Template Jinja2 menampilkan data terbaru.

Itulah arti dari website yang hidup dan bisa berubah berdasarkan data.

## E. Tahap Belajar

### Tahap 1 - Memahami alur end-to-end (30-45 menit)

Aktivitas:
- Guru menjelaskan flow dari form ke database ke halaman publik.
- Siswa memetakan setiap fungsi.

Output:
- Siswa paham peran model, route, template, dan database.

### Tahap 2 - CRUD admin ke database (60-90 menit)

Aktivitas:
- Buat form `create` dan `update` untuk artikel.
- Simpan data ke tabel.

Output:
- Data masuk ke database dengan benar.

### Tahap 3 - Menampilkan data ke template publik (45-60 menit)

Aktivitas:
- Query database dari route publik.
- Render looping Jinja2.

Output:
- Halaman depan menampilkan data nyata.

### Tahap 4 - Edit dan delete dengan PRG (45-60 menit)

Aktivitas:
- Setelah submit, redirect ke halaman list atau detail.
- Uji edit dan hapus.

Output:
- Aplikasi aman dari pengiriman ulang data.

### Tahap 5 - Uji skenario nyata (30-45 menit)

Aktivitas:
- Tambah artikel dari admin.
- Cek halaman publik.
- Edit judul/artikel.
- Hapus data.

Output:
- Website running end-to-end.

## F. Struktur File yang Dipakai

```text
backend/app/
|-- database.py
|-- models.py
|-- routers/
|   |-- admin.py
|   |-- landing.py
|-- templates/
|   |-- base.html
|   |-- landing.html
|   |-- admin/
|       |-- artikel_form.html
``` 

## G. Model Data

Model paling sederhana untuk artikel:

```python
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Artikel(Base):
    __tablename__ = "artikel"

    id = Column(Integer, primary_key=True, index=True)
    judul = Column(String(200), nullable=False)
    isi = Column(Text, nullable=False)
    kategori = Column(String(100), nullable=True)
```

Penjelasan:
- `judul`: judul artikel.
- `isi`: konten utama artikel.
- `kategori`: kelompok artikel.

## H. Route Admin: Form Tambah Artikel

Contoh route create:

```python
from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Artikel

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/artikel/tambah")
def artikel_tambah_form(request: Request):
    return templates.TemplateResponse(
        "admin/artikel_form.html",
        {"request": request, "artikel": None},
    )


@router.post("/artikel/tambah")
def artikel_tambah(
    request: Request,
    judul: str = Form(...),
    isi: str = Form(...),
    kategori: str = Form("Umum"),
    db: Session = Depends(get_db),
):
    artikel = Artikel(
        judul=judul,
        isi=isi,
        kategori=kategori,
    )
    db.add(artikel)
    db.commit()
    db.refresh(artikel)

    return RedirectResponse(url="/admin/artikel", status_code=303)
```

## I. Route Admin: Menampilkan Daftar Artikel

```python
@router.get("/artikel")
def artikel_list(request: Request, db: Session = Depends(get_db)):
    items = db.query(Artikel).order_by(Artikel.id.desc()).all()
    return templates.TemplateResponse(
        "admin/dashboard.html",
        {"request": request, "items": items},
    )
```

## J. Route Admin: Edit Artikel

```python
@router.get("/artikel/edit/{artikel_id}")
def artikel_edit_form(artikel_id: int, request: Request, db: Session = Depends(get_db)):
    artikel = db.query(Artikel).filter(Artikel.id == artikel_id).first()
    if not artikel:
        return RedirectResponse(url="/admin/artikel", status_code=303)

    return templates.TemplateResponse(
        "admin/artikel_form.html",
        {"request": request, "artikel": artikel},
    )


@router.post("/artikel/edit/{artikel_id}")
def artikel_edit(
    artikel_id: int,
    request: Request,
    judul: str = Form(...),
    isi: str = Form(...),
    kategori: str = Form("Umum"),
    db: Session = Depends(get_db),
):
    artikel = db.query(Artikel).filter(Artikel.id == artikel_id).first()
    if not artikel:
        return RedirectResponse(url="/admin/artikel", status_code=303)

    artikel.judul = judul
    artikel.isi = isi
    artikel.kategori = kategori
    db.commit()

    return RedirectResponse(url="/admin/artikel", status_code=303)
```

## K. Route Admin: Hapus Artikel

```python
@router.post("/artikel/delete/{artikel_id}")
def artikel_delete(artikel_id: int, db: Session = Depends(get_db)):
    artikel = db.query(Artikel).filter(Artikel.id == artikel_id).first()
    if artikel:
        db.delete(artikel)
        db.commit()

    return RedirectResponse(url="/admin/artikel", status_code=303)
```

## L. Template Form Admin

Konten template form:

```html
{% extends "base.html" %}
{% block content %}
<h1>{% if artikel %}Edit Artikel{% else %}Tambah Artikel{% endif %}</h1>

<form method="post" action="{% if artikel %}/admin/artikel/edit/{{ artikel.id }}{% else %}/admin/artikel/tambah{% endif %}">
    <div>
        <label>Judul</label>
        <input type="text" name="judul" value="{{ artikel.judul if artikel else '' }}" required>
    </div>

    <div>
        <label>Kategori</label>
        <input type="text" name="kategori" value="{{ artikel.kategori if artikel else 'Umum' }}">
    </div>

    <div>
        <label>Isi</label>
        <textarea name="isi" rows="8" required>{{ artikel.isi if artikel else '' }}</textarea>
    </div>

    <button type="submit">Simpan</button>
</form>
{% endblock %}
```

## M. Route Publik: Menampilkan Artikel di Halaman Depan

```python
from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Artikel

router = APIRouter(tags=["public"])


@router.get("/")
def landing_page(request: Request, db: Session = Depends(get_db)):
    artikel_list = db.query(Artikel).order_by(Artikel.id.desc()).all()
    return templates.TemplateResponse(
        "landing.html",
        {"request": request, "artikel_list": artikel_list},
    )
```

## N. Template Publik

```html
{% extends "base.html" %}
{% block content %}
<h1>Berita & Artikel</h1>

{% if artikel_list %}
    {% for item in artikel_list %}
        <article>
            <h2>{{ item.judul }}</h2>
            <p><small>{{ item.kategori }}</small></p>
            <p>{{ item.isi }}</p>
        </article>
    {% else %}
        <p>Belum ada artikel.</p>
    {% endfor %}
{% else %}
    <p>Belum ada artikel.</p>
{% endif %}
{% endblock %}
```

## O. Prinsip Penting: PRG (Post-Redirect-Get)

Setelah submit form, jangan langsung render halaman hasil.
Lebih aman seperti ini:

```python
return RedirectResponse(url="/admin/artikel", status_code=303)
```

Kenapa penting?
- Menghindari submit ulang saat refresh browser.
- Membuat alur lebih aman dan stabil.
- Menjaga data tetap konsisten.

## P. Checklist Praktik Siswa

1. Form tambah artikel muncul di admin.
2. Data masuk ke database setelah submit.
3. Halaman depan menampilkan artikel terbaru.
4. Edit artikel berhasil mengubah isi.
5. Hapus artikel berhasil menghilangkan data.
6. Setelah refresh, tidak terjadi duplikasi data.

## Q. Rubrik Penilaian

Skor 1-4 per aspek:

1. Kesesuaian form HTML dan route backend.
2. Keberhasilan simpan data ke database.
3. Kualitas render Jinja2 di halaman publik.
4. Keberhasilan edit dan hapus.
5. Penerapan PRG dan UX yang rapi.

Nilai akhir = rata-rata 5 aspek.

## R. Tugas Lanjutan

1. Tambahkan tombol detail artikel di halaman publik.
2. Buat halaman detail artikel per ID.
3. Tambahkan validasi form seperti judul tidak boleh kosong.
4. Tambahkan paginasi jika artikel banyak.
5. Buat fitur pencarian artikel di halaman publik.

## S. Penutup

Setelah Pembelajaran 11:

- Siswa sudah melihat alur end-to-end aplikasi web: input, penyimpanan, tampil, edit, dan hapus.
- Siswa siap lanjut ke tahap berikutnya: pengujian API, keamanan, optimasi, dan deployment.
