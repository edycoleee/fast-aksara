# Branch Pembelajaran Jinja2

Branch ini dibuat untuk memahami Jinja2 sebagai template engine di FastAPI. Fokus pembelajaran adalah bagaimana backend mengirim data ke HTML dan bagaimana template menampilkan data secara dinamis.

Referensi utama: `03-jinja.md`

---

## Tujuan belajar

Setelah mempelajari materi ini, siswa diharapkan mampu:
- memahami konsep template engine,
- memahami hubungan FastAPI dan Jinja2,
- mengirim data dari Python ke HTML,
- menampilkan variabel dengan `{{ ... }}`,
- membuat logika kondisi dengan `{% if %}`,
- menampilkan data dalam daftar dengan `{% for %}`,
- memahami template inheritance (`extends`),
- membagi komponen reusable dengan `include` dan `block`,
- membuat halaman web yang dinamis dari data backend.

---

## Kenapa Jinja2 penting?

JavaScript membuat halaman reaktif di browser. Jinja2 membuat halaman bisa dibuat dari data di server.

Contoh penggunaan Jinja2:
- daftar artikel muncul otomatis,
- halaman profil ditampilkan berdasarkan data user,
- menu admin bisa ditentukan dari backend,
- halaman dinamis dibuat tanpa menulis HTML satu per satu.

Jinja2 cocok untuk aplikasi seperti website Aksara, portal desa, dokumentasi, dan dashboard admin.

---

## Urutan belajar yang logis

Pembelajaran Jinja2 sebaiknya dilakukan bertahap seperti ini:

1. Pahami konsep template engine
2. Pahami FastAPI sebagai backend
3. Pahami route dan method HTTP
4. Setup Jinja2 di FastAPI
5. Gunakan variabel `{{ }}`
6. Gunakan kondisi `{% if %}`
7. Gunakan loop `{% for %}`
8. Gunakan data object dan list
9. Gunakan template inheritance (`extends`)
10. Gunakan include dan reusable component
11. Terapkan pada form, data nyata, dan halaman aplikasi

---

## 1. Konsep template engine

Template engine adalah sistem yang menggabungkan:
- data dari Python,
- template HTML,
- hasil akhirnya menjadi halaman web yang bisa tampil di browser.

Alur dasar:

```text
Data Python -> Jinja2 -> HTML final -> browser
```

### Contoh sederhana:

```python
@app.get("/halo")
def halo(request: Request):
    return templates.TemplateResponse(
        "halo.html",
        {"request": request, "judul": "Selamat Datang", "nama": "Ari"}
    )
```

```html
<h1>{{ judul }}</h1>
<p>Halo, {{ nama }}!</p>
```

Hasil akhirnya di browser:

```html
<h1>Selamat Datang</h1>
<p>Halo, Ari!</p>
```

---

## 2. Konsep FastAPI sebelum Jinja2

Sebelum belajar Jinja2, kita harus paham bahwa FastAPI adalah backend yang menerima request dan menyiapkan data.

### Route
Route adalah alamat URL yang bisa diakses browser, misalnya:

```python
@app.get("/")
@app.get("/profil")
@app.get("/artikel")
```

### Method HTTP
Method HTTP adalah jenis aksi yang dilakukan:

- `GET` = ambil data atau halaman
- `POST` = kirim data baru
- `PUT` = ubah data yang sudah ada
- `DELETE` = hapus data

Contoh:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Halaman utama"}

@app.post("/artikel")
def tambah_artikel():
    return {"message": "Artikel ditambahkan"}
```

FastAPI mempersiapkan data, lalu Jinja2 menampilkan data itu ke HTML.

---

## 3. Setup Jinja2 di FastAPI

### Langkah install
```bash
pip install jinja2
```

### Struktur folder umum
```text
backend/
|-- app/
|   |-- main.py
|   |-- templates/
|       |-- base.html
|       |-- landing.html
```

### Konfigurasi FastAPI
```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
```

### Render template
```python
@app.get("/")
def landing(request: Request):
    return templates.TemplateResponse("landing.html", {"request": request, "judul": "Aksara"})
```

### Penjelasan:
- `request` wajib ada agar template bisa bekerja,
- `judul` adalah data yang dikirim ke template,
- `landing.html` adalah halaman yang akan dirender.

---

## 4. Variabel di Jinja2

Variable ditulis dengan `{{ ... }}`.

### Contoh backend
```python
@app.get("/profil")
def profil(request: Request):
    context = {
        "request": request,
        "nama": "Ari",
        "asal": "Podorejo",
        "umur": 17,
    }
    return templates.TemplateResponse("profil.html", context)
```

### Contoh template
```html
<h1>Halo, {{ nama }}</h1>
<p>Asal: {{ asal }}</p>
<p>Umur: {{ umur }}</p>
```

### Hasil browser
```html
<h1>Halo, Ari</h1>
<p>Asal: Podorejo</p>
<p>Umur: 17</p>
```

### Latihan kecil
- tampilkan nama siswa,
- tampilkan kategori artikel,
- tampilkan tanggal hari ini.

---

## 5. Kondisi dengan `if`

Jinja2 mendukung logika kondisional.

### Sintaks
```html
{% if kondisi %}
    ...
{% else %}
    ...
{% endif %}
```

### Contoh
```html
{% if login %}
    <p>Anda sudah login sebagai {{ nama }}</p>
{% else %}
    <p>Silakan login terlebih dahulu</p>
{% endif %}
```

### Kegunaan:
- cek status login,
- tampilkan tombol login/logout,
- tampilkan pesan admin/user,
- tampilkan status stok atau data kosong.

---

## 6. Loop dengan `for`

Loop dipakai untuk menampilkan data dalam bentuk daftar.

### Sintaks
```html
{% for item in daftar %}
    {{ item }}
{% endfor %}
```

### Contoh backend
```python
@app.get("/artikel")
def artikel(request: Request):
    daftar = ["Aksara Jawa", "Sejarah Desa", "Budaya Lokal"]
    return templates.TemplateResponse("artikel.html", {"request": request, "daftar": daftar})
```

### Contoh template
```html
<ul>
  {% for item in daftar %}
    <li>{{ item }}</li>
  {% endfor %}
</ul>
```

### Output browser
```html
<ul>
  <li>Aksara Jawa</li>
  <li>Sejarah Desa</li>
  <li>Budaya Lokal</li>
</ul>
```

### Kegunaan:
- daftar artikel,
- e-library,
- katalog dokumentasi,
- card berita,
- list data dari database.

---

## 7. Data object dan list of object

Jinja2 juga kuat saat data yang dikirim berbentuk object atau list object.

### Contoh backend
```python
artikel = [
    {"judul": "Aksara Jawa", "kategori": "Budaya"},
    {"judul": "Sejarah Desa", "kategori": "Sejarah"},
]
```

### Contoh template
```html
{% for item in artikel %}
  <div class="card">
    <h3>{{ item.judul }}</h3>
    <p>{{ item.kategori }}</p>
  </div>
{% endfor %}
```

Ini sangat sering dipakai di aplikasi nyata.

---

## 8. Empty state / data kosong

Data tidak selalu ada. Kadang daftar kosong.

### Contoh
```html
{% if artikel %}
  {% for item in artikel %}
    <p>{{ item.judul }}</p>
  {% endfor %}
{% else %}
  <p>Belum ada data.</p>
{% endif %}
```

### Kenapa penting?
User perlu tahu kalau data memang belum ada, bukan halaman yang kosong.

---

## 9. Template inheritance (`extends`)

Jinja2 mendukung template dasar yang bisa dipakai berulang.

### `base.html`
```html
<!DOCTYPE html>
<html>
  <head>
    <title>{% block title %}Aksara{% endblock %}</title>
  </head>
  <body>
    <header>
      <nav>Menu</nav>
    </header>

    <main>
      {% block content %}{% endblock %}
    </main>
  </body>
</html>
```

### `landing.html`
```html
{% extends "base.html" %}

{% block title %}Landing Page{% endblock %}

{% block content %}
  <h1>Selamat Datang di Aksara</h1>
  <p>Ini halaman utama website.</p>
{% endblock %}
```

### Kegunaan:
- navbar sama untuk semua halaman,
- footer bisa dipakai ulang,
- halaman lebih konsisten,
- kode tidak berulang.

---

## 10. Include untuk komponen reusable

Jinja2 juga bisa memanggil template lain dengan `{% include %}`.

### `navbar.html`
```html
<nav>
  <a href="/">Home</a>
  <a href="/beranda">Beranda</a>
  <a href="/elibrary">E-Library</a>
</nav>
```

### `base.html`
```html
<body>
  {% include "navbar.html" %}
  {% block content %}{% endblock %}
</body>
```

### Kegunaan:
- navbar,
- sidebar,
- footer,
- alert box,
- tombol aksi reuse.

---

## 11. Form dan Jinja2

Jinja2 sering dipakai untuk form agar value default bisa tampil otomatis.

```html
<form method="post">
  <input type="text" name="judul" value="{{ artikel.judul if artikel else '' }}">
  <textarea name="isi">{{ artikel.isi if artikel else '' }}</textarea>
  <button type="submit">Simpan</button>
</form>
```

### Artinya:
- kalau data ada, tampilkan datanya,
- kalau tidak ada, tampilkan kosong,
- cocok untuk form edit dan tambah data.

---

## 12. Hubungan Jinja2 dengan JavaScript

Jinja2 dan JavaScript bekerja bersama-sama.

- Jinja2 menyiapkan HTML dari data backend,
- JavaScript membuat halaman lebih interaktif di browser,
- FastAPI menjadi penghubung data.

### Contoh alur:
```text
Jinja2 menampilkan list artikel
JavaScript menangkap klik tombol edit
FastAPI menerima request dan menyimpan perubahan
```

Jadi:
- Jinja2 = menampilkan data
- JavaScript = interaksi user
- FastAPI = backend yang memproses data

---

## Target akhir pembelajaran

Setelah memahami Jinja2, siswa siap untuk:
- membuat halaman dinamis dengan data Python,
- menampilkan list dan object di HTML,
- membuat layout dinamis yang terhubung dengan backend,
- lanjut ke CRUD web app,
- menghubungkan Jinja2, FastAPI, dan JavaScript secara bersamaan.

---

## Kesimpulan

Jinja2 adalah jembatan antara backend dan frontend.

Dengan Jinja2, kita bisa:
- mengambil data dari Python,
- menyiapkan template HTML,
- menampilkan isi yang berubah sesuai data,
- membuat halaman aplikasi lebih rapi dan dinamis.

Tanpa Jinja2, kita harus menulis HTML satu per satu. Dengan Jinja2, kita bisa membuat halaman yang dibuat dari data secara otomatis.

---

## Ringkasan singkat

Belajar Jinja2 itu berarti belajar:
- route dan data backend,
- variabel `{{ }}`,
- kondisi `{% if %}`,
- loop `{% for %}`,
- data object dan list,
- template inheritance,
- reusable component,
- dan integrasi dengan FastAPI dan JavaScript.

Itulah fondasi penting sebelum masuk ke aplikasi web yang lebih kompleks.
