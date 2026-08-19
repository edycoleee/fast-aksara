# Pembelajaran 6 - Tahap 2

## Object -> Template Dinamis (FastAPI + Jinja)

Pembelajaran ini melanjutkan Pembelajaran 5 Tahap 1.
Jika sebelumnya siswa membuat HTML statis berbasis mockup, sekarang siswa belajar membuat halaman dinamis dengan data dari Python.

## A. Tujuan

- Siswa memahami alur data: object Python -> route FastAPI -> template Jinja -> halaman web.
- Siswa dapat menampilkan list data menggunakan loop Jinja.
- Siswa dapat melakukan filter kategori sederhana di backend.
- Siswa siap lanjut ke CRUD admin pada tahap berikutnya.

## B. Hasil Akhir

Di akhir pembelajaran ini, siswa mampu:

1. Membuat data dummy Python (list/dictionary).
2. Mengirim data ke template lewat `TemplateResponse`.
3. Menampilkan data di 9 halaman publik secara dinamis.
4. Menangani kondisi data kosong dengan `{% if %}`.

## C. Estimasi Waktu

- 2 sampai 4 pertemuan (180-360 menit).

## D. Alur Belajar

### Tahap 1 - Siapkan Data Python (30-45 menit)

Aktivitas:
- Membuat variabel data di route atau modul data.
- Gunakan struktur list of dict.

Output:
- Data `elibrary_items`, `dokumentasi_items`, `artikel_items` siap dipakai.

### Tahap 2 - Kirim Data ke Template (30-45 menit)

Aktivitas:
- Gunakan `templates.TemplateResponse()`.
- Kirim `request` dan variabel data ke template.

Output:
- Template sudah bisa menerima context.

### Tahap 3 - Render Dinamis di HTML (45-60 menit)

Aktivitas:
- Tulis loop Jinja: `{% for item in items %}`.
- Tulis fallback kosong: `{% if items %}` / `{% else %}`.

Output:
- Daftar konten tampil otomatis dari data Python.

### Tahap 4 - Filter Kategori di Backend (45-60 menit)

Aktivitas:
- Filter data `artikel`/`dokumentasi` per kategori (`tunas`, `karya`, `cakra`, `kersa`).

Output:
- Tiap halaman program menampilkan data kategori yang sesuai.

### Tahap 5 - Validasi Tampilan (30 menit)

Aktivitas:
- Uji semua route publik.
- Uji kondisi ada data dan data kosong.

Output:
- Semua halaman dinamis berjalan stabil.

### Jinja2 Dasar - Render Landing HTML (Praktik Cepat)

Tujuan mini-praktik:
- Siswa berhasil menampilkan 1 halaman `landing.html` dari route FastAPI menggunakan Jinja2.

Lokasi kerja:
- Folder proyek: `backend/`

#### 1) Siapkan Virtual Environment

Jalankan di terminal (Windows PowerShell):

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

####  Membuat file requirements.txt
```
fastapi
uvicorn[standard]
jinja2
sqlalchemy
python-multipart
python-jose[cryptography]
passlib[bcrypt]
bcrypt==4.0.1
python-dotenv
aiofiles
python-magic
```


```
pip install -r requirements.txt
```

Hasil yang diharapkan:
- Prompt terminal menampilkan `(.venv)`.
- Dependensi FastAPI dan Jinja2 terpasang.

#### 2) Buat atau Cek File Template Landing

Pastikan file ini ada:
- `backend/app/templates/landing.html`

Isi minimal:

```html
<!doctype html>
<html lang="id">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Landing</title>
</head>
<body>
	<h1>{{ program_info.nama_program }}</h1>
	<p>{{ program_info.tagline }}</p>

	<ul>
		{% for nama in program_info.program_inti %}
			<li>{{ nama }}</li>
		{% endfor %}
	</ul>
</body>
</html>
```

#### 3) Buat atau Cek Route Landing

Pastikan route mengirim data ke template.
Contoh minimal di router landing:

```python
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def landing(request: Request):
		program_info = {
				"nama_program": "Ngrembaka Aksara",
				"tagline": "Gerakan literasi berbasis kampung belajar",
				"program_inti": ["Tunas", "Karya", "Cakra", "Kersa"],
		}
		return templates.TemplateResponse(
				"landing.html",
				{"request": request, "program_info": program_info},
		)
```

Catatan penting:
- `request` wajib dikirim ke context template.
- Nama file template harus sama persis: `landing.html`.

#### 4) Jalankan Uvicorn

```powershell
uvicorn app.main:app --reload
```

Jika port `8000` sudah dipakai, gunakan:

```powershell
uvicorn app.main:app --reload --port 8002
```

#### 5) Akses Web di Browser

Buka salah satu:
- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8002/`

Jika berhasil, halaman menampilkan:
- Judul program dari `program_info.nama_program`
- Tagline dari `program_info.tagline`
- Daftar program inti dari loop Jinja

#### 6) Checklist Keberhasilan Praktik

1. Server `uvicorn` jalan tanpa error.
2. Route `/` bisa diakses.
3. Variabel Jinja tampil (bukan teks mentah `{{ ... }}`).
4. Loop daftar program muncul minimal 4 item.



## E. Struktur Konsep Folder

```text
backend/app/
|-- routers/
|   |-- landing.py
|   |-- beranda.py
|   |-- elibrary.py
|   |-- tunas.py
|   |-- karya.py
|   |-- cakra.py
|   |-- kersa.py
|-- templates/
|   |-- landing.html
|   |-- beranda.html
|   |-- profil_aksara.html
|   |-- profil_kelurahan.html
|   |-- elibrary.html
|   |-- tunas.html
|   |-- karya.html
|   |-- cakra.html
|   |-- kersa.html
```

## F. Kunci Dasar Route FastAPI

Contoh pola dasar route dinamis:

```python
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/contoh")
def contoh_page(request: Request):
		data = [{"judul": "Item 1"}, {"judul": "Item 2"}]
		return templates.TemplateResponse(
				"contoh.html",
				{"request": request, "items": data},
		)
```

## G. Kunci Dasar Template Jinja

Contoh loop dan empty state:

```html
{% if items %}
	{% for item in items %}
		<article>
			<h3>{{ item.judul }}</h3>
		</article>
	{% endfor %}
{% else %}
	<p>Belum ada data.</p>
{% endif %}
```

## H. Jawaban Detail per Halaman Publik

### 1) Landing (`/` -> `landing.html`)

Data backend:
- `program_info` berisi `nama_program`, `tagline`, `program_inti`.

Route kunci:

```python
@router.get("/")
def landing(request: Request):
		program_info = {
				"nama_program": "Ngrembaka Aksara",
				"tagline": "Gerakan literasi berbasis kampung belajar",
				"program_inti": ["Tunas", "Karya", "Cakra", "Kersa"],
		}
		return templates.TemplateResponse(
				"landing.html",
				{"request": request, "program_info": program_info},
		)
```

Template kunci:

```html
<h1>{{ program_info.nama_program }}</h1>
<p>{{ program_info.tagline }}</p>
<ul>
	{% for nama in program_info.program_inti %}
		<li>{{ nama }}</li>
	{% endfor %}
</ul>
```

### 2) Beranda (`/beranda` -> `beranda.html`)

Data backend:
- `profil_program`: `visi`, `tujuan`.

Template kunci:

```html
<h2>Visi</h2>
<p>{{ profil_program.visi }}</p>
<h2>Tujuan</h2>
<ol>
	{% for item in profil_program.tujuan %}
		<li>{{ item }}</li>
	{% endfor %}
</ol>
```

### 3) Profil Aksara (`/profil/ngrembaka-aksara` -> `profil_aksara.html`)

Data backend:
- `profil_program`.
- `sasaran_program` list dict.

Template kunci:

```html
<table>
	<tr><th>Kelompok</th><th>Fokus</th></tr>
	{% for row in sasaran_program %}
		<tr>
			<td>{{ row.kelompok }}</td>
			<td>{{ row.fokus }}</td>
		</tr>
	{% endfor %}
</table>
```

### 4) Profil Kelurahan (`/profil/kelurahan-podorejo` -> `profil_kelurahan.html`)

Data backend:
- `profil_kelurahan` dict.

Template kunci:

```html
<h1>Profil Kelurahan {{ profil_kelurahan.nama_kelurahan }}</h1>
<ul>
	<li>Penduduk: {{ profil_kelurahan.jumlah_penduduk }}</li>
	<li>RW: {{ profil_kelurahan.jumlah_rw }}</li>
</ul>
```

### 5) E-Library (`/elibrary` -> `elibrary.html`)

Data backend:
- `elibrary_items` list dict.

Route kunci:

```python
@router.get("/elibrary")
def elibrary(request: Request):
		elibrary_items = [
				{
						"judul": "Panduan Menulis Cerita",
						"kategori": "Literasi",
						"deskripsi": "Materi dasar menulis cerita",
						"link": "panduan-menulis.pdf",
						"link_type": "internal",
				}
		]
		return templates.TemplateResponse(
				"elibrary.html",
				{"request": request, "items": elibrary_items},
		)
```

Template kunci:

```html
{% if items %}
	{% for item in items %}
		<article>
			<h3>{{ item.judul }}</h3>
			<p>Kategori: {{ item.kategori }}</p>
			<p>{{ item.deskripsi }}</p>
			{% if item.link_type == "internal" %}
				<a href="{{ item.link }}">Unduh PDF</a>
			{% else %}
				<a href="{{ item.link }}">Tonton</a>
			{% endif %}
		</article>
	{% endfor %}
{% else %}
	<p>Belum ada koleksi.</p>
{% endif %}
```

### 6) Tunas (`/pojok-literasi/tunas` -> `tunas.html`)

Data backend:
- `dokumentasi_tunas` hasil filter kategori `tunas`.
- `artikel_tunas` hasil filter kategori `tunas`.

Route kunci:

```python
dokumentasi_tunas = [d for d in dokumentasi_items if d["kategori"] == "tunas"]
artikel_tunas = [a for a in artikel_items if a["kategori"] == "tunas"]
```

Template kunci:

```html
<h2>Dokumentasi</h2>
{% for item in dokumentasi_tunas %}
	<article>
		<h3>{{ item.judul }}</h3>
		<p>{{ item.deskripsi }}</p>
	</article>
{% endfor %}
```

### 7) Karya (`/pojok-literasi/karya` -> `karya.html`)

Data backend:
- `dokumentasi_karya`.
- `artikel_karya`.

Template kunci:

```html
{% if dokumentasi_karya %}
	{% for item in dokumentasi_karya %}
		<article>
			<h3>{{ item.judul }}</h3>
			<p>{{ item.deskripsi }}</p>
		</article>
	{% endfor %}
{% else %}
	<p>Belum ada karya.</p>
{% endif %}
```

### 8) Cakra (`/pojok-literasi/cakra` -> `cakra.html`)

Data backend:
- `materi_program` list dict.
- `artikel_cakra`.

Template kunci:

```html
<table>
	<tr><th>No</th><th>Materi</th><th>Target</th></tr>
	{% for m in materi_program %}
		<tr>
			<td>{{ loop.index }}</td>
			<td>{{ m.materi }}</td>
			<td>{{ m.target }}</td>
		</tr>
	{% endfor %}
</table>
```

### 9) Kersa (`/pojok-literasi/kersa` -> `kersa.html`)

Data backend:
- `artikel_kersa`.

Template kunci:

```html
{% if artikel_kersa %}
	{% for item in artikel_kersa %}
		<article>
			<h3>{{ item.judul }}</h3>
			<p>{{ item.deskripsi }}</p>
		</article>
	{% endfor %}
{% else %}
	<p>Belum ada artikel kesehatan/keterampilan.</p>
{% endif %}
```

## I. Checklist Penilaian

1. Semua route publik menerima `request` dan mengirim context ke template.
2. Semua template publik memakai Jinja (`{{ }}` dan `{% %}`).
3. Minimal 3 halaman memakai loop dengan benar.
4. Minimal 2 halaman memakai empty state.
5. Filter kategori di halaman program berjalan sesuai tujuan.

Skor per poin: 1-4.
Nilai akhir: rata-rata seluruh poin.

## J. Tugas Praktik Siswa

1. Ubah minimal 2 data dummy dan lihat perubahan langsung di halaman.
2. Tambahkan 1 item baru ke `elibrary_items` dan pastikan tampil otomatis.
3. Kosongkan sementara `artikel_kersa`, lalu cek apakah empty state muncul.
4. Tambahkan 1 kategori baru dan diskusikan dampaknya ke filter halaman.

## K. Penutup

Setelah Pembelajaran 6:

- Siswa memahami konsep dinamis dari backend ke frontend.
- Siswa siap lanjut ke Pembelajaran 7: CRUD sederhana (create/read/update/delete) untuk konten.
