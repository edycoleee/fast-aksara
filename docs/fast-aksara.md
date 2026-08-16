# Rencana Pembangunan Web Ngrembaka Aksara
## FastAPI + Jinja2 + SQLite + Admin CMS

---

## TAHAP 1 — Setup Project

### 1.1 Struktur Folder
```
fast-aksara/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── routers/
│   │   ├── landing.py
│   │   ├── beranda.py
│   │   ├── profil_aksara.py
│   │   ├── profil_kelurahan.py
│   │   ├── elibrary.py
│   │   ├── tunas.py
│   │   ├── karya.py
│   │   ├── cakra.py
│   │   ├── kersa.py
│   │   └── admin.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── landing.html
│   │   ├── beranda.html
│   │   ├── profil_aksara.html
│   │   ├── profil_kelurahan.html
│   │   ├── elibrary.html
│   │   ├── tunas.html
│   │   ├── karya.html
│   │   ├── cakra.html
│   │   ├── kersa.html
│   │   └── admin/
│   │       ├── login.html
│   │       ├── dashboard.html
│   │       ├── elibrary_form.html
│   │       ├── dokumentasi_form.html
│   │       └── artikel_form.html
│   └── static/
│       ├── css/
│       │   └── style.css
│       ├── js/
│       │   └── main.js
│       ├── images/
│       └── uploads/
│           ├── images/      ← gambar thumbnail & foto kegiatan (lokal)
│           └── pdf/         ← modul, ebook, artikel PDF (lokal)
├── aksara.db
├── requirements.txt
└── .env
```

### 1.2 Dependensi (requirements.txt)
```
fastapi
uvicorn[standard]
jinja2
sqlalchemy
python-multipart
python-jose[cryptography]
passlib[bcrypt]
python-dotenv
aiofiles
python-magic        # validasi MIME type file upload
```

### 1.3 Strategi Storage — Hybrid Mode

| Jenis Konten | Disimpan Di | Keterangan |
|---|---|---|
| Gambar thumbnail | `static/uploads/images/` (lokal) | jpg/png/webp, maks 2 MB |
| PDF modul/ebook/artikel | `static/uploads/pdf/` (lokal) | maks 20 MB |
| Video pembelajaran | YouTube (embed) | Hanya simpan URL YouTube di DB |
| Video dokumentasi kegiatan | YouTube (embed) | Hanya simpan URL YouTube di DB |

**Alasan Hybrid:**
- PDF dan gambar berukuran kecil, aman disimpan lokal di server
- Video berukuran besar → tetap di YouTube, web hanya embed `<iframe>`
- Hemat disk server, tidak perlu object storage berbayar di tahap awal
- Bisa dimigrasi ke Cloudflare R2 / Backblaze B2 di kemudian hari tanpa ubah skema DB

---

## TAHAP 2 — Database Layer

### 2.1 `database.py`
- Buat koneksi SQLite dengan SQLAlchemy
- Buat `SessionLocal` (session factory)
- Buat `Base` (deklaratif model)
- Fungsi `get_db()` sebagai dependency injection FastAPI

### 2.2 `models.py` — Tabel SQLite

**Tabel `elibrary`**
| Kolom       | Tipe    | Keterangan                                         |
|-------------|---------|---------------------------------------------------|
| id          | Integer | Primary key, autoincrement                        |
| kategori    | String  | modul-pembelajaran / ebook / buku-cerita / buku-literasi-digital / buku-keterampilan |
| judul       | String  | Judul resource                                    |
| deskripsi   | Text    | Deskripsi singkat                                 |
| link        | String  | URL YouTube (video) **atau** path PDF lokal       |
| link_type   | String  | `external` (YouTube/URL) / `internal` (file lokal)|
| gambar      | String  | Path gambar thumbnail lokal                       |
| created_at  | DateTime| Waktu dibuat                                      |

**Tabel `dokumentasi`**
| Kolom       | Tipe    | Keterangan                                         |
|-------------|---------|---------------------------------------------------|
| id          | Integer | Primary key, autoincrement                        |
| kategori    | String  | dokumentasi-tunas / karya-digital / karya-media-sosial / gambar-carosel |
| judul       | String  | Judul dokumentasi                                 |
| deskripsi   | Text    | Deskripsi kegiatan                                |
| link_gambar | String  | Path gambar lokal (`static/uploads/images/...`)   |
| link_video  | String  | URL YouTube embed (opsional, jika ada video)      |
| created_at  | DateTime| Waktu dibuat                                      |

**Tabel `artikel`**
| Kolom       | Tipe    | Keterangan                                         |
|-------------|---------|---------------------------------------------------|
| id          | Integer | Primary key, autoincrement                        |
| kategori    | String  | artikel-tunas / artikel-cakra / artikel-kersa-kesehatan / artikel-kersa-keterampilan |
| judul       | String  | Judul artikel                                     |
| deskripsi   | Text    | Deskripsi singkat                                 |
| link_pdf    | String  | Path PDF artikel                                  |
| gambar      | String  | Path gambar cover                                 |
| created_at  | DateTime| Waktu dibuat                                      |

**Tabel `admin_user`**
| Kolom        | Tipe    | Keterangan              |
|--------------|---------|-------------------------|
| id           | Integer | Primary key             |
| username     | String  | Username unik           |
| hashed_password | String | Password di-hash bcrypt |

---

## TAHAP 3 — Routing & Halaman Publik

Setiap router menangani satu halaman, mengambil data dari SQLite, lalu me-render template Jinja2.

| Router               | Path URL                        | Data dari DB                        |
|----------------------|---------------------------------|-------------------------------------|
| `landing.py`         | `/`                             | elibrary (5 kategori), artikel      |
| `beranda.py`         | `/beranda`                      | —  (konten statis)                  |
| `profil_aksara.py`   | `/profil/ngrembaka-aksara`      | — (konten statis)                   |
| `profil_kelurahan.py`| `/profil/kelurahan-podorejo`    | — (konten statis)                   |
| `elibrary.py`        | `/elibrary`                     | elibrary (semua kategori)           |
| `elibrary.py`        | `/elibrary/{kategori}`          | elibrary filter by kategori         |
| `tunas.py`           | `/pojok-literasi/tunas`         | dokumentasi-tunas, artikel-tunas    |
| `karya.py`           | `/pojok-literasi/karya`         | karya-digital, karya-media-sosial   |
| `cakra.py`           | `/pojok-literasi/cakra`         | artikel-cakra                       |
| `kersa.py`           | `/pojok-literasi/kersa`         | artikel-kersa-kesehatan, artikel-kersa-keterampilan |

---

## TAHAP 4 — Template Frontend

### 4.1 `base.html`
- Navbar: Logo + menu Beranda, Profil, E-Library, Pojok Literasi + CTA "Hubungi Kami"
- Footer: Google Maps embed, kontak, link WhatsApp, hak cipta
- CDN: Bootstrap 5 + Font Awesome 6 + Google Fonts
- Font: Inter/Poppins (Google Fonts) — bersih dan mudah dibaca

### 4.1.1 Palet Warna Tema

| Peran | Hex | Penggunaan |
|---|---|---|
| Background / Surface | `#E8F5E9` | Background section, card background |
| Accent Light | `#A5D6A7` | Border card, hover state, divider |
| Primary | `#66BB6A` | Tombol utama, badge, icon aktif |
| Primary Dark | `#1B5E20` | Navbar, footer, heading utama, CTA |

```css
:root {
  --color-bg:        #E8F5E9;
  --color-accent:    #A5D6A7;
  --color-primary:   #66BB6A;
  --color-dark:      #1B5E20;
  --color-white:     #FFFFFF;
  --color-text:      #1B5E20;
}
```

**Penerapan per komponen:**
- **Navbar & Footer**: background `#1B5E20`, teks putih
- **Hero Section**: background `#1B5E20`, teks putih
- **Section background**: bergantian `#FFFFFF` dan `#E8F5E9`
- **Card**: background putih, border-left `#66BB6A`, shadow ringan
- **Tombol primer**: background `#66BB6A`, hover `#1B5E20`
- **Tombol outline**: border `#66BB6A`, teks `#1B5E20`
- **Badge/tag kategori**: background `#A5D6A7`, teks `#1B5E20`

### 4.2 Komponen Reusable (Jinja2 Macro)
- **Card E-Library**: gambar thumbnail, judul, deskripsi, tombol link
- **Card Dokumentasi**: gambar kegiatan, judul, deskripsi
- **Card Artikel**: gambar cover, judul, deskripsi, tombol unduh PDF
- **Card Profil**: gambar, judul, deskripsi singkat, tombol "Selengkapnya"

### 4.3 Responsif
- Mobile-first layout menggunakan grid Bootstrap
- Navbar collapse untuk mobile
- Gambar fluid dan card stack di layar kecil

---

## TAHAP 5 — Admin CMS

### 5.1 Autentikasi
- Halaman login `/admin/login` (form username + password)
- Password di-hash dengan `bcrypt` via `passlib`
- Setelah login, token JWT disimpan di **HTTP-only cookie** (aman dari XSS)
- Semua route `/admin/*` dilindungi middleware `verify_token`
- Logout menghapus cookie

### 5.2 Dashboard Admin `/admin`
- Ringkasan jumlah data: total E-Library, dokumentasi, artikel
- Menu navigasi ke CRUD tiap tabel

### 5.3 CRUD E-Library `/admin/elibrary`
- List semua data dengan filter kategori
- Form tambah: judul, kategori (dropdown), deskripsi, upload gambar, link/upload PDF
- Form edit (isi otomatis dari data existing)
- Tombol hapus dengan konfirmasi

### 5.4 CRUD Dokumentasi `/admin/dokumentasi`
- List semua data dengan filter kategori
- Form tambah: judul, kategori (dropdown), deskripsi, upload gambar
- Form edit & hapus

### 5.5 CRUD Artikel `/admin/artikel`
- List semua data dengan filter kategori
- Form tambah: judul, kategori (dropdown), deskripsi, upload gambar cover, upload PDF
- Form edit & hapus

### 5.6 Upload File — Hybrid Mode

**File yang diupload lokal (disimpan di server):**
- Gambar thumbnail & foto kegiatan → `static/uploads/images/`
- PDF modul, ebook, artikel → `static/uploads/pdf/`

**File yang tidak diupload (embed eksternal):**
- Video pembelajaran & dokumentasi → input berupa URL YouTube, disimpan sebagai teks di DB
- Di template, URL YouTube dikonversi otomatis ke format embed `https://www.youtube.com/embed/{id}`

**Aturan validasi upload:**
- Cek MIME type dengan `python-magic` (bukan hanya ekstensi)
- Gambar: hanya `image/jpeg`, `image/png`, `image/webp`, maks **2 MB**
- PDF: hanya `application/pdf`, maks **20 MB**
- Nama file di-rename dengan UUID agar tidak bisa ditebak
- File lama dihapus dari disk saat data di-edit atau dihapus

---

## TAHAP 6 — Konfigurasi & Keamanan

- File `.env` menyimpan: `SECRET_KEY`, `ADMIN_USERNAME`, `ADMIN_PASSWORD_HASH`, `MAX_UPLOAD_IMAGE_MB`, `MAX_UPLOAD_PDF_MB`
- `SECRET_KEY` digunakan untuk signing JWT
- Static files dilayani oleh FastAPI `StaticFiles` mount
- Folder `static/uploads/` hanya boleh berisi gambar dan PDF — tidak ada file executable
- Database file `aksara.db` tidak diekspos ke publik
- CORS dikonfigurasi hanya untuk origin yang diizinkan
- Validasi MIME type dilakukan di backend dengan `python-magic` (tidak percaya header dari client)

---

## TAHAP 7 — Auto-Seed via Startup Event (Singleton)

Tidak menggunakan `seed.py` manual. Akun admin dibuat otomatis saat aplikasi pertama kali dijalankan melalui **FastAPI lifespan**:

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)  # buat tabel
    _seed_admin()                           # buat akun admin jika belum ada
    yield
```

- `_seed_admin()` membaca `ADMIN_USERNAME` dan `ADMIN_PASSWORD` dari `.env`
- Jika akun sudah ada → dilewati (aman dijalankan berulang)
- Di production: cukup set `.env` lalu jalankan `uvicorn` — akun admin terbuat otomatis
- Tidak ada script manual yang harus diingat

**Catatan dependensi:** pin `bcrypt==4.0.1` karena bcrypt 4.x+ konflik dengan passlib.

## TAHAP 9 — Upload File Lokal (Hybrid Mode)

Admin CMS saat ini hanya menerima input URL teks. Tahap ini mengimplementasikan upload file nyata ke server.

### 9.1 Upload Gambar (di form E-Library, Dokumentasi, Artikel)
- Input `<input type="file">` di form admin
- Backend: terima `UploadFile` dari FastAPI
- Validasi MIME type dengan `python-magic`
- Rename file dengan UUID, simpan ke `static/uploads/images/`
- Simpan path relatif ke DB (contoh: `/static/uploads/images/abc123.jpg`)
- File lama dihapus dari disk saat data diedit atau dihapus

### 9.2 Upload PDF (di form E-Library dan Artikel)
- Input `<input type="file" accept=".pdf">` di form admin
- Validasi MIME type: hanya `application/pdf`, maks 20 MB
- Rename dengan UUID, simpan ke `static/uploads/pdf/`
- Simpan path relatif ke DB

### 9.3 Helper `upload.py`
Buat `app/upload.py` sebagai modul reusable:
```python
async def save_image(file: UploadFile) -> str  # return path
async def save_pdf(file: UploadFile) -> str    # return path
def delete_file(path: str) -> None             # hapus file lama
```

---

## TAHAP 10 — Testing & Deploy

1. Upload project ke server (VPS/Hostinger/Railway/Render)
2. Install dependensi: `pip install -r requirements.txt`
3. Jalankan: `uvicorn app.main:app --host 0.0.0.0 --port 8000`
4. Konfigurasi Nginx sebagai reverse proxy (jika VPS)
5. Pastikan folder `static/uploads/` dan file `aksara.db` berada di **persistent storage** (tidak ikut container reset)
6. Backup berkala untuk `aksara.db` + folder `uploads/` (PDF & gambar lokal)

### Catatan Skalabilitas Storage
- Tahap awal: storage lokal di server sudah cukup
- Jika konten PDF & gambar tumbuh besar (>5 GB): migrasi ke **Cloudflare R2** (gratis 10 GB/bulan) atau **Backblaze B2**
- Migrasi tidak perlu ubah skema DB — cukup ganti nilai kolom `link` dari path lokal ke URL object storage

---

## Urutan Eksekusi

1. [x] Setup folder & `requirements.txt`
2. [x] `database.py` + `models.py`
3. [x] `main.py` (entry point + auto-seed lifespan)
4. [x] `base.html` + `style.css` (tema hijau, palet 4 warna)
5. [x] Router + template Landing Page
6. [x] Router + template Beranda
7. [x] Router + template Profil (2 halaman konten penuh)
8. [x] Router + template E-Library (filter kategori)
9. [x] Router + template 4 Pojok Literasi
10. [x] Admin: autentikasi JWT HTTP-only cookie (login/logout)
11. [x] Admin: CRUD E-Library
12. [x] Admin: CRUD Dokumentasi
13. [x] Admin: CRUD Artikel
14. [x] Auto-seed admin via lifespan (singleton, baca dari .env)
15. [ ] Upload file lokal: gambar & PDF (Tahap 9)
16. [ ] Testing & deploy (Tahap 8)
