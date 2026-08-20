# Jinja2 untuk Aplikasi FastAPI: Tahap Belajar dari Setup sampai Mahir

Dokumen ini dibuat untuk siswa yang sudah belajar JavaScript dasar, tetapi belum memahami Jinja2. Tujuan pembelajaran adalah menguasai cara mengirim data dari backend FastAPI ke template HTML, lalu menampilkan data secara dinamis di halaman web.

Jinja2 adalah template engine yang dipakai di FastAPI untuk:
- menampilkan data dari Python ke HTML,
- membuat halaman dinamis,
- menggunakan variabel, loop, kondisi, dan komponen template.

---

## 1. Tujuan pembelajaran

Setelah mempelajari materi ini, siswa mampu:
- memahami konsep template engine,
- menginstal dan mengatur Jinja2 di FastAPI,
- mengirim variabel dari backend ke template,
- menampilkan data di HTML dengan `{{ }}`,
- membuat logika sederhana dengan `{% if %}` dan `{% for %}`,
- membagi template agar reusable,
- menghubungkan template dengan data aplikasi yang sebenarnya.

---

## 2. Kenapa Jinja2 penting?

JavaScript membuat halaman jadi interaktif di browser. Jinja2 membuat halaman bisa dibuat dari data di server.

Contoh:
- artikel dari database akan ditampilkan di halaman,
- daftar dokumentasi muncul otomatis,
- menu aktif dapat ditentukan di backend,
- halaman ditampilkan secara dinamis tanpa menulis HTML satu per satu.

Jinja2 adalah alat penting untuk aplikasi seperti website Aksara.

---

## 3. Tahap 1: Pahami konsep template engine

### Konsep dasar
Template engine adalah sistem yang menggabungkan:
- data dari Python,
- template HTML,
- hasil akhirnya menjadi halaman web yang tampil di browser.

Bayangkan seperti ini:

```text
Data Python -> Jinja2 -> HTML final -> browser
```

### Konsep FastAPI

Sebelum belajar Jinja2, penting untuk memahami bahwa FastAPI adalah backend yang mengatur bagaimana aplikasi menerima permintaan dari browser dan mengirimkan hasilnya.

FastAPI bekerja dengan konsep route dan method HTTP.

#### 1. Route
Route adalah alamat URL yang bisa diakses oleh browser, misalnya:

```python
@app.get("/")
@app.get("/profil")
@app.get("/artikel")
```

Artinya:
- `/` = halaman utama
- `/profil` = halaman profil
- `/artikel` = halaman daftar artikel

#### 2. Method HTTP
Method HTTP adalah jenis aksi yang dikirim dari browser ke server.

- `GET` = mengambil data atau halaman
- `POST` = mengirim data baru
- `PUT` = mengubah data yang sudah ada
- `DELETE` = menghapus data

Contoh sederhana:

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

Penjelasannya:
- `GET /` berarti browser meminta halaman utama
- `POST /artikel` berarti browser mengirim data untuk menambah artikel

#### 3. Hubungan FastAPI dengan Jinja2
FastAPI berperan sebagai backend yang:
- menerima request dari browser,
- memproses data,
- menyiapkan variabel yang akan ditampilkan,
- lalu mengirim ke template Jinja2.

Jadi, sebelum Jinja2 bisa bekerja, selalu ada FastAPI yang menangani route dan data.


**Contoh Aplikasi Fast-Api**

Struktur file sangat kecil:

```
fastapi_sederhana/
│
├── main.py
└── requirements.txt
```

Semua file aku jelaskan **detail** supaya benar‑benar mudah dipahami.

---

# 📦 File 1 — **requirements.txt**
Isi file ini untuk menginstall FastAPI dan Uvicorn.

```
fastapi
uvicorn
```

---

# 🐍 File 2 — **main.py**  
Ini file utama yang berisi seluruh API: GET, POST, PUT, DELETE.

Aku beri **penjelasan di setiap bagian** supaya anak SMA langsung paham.

```python
# ============================
# IMPORT LIBRARY
# ============================
# FastAPI = membuat API
# HTTPException = untuk error (misal data tidak ditemukan)
from fastapi import FastAPI, HTTPException

# ============================
# MEMBUAT OBJECT PENYIMPANAN DATA
# ============================
# Kita pakai list sebagai "database sederhana"
# Setiap artikel adalah object dictionary
# Contoh:
# { "id": 1, "judul": "Belajar FastAPI", "isi": "FastAPI itu mudah" }

artikel_list = []

# ============================
# MEMBUAT APLIKASI FASTAPI
# ============================
app = FastAPI()


# ============================
# ROUTE GET (AMBIL DATA)
# ============================
# GET /artikel → mengembalikan semua artikel
@app.get("/artikel")
def get_semua_artikel():
    return artikel_list


# ============================
# ROUTE POST (TAMBAH DATA)
# ============================
# POST /artikel → menambah artikel baru
# Parameter dikirim lewat query:
# /artikel?judul=abc&isi=def
@app.post("/artikel")
def tambah_artikel(judul: str, isi: str):
    # Buat ID otomatis
    new_id = len(artikel_list) + 1

    # Buat object artikel
    artikel = {
        "id": new_id,
        "judul": judul,
        "isi": isi
    }

    # Masukkan ke list
    artikel_list.append(artikel)

    return {"message": "Artikel ditambahkan", "data": artikel}


# ============================
# ROUTE PUT (UPDATE DATA)
# ============================
# PUT /artikel/1?judul=baru&isi=baru
@app.put("/artikel/{artikel_id}")
def update_artikel(artikel_id: int, judul: str, isi: str):
    # Cari artikel berdasarkan ID
    for artikel in artikel_list:
        if artikel["id"] == artikel_id:
            artikel["judul"] = judul
            artikel["isi"] = isi
            return {"message": "Artikel diupdate", "data": artikel}

    # Jika tidak ditemukan
    raise HTTPException(status_code=404, detail="Artikel tidak ditemukan")


# ============================
# ROUTE DELETE (HAPUS DATA)
# ============================
# DELETE /artikel/1
@app.delete("/artikel/{artikel_id}")
def hapus_artikel(artikel_id: int):
    for artikel in artikel_list:
        if artikel["id"] == artikel_id:
            artikel_list.remove(artikel)
            return {"message": "Artikel dihapus"}

    raise HTTPException(status_code=404, detail="Artikel tidak ditemukan")
```
---

# 🚀 Cara Menjalankan

## 1. Install dependency
```
pip install -r requirements.txt
```

## 2. Jalankan server
```
uvicorn main:app --reload
```

## 3. Buka browser
```
http://localhost:8000/docs
```

Di sana kamu bisa **uji GET, POST, PUT, DELETE** dengan tampilan interaktif.

---

# 🧪 Contoh Cara Menggunakan API

### 1. Tambah artikel (POST)
```
POST http://localhost:8000/artikel?judul=Belajar FastAPI&isi=FastAPI itu mudah
```

### 2. Ambil semua artikel (GET)
```
GET http://localhost:8000/artikel
```

### 3. Update artikel (PUT)
```
PUT http://localhost:8000/artikel/1?judul=Judul Baru&isi=Isi Baru
```

### 4. Hapus artikel (DELETE)
```
DELETE http://localhost:8000/artikel/1
```

---

# 🎯 Ringkasan
Dengan contoh ini, anak SMA bisa memahami:

- **GET** → ambil data  
- **POST** → tambah data  
- **PUT** → ubah data  
- **DELETE** → hapus data  
- Data disimpan dalam **object list**, bukan database  
- Semua route sangat sederhana dan mudah dibaca  

---

**unit test lengkap**
---

# 📁 Struktur Folder Baru (ditambah folder `tests/`)
```
fastapi_sederhana/
│
├── main.py
├── requirements.txt
└── tests/
    └── test_main.py
```

---

# 🧪 File: `tests/test_main.py`  
Unit test menggunakan **pytest** + **FastAPI TestClient**.

Semua test dibuat **sederhana**, mengikuti API GET, POST, PUT, DELETE yang kamu punya.

```python
# ============================================
# IMPORT
# ============================================
from fastapi.testclient import TestClient
from main import app, artikel_list

# Buat client untuk testing
client = TestClient(app)

# Reset data sebelum setiap test
def setup_function():
    artikel_list.clear()


# ============================================
# TEST GET (awal harus kosong)
# ============================================
def test_get_awal_kosong():
    response = client.get("/artikel")
    assert response.status_code == 200
    assert response.json() == []


# ============================================
# TEST POST (tambah artikel)
# ============================================
def test_post_tambah_artikel():
    response = client.post("/artikel?judul=Test&isi=Isi Test")
    assert response.status_code == 200
    data = response.json()["data"]

    assert data["id"] == 1
    assert data["judul"] == "Test"
    assert data["isi"] == "Isi Test"


# ============================================
# TEST PUT (update artikel)
# ============================================
def test_put_update_artikel():
    # Tambah dulu
    client.post("/artikel?judul=Test&isi=Isi Test")

    # Update
    response = client.put("/artikel/1?judul=Baru&isi=Isi Baru")
    assert response.status_code == 200
    data = response.json()["data"]

    assert data["judul"] == "Baru"
    assert data["isi"] == "Isi Baru"


# ============================================
# TEST DELETE (hapus artikel)
# ============================================
def test_delete_artikel():
    # Tambah dulu
    client.post("/artikel?judul=Test&isi=Isi Test")

    # Hapus
    response = client.delete("/artikel/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Artikel dihapus"

    # Pastikan list kosong lagi
    assert artikel_list == []


# ============================================
# TEST ERROR: update artikel yang tidak ada
# ============================================
def test_update_artikel_tidak_ada():
    response = client.put("/artikel/99?judul=x&isi=y")
    assert response.status_code == 404
    assert response.json()["detail"] == "Artikel tidak ditemukan"


# ============================================
# TEST ERROR: hapus artikel yang tidak ada
# ============================================
def test_hapus_artikel_tidak_ada():
    response = client.delete("/artikel/99")
    assert response.status_code == 404
    assert response.json()["detail"] == "Artikel tidak ditemukan"
```

---

# 📦 Tambahkan dependency untuk testing  
Edit `requirements.txt`:

```
fastapi
uvicorn
pytest
```

---

# ▶️ Cara Menjalankan Unit Test

Masuk ke folder project:

```
cd fastapi_sederhana
```

Jalankan:

```
pytest
```

Jika berhasil, outputnya seperti:

```
==================== test session starts ====================
collected 6 items

tests/test_main.py ......                                 [100%]

===================== 6 passed in 0.50s =====================
```

---

# 🚀 Cara Menjalankan Server FastAPI

```
uvicorn main:app --reload
```

---

# 🌐 Cara Akses Swagger (API Docs)

Buka browser:

```
http://localhost:8000/docs
```

Swagger akan menampilkan:

- GET /artikel  
- POST /artikel  
- PUT /artikel/{id}  
- DELETE /artikel/{id}  

Semua bisa diuji langsung dari browser.

---

# 🎯 Ringkasan
Dengan tambahan ini, kamu sekarang punya:

- **Unit test lengkap** untuk GET, POST, PUT, DELETE  
- **Test error** untuk ID yang tidak ditemukan  
- **Cara menjalankan pytest**  
- **Cara menjalankan server**  
- **Cara akses Swagger UI**

---


### Konsep Render Jinja2

Render Jinja2 berarti proses mengubah template HTML yang berisi kode Jinja2 menjadi halaman HTML final yang bisa tampil di browser.

Prosesnya kira-kira seperti ini:

```text
Browser mengirim request -> FastAPI menerima request -> route menyiapkan data -> Jinja2 membaca template -> variabel/if/for diganti dengan nilai sebenarnya -> HTML final dikirim ke browser
```

Jadi, Jinja2 bukan hanya menampilkan HTML biasa, tetapi bekerja seperti mesin yang "mengisi" bagian dinamis dari template dengan data dari Python.

Contoh sederhana:

```python
# backend
@app.get("/halo")
def halo(request: Request):
    return templates.TemplateResponse(
        "halo.html",
        {"request": request, "judul": "Selamat Datang", "nama": "Ari"}
    )
```

```html
<!-- template -->
<h1>{{ judul }}</h1>
<p>Halo, {{ nama }}!</p>
```

Setelah proses render, browser menerima HTML seperti ini:

```html
<h1>Selamat Datang</h1>
<p>Halo, Ari!</p>
```

### Perbedaan HTML biasa dan template Jinja2

HTML biasa:
```html
<h1>Selamat Datang</h1>
```

Jinja2:
```html
<h1>{{ judul }}</h1>
```

Artinya:
- `judul` adalah data yang dikirim dari backend,
- Jinja2 mengganti `{{ judul }}` dengan isi yang sebenarnya.

### Contoh sederhana
Backend Python:
```python
judul = "Selamat Datang"
```

Template HTML:
```html
<h1>{{ judul }}</h1>
```

Hasil akhirnya di browser:
```html
<h1>Selamat Datang</h1>
```

**Jinja2** + **halaman HTML**
---

# 🎯 **Tujuan versi ini**
- FastAPI sebagai backend  
- Jinja2 sebagai template engine  
- HTML sebagai tampilan  
- Data disimpan dalam **list** (bukan database)  
- CRUD sederhana: GET, POST, PUT, DELETE  
- Halaman HTML untuk menampilkan daftar artikel  

---

# 📁 **Struktur Folder**

```
fastapi_jinja_sederhana/
│
├── main.py
├── requirements.txt
└── templates/
    ├── home.html
    └── artikel.html
```

---

# 📦 **File 1 — requirements.txt**

```
fastapi
uvicorn
jinja2
python-multipart
```

---

# 🐍 **File 2 — main.py (penjelasan sangat detail)**

```python
# ============================
# IMPORT LIBRARY
# ============================
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

# ============================
# SETUP TEMPLATE FOLDER
# ============================
# Folder "templates" akan menyimpan file HTML
templates = Jinja2Templates(directory="templates")

# ============================
# DATA SEDERHANA (LIST)
# ============================
# Ini sebagai "database" sederhana
artikel_list = []

# ============================
# MEMBUAT APLIKASI FASTAPI
# ============================
app = FastAPI()


# ============================
# HALAMAN UTAMA (HTML)
# ============================
@app.get("/")
def home(request: Request):
    # Mengirim data ke template home.html
    return templates.TemplateResponse(
        "home.html",
        {"request": request, "title": "Halaman Utama"}
    )


# ============================
# HALAMAN LIST ARTIKEL (HTML)
# ============================
@app.get("/artikel")
def halaman_artikel(request: Request):
    return templates.TemplateResponse(
        "artikel.html",
        {
            "request": request,
            "artikel_list": artikel_list
        }
    )


# ============================
# POST ARTIKEL (FORM HTML)
# ============================
@app.post("/artikel")
def tambah_artikel(judul: str = Form(...), isi: str = Form(...)):
    new_id = len(artikel_list) + 1

    artikel = {
        "id": new_id,
        "judul": judul,
        "isi": isi
    }

    artikel_list.append(artikel)

    # Redirect kembali ke halaman artikel
    return RedirectResponse(url="/artikel", status_code=303)


# ============================
# DELETE ARTIKEL
# ============================
@app.get("/artikel/hapus/{artikel_id}")
def hapus_artikel(artikel_id: int):
    for artikel in artikel_list:
        if artikel["id"] == artikel_id:
            artikel_list.remove(artikel)
            break

    return RedirectResponse(url="/artikel", status_code=303)
```

---

# 🖼️ **File 3 — templates/home.html**

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>Selamat datang di FastAPI + Jinja2</h1>

    <p>Ini adalah contoh sederhana untuk anak SMA.</p>

    <a href="/artikel">Lihat daftar artikel</a>
</body>
</html>
```

---

# 🖼️ **File 4 — templates/artikel.html**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Daftar Artikel</title>
</head>
<body>
    <h1>Daftar Artikel</h1>

    <!-- Form tambah artikel -->
    <form action="/artikel" method="post">
        <label>Judul:</label><br>
        <input type="text" name="judul" required><br><br>

        <label>Isi:</label><br>
        <textarea name="isi" required></textarea><br><br>

        <button type="submit">Tambah Artikel</button>
    </form>

    <hr>

    <!-- Menampilkan daftar artikel -->
    <h2>List Artikel:</h2>

    {% if artikel_list %}
        <ul>
            {% for a in artikel_list %}
                <li>
                    <strong>{{ a.judul }}</strong><br>
                    {{ a.isi }}<br>
                    <a href="/artikel/hapus/{{ a.id }}">Hapus</a>
                </li>
                <br>
            {% endfor %}
        </ul>
    {% else %}
        <p>Belum ada artikel.</p>
    {% endif %}

    <a href="/">Kembali ke Home</a>
</body>
</html>
```

---

# 🚀 **Cara Menjalankan**

## 1. Install dependency
```
pip install -r requirements.txt
```

## 2. Jalankan server
```
uvicorn main:app --reload
```

## 3. Buka browser
```
http://localhost:8000
```


---

## 4. Tahap 2: Setup Jinja2 di FastAPI

### Langkah pertama: install dependency
Biasanya Jinja2 sudah ada kalau project FastAPI dibuat dengan template support, tetapi bisa tetap dicek:

```bash
pip install jinja2
```

### Langkah kedua: buat template folder
Biasa struktur seperti ini:

```text
backend/
|-- app/
|   |-- main.py
|   |-- templates/
|       |-- base.html
|       |-- landing.html
```

### Langkah ketiga: konfigurasi di FastAPI
```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
```

### Langkah keempat: render template
```python
@app.get("/")
def landing(request: Request):
    return templates.TemplateResponse("landing.html", {"request": request, "judul": "Aksara"})
```

### Penjelasan:
- `request` wajib ada agar template bisa bekerja dengan FastAPI,
- `judul` adalah data yang dikirim ke template,
- `landing.html` adalah file HTML yang akan dirender.

---

### Script semua file
---

## 📁 Struktur Folder
```
backend/
|-- app/
|   |-- main.py
|   |-- templates/
|       |-- base.html
|       |-- landing.html
```

---

## 🟦 `main.py`
File utama FastAPI yang mengatur routing dan render template.

```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# folder template
templates = Jinja2Templates(directory="app/templates")

# contoh jika nanti ada folder static
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def landing(request: Request):
    return templates.TemplateResponse(
        "landing.html",
        {
            "request": request,
            "judul": "Aksara"
        }
    )
```

---

## 🟦 `templates/base.html`
Template dasar yang bisa dipakai ulang oleh halaman lain.

```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{{ judul }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
        }
        header {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>

<header>
    <h1>{{ judul }}</h1>
</header>

<!-- Tempat halaman lain memasukkan konten -->
{% block content %}{% endblock %}

</body>
</html>
```

---

## 🟦 `templates/landing.html`
Halaman landing yang memakai `base.html`.

```html
{% extends "base.html" %}

{% block content %}
<p>Selamat datang di halaman landing FastAPI + Jinja2!</p>
<p>Ini adalah contoh template sederhana.</p>
{% endblock %}
```

---

## 🚀 Cara Menjalankan
Masuk ke folder `backend` lalu jalankan:

```bash
uvicorn app.main:app --reload
```

Buka browser:

```
http://localhost:8000
```

---


## 5. Tahap 3: Variable di Jinja2

Variable adalah data yang dikirim dari backend ke template.

### Sintaks variabel
```html
{{ nama }}
{{ usia }}
{{ judul_artikel }}
```

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
- buat template yang menampilkan nama siswa,
- buat template yang menampilkan kategori artikel,
- buat template yang menampilkan tanggal hari ini.

---
Variable di Jinja2 adalah **fondasi** untuk membuat halaman dinamis. Di tahap ini kamu akan melihat bagaimana FastAPI mengirim data ke template, lalu template menampilkannya dengan sintaks `{{ ... }}`.

---

## 🎯 Inti Jawaban Singkat
Variable Jinja2 ditulis dengan **double curly braces**: **`{{ nama }}`**.  
FastAPI mengirim data melalui dictionary `context`, dan template menampilkannya.

---

## 🧩 Penjelasan Lengkap + Script Semua File

---

### 🟦 1. Backend: route `/profil`
Ini contoh lengkap file `main.py` yang memuat route baru untuk latihan variable.

```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

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

**Keterangan penting:**
- `request` **wajib** dikirim agar Jinja2 bisa bekerja.
- Semua variable lain (`nama`, `asal`, `umur`) bebas kamu tentukan.
- `profil.html` adalah template yang akan menampilkan data.

---

### 🟦 2. Template: `profil.html`
Template ini menerima variable dari backend dan menampilkannya.

```html
<h1>Halo, {{ nama }}</h1>
<p>Asal: {{ asal }}</p>
<p>Umur: {{ umur }}</p>
```

**Cara kerja Jinja2:**
- `{{ nama }}` → diganti menjadi **Ari**
- `{{ asal }}` → diganti menjadi **Podorejo**
- `{{ umur }}` → diganti menjadi **17**

---

### 🟦 3. Hasil di browser
```html
<h1>Halo, Ari</h1>
<p>Asal: Podorejo</p>
<p>Umur: 17</p>
```

---

## 🧪 Latihan Kecil (Dengan Script Lengkap)

Berikut **3 latihan** yang kamu minta, lengkap dengan **backend + template**.

---

# 🟩 Latihan 1 — Template menampilkan nama siswa

### Backend (`main.py`)
Tambahkan route:

```python
@app.get("/siswa")
def siswa(request: Request):
    return templates.TemplateResponse(
        "siswa.html",
        {
            "request": request,
            "nama_siswa": "Dewi Lestari"
        }
    )
```

### Template (`siswa.html`)
```html
<h2>Nama Siswa: {{ nama_siswa }}</h2>
```

---

# 🟩 Latihan 2 — Template menampilkan kategori artikel

### Backend
```python
@app.get("/artikel")
def artikel(request: Request):
    return templates.TemplateResponse(
        "artikel.html",
        {
            "request": request,
            "kategori": "Teknologi Pendidikan"
        }
    )
```

### Template (`artikel.html`)
```html
<p>Kategori Artikel: <strong>{{ kategori }}</strong></p>
```

---

# 🟩 Latihan 3 — Template menampilkan tanggal hari ini

### Backend
Gunakan Python `datetime`.

```python
from datetime import datetime

@app.get("/tanggal")
def tanggal(request: Request):
    today = datetime.now().strftime("%d-%m-%Y")
    return templates.TemplateResponse(
        "tanggal.html",
        {
            "request": request,
            "hari_ini": today
        }
    )
```

### Template (`tanggal.html`)
```html
<p>Tanggal hari ini: {{ hari_ini }}</p>
```

---

## 📌 Ringkasan Konsep Variable Jinja2
- Variable ditulis dengan `{{ ... }}`  
- Data dikirim dari FastAPI melalui dictionary  
- Template menerima dan menampilkan data  
- Bisa berupa teks, angka, tanggal, list, object, dll  

---


## 6. Tahap 4: Kondisi dengan if

Jinja2 mendukung logika kondisional.

### Sintaks
```html
{% if kondisi %}
    ...
{% else %}
    ...
{% endif %}
```

### Contoh backend
```python
@app.get("/status")
def status(request: Request):
    return templates.TemplateResponse(
        "status.html",
        {"request": request, "login": True, "nama": "Admin"}
    )
```

### Template
```html
{% if login %}
    <p>Anda sudah login sebagai {{ nama }}</p>
{% else %}
    <p>Silakan login terlebih dahulu</p>
{% endif %}
```

### Saat dipakai di aplikasi ini
- cek apakah user login,
- tampilkan tombol login/logout,
- tampilkan pesan untuk admin atau user umum,
- tampilkan status kosong jika data belum ada.

### Contoh aplikasi nyata
```html
{% if user %}
  <a href="/admin/logout">Logout</a>
{% else %}
  <a href="/admin/login">Login Admin</a>
{% endif %}
```


# 🧩 Tahap 4 — Kondisi dengan `if` di Jinja2  
Berikut **5 latihan lengkap** dari level dasar sampai mahir.

---

# 📁 Struktur Folder (dipakai untuk semua latihan)
```
backend/
|-- app/
|   |-- main.py
|   |-- templates/
|       |-- base.html
|       |-- latihan1.html
|       |-- latihan2.html
|       |-- latihan3.html
|       |-- latihan4.html
|       |-- latihan5.html
```

---

# 🟦 `base.html` (dipakai semua latihan)
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{{ judul }}</title>
</head>
<body>
    <h1>{{ judul }}</h1>
    <hr>
    {% block content %}{% endblock %}
</body>
</html>
```

---

# 🟦 `main.py` (backend untuk semua latihan)
```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Latihan 1
@app.get("/latihan1")
def latihan1(request: Request):
    return templates.TemplateResponse(
        "latihan1.html",
        {"request": request, "nilai": 85, "judul": "Latihan 1 - Kondisi Dasar"}
    )

# Latihan 2
@app.get("/latihan2")
def latihan2(request: Request):
    return templates.TemplateResponse(
        "latihan2.html",
        {"request": request, "login": False, "judul": "Latihan 2 - Login/Logout"}
    )

# Latihan 3
@app.get("/latihan3")
def latihan3(request: Request):
    return templates.TemplateResponse(
        "latihan3.html",
        {
            "request": request,
            "role": "admin",
            "judul": "Latihan 3 - Role Admin/User"
        }
    )

# Latihan 4
@app.get("/latihan4")
def latihan4(request: Request):
    return templates.TemplateResponse(
        "latihan4.html",
        {
            "request": request,
            "stok": 0,
            "judul": "Latihan 4 - Cek Stok Barang"
        }
    )

# Latihan 5
@app.get("/latihan5")
def latihan5(request: Request):
    return templates.TemplateResponse(
        "latihan5.html",
        {
            "request": request,
            "umur": 17,
            "status": None,
            "judul": "Latihan 5 - Kondisi Bertingkat"
        }
    )
```

---

# 🧪 LATIHAN 1 — Kondisi Dasar  
**Tujuan:** siswa memahami `if` paling sederhana.

## 🟦 `latihan1.html`
```html
{% extends "base.html" %}

{% block content %}
<p>Nilai kamu: {{ nilai }}</p>

{% if nilai >= 75 %}
    <p>Status: Lulus 🎉</p>
{% else %}
    <p>Status: Tidak lulus</p>
{% endif %}
{% endblock %}
```

---

# 🧪 LATIHAN 2 — Login / Logout  
**Tujuan:** siswa memahami kondisi boolean.

## 🟦 `latihan2.html`
```html
{% extends "base.html" %}

{% block content %}
{% if login %}
    <p>Anda sudah login.</p>
    <a href="/logout">Logout</a>
{% else %}
    <p>Anda belum login.</p>
    <a href="/login">Login</a>
{% endif %}
{% endblock %}
```

---

# 🧪 LATIHAN 3 — Role Admin / User  
**Tujuan:** siswa memahami kondisi berdasarkan string.

## 🟦 `latihan3.html`
```html
{% extends "base.html" %}

{% block content %}
{% if role == "admin" %}
    <p>Halo Admin! Anda punya akses penuh.</p>
    <a href="/admin/dashboard">Masuk Dashboard</a>
{% else %}
    <p>Halo User! Anda hanya bisa melihat halaman umum.</p>
    <a href="/user/home">Masuk Halaman User</a>
{% endif %}
{% endblock %}
```

---

# 🧪 LATIHAN 4 — Cek Stok Barang  
**Tujuan:** siswa memahami kondisi angka dan status kosong.

## 🟦 `latihan4.html`
```html
{% extends "base.html" %}

{% block content %}
<p>Stok barang: {{ stok }}</p>

{% if stok > 0 %}
    <p>Status: Barang tersedia ✔️</p>
{% else %}
    <p>Status: Stok habis ❌</p>
{% endif %}
{% endblock %}
```

---

# 🧪 LATIHAN 5 — Kondisi Bertingkat (if / elif / else)  
**Tujuan:** siswa memahami kondisi kompleks.

## 🟦 `latihan5.html`
```html
{% extends "base.html" %}

{% block content %}
<p>Umur: {{ umur }}</p>

{% if status %}
    <p>Status: {{ status }}</p>
{% elif umur >= 18 %}
    <p>Kategori: Dewasa</p>
{% elif umur >= 13 %}
    <p>Kategori: Remaja</p>
{% else %}
    <p>Kategori: Anak-anak</p>
{% endif %}
{% endblock %}
```

---

# 🚀 Cara Menjalankan Semua Latihan
Masuk ke folder `backend`:

```bash
uvicorn app.main:app --reload
```

Lalu buka di browser:

- http://localhost:8000/latihan1  
- http://localhost:8000/latihan2  
- http://localhost:8000/latihan3  
- http://localhost:8000/latihan4  
- http://localhost:8000/latihan5  


---

## 7. Tahap 5: Loop dengan for

Loop digunakan untuk menampilkan daftar data.

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

### Template
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

### Untuk aplikasi seperti Aksara
Loop dipakai untuk:
- daftar artikel,
- daftar dokumentasi,
- daftar e-library,
- daftar kegiatan di halaman beranda,
- card produk / berita.

### Contoh data object
```python
artikel = [
    {"judul": "Aksara Jawa", "kategori": "Budaya"},
    {"judul": "Sejarah Desa", "kategori": "Sejarah"},
]
```

### Template
```html
{% for item in artikel %}
  <div class="card">
    <h3>{{ item.judul }}</h3>
    <p>{{ item.kategori }}</p>
  </div>
{% endfor %}
```

### Latihan kecil
- tampilkan daftar nama teman dari list Python,
- tampilkan daftar artikel dengan judul dan kategori,
- tampilkan data dalam bentuk tabel HTML sederhana.

---

# 🎯 Inti Jawaban Singkat
Loop Jinja2 memakai sintaks:

```html
{% for item in daftar %}
    {{ item }}
{% endfor %}
```

Loop dipakai untuk daftar artikel, card berita, tabel data, e-library, dokumentasi, dan banyak komponen dinamis lainnya.

---

# 📁 Struktur Folder (dipakai semua latihan)
```
backend/
|-- app/
|   |-- main.py
|   |-- templates/
|       |-- base.html
|       |-- loop1.html
|       |-- loop2.html
|       |-- loop3.html
|       |-- loop4.html
|       |-- loop5.html
```

---

# 🟦 `base.html`
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{{ judul }}</title>
</head>
<body>
    <h1>{{ judul }}</h1>
    <hr>
    {% block content %}{% endblock %}
</body>
</html>
```

---

# 🟦 `main.py` (backend untuk semua latihan)
```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Latihan 1 — Loop dasar
@app.get("/loop1")
def loop1(request: Request):
    daftar = ["Budi", "Siti", "Ari", "Dewi"]
    return templates.TemplateResponse(
        "loop1.html",
        {"request": request, "daftar": daftar, "judul": "Latihan 1 - Loop Dasar"}
    )

# Latihan 2 — Loop artikel (judul + kategori)
@app.get("/loop2")
def loop2(request: Request):
    artikel = [
        {"judul": "Aksara Jawa", "kategori": "Budaya"},
        {"judul": "Sejarah Desa", "kategori": "Sejarah"},
        {"judul": "Kuliner Lokal", "kategori": "Kuliner"},
    ]
    return templates.TemplateResponse(
        "loop2.html",
        {"request": request, "artikel": artikel, "judul": "Latihan 2 - Loop Artikel"}
    )

# Latihan 3 — Loop tabel data
@app.get("/loop3")
def loop3(request: Request):
    siswa = [
        {"nama": "Ari", "kelas": "XI", "nilai": 88},
        {"nama": "Dewi", "kelas": "X", "nilai": 92},
        {"nama": "Budi", "kelas": "XI", "nilai": 75},
    ]
    return templates.TemplateResponse(
        "loop3.html",
        {"request": request, "siswa": siswa, "judul": "Latihan 3 - Loop Tabel"}
    )

# Latihan 4 — Loop dengan kondisi di dalam loop
@app.get("/loop4")
def loop4(request: Request):
    nilai = [95, 60, 80, 45, 100]
    return templates.TemplateResponse(
        "loop4.html",
        {"request": request, "nilai": nilai, "judul": "Latihan 4 - Loop + Kondisi"}
    )

# Latihan 5 — Loop object card (mirip aplikasi Aksara)
@app.get("/loop5")
def loop5(request: Request):
    kegiatan = [
        {"judul": "Festival Aksara", "tanggal": "12 Agustus", "status": "Selesai"},
        {"judul": "Pelatihan Menulis Jawa", "tanggal": "20 Agustus", "status": "Berlangsung"},
        {"judul": "Lomba Kaligrafi", "tanggal": "30 Agustus", "status": "Akan Datang"},
    ]
    return templates.TemplateResponse(
        "loop5.html",
        {"request": request, "kegiatan": kegiatan, "judul": "Latihan 5 - Loop Card"}
    )
```

---

# 🧪 LATIHAN 1 — Loop Dasar (List Nama Teman)
**Tujuan:** memahami loop paling sederhana.

## 🟦 `loop1.html`
```html
{% extends "base.html" %}

{% block content %}
<ul>
    {% for nama in daftar %}
        <li>{{ nama }}</li>
    {% endfor %}
</ul>
{% endblock %}
```

---

# 🧪 LATIHAN 2 — Loop Artikel (Judul + Kategori)
**Tujuan:** loop object dictionary.

## 🟦 `loop2.html`
```html
{% extends "base.html" %}

{% block content %}
{% for item in artikel %}
    <div style="margin-bottom: 10px;">
        <h3>{{ item.judul }}</h3>
        <p>Kategori: {{ item.kategori }}</p>
    </div>
{% endfor %}
{% endblock %}
```

---

# 🧪 LATIHAN 3 — Loop Tabel HTML
**Tujuan:** menampilkan data dalam bentuk tabel.

## 🟦 `loop3.html`
```html
{% extends "base.html" %}

{% block content %}
<table border="1" cellpadding="5">
    <tr>
        <th>Nama</th>
        <th>Kelas</th>
        <th>Nilai</th>
    </tr>

    {% for s in siswa %}
    <tr>
        <td>{{ s.nama }}</td>
        <td>{{ s.kelas }}</td>
        <td>{{ s.nilai }}</td>
    </tr>
    {% endfor %}
</table>
{% endblock %}
```

---

# 🧪 LATIHAN 4 — Loop + Kondisi di Dalam Loop
**Tujuan:** menggabungkan loop dan if.

## 🟦 `loop4.html`
```html
{% extends "base.html" %}

{% block content %}
<ul>
    {% for n in nilai %}
        {% if n >= 75 %}
            <li>{{ n }} — Lulus ✔️</li>
        {% else %}
            <li>{{ n }} — Tidak Lulus ❌</li>
        {% endif %}
    {% endfor %}
</ul>
{% endblock %}
```

---

# 🧪 LATIHAN 5 — Loop Card (Aplikasi Nyata)
**Tujuan:** membuat card seperti aplikasi berita/kegiatan.

## 🟦 `loop5.html`
```html
{% extends "base.html" %}

{% block content %}
{% for item in kegiatan %}
<div style="border:1px solid #ccc; padding:10px; margin-bottom:10px;">
    <h3>{{ item.judul }}</h3>
    <p>Tanggal: {{ item.tanggal }}</p>

    {% if item.status == "Berlangsung" %}
        <p>Status: <strong style="color:green;">Sedang berlangsung</strong></p>
    {% elif item.status == "Akan Datang" %}
        <p>Status: <strong style="color:blue;">Akan datang</strong></p>
    {% else %}
        <p>Status: <strong style="color:gray;">Selesai</strong></p>
    {% endif %}
</div>
{% endfor %}
{% endblock %}
```

---

# 🚀 Cara Menjalankan
```bash
uvicorn app.main:app --reload
```

Lalu buka:

- http://localhost:8000/loop1  
- http://localhost:8000/loop2  
- http://localhost:8000/loop3  
- http://localhost:8000/loop4  
- http://localhost:8000/loop5  

---


## 8. Tahap 6: Loop bersarang (nested loop)

Kadang data kita bersifat bersarang, misalnya kategori memiliki banyak artikel.

### Contoh data
```python
kategori = [
    {"nama": "Budaya", "items": ["Aksara", "Wayang", "Kesenian"]},
    {"nama": "Sejarah", "items": ["Sejarah Desa", "Pahlawan Lokal"]},
]
```

### Template
```html
{% for group in kategori %}
  <h3>{{ group.nama }}</h3>
  <ul>
    {% for item in group.items %}
      <li>{{ item }}</li>
    {% endfor %}
  </ul>
{% endfor %}
```

### Keterangan
Ini sering dipakai saat kita membuat menu kategori atau daftar konten yang dibagi kelompok.

---

# 🎯 Inti Jawaban Singkat
Loop bersarang memakai pola:

```html
{% for group in data %}
    {% for item in group.items %}
        {{ item }}
    {% endfor %}
{% endfor %}
```

Dipakai untuk kategori, menu, card berita, tabel bertingkat, dan struktur data kompleks lainnya.

---

# 📁 Struktur Folder (dipakai semua latihan)
```
backend/
|-- app/
|   |-- main.py
|   |-- templates/
|       |-- base.html
|       |-- nested1.html
|       |-- nested2.html
|       |-- nested3.html
|       |-- nested4.html
|       |-- nested5.html
```

---

# 🟦 `base.html`
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{{ judul }}</title>
</head>
<body>
    <h1>{{ judul }}</h1>
    <hr>
    {% block content %}{% endblock %}
</body>
</html>
```

---

# 🟦 `main.py` (backend untuk semua latihan)
```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Latihan 1 — Loop bersarang dasar
@app.get("/nested1")
def nested1(request: Request):
    kategori = [
        {"nama": "Buah", "items": ["Apel", "Jeruk", "Mangga"]},
        {"nama": "Sayur", "items": ["Bayam", "Wortel"]},
    ]
    return templates.TemplateResponse(
        "nested1.html",
        {"request": request, "kategori": kategori, "judul": "Latihan 1 - Nested Loop Dasar"}
    )

# Latihan 2 — Kategori + Artikel (judul + kategori)
@app.get("/nested2")
def nested2(request: Request):
    data = [
        {
            "kategori": "Budaya",
            "artikel": [
                {"judul": "Aksara Jawa", "penulis": "Ari"},
                {"judul": "Wayang Kulit", "penulis": "Dewi"},
            ]
        },
        {
            "kategori": "Sejarah",
            "artikel": [
                {"judul": "Sejarah Desa", "penulis": "Budi"},
            ]
        }
    ]
    return templates.TemplateResponse(
        "nested2.html",
        {"request": request, "data": data, "judul": "Latihan 2 - Nested Artikel"}
    )

# Latihan 3 — Tabel bertingkat
@app.get("/nested3")
def nested3(request: Request):
    kelas = [
        {
            "nama": "Kelas X",
            "siswa": ["Ari", "Dewi", "Siti"]
        },
        {
            "nama": "Kelas XI",
            "siswa": ["Budi", "Rina"]
        }
    ]
    return templates.TemplateResponse(
        "nested3.html",
        {"request": request, "kelas": kelas, "judul": "Latihan 3 - Nested Tabel"}
    )

# Latihan 4 — Nested + kondisi
@app.get("/nested4")
def nested4(request: Request):
    kegiatan = [
        {
            "bulan": "Agustus",
            "items": [
                {"judul": "Festival Aksara", "status": "Selesai"},
                {"judul": "Pelatihan Menulis", "status": "Berlangsung"},
            ]
        },
        {
            "bulan": "September",
            "items": [
                {"judul": "Lomba Kaligrafi", "status": "Akan Datang"},
            ]
        }
    ]
    return templates.TemplateResponse(
        "nested4.html",
        {"request": request, "kegiatan": kegiatan, "judul": "Latihan 4 - Nested + Kondisi"}
    )

# Latihan 5 — Nested card (mirip aplikasi Aksara)
@app.get("/nested5")
def nested5(request: Request):
    menu = [
        {
            "judul": "Dokumentasi",
            "items": [
                {"nama": "Foto Kegiatan", "jumlah": 120},
                {"nama": "Video Upacara", "jumlah": 12},
            ]
        },
        {
            "judul": "E-Library",
            "items": [
                {"nama": "Aksara Jawa", "jumlah": 34},
                {"nama": "Sejarah Lokal", "jumlah": 18},
            ]
        }
    ]
    return templates.TemplateResponse(
        "nested5.html",
        {"request": request, "menu": menu, "judul": "Latihan 5 - Nested Card"}
    )
```

---

# 🧪 LATIHAN 1 — Nested Loop Dasar  
**Tujuan:** memahami loop bersarang paling sederhana.

## 🟦 `nested1.html`
```html
{% extends "base.html" %}

{% block content %}
{% for group in kategori %}
    <h3>{{ group.nama }}</h3>
    <ul>
        {% for item in group.items %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
{% endfor %}
{% endblock %}
```

---

# 🧪 LATIHAN 2 — Nested Artikel (Judul + Penulis)  
**Tujuan:** nested loop dengan object dictionary.

## 🟦 `nested2.html`
```html
{% extends "base.html" %}

{% block content %}
{% for row in data %}
    <h2>Kategori: {{ row.kategori }}</h2>
    <ul>
        {% for art in row.artikel %}
            <li>{{ art.judul }} — oleh {{ art.penulis }}</li>
        {% endfor %}
    </ul>
{% endfor %}
{% endblock %}
```

---

# 🧪 LATIHAN 3 — Nested Tabel  
**Tujuan:** nested loop untuk tabel bertingkat.

## 🟦 `nested3.html`
```html
{% extends "base.html" %}

{% block content %}
{% for k in kelas %}
    <h3>{{ k.nama }}</h3>
    <table border="1" cellpadding="5">
        {% for s in k.siswa %}
        <tr>
            <td>{{ s }}</td>
        </tr>
        {% endfor %}
    </table>
    <br>
{% endfor %}
{% endblock %}
```

---

# 🧪 LATIHAN 4 — Nested + Kondisi  
**Tujuan:** nested loop dengan kondisi di dalam loop.

## 🟦 `nested4.html`
```html
{% extends "base.html" %}

{% block content %}
{% for bulan in kegiatan %}
    <h2>{{ bulan.bulan }}</h2>

    {% for item in bulan.items %}
        <p>
            <strong>{{ item.judul }}</strong> —
            {% if item.status == "Berlangsung" %}
                <span style="color:green;">Sedang berlangsung</span>
            {% elif item.status == "Akan Datang" %}
                <span style="color:blue;">Akan datang</span>
            {% else %}
                <span style="color:gray;">Selesai</span>
            {% endif %}
        </p>
    {% endfor %}
    <hr>
{% endfor %}
{% endblock %}
```

---

# 🧪 LATIHAN 5 — Nested Card (Aplikasi Nyata)  
**Tujuan:** membuat card bertingkat seperti menu dokumentasi / e-library.

## 🟦 `nested5.html`
```html
{% extends "base.html" %}

{% block content %}
{% for m in menu %}
<div style="border:1px solid #ccc; padding:10px; margin-bottom:15px;">
    <h2>{{ m.judul }}</h2>

    {% for item in m.items %}
        <div style="margin-left:20px;">
            <p>{{ item.nama }} — {{ item.jumlah }} file</p>
        </div>
    {% endfor %}
</div>
{% endfor %}
{% endblock %}
```

---

# 🚀 Cara Menjalankan
```bash
uvicorn app.main:app --reload
```

Lalu buka:

- http://localhost:8000/nested1  
- http://localhost:8000/nested2  
- http://localhost:8000/nested3  
- http://localhost:8000/nested4  
- http://localhost:8000/nested5  

---


## 9. Tahap 7: Filter dan operasi sederhana di Jinja2

Jinja2 juga memungkinkan beberapa operasi sederhana di template.

### Contoh:
```html
{{ nama|upper }}
{{ text|lower }}
{{ angka + 10 }}
```

### Contoh filter umum
- `upper` → huruf besar semua
- `lower` → huruf kecil semua
- `title` → kapital setiap kata
- `default` → nilai default kalau kosong

### Contoh:
```html
<p>{{ judul|upper }}</p>
<p>{{ nama|default('Tamu') }}</p>
```

### Kapan dipakai?
- menampilkan judul besar,
- menampilkan nama default jika belum ada,
- menghitung nilai atau menampilkan label.

---


## 🎯 Inti Jawaban Singkat
Filter Jinja2 memakai sintaks:

```html
{{ variabel|filter }}
{{ angka + 10 }}
```

Filter umum:
- `upper` → huruf besar semua  
- `lower` → huruf kecil semua  
- `title` → kapital setiap kata  
- `default` → nilai default jika kosong  

---

## 📁 Struktur Folder (dipakai semua latihan)
```
backend/
|-- app/
|   |-- main.py
|   |-- templates/
|       |-- base.html
|       |-- filter1.html
|       |-- filter2.html
|       |-- filter3.html
|       |-- filter4.html
|       |-- filter5.html
```

---

## 🟦 `base.html`
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{{ judul }}</title>
</head>
<body>
    <h1>{{ judul }}</h1>
    <hr>
    {% block content %}{% endblock %}
</body>
</html>
```

---

## 🟦 `main.py` (backend untuk semua latihan)
```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Latihan 1 — Filter upper, lower, title
@app.get("/filter1")
def filter1(request: Request):
    return templates.TemplateResponse(
        "filter1.html",
        {
            "request": request,
            "nama": "edy pratama",
            "judul": "Latihan 1 - Filter Dasar"
        }
    )

# Latihan 2 — Filter default
@app.get("/filter2")
def filter2(request: Request):
    return templates.TemplateResponse(
        "filter2.html",
        {
            "request": request,
            "nama": None,
            "judul": "Latihan 2 - Filter Default"
        }
    )

# Latihan 3 — Operasi angka
@app.get("/filter3")
def filter3(request: Request):
    return templates.TemplateResponse(
        "filter3.html",
        {
            "request": request,
            "nilai": 80,
            "judul": "Latihan 3 - Operasi Angka"
        }
    )

# Latihan 4 — Filter dalam loop
@app.get("/filter4")
def filter4(request: Request):
    artikel = [
        {"judul": "aksara jawa", "kategori": "budaya"},
        {"judul": "sejarah desa", "kategori": "sejarah"},
    ]
    return templates.TemplateResponse(
        "filter4.html",
        {
            "request": request,
            "artikel": artikel,
            "judul": "Latihan 4 - Filter dalam Loop"
        }
    )

# Latihan 5 — Filter + operasi + default
@app.get("/filter5")
def filter5(request: Request):
    data = {
        "nama": "",
        "umur": 17,
        "nilai": None
    }
    return templates.TemplateResponse(
        "filter5.html",
        {
            "request": request,
            "data": data,
            "judul": "Latihan 5 - Filter Mahir"
        }
    )
```

---

# 🧪 LATIHAN 1 — Filter Upper, Lower, Title  
**Tujuan:** memahami filter dasar.

## 🟦 `filter1.html`
```html
{% extends "base.html" %}

{% block content %}
<p>Nama asli: {{ nama }}</p>
<p>Upper: {{ nama|upper }}</p>
<p>Lower: {{ nama|lower }}</p>
<p>Title: {{ nama|title }}</p>
{% endblock %}
```

---

# 🧪 LATIHAN 2 — Filter Default  
**Tujuan:** menampilkan nilai default jika kosong.

## 🟦 `filter2.html`
```html
{% extends "base.html" %}

{% block content %}
<p>Nama user: {{ nama|default("Tamu") }}</p>
{% endblock %}
```

---

# 🧪 LATIHAN 3 — Operasi Angka  
**Tujuan:** operasi matematika sederhana.

## 🟦 `filter3.html`
```html
{% extends "base.html" %}

{% block content %}
<p>Nilai asli: {{ nilai }}</p>
<p>Nilai + 10: {{ nilai + 10 }}</p>
<p>Nilai x 2: {{ nilai * 2 }}</p>
<p>Nilai akhir (bonus 5): {{ nilai + 5 }}</p>
{% endblock %}
```

---

# 🧪 LATIHAN 4 — Filter dalam Loop  
**Tujuan:** menggabungkan loop + filter.

## 🟦 `filter4.html`
```html
{% extends "base.html" %}

{% block content %}
{% for item in artikel %}
    <div style="margin-bottom:10px;">
        <h3>{{ item.judul|title }}</h3>
        <p>Kategori: {{ item.kategori|upper }}</p>
    </div>
{% endfor %}
{% endblock %}
```

---

# 🧪 LATIHAN 5 — Filter Mahir (default + operasi + title)  
**Tujuan:** kombinasi filter dan operasi.

## 🟦 `filter5.html`
```html
{% extends "base.html" %}

{% block content %}
<p>Nama: {{ data.nama|default("Tidak diketahui")|title }}</p>
<p>Umur: {{ data.umur }} tahun</p>
<p>Nilai: {{ data.nilai|default(0) }}</p>
<p>Nilai + 20: {{ data.nilai|default(0) + 20 }}</p>
{% endblock %}
```

---

# 🚀 Cara Menjalankan
```bash
uvicorn app.main:app --reload
```

Lalu buka:

- http://localhost:8000/filter1  
- http://localhost:8000/filter2  
- http://localhost:8000/filter3  
- http://localhost:8000/filter4  
- http://localhost:8000/filter5  

---

## 10. Tahap 8: Template inheritance (extends)

Template inheritance adalah salah satu fitur paling penting Jinja2.

### Ide dasar
Kita punya satu template utama, lalu halaman lain hanya menambahkan bagian tertentu.

### Contoh base template
`base.html`
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

### Child template
`landing.html`
```html
{% extends "base.html" %}

{% block title %}Landing Page{% endblock %}

{% block content %}
  <h1>Selamat Datang di Aksara</h1>
  <p>Ini halaman utama website.</p>
{% endblock %}
```

### Mengapa penting?
Dengan `extends`, kita tidak perlu menulis header, navbar, footer berulang-ulang.

Ini sangat cocok untuk aplikasi besar seperti:
- landing page,
- halaman publik,
- halaman admin,
- dashboard dan form.

---

## 🎯 Inti Jawaban Singkat
Dengan `{% extends %}`, kita membuat satu template utama (base), lalu halaman lain hanya mengisi bagian tertentu melalui `{% block %}`.

---

## 📁 Struktur Folder (dipakai semua latihan)
```
backend/
|-- app/
|   |-- main.py
|   |-- templates/
|       |-- base.html
|       |-- home.html
|       |-- profil.html
|       |-- artikel.html
|       |-- admin.html
|       |-- dashboard.html
```

---

## 🟦 `base.html` (template utama)
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Aplikasi Aksara{% endblock %}</title>
</head>
<body>

<header style="background:#eee; padding:10px;">
    <nav>
        <a href="/home">Home</a> |
        <a href="/profil">Profil</a> |
        <a href="/artikel">Artikel</a> |
        <a href="/admin">Admin</a>
    </nav>
</header>

<main style="padding:20px;">
    {% block content %}{% endblock %}
</main>

<footer style="background:#eee; padding:10px; margin-top:20px;">
    <p>© 2026 Aksara</p>
</footer>

</body>
</html>
```

---

## 🟦 `main.py` (backend untuk semua latihan)
```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/home")
def home(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {"request": request, "judul": "Home"}
    )

@app.get("/profil")
def profil(request: Request):
    return templates.TemplateResponse(
        "profil.html",
        {"request": request, "judul": "Profil Pengguna", "nama": "Edy"}
    )

@app.get("/artikel")
def artikel(request: Request):
    daftar = ["Aksara Jawa", "Sejarah Desa", "Budaya Lokal"]
    return templates.TemplateResponse(
        "artikel.html",
        {"request": request, "judul": "Daftar Artikel", "daftar": daftar}
    )

@app.get("/admin")
def admin(request: Request):
    return templates.TemplateResponse(
        "admin.html",
        {"request": request, "judul": "Halaman Admin", "login": False}
    )

@app.get("/dashboard")
def dashboard(request: Request):
    data = [
        {"judul": "Pengunjung Hari Ini", "jumlah": 120},
        {"judul": "Artikel Baru", "jumlah": 5},
        {"judul": "Komentar Masuk", "jumlah": 18},
    ]
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "judul": "Dashboard Admin", "data": data}
    )
```

---

# 🧪 LATIHAN 1 — Halaman Home (extends + block title + block content)

## 🟦 `home.html`
```html
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
<h2>Selamat Datang di Website Aksara</h2>
<p>Ini adalah halaman utama.</p>
{% endblock %}
```

---

# 🧪 LATIHAN 2 — Halaman Profil (extends + variable)
## 🟦 `profil.html`
```html
{% extends "base.html" %}

{% block title %}Profil{% endblock %}

{% block content %}
<h2>Profil Pengguna</h2>
<p>Nama: {{ nama }}</p>
{% endblock %}
```

---

# 🧪 LATIHAN 3 — Halaman Artikel (extends + loop)
## 🟦 `artikel.html`
```html
{% extends "base.html" %}

{% block title %}Artikel{% endblock %}

{% block content %}
<h2>Daftar Artikel</h2>
<ul>
    {% for item in daftar %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>
{% endblock %}
```

---

# 🧪 LATIHAN 4 — Halaman Admin (extends + kondisi)
## 🟦 `admin.html`
```html
{% extends "base.html" %}

{% block title %}Admin{% endblock %}

{% block content %}
<h2>Halaman Admin</h2>

{% if login %}
    <p>Anda sudah login sebagai admin.</p>
{% else %}
    <p>Anda belum login.</p>
    <a href="/login">Login Admin</a>
{% endif %}
{% endblock %}
```

---

# 🧪 LATIHAN 5 — Dashboard Admin (extends + loop + card)
## 🟦 `dashboard.html`
```html
{% extends "base.html" %}

{% block title %}Dashboard{% endblock %}

{% block content %}
<h2>Dashboard Admin</h2>

{% for item in data %}
<div style="border:1px solid #ccc; padding:10px; margin-bottom:10px;">
    <h3>{{ item.judul }}</h3>
    <p>{{ item.jumlah }} data</p>
</div>
{% endfor %}
{% endblock %}
```

---

# 🚀 Cara Menjalankan
```bash
uvicorn app.main:app --reload
```

Lalu buka:

- http://localhost:8000/home  
- http://localhost:8000/profil  
- http://localhost:8000/artikel  
- http://localhost:8000/admin  
- http://localhost:8000/dashboard  

---


## 11. Tahap 9: Block dan reusable section

`block` adalah area yang bisa diisi di template anak.

### Contoh base
```html
<div class="container">
  {% block content %}{% endblock %}
</div>
```

### Contoh child
```html
{% extends "base.html" %}
{% block content %}
  <h2>Halaman Profil</h2>
{% endblock %}
```

### Kapan dipakai?
- untuk menampilkan konten utama per halaman,
- untuk halaman artikel, profil, dokumentasi, admin,
- untuk membuat struktur yang konsisten.

---

## 🎯 Inti Jawaban Singkat
`block` adalah area kosong yang disediakan di template induk (base), lalu diisi oleh template anak.

Dipakai untuk:
- konten utama halaman,
- judul halaman,
- sidebar,
- card,
- komponen admin,
- layout dashboard.

---

## 📁 Struktur Folder (dipakai semua latihan)
```
backend/
|-- app/
|   |-- main.py
|   |-- templates/
|       |-- base.html
|       |-- block1.html
|       |-- block2.html
|       |-- block3.html
|       |-- block4.html
|       |-- block5.html
```

---

## 🟦 `base.html` — Template Utama Dengan Banyak Block
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Aplikasi Aksara{% endblock %}</title>
</head>
<body>

<header style="background:#eee; padding:10px;">
    {% block header %}
    <h2>Header Default</h2>
    {% endblock %}
</header>

<aside style="float:left; width:20%; background:#f5f5f5; padding:10px;">
    {% block sidebar %}
    <p>Sidebar Default</p>
    {% endblock %}
</aside>

<main style="float:left; width:75%; padding:20px;">
    {% block content %}{% endblock %}
</main>

<footer style="clear:both; background:#eee; padding:10px; margin-top:20px;">
    {% block footer %}
    <p>Footer Default</p>
    {% endblock %}
</footer>

</body>
</html>
```

---

## 🟦 `main.py` — Backend Untuk Semua Latihan
```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/block1")
def block1(request: Request):
    return templates.TemplateResponse(
        "block1.html",
        {"request": request, "judul": "Latihan 1 - Block Dasar"}
    )

@app.get("/block2")
def block2(request: Request):
    return templates.TemplateResponse(
        "block2.html",
        {"request": request, "judul": "Latihan 2 - Block Title + Content"}
    )

@app.get("/block3")
def block3(request: Request):
    return templates.TemplateResponse(
        "block3.html",
        {"request": request, "judul": "Latihan 3 - Block Sidebar"}
    )

@app.get("/block4")
def block4(request: Request):
    data = ["Aksara Jawa", "Sejarah Desa", "Budaya Lokal"]
    return templates.TemplateResponse(
        "block4.html",
        {"request": request, "judul": "Latihan 4 - Block + Loop", "data": data}
    )

@app.get("/block5")
def block5(request: Request):
    return templates.TemplateResponse(
        "block5.html",
        {"request": request, "judul": "Latihan 5 - Block Reusable Section"}
    )
```

---

# 🧪 LATIHAN 1 — Block Dasar (Mengisi Content Saja)
## 🟦 `block1.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Ini halaman sederhana</h2>
<p>Hanya mengisi block content.</p>
{% endblock %}
```

---

# 🧪 LATIHAN 2 — Block Title + Content
## 🟦 `block2.html`
```html
{% extends "base.html" %}

{% block title %}Halaman Profil{% endblock %}

{% block content %}
<h2>Profil Pengguna</h2>
<p>Nama: Edy</p>
{% endblock %}
```

---

# 🧪 LATIHAN 3 — Block Sidebar (Mengganti Sidebar Default)
## 🟦 `block3.html`
```html
{% extends "base.html" %}

{% block sidebar %}
<h3>Menu Profil</h3>
<ul>
    <li>Data Diri</li>
    <li>Riwayat</li>
    <li>Pengaturan</li>
</ul>
{% endblock %}

{% block content %}
<h2>Halaman Profil</h2>
<p>Ini konten utama.</p>
{% endblock %}
```

---

# 🧪 LATIHAN 4 — Block + Loop (Daftar Artikel)
## 🟦 `block4.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Daftar Artikel</h2>
<ul>
    {% for item in data %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>
{% endblock %}
```

---

# 🧪 LATIHAN 5 — Block Reusable Section (Header + Footer Khusus)
## 🟦 `block5.html`
```html
{% extends "base.html" %}

{% block header %}
<h2>Header Khusus Halaman Admin</h2>
{% endblock %}

{% block content %}
<h2>Dashboard Admin</h2>
<p>Selamat datang di dashboard.</p>
{% endblock %}

{% block footer %}
<p>Footer Khusus Admin — © 2026</p>
{% endblock %}
```

---

# 🚀 Cara Menjalankan
```bash
uvicorn app.main:app --reload
```

Lalu buka:

- http://localhost:8000/block1  
- http://localhost:8000/block2  
- http://localhost:8000/block3  
- http://localhost:8000/block4  
- http://localhost:8000/block5  



## 12. Tahap 10: Include untuk komponen kecil

Jinja2 bisa memanggil template lain dengan `{% include %}`.

### Contoh
`navbar.html`
```html
<nav>
  <a href="/">Home</a>
  <a href="/beranda">Beranda</a>
  <a href="/elibrary">E-Library</a>
</nav>
```

`base.html`
```html
<body>
  {% include "navbar.html" %}
  {% block content %}{% endblock %}
</body>
```

### Kenapa penting?
Karena di proyek besar, komponen seperti:
- navbar,
- sidebar,
- footer,
- tombol aksi,
- alert box,
sering dipakai berulang.

---
---

## 🎯 Inti Jawaban Singkat
`include` digunakan untuk menyisipkan template kecil ke dalam template lain:

```html
{% include "navbar.html" %}
```

Dipakai untuk:
- navbar,
- sidebar,
- footer,
- card,
- alert box,
- tombol aksi,
- komponen kecil yang sering dipakai ulang.

---

## 📁 Struktur Folder (dipakai semua latihan)
```
backend/
|-- app/
|   |-- main.py
|   |-- templates/
|       |-- base.html
|       |-- navbar.html
|       |-- footer.html
|       |-- card.html
|       |-- alert.html
|       |-- include1.html
|       |-- include2.html
|       |-- include3.html
|       |-- include4.html
|       |-- include5.html
```

---

## 🟦 Komponen Reusable (dipakai semua latihan)

### `navbar.html`
```html
<nav style="background:#eee; padding:10px;">
  <a href="/home">Home</a> |
  <a href="/profil">Profil</a> |
  <a href="/artikel">Artikel</a>
</nav>
```

### `footer.html`
```html
<footer style="background:#eee; padding:10px; margin-top:20px;">
  <p>© 2026 Aksara</p>
</footer>
```

### `alert.html`
```html
<div style="padding:10px; background:#ffdddd; border:1px solid #ff8888;">
  {{ pesan }}
</div>
```

### `card.html`
```html
<div style="border:1px solid #ccc; padding:10px; margin-bottom:10px;">
  <h3>{{ judul }}</h3>
  <p>{{ isi }}</p>
</div>
```

---

## 🟦 `base.html`
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{{ judul }}</title>
</head>
<body>

{% include "navbar.html" %}

<main style="padding:20px;">
    {% block content %}{% endblock %}
</main>

{% include "footer.html" %}

</body>
</html>
```

---

## 🟦 `main.py` — Backend untuk semua latihan
```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/include1")
def include1(request: Request):
    return templates.TemplateResponse(
        "include1.html",
        {"request": request, "judul": "Latihan 1 - Include Navbar"}
    )

@app.get("/include2")
def include2(request: Request):
    return templates.TemplateResponse(
        "include2.html",
        {"request": request, "judul": "Latihan 2 - Include Alert", "pesan": "Data tidak ditemukan!"}
    )

@app.get("/include3")
def include3(request: Request):
    data = [
        {"judul": "Aksara Jawa", "isi": "Artikel tentang aksara tradisional."},
        {"judul": "Sejarah Desa", "isi": "Dokumentasi sejarah lokal."},
    ]
    return templates.TemplateResponse(
        "include3.html",
        {"request": request, "judul": "Latihan 3 - Include Card", "data": data}
    )

@app.get("/include4")
def include4(request: Request):
    return templates.TemplateResponse(
        "include4.html",
        {"request": request, "judul": "Latihan 4 - Include Sidebar"}
    )

@app.get("/include5")
def include5(request: Request):
    return templates.TemplateResponse(
        "include5.html",
        {"request": request, "judul": "Latihan 5 - Include + Extends + Loop"}
    )
```

---

# 🧪 LATIHAN 1 — Include Navbar  
**Tujuan:** memahami include paling dasar.

## 🟦 `include1.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Halaman Home</h2>
<p>Navbar diambil dari file terpisah.</p>
{% endblock %}
```

---

# 🧪 LATIHAN 2 — Include Alert Box  
**Tujuan:** include dengan variable.

## 🟦 `include2.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Halaman Peringatan</h2>

{% include "alert.html" %}
{% endblock %}
```

---

# 🧪 LATIHAN 3 — Include Card (Loop + Komponen Reusable)
**Tujuan:** include dalam loop.

## 🟦 `include3.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Daftar Artikel</h2>

{% for item in data %}
    {% include "card.html" %}
{% endfor %}
{% endblock %}
```

---

# 🧪 LATIHAN 4 — Include Sidebar (Komponen Tambahan)
Tambahkan file:

### `sidebar.html`
```html
<div style="background:#f5f5f5; padding:10px;">
  <h3>Menu Samping</h3>
  <ul>
    <li>Dashboard</li>
    <li>Pengaturan</li>
    <li>Logout</li>
  </ul>
</div>
```

## 🟦 `include4.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Halaman Admin</h2>

{% include "sidebar.html" %}
{% endblock %}
```

---

# 🧪 LATIHAN 5 — Include + Extends + Loop (Komponen Besar)
**Tujuan:** kombinasi semua konsep.

Tambahkan file:

### `kegiatan_card.html`
```html
<div style="border:1px solid #ccc; padding:10px; margin-bottom:10px;">
  <h3>{{ item.judul }}</h3>
  <p>Tanggal: {{ item.tanggal }}</p>
  <p>Status: {{ item.status }}</p>
</div>
```

## 🟦 `include5.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Daftar Kegiatan</h2>

{% for item in [
    {"judul": "Festival Aksara", "tanggal": "12 Agustus", "status": "Selesai"},
    {"judul": "Pelatihan Menulis", "tanggal": "20 Agustus", "status": "Berlangsung"},
    {"judul": "Lomba Kaligrafi", "tanggal": "30 Agustus", "status": "Akan Datang"}
] %}
    {% include "kegiatan_card.html" %}
{% endfor %}
{% endblock %}
```

---

# 🚀 Cara Menjalankan
```bash
uvicorn app.main:app --reload
```

Lalu buka:

- http://localhost:8000/include1  
- http://localhost:8000/include2  
- http://localhost:8000/include3  
- http://localhost:8000/include4  
- http://localhost:8000/include5  




## 13. Tahap 11: Template dari data object

Jinja2 sangat kuat ketika data yang dikirim sudah berupa object.

### Backend
```python
profil = {
    "nama": "Ari",
    "asal": "Podorejo",
    "status": "Siswa"
}
```

### Template
```html
<h1>{{ profil.nama }}</h1>
<p>Asal: {{ profil.asal }}</p>
<p>Status: {{ profil.status }}</p>
```

### Ini sering dipakai di aplikasi nyata
- data profil admin,
- data website settings,
- detail artikel,
- info pengguna login.

---

## 🎯 Inti Jawaban Singkat
Jika backend mengirim object:

```python
profil = {"nama": "Ari", "asal": "Podorejo", "status": "Siswa"}
```

Maka template bisa mengakses:

```html
{{ profil.nama }}
{{ profil.asal }}
{{ profil.status }}
```

Dipakai untuk:
- **data profil admin**  
- **detail artikel**  
- **website settings**  
- **info pengguna login**  

---

# 📁 Struktur Folder (dipakai semua latihan)
```
backend/
|-- app/
|   |-- main.py
|   |-- templates/
|       |-- base.html
|       |-- obj1.html
|       |-- obj2.html
|       |-- obj3.html
|       |-- obj4.html
|       |-- obj5.html
```

---

# 🟦 `base.html`
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{{ judul }}</title>
</head>
<body style="padding:20px;">
    {% block content %}{% endblock %}
</body>
</html>
```

---

# 🟦 `main.py` — Backend untuk semua latihan
```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Latihan 1 — Object profil sederhana
@app.get("/obj1")
def obj1(request: Request):
    profil = {"nama": "Ari", "asal": "Podorejo", "status": "Siswa"}
    return templates.TemplateResponse(
        "obj1.html",
        {"request": request, "judul": "Latihan 1 - Object Profil", "profil": profil}
    )

# Latihan 2 — Object artikel
@app.get("/obj2")
def obj2(request: Request):
    artikel = {
        "judul": "Aksara Jawa",
        "kategori": "Budaya",
        "penulis": "Edy",
        "tahun": 2026
    }
    return templates.TemplateResponse(
        "obj2.html",
        {"request": request, "judul": "Latihan 2 - Object Artikel", "artikel": artikel}
    )

# Latihan 3 — Object settings website
@app.get("/obj3")
def obj3(request: Request):
    settings = {
        "nama_web": "Aksara Nusantara",
        "versi": "1.0.3",
        "mode": "production",
        "admin": "Super Admin"
    }
    return templates.TemplateResponse(
        "obj3.html",
        {"request": request, "judul": "Latihan 3 - Object Settings", "settings": settings}
    )

# Latihan 4 — Object user login + kondisi
@app.get("/obj4")
def obj4(request: Request):
    user = {
        "nama": "Edy",
        "role": "admin",
        "login": True
    }
    return templates.TemplateResponse(
        "obj4.html",
        {"request": request, "judul": "Latihan 4 - Object Login", "user": user}
    )

# Latihan 5 — Object + nested object
@app.get("/obj5")
def obj5(request: Request):
    detail = {
        "judul": "Festival Aksara",
        "tanggal": "12 Agustus 2026",
        "lokasi": "Balai Desa",
        "penanggung_jawab": {
            "nama": "Pak Seno",
            "jabatan": "Ketua Panitia"
        }
    }
    return templates.TemplateResponse(
        "obj5.html",
        {"request": request, "judul": "Latihan 5 - Object Nested", "detail": detail}
    )
```

---

# 🧪 LATIHAN 1 — Object Profil  
## 🟦 `obj1.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Profil Siswa</h2>
<p>Nama: {{ profil.nama }}</p>
<p>Asal: {{ profil.asal }}</p>
<p>Status: {{ profil.status }}</p>
{% endblock %}
```

---

# 🧪 LATIHAN 2 — Object Artikel  
## 🟦 `obj2.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Detail Artikel</h2>
<p>Judul: {{ artikel.judul }}</p>
<p>Kategori: {{ artikel.kategori }}</p>
<p>Penulis: {{ artikel.penulis }}</p>
<p>Tahun: {{ artikel.tahun }}</p>
{% endblock %}
```

---

# 🧪 LATIHAN 3 — Object Settings Website  
## 🟦 `obj3.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Pengaturan Website</h2>
<p>Nama Website: {{ settings.nama_web }}</p>
<p>Versi: {{ settings.versi }}</p>
<p>Mode: {{ settings.mode }}</p>
<p>Admin: {{ settings.admin }}</p>
{% endblock %}
```

---

# 🧪 LATIHAN 4 — Object Login + Kondisi  
## 🟦 `obj4.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Status Login</h2>

{% if user.login %}
    <p>Halo {{ user.nama }} ({{ user.role|upper }})</p>
    <p>Status: Login ✔️</p>
{% else %}
    <p>Anda belum login.</p>
{% endif %}
{% endblock %}
```

---

# 🧪 LATIHAN 5 — Object Nested (Object di dalam Object)  
## 🟦 `obj5.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Detail Kegiatan</h2>
<p>Judul: {{ detail.judul }}</p>
<p>Tanggal: {{ detail.tanggal }}</p>
<p>Lokasi: {{ detail.lokasi }}</p>

<h3>Penanggung Jawab</h3>
<p>Nama: {{ detail.penanggung_jawab.nama }}</p>
<p>Jabatan: {{ detail.penanggung_jawab.jabatan }}</p>
{% endblock %}
```

---

# 🚀 Cara Menjalankan
```bash
uvicorn app.main:app --reload
```

Lalu buka:

- http://localhost:8000/obj1  
- http://localhost:8000/obj2  
- http://localhost:8000/obj3  
- http://localhost:8000/obj4  
- http://localhost:8000/obj5  

---

## 14. Tahap 12: Menggunakan list of object

Data aplikasi biasanya berbentuk list object, bukan hanya string sederhana.

### Backend
```python
artikel = [
    {"id": 1, "judul": "Aksara Jawa", "kategori": "Budaya"},
    {"id": 2, "judul": "Sejarah Desa", "kategori": "Sejarah"},
]
```

### Template
```html
{% for item in artikel %}
  <div class="card">
    <h3>{{ item.judul }}</h3>
    <p>{{ item.kategori }}</p>
  </div>
{% endfor %}
```

### Kegiatan penting
- menampilkan data dari database,
- menampilkan hasil query SQLAlchemy,
- menampilkan daftar program, dokumentasi, atau artikel.
---

## 🎯 Inti Jawaban Singkat
Jika backend mengirim list berisi object:

```python
artikel = [
    {"id": 1, "judul": "Aksara Jawa", "kategori": "Budaya"},
    {"id": 2, "judul": "Sejarah Desa", "kategori": "Sejarah"},
]
```

Template bisa mengakses:

```html
{% for item in artikel %}
  {{ item.judul }}
  {{ item.kategori }}
{% endfor %}
```

Dipakai untuk:
- **daftar artikel**  
- **hasil query database**  
- **daftar dokumentasi**  
- **daftar kegiatan**  

---

# 📁 Struktur Folder (dipakai semua latihan)
```
backend/
|-- app/
|   |-- main.py
|   |-- templates/
|       |-- base.html
|       |-- list1.html
|       |-- list2.html
|       |-- list3.html
|       |-- list4.html
|       |-- list5.html
```

---

# 🟦 `base.html`
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{{ judul }}</title>
</head>
<body style="padding:20px;">
    {% block content %}{% endblock %}
</body>
</html>
```

---

# 🟦 `main.py` — Backend untuk semua latihan
```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Latihan 1 — List of object sederhana
@app.get("/list1")
def list1(request: Request):
    artikel = [
        {"id": 1, "judul": "Aksara Jawa", "kategori": "Budaya"},
        {"id": 2, "judul": "Sejarah Desa", "kategori": "Sejarah"},
    ]
    return templates.TemplateResponse(
        "list1.html",
        {"request": request, "judul": "Latihan 1 - List Object", "artikel": artikel}
    )

# Latihan 2 — List object + link detail
@app.get("/list2")
def list2(request: Request):
    artikel = [
        {"id": 10, "judul": "Kuliner Lokal", "kategori": "Kuliner"},
        {"id": 11, "judul": "Pahlawan Desa", "kategori": "Sejarah"},
    ]
    return templates.TemplateResponse(
        "list2.html",
        {"request": request, "judul": "Latihan 2 - List + Link", "artikel": artikel}
    )

# Latihan 3 — List object + kondisi
@app.get("/list3")
def list3(request: Request):
    kegiatan = [
        {"judul": "Festival Aksara", "status": "Selesai"},
        {"judul": "Pelatihan Menulis", "status": "Berlangsung"},
        {"judul": "Lomba Kaligrafi", "status": "Akan Datang"},
    ]
    return templates.TemplateResponse(
        "list3.html",
        {"request": request, "judul": "Latihan 3 - List + Kondisi", "kegiatan": kegiatan}
    )

# Latihan 4 — List object + filter
@app.get("/list4")
def list4(request: Request):
    siswa = [
        {"nama": "Ari", "kelas": "XI", "nilai": 88},
        {"nama": "Dewi", "kelas": "X", "nilai": 92},
        {"nama": "Budi", "kelas": "XI", "nilai": 75},
    ]
    return templates.TemplateResponse(
        "list4.html",
        {"request": request, "judul": "Latihan 4 - List + Filter", "siswa": siswa}
    )

# Latihan 5 — List object + nested object
@app.get("/list5")
def list5(request: Request):
    dokumentasi = [
        {
            "judul": "Festival Aksara",
            "foto": ["foto1.jpg", "foto2.jpg", "foto3.jpg"]
        },
        {
            "judul": "Pelatihan Menulis",
            "foto": ["fotoA.jpg", "fotoB.jpg"]
        }
    ]
    return templates.TemplateResponse(
        "list5.html",
        {"request": request, "judul": "Latihan 5 - List Nested", "dokumentasi": dokumentasi}
    )
```

---

# 🧪 LATIHAN 1 — List of Object Sederhana  
## 🟦 `list1.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Daftar Artikel</h2>

{% for item in artikel %}
<div style="border:1px solid #ccc; padding:10px; margin-bottom:10px;">
    <h3>{{ item.judul }}</h3>
    <p>Kategori: {{ item.kategori }}</p>
</div>
{% endfor %}
{% endblock %}
```

---

# 🧪 LATIHAN 2 — List Object + Link Detail  
## 🟦 `list2.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Artikel dengan Link Detail</h2>

{% for item in artikel %}
<div style="margin-bottom:10px;">
    <h3>{{ item.judul }}</h3>
    <p>Kategori: {{ item.kategori }}</p>
    <a href="/detail/{{ item.id }}">Lihat Detail</a>
</div>
{% endfor %}
{% endblock %}
```

---

# 🧪 LATIHAN 3 — List Object + Kondisi  
## 🟦 `list3.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Daftar Kegiatan</h2>

{% for item in kegiatan %}
<div style="margin-bottom:10px;">
    <h3>{{ item.judul }}</h3>

    {% if item.status == "Berlangsung" %}
        <p style="color:green;">Sedang berlangsung</p>
    {% elif item.status == "Akan Datang" %}
        <p style="color:blue;">Akan datang</p>
    {% else %}
        <p style="color:gray;">Selesai</p>
    {% endif %}
</div>
{% endfor %}
{% endblock %}
```

---

# 🧪 LATIHAN 4 — List Object + Filter  
## 🟦 `list4.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Daftar Nilai Siswa</h2>

<table border="1" cellpadding="5">
    <tr>
        <th>Nama</th>
        <th>Kelas</th>
        <th>Nilai</th>
        <th>Status</th>
    </tr>

    {% for s in siswa %}
    <tr>
        <td>{{ s.nama|title }}</td>
        <td>{{ s.kelas }}</td>
        <td>{{ s.nilai }}</td>
        <td>
            {% if s.nilai >= 75 %}
                Lulus
            {% else %}
                Tidak Lulus
            {% endif %}
        </td>
    </tr>
    {% endfor %}
</table>
{% endblock %}
```

---

# 🧪 LATIHAN 5 — List Object + Nested Object  
## 🟦 `list5.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Dokumentasi Kegiatan</h2>

{% for item in dokumentasi %}
<div style="border:1px solid #ccc; padding:10px; margin-bottom:10px;">
    <h3>{{ item.judul }}</h3>

    <p>Foto:</p>
    <ul>
        {% for f in item.foto %}
            <li>{{ f }}</li>
        {% endfor %}
    </ul>
</div>
{% endfor %}
{% endblock %}
```

---

# 🚀 Cara Menjalankan
```bash
uvicorn app.main:app --reload
```

Lalu buka:

- http://localhost:8000/list1  
- http://localhost:8000/list2  
- http://localhost:8000/list3  
- http://localhost:8000/list4  
- http://localhost:8000/list5  


---

## 15. Tahap 13: Null / empty state

Di aplikasi nyata, data kadang belum ada.

### Contoh backend
```python
artikel = []
```

### Template
```html
{% if artikel %}
  {% for item in artikel %}
    <p>{{ item.judul }}</p>
  {% endfor %}
{% else %}
  <p>Belum ada data.</p>
{% endif %}
```

### Mengapa penting?
User perlu melihat pesan yang jelas ketika data kosong, bukan halaman yang kosong saja.

Ini sering dipakai pada:
- daftar artikel kosong,
- daftar dokumen kosong,
- hasil pencarian tidak ditemukan,
- dashboard tanpa data sama sekali.

---

## 🎯 Inti konsep  
Gunakan kondisi:

```html
{% if data %}
    ... tampilkan data ...
{% else %}
    ... tampilkan pesan kosong ...
{% endif %}
```

Dipakai untuk:
- daftar artikel kosong,  
- daftar dokumen kosong,  
- hasil pencarian tidak ditemukan,  
- dashboard tanpa data,  
- list dari database yang belum terisi.

---

# 📁 Struktur Folder (dipakai semua latihan)
```
backend/
|-- app/
|   |-- main.py
|   |-- templates/
|       |-- base.html
|       |-- empty1.html
|       |-- empty2.html
|       |-- empty3.html
|       |-- empty4.html
|       |-- empty5.html
```

---

# 🟦 `base.html`
```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>{{ judul }}</title>
</head>
<body style="padding:20px;">
    {% block content %}{% endblock %}
</body>
</html>
```

---

# 🟦 `main.py` — Backend untuk semua latihan
```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Latihan 1 — List kosong
@app.get("/empty1")
def empty1(request: Request):
    artikel = []
    return templates.TemplateResponse(
        "empty1.html",
        {"request": request, "judul": "Latihan 1 - List Kosong", "artikel": artikel}
    )

# Latihan 2 — Null object
@app.get("/empty2")
def empty2(request: Request):
    profil = None
    return templates.TemplateResponse(
        "empty2.html",
        {"request": request, "judul": "Latihan 2 - Null Object", "profil": profil}
    )

# Latihan 3 — Hasil pencarian kosong
@app.get("/empty3")
def empty3(request: Request):
    hasil = []
    keyword = "aksara"
    return templates.TemplateResponse(
        "empty3.html",
        {"request": request, "judul": "Latihan 3 - Pencarian Kosong", "hasil": hasil, "keyword": keyword}
    )

# Latihan 4 — Dashboard tanpa data
@app.get("/empty4")
def empty4(request: Request):
    statistik = []
    return templates.TemplateResponse(
        "empty4.html",
        {"request": request, "judul": "Latihan 4 - Dashboard Kosong", "statistik": statistik}
    )

# Latihan 5 — List object tetapi beberapa field kosong
@app.get("/empty5")
def empty5(request: Request):
    artikel = [
        {"judul": "", "kategori": "Budaya"},
        {"judul": None, "kategori": "Sejarah"},
    ]
    return templates.TemplateResponse(
        "empty5.html",
        {"request": request, "judul": "Latihan 5 - Field Kosong", "artikel": artikel}
    )
```

---

# 🧪 LATIHAN 1 — List Kosong  
**Tujuan:** menampilkan pesan ketika list tidak berisi data.

## 🟦 `empty1.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Daftar Artikel</h2>

{% if artikel %}
    {% for item in artikel %}
        <p>{{ item.judul }}</p>
    {% endfor %}
{% else %}
    <p style="color:gray;">Belum ada artikel.</p>
{% endif %}
{% endblock %}
```

---

# 🧪 LATIHAN 2 — Null Object  
**Tujuan:** menangani object yang belum ada sama sekali.

## 🟦 `empty2.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Profil Pengguna</h2>

{% if profil %}
    <p>Nama: {{ profil.nama }}</p>
    <p>Asal: {{ profil.asal }}</p>
{% else %}
    <p style="color:gray;">Profil belum tersedia.</p>
{% endif %}
{% endblock %}
```

---

# 🧪 LATIHAN 3 — Hasil Pencarian Kosong  
**Tujuan:** menampilkan pesan “tidak ditemukan”.

## 🟦 `empty3.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Hasil Pencarian: "{{ keyword }}"</h2>

{% if hasil %}
    {% for item in hasil %}
        <p>{{ item.judul }}</p>
    {% endfor %}
{% else %}
    <p style="color:red;">Tidak ada hasil ditemukan.</p>
{% endif %}
{% endblock %}
```

---

# 🧪 LATIHAN 4 — Dashboard Tanpa Data  
**Tujuan:** menangani dashboard kosong.

## 🟦 `empty4.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Dashboard Statistik</h2>

{% if statistik %}
    {% for item in statistik %}
        <p>{{ item.nama }}: {{ item.jumlah }}</p>
    {% endfor %}
{% else %}
    <p style="color:gray;">Belum ada data statistik.</p>
{% endif %}
{% endblock %}
```

---

# 🧪 LATIHAN 5 — Field Kosong dalam List Object  
**Tujuan:** menangani field kosong dengan `default`.

## 🟦 `empty5.html`
```html
{% extends "base.html" %}

{% block content %}
<h2>Daftar Artikel</h2>

{% for item in artikel %}
<div style="border:1px solid #ccc; padding:10px; margin-bottom:10px;">
    <p>Judul: {{ item.judul|default("Tidak ada judul") }}</p>
    <p>Kategori: {{ item.kategori }}</p>
</div>
{% endfor %}
{% endblock %}
```

---

# 🚀 Cara Menjalankan
```bash
uvicorn app.main:app --reload
```

Lalu buka:

- http://localhost:8000/empty1  
- http://localhost:8000/empty2  
- http://localhost:8000/empty3  
- http://localhost:8000/empty4  
- http://localhost:8000/empty5  

---

## 16. Tahap 14: HTML form dan Jinja2

Jinja2 juga sering dipakai di form HTML agar value default bisa diisi otomatis.

### Contoh form sederhana
```html
<form method="post">
  <input type="text" name="judul" value="{{ artikel.judul if artikel else '' }}">
  <textarea name="isi">{{ artikel.isi if artikel else '' }}</textarea>
  <button type="submit">Simpan</button>
</form>
```

### Penjelasan:
- `if artikel else ''` artinya kalau ada data, tampilkan data lama,
- kalau belum ada, tampilkan kosong.

### Ini cocok untuk:
- form tambah artikel,
- form edit data,
- form login,
- form upload.

---

## 17. Tahap 15: Jinja2 dengan URL dan route

Dalam aplikasi web, kita sering perlu menampilkan URL dinamis.

### Contoh:
```html
<a href="/artikel/{{ item.id }}">Lihat detail</a>
```

### Atau di backend
```python
return templates.TemplateResponse("detail.html", {"request": request, "item": item})
```

### Penting karena:
- setiap item punya link detail,
- halaman publik beragam sesuai data,
- route tidak harus ditulis satu per satu untuk semua artikel.

---

## 18. Tahap 16: Keunggulan Jinja2 untuk proyek besar

Jinja2 membuat aplikasi lebih terstruktur karena:
- data dipisahkan dari HTML,
- halaman bisa dibuat berulang tanpa menyalin banyak kode,
- struktur HTML konsisten,
- logic sederhana ada di template,
- backend hanya mengirim data yang relevan.

### Ini cocok untuk aplikasi seperti ini:
- landing page,
- profil desa,
- beranda,
- elibrary,
- dokumentasi,
- dashboard admin,
- form CRUD.

---

## 19. Praktik yang paling cocok untuk siswa SMA

Untuk belajar bertahap, siswa bisa mulai dari mini proyek kecil:

### Praktek 1: Tampilkan nama
```python
@app.get("/halo")
def halo(request: Request):
    return templates.TemplateResponse("halo.html", {"request": request, "nama": "Ari"})
```

```html
<h1>Halo {{ nama }}</h1>
```

### Praktek 2: Tampilkan daftar
```python
list_siswa = ["Ari", "Budi", "Cika"]
```

```html
<ul>
  {% for nama in list_siswa %}
    <li>{{ nama }}</li>
  {% endfor %}
</ul>
```

### Praktek 3: Kondisi login
```html
{% if login %}
  <p>Selamat datang</p>
{% else %}
  <p>Silakan masuk</p>
{% endif %}
```

### Praktek 4: Template dasar
- `base.html`
- `home.html`
- `profile.html`

### Praktek 5: Data artikel
- tampilkan daftar artikel dari Python list,
- tampilkan judul dan kategori,
- munculkan pesan jika kosong.

---

## 20. Ringkasan tahap belajar Jinja2

Tahap belajar Jinja2 yang paling logis adalah:

1. Pahami konsep template engine.
2. Setup FastAPI + Jinja2.
3. Gunakan variabel `{{ }}`.
4. Gunakan kondisi `{% if %}`.
5. Gunakan loop `{% for %}`.
6. Gunakan data object dan list.
7. Pahami empty state.
8. Gunakan template inheritance (`extends`).
9. Pakai include untuk komponen reusable.
10. Integrasikan dengan form dan data backend.

---

## 21. Hubungan Jinja2 dengan JavaScript

Setelah siswa paham Jinja2, maka masuk ke JavaScript akan terasa lebih mudah karena:

- Jinja2 membuat HTML dari data server,
- JavaScript membuat HTML menjadi interaktif di browser,
- keduanya saling melengkapi.

Contoh hubungan:

```text
Jinja2 menyiapkan daftar artikel di halaman
JavaScript menangkap klik pada tombol edit atau delete
FastAPI menerima request dan menyimpan data baru
```

Jinja2 memberitahu HTML apa yang harus ditampilkan, lalu JavaScript mengatur bagaimana user berinteraksi dengan halaman itu.

---

## 22. Kesimpulan

Jinja2 adalah tahap penting sebelum melangkah ke JavaScript lanjutan, karena siswa harus paham dulu:
- bagaimana data masuk ke template,
- bagaimana HTML dibuat dinamis,
- bagaimana halaman web dibangun dari backend.

Setelah itu, JavaScript akan lebih mudah dipahami sebagai alat untuk interaksi user, bukan sebagai cara utama untuk menampilkan data dari server.

Jinja2 = data masuk ke HTML.
JavaScript = interaksi di browser.
FastAPI = backend yang menyuplai data.

Itulah fondasi dari aplikasi web modern.

---

## 23. Catatan guru

Untuk pembelajaran SMA, Jinja2 sebaiknya diajarkan dengan pendekatan praktik:
- mulai dari variabel sederhana,
- lalu loop,
- lalu kondisi,
- lalu template dasar,
- lalu form dan data nyata,
- baru masuk ke interaksi JavaScript.

Pendekatan bertahap akan membuat siswa lebih paham, bukan sekadar menyalin kode.
