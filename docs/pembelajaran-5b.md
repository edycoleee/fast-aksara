# Lanjutan Jinja + CRUD dengan SQLite

Dokumen ini melanjutkan `pembelajaran-5a.md`.
Jika sebelumnya CRUD Todo masih pakai list Python (in-memory), sekarang kita pindahkan ke SQLite supaya data tersimpan permanen.

## A. Tujuan

- Siswa memahami kenapa butuh database.
- Siswa bisa membuat tabel Todo di SQLite dengan SQLAlchemy.
- Siswa bisa menjalankan CRUD Todo dari form Jinja ke database.
- Siswa bisa melihat perubahan data tetap ada setelah server restart.

## B. Alur Konsep

1. User klik tombol pada halaman Todo.
2. Request masuk ke route FastAPI.
3. Route menjalankan query SQLAlchemy ke SQLite.
4. Hasil query dikirim ke template Jinja.
5. Jinja render ulang tabel/list Todo.

## C. Struktur File Mini Praktik

```text
backend/app/
|-- database.py
|-- models_todo.py
|-- routers/
|   |-- todo_sqlite.py
|-- templates/
|   |-- todo_sqlite.html
```

## D. Step 1 - Konfigurasi SQLite

File `backend/app/database.py`:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./todo.db"

engine = create_engine(
		DATABASE_URL,
		connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
		db = SessionLocal()
		try:
				yield db
		finally:
				db.close()
```

Catatan:
- File database akan terbentuk sebagai `todo.db` di folder `backend/` saat tabel dibuat.

## E. Step 2 - Buat Model Todo

File `backend/app/models_todo.py`:

```python
from sqlalchemy import Boolean, Column, Integer, String
from app.database import Base


class Todo(Base):
		__tablename__ = "todos"

		id = Column(Integer, primary_key=True, index=True)
		title = Column(String(200), nullable=False)
		done = Column(Boolean, default=False, nullable=False)
```

## F. Step 3 - Buat Route CRUD SQLite

File `backend/app/routers/todo_sqlite.py`:

```python
from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models_todo import Todo

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Buat tabel jika belum ada
Base.metadata.create_all(bind=engine)


@router.get("/todo-sqlite")
def todo_page(request: Request, db: Session = Depends(get_db)):
		todos = db.query(Todo).order_by(Todo.id.desc()).all()
		return templates.TemplateResponse(
				"todo_sqlite.html",
				{"request": request, "todos": todos, "edit_item": None},
		)


@router.post("/todo-sqlite/create")
def todo_create(title: str = Form(...), db: Session = Depends(get_db)):
		db.add(Todo(title=title, done=False))
		db.commit()
		return RedirectResponse(url="/todo-sqlite", status_code=303)


@router.get("/todo-sqlite/edit/{todo_id}")
def todo_edit(todo_id: int, request: Request, db: Session = Depends(get_db)):
		todos = db.query(Todo).order_by(Todo.id.desc()).all()
		edit_item = db.query(Todo).filter(Todo.id == todo_id).first()
		return templates.TemplateResponse(
				"todo_sqlite.html",
				{"request": request, "todos": todos, "edit_item": edit_item},
		)


@router.post("/todo-sqlite/update/{todo_id}")
def todo_update(
		todo_id: int,
		title: str = Form(...),
		done: str = Form("false"),
		db: Session = Depends(get_db),
):
		item = db.query(Todo).filter(Todo.id == todo_id).first()
		if item:
				item.title = title
				item.done = done == "true"
				db.commit()
		return RedirectResponse(url="/todo-sqlite", status_code=303)


@router.post("/todo-sqlite/delete/{todo_id}")
def todo_delete(todo_id: int, db: Session = Depends(get_db)):
		item = db.query(Todo).filter(Todo.id == todo_id).first()
		if item:
				db.delete(item)
				db.commit()
		return RedirectResponse(url="/todo-sqlite", status_code=303)
```

## G. Step 4 - Template Jinja Todo SQLite

File `backend/app/templates/todo_sqlite.html`:

```html
<!doctype html>
<html lang="id">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>CRUD Todo SQLite</title>
</head>
<body>
	<h1>CRUD Todo SQLite</h1>

	{% if edit_item %}
		<h2>Edit Todo</h2>
		<form method="post" action="/todo-sqlite/update/{{ edit_item.id }}">
			<input type="text" name="title" value="{{ edit_item.title }}" required />
			<select name="done">
				<option value="false" {% if not edit_item.done %}selected{% endif %}>Belum</option>
				<option value="true" {% if edit_item.done %}selected{% endif %}>Selesai</option>
			</select>
			<button type="submit">Update</button>
			<a href="/todo-sqlite">Batal</a>
		</form>
	{% else %}
		<h2>Tambah Todo</h2>
		<form method="post" action="/todo-sqlite/create">
			<input type="text" name="title" placeholder="Tulis todo..." required />
			<button type="submit">Tambah</button>
		</form>
	{% endif %}

	<h2>Daftar Todo</h2>
	{% if todos %}
		<table border="1" cellpadding="8" cellspacing="0">
			<tr>
				<th>No</th>
				<th>Judul</th>
				<th>Status</th>
				<th>Aksi</th>
			</tr>
			{% for t in todos %}
			<tr>
				<td>{{ loop.index }}</td>
				<td>{{ t.title }}</td>
				<td>{% if t.done %}Selesai{% else %}Belum{% endif %}</td>
				<td>
					<a href="/todo-sqlite/edit/{{ t.id }}">Edit</a>
					<form method="post" action="/todo-sqlite/delete/{{ t.id }}" style="display:inline;">
						<button type="submit">Hapus</button>
					</form>
				</td>
			</tr>
			{% endfor %}
		</table>
	{% else %}
		<p>Belum ada todo.</p>
	{% endif %}
</body>
</html>
```

## H. Step 5 - Daftarkan Router di Main

Di `backend/app/main.py`, pastikan router di-include:

```python
from app.routers import todo_sqlite

app.include_router(todo_sqlite.router)
```

## I. Jalankan dan Uji

Perintah:

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --port 8002
```

Akses:
- `http://127.0.0.1:8002/todo-sqlite`

Checklist uji:

1. Tambah todo baru -> data muncul di tabel.
2. Edit todo -> judul/status berubah.
3. Hapus todo -> baris hilang.
4. Restart server -> data tetap ada (karena tersimpan di SQLite).

## J. Kenapa Ini Lebih Baik dari In-Memory?

- In-memory: data hilang saat server mati.
- SQLite: data tersimpan di file `.db`, tetap ada setelah restart.
- Ini langkah penting sebelum naik ke database server besar (PostgreSQL/MySQL).

## K. Latihan Lanjutan

1. Tambahkan kolom `deadline` pada model Todo.
2. Tambahkan filter status (`all`, `done`, `pending`) via query parameter.
3. Tambahkan validasi: judul minimal 3 karakter.
4. Tambahkan kolom `created_at` dan tampilkan di tabel.

## L. Versi Lanjutan: Validasi + Search + Pagination

Bagian ini adalah kelanjutan langsung dari CRUD SQLite di atas.

### 1) Upgrade Model Todo

Tambahkan `created_at` dan `deadline` pada model:

```python
from sqlalchemy import Boolean, Column, DateTime, Integer, String, func

class Todo(Base):
	__tablename__ = "todos"

	id = Column(Integer, primary_key=True, index=True)
	title = Column(String(200), nullable=False)
	done = Column(Boolean, default=False, nullable=False)
	deadline = Column(String(20), nullable=True)
	created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
```

Catatan:
- Setelah ubah model, hapus `todo.db` untuk praktik ulang sederhana.
- Jika tidak ingin hapus data lama, gunakan migration (misalnya Alembic).

### 2) Route GET dengan Search + Filter + Pagination

```python
from math import ceil
from fastapi import Query

@router.get("/todo-sqlite")
def todo_page(
	request: Request,
	q: str = Query(""),
	status: str = Query("all"),
	page: int = Query(1, ge=1),
	per_page: int = Query(5, ge=1, le=50),
	db: Session = Depends(get_db),
):
	query = db.query(Todo)

	if q.strip():
		query = query.filter(Todo.title.ilike(f"%{q.strip()}%"))

	if status == "done":
		query = query.filter(Todo.done.is_(True))
	elif status == "pending":
		query = query.filter(Todo.done.is_(False))

	total = query.count()
	total_pages = max(1, ceil(total / per_page))
	if page > total_pages:
		page = total_pages

	todos = (
		query.order_by(Todo.id.desc())
		.offset((page - 1) * per_page)
		.limit(per_page)
		.all()
	)

	return templates.TemplateResponse(
		"todo_sqlite.html",
		{
			"request": request,
			"todos": todos,
			"edit_item": None,
			"q": q,
			"status": status,
			"page": page,
			"per_page": per_page,
			"total": total,
			"total_pages": total_pages,
		},
	)
```

### 3) Validasi Input pada Create/Update

```python
@router.post("/todo-sqlite/create")
def todo_create(
	request: Request,
	title: str = Form(...),
	deadline: str = Form(""),
	db: Session = Depends(get_db),
):
	clean_title = title.strip()
	if len(clean_title) < 3:
		todos = db.query(Todo).order_by(Todo.id.desc()).limit(10).all()
		return templates.TemplateResponse(
			"todo_sqlite.html",
			{
				"request": request,
				"todos": todos,
				"edit_item": None,
				"error": "Judul minimal 3 karakter.",
			},
			status_code=400,
		)

	db.add(Todo(title=clean_title, done=False, deadline=deadline or None))
	db.commit()
	return RedirectResponse(url="/todo-sqlite", status_code=303)
```

### 4) Tambahan Form Search + Filter di Template

```html
<form method="get" action="/todo-sqlite">
  <input type="text" name="q" value="{{ q or '' }}" placeholder="Cari judul todo..." />
  <select name="status">
	<option value="all" {% if status == 'all' %}selected{% endif %}>Semua</option>
	<option value="done" {% if status == 'done' %}selected{% endif %}>Selesai</option>
	<option value="pending" {% if status == 'pending' %}selected{% endif %}>Belum</option>
  </select>
  <button type="submit">Filter</button>
</form>
```

### 5) Tambahan Pagination di Template

```html
{% if total_pages > 1 %}
  <nav>
	{% if page > 1 %}
	  <a href="?q={{ q }}&status={{ status }}&page={{ page - 1 }}&per_page={{ per_page }}">Prev</a>
	{% endif %}

	<span>Halaman {{ page }} / {{ total_pages }}</span>

	{% if page < total_pages %}
	  <a href="?q={{ q }}&status={{ status }}&page={{ page + 1 }}&per_page={{ per_page }}">Next</a>
	{% endif %}
  </nav>
{% endif %}
```

### 6) Checklist Uji Versi Lanjutan

1. Input judul kurang dari 3 karakter ditolak.
2. Search keyword menampilkan data sesuai judul.
3. Filter status `done/pending` berjalan benar.
4. Pagination `Prev/Next` berpindah halaman dengan data yang tepat.
5. Parameter URL (`q`, `status`, `page`) tetap terbawa antar klik.

### 7) Catatan Pengajaran

Urutan ajar yang disarankan:

1. Ajarkan validasi dulu.
2. Lanjut ke search + filter.
3. Terakhir pagination.

Alasannya:
- Siswa lebih cepat paham alur data jika dari kasus paling sederhana dulu.
