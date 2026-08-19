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

## CRUD OBJECT TODO-LIST

Bagian ini fokus untuk memahami alur lengkap:

1. Data object disiapkan di Python.
2. Data dikirim ke template pakai Jinja.
3. JavaScript dipakai untuk interaksi tombol (edit/hapus) tanpa bingung ganti halaman.

### A. Tujuan Mini Proyek

- Siswa paham peran masing-masing: FastAPI, Jinja, JavaScript.
- Siswa bisa membuat CRUD sederhana untuk object `Todo`.
- Siswa bisa membaca alur data dari backend ke frontend lalu balik lagi ke backend.

### B. Alur Konsep (Wajib Dipahami)

1. Browser request ke route `GET /todo`.
2. FastAPI siapkan list object todo.
3. FastAPI render `todo.html` dengan Jinja.
4. Siswa klik tombol Edit/Hapus.
5. JavaScript mengisi form edit atau submit form hapus.
6. Route `POST` memproses data lalu redirect kembali ke `/todo`.

### C. Struktur File Mini Praktik

```text
backend/app/
|-- routers/
|   |-- todo.py
|-- templates/
|   |-- todo.html
```

### D. Step 1 - Object Todo di Router (Python)

Contoh object sederhana (sementara pakai memori):

```python
# app/routers/todo.py
from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

todos = [
		{"id": 1, "title": "Belajar Jinja", "done": False},
		{"id": 2, "title": "Latihan JavaScript", "done": True},
]


@router.get("/todo")
def todo_page(request: Request):
		return templates.TemplateResponse("todo.html", {"request": request, "todos": todos})
```

### E. Step 2 - Create, Update, Delete Route

```python
@router.post("/todo/create")
def todo_create(title: str = Form(...)):
		new_id = max([t["id"] for t in todos], default=0) + 1
		todos.append({"id": new_id, "title": title, "done": False})
		return RedirectResponse(url="/todo", status_code=303)


@router.post("/todo/update")
def todo_update(todo_id: int = Form(...), title: str = Form(...), done: str = Form("false")):
		for t in todos:
				if t["id"] == todo_id:
						t["title"] = title
						t["done"] = done == "true"
						break
		return RedirectResponse(url="/todo", status_code=303)


@router.post("/todo/delete")
def todo_delete(todo_id: int = Form(...)):
		idx = next((i for i, t in enumerate(todos) if t["id"] == todo_id), None)
		if idx is not None:
				todos.pop(idx)
		return RedirectResponse(url="/todo", status_code=303)
```

### F. Step 3 - Template Jinja + JavaScript

```html
<!doctype html>
<html lang="id">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>CRUD Todo</title>
</head>
<body>
	<h1>CRUD Object Todo-List</h1>

	<h2>Tambah Todo</h2>
	<form method="post" action="/todo/create">
		<input type="text" name="title" placeholder="Tulis todo..." required />
		<button type="submit">Tambah</button>
	</form>

	<h2>Edit Todo</h2>
	<form id="editForm" method="post" action="/todo/update">
		<input type="hidden" name="todo_id" id="edit_id" />
		<input type="text" name="title" id="edit_title" placeholder="Judul todo" required />
		<select name="done" id="edit_done">
			<option value="false">Belum</option>
			<option value="true">Selesai</option>
		</select>
		<button type="submit">Update</button>
	</form>

	<h2>Daftar Todo</h2>
	{% if todos %}
		<ul>
			{% for t in todos %}
			<li>
				<strong>{{ t.title }}</strong>
				- {% if t.done %}Selesai{% else %}Belum{% endif %}

				<button
					type="button"
					class="btn-edit"
					data-id="{{ t.id }}"
					data-title="{{ t.title }}"
					data-done="{{ 'true' if t.done else 'false' }}"
				>
					Edit
				</button>

				<form method="post" action="/todo/delete" style="display:inline;">
					<input type="hidden" name="todo_id" value="{{ t.id }}" />
					<button type="submit">Hapus</button>
				</form>
			</li>
			{% endfor %}
		</ul>
	{% else %}
		<p>Belum ada todo.</p>
	{% endif %}

	<script>
		const editButtons = document.querySelectorAll('.btn-edit');
		const editId = document.getElementById('edit_id');
		const editTitle = document.getElementById('edit_title');
		const editDone = document.getElementById('edit_done');

		editButtons.forEach((btn) => {
			btn.addEventListener('click', () => {
				editId.value = btn.dataset.id;
				editTitle.value = btn.dataset.title;
				editDone.value = btn.dataset.done;
				editTitle.focus();
			});
		});
	</script>
</body>
</html>
```

### G. Kenapa Perlu JavaScript di Sini?

- Jinja bekerja saat server render HTML.
- JavaScript bekerja setelah halaman tampil di browser.
- Pada contoh ini, JavaScript membantu mengisi form edit otomatis saat tombol Edit diklik.

Ringkasnya:
- Jinja: menampilkan data awal.
- JavaScript: interaksi pengguna di halaman.

### H. Checklist Keberhasilan CRUD Todo

1. `GET /todo` menampilkan daftar todo dari object Python.
2. Form tambah bisa menambah data baru.
3. Tombol Edit bisa mengisi form update.
4. Update berhasil mengubah judul/status.
5. Hapus berhasil mengurangi data.
6. Setelah aksi POST, halaman kembali ke `/todo`.

### I. Latihan Lanjutan

1. Tambahkan field `deadline` pada object todo.
2. Tambahkan filter tampilan: semua, selesai, belum.
3. Tambahkan validasi: judul minimal 3 karakter.
4. Ubah tampilan list menjadi tabel.


## Integrasi Action Button -> API Backend -> Render Ulang Tabel

Ya, intinya memang seperti itu.
Supaya benar-benar paham, lihat alur detail berikut.

### A. Gambaran Besar Alur

1. User klik tombol aksi di halaman (`Tambah`, `Update`, `Hapus`).
2. Browser mengirim request `POST` ke route backend.
3. Backend mengubah data object (create/update/delete).
4. Backend melakukan `RedirectResponse` ke route `GET /todo`.
5. Route `GET /todo` render ulang template Jinja.
6. Tabel/list tampil lagi dengan data terbaru.

Kesimpulan:
- Tombol aksi tidak langsung mengubah HTML permanen di browser.
- Perubahan final selalu berasal dari backend, lalu dirender ulang oleh Jinja.

### B. Detail per Tombol

#### 1) Tombol Tambah

Frontend:
- Form `action="/todo/create" method="post"`.

Backend:
- Route `/todo/create` menerima `title`.
- Backend menambah object baru ke `todos`.
- Backend redirect ke `/todo`.

Hasil di UI:
- Item baru muncul saat halaman `/todo` dirender ulang.

#### 2) Tombol Edit + Update

Frontend (JavaScript):
- Tombol `Edit` membawa `data-id`, `data-title`, `data-done`.
- JavaScript isi form update secara otomatis (`edit_id`, `edit_title`, `edit_done`).

Backend:
- Form update kirim ke `/todo/update`.
- Backend cari `todo_id` yang cocok.
- Backend ubah nilai `title` dan `done`.
- Backend redirect ke `/todo`.

Hasil di UI:
- Baris data berubah sesuai hasil update.

#### 3) Tombol Hapus

Frontend:
- Tombol `Hapus` kirim `todo_id` ke `/todo/delete`.

Backend:
- Backend cari index item berdasarkan `todo_id`.
- Item dihapus dari list.
- Backend redirect ke `/todo`.

Hasil di UI:
- Data hilang dari tabel/list setelah render ulang.

### C. Bedakan Peran Jinja dan JavaScript

Peran Jinja:
- Menampilkan data dari backend saat halaman dibuat.
- Menentukan struktur data yang tampil (`for`, `if`, `else`).

Peran JavaScript:
- Membantu interaksi instan di browser.
- Contoh di sini: mengisi form edit tanpa pindah halaman.

Aturan mudah mengingat:
- Jinja = server-side rendering.
- JavaScript = browser-side interaction.

### D. Kenapa Harus Redirect Setelah POST?

Alasan utama:
- Mencegah form terkirim ulang saat user refresh.
- Menjaga pola standar web: POST -> Redirect -> GET.
- Memastikan tampilan selalu mengambil data terbaru dari backend.

Pola ini disebut:
- PRG (`Post/Redirect/Get`).

### E. Contoh Urutan Nyata (Simulasi)

Skenario: user menambah todo "Belajar API".

1. User isi form tambah lalu klik `Tambah`.
2. Browser kirim `POST /todo/create`.
3. Backend menambahkan object:
	- `{"id": 3, "title": "Belajar API", "done": False}`
4. Backend kirim redirect ke `GET /todo`.
5. Jinja loop data terbaru.
6. List sekarang berisi 3 item.

### F. Checklist Pemahaman Siswa

Siswa dianggap paham jika bisa menjawab:

1. Setelah klik tombol `Tambah`, route mana yang menerima data?
2. Kenapa setelah `POST` tidak langsung return HTML, tetapi redirect dulu?
3. Bagian mana yang dikerjakan Jinja, mana yang dikerjakan JavaScript?
4. Kenapa data di tabel bisa berubah walau template HTML tidak ditulis ulang manual?

### G. Error Umum dan Cara Cek

1. Data tidak berubah setelah submit:
- Cek route `POST` benar atau tidak.
- Cek nama field form sama dengan parameter `Form(...)`.

2. Tombol Edit tidak mengisi form:
- Cek atribut `data-id`, `data-title`, `data-done` ada di tombol.
- Cek ID input JS sama: `edit_id`, `edit_title`, `edit_done`.

3. Halaman kosong setelah aksi:
- Cek redirect menuju `/todo`.
- Cek route `GET /todo` mengirim `todos` ke template.
