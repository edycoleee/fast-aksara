# Pembelajaran 7 - CRUD Admin

## Create, Read, Update, Delete untuk Modul Admin

Pembelajaran ini melanjutkan Pembelajaran 6.
Jika pada tahap sebelumnya siswa sudah bisa render data dinamis dengan Jinja2, maka pada tahap ini siswa belajar mengelola data dari halaman admin.

## A. Tujuan

- Siswa memahami alur CRUD dari form admin ke backend.
- Siswa dapat membuat route Create, Read, Update, dan Delete di FastAPI.
- Siswa dapat membuat template form admin untuk tambah dan edit data.
- Siswa mampu menerapkan validasi sederhana dan redirect setelah simpan.

## B. Hasil Akhir

Di akhir pembelajaran, siswa mampu:

1. Menambah data dari form admin.
2. Menampilkan daftar data dalam tabel admin.
3. Mengubah data lewat mode edit.
4. Menghapus data dari tabel.
5. Menjaga alur modul admin tetap rapi.

## C. Estimasi Waktu

- 3 sampai 5 pertemuan (270-450 menit).

## D. Tahap Belajar

### Tahap 1 - Pahami Alur CRUD (30-45 menit)

Aktivitas:
- Jelaskan alur request form -> route POST -> simpan data -> redirect.
- Bedakan route GET (tampil halaman) dan POST (proses data).

Output:
- Siswa paham siklus CRUD tiap modul admin.

### Tahap 2 - Read + Create (60-90 menit)

Aktivitas:
- Tampilkan data list dalam tabel.
- Tambahkan form untuk data baru.

Output:
- Siswa berhasil menambah data dari admin ke daftar.

### Tahap 3 - Edit + Update (60-90 menit)

Aktivitas:
- Buat tombol Edit pada tabel.
- Tampilkan form edit terisi otomatis.
- Simpan hasil update.

Output:
- Data bisa diubah tanpa membuat item baru.

### Tahap 4 - Delete Aman (45-60 menit)

Aktivitas:
- Buat tombol Hapus.
- Terapkan konfirmasi dasar (opsional) di frontend.

Output:
- Data bisa dihapus dan tabel langsung terbarui.

### Tahap 5 - Validasi dan Uji Modul (30-45 menit)

Aktivitas:
- Uji skenario field kosong.
- Uji tambah/edit/hapus berulang.
- Uji redirect sukses.

Output:
- Modul admin stabil dipakai.

## E. Struktur Modul Admin

```text
backend/app/
|-- routers/admin.py
|-- templates/admin/
|   |-- login.html
|   |-- dashboard.html
|   |-- elibrary_form.html
|   |-- dokumentasi_form.html
|   |-- artikel_form.html
|   |-- settings.html
```

## F. Contoh Route CRUD FastAPI

Contoh berikut pola minimal. Nama fungsi dan model boleh disesuaikan dengan proyek.

### 1) READ (list data)

```python
@router.get("/admin/elibrary")
def admin_elibrary(request: Request, db: Session = Depends(get_db)):
		items = db.query(ELibrary).order_by(ELibrary.id.desc()).all()
		return templates.TemplateResponse(
				"admin/elibrary_form.html",
				{"request": request, "items": items, "edit_item": None},
		)
```

### 2) CREATE (tambah data)

```python
@router.post("/admin/elibrary")
def admin_elibrary_create(
		request: Request,
		judul: str = Form(...),
		kategori: str = Form(...),
		deskripsi: str = Form(""),
		db: Session = Depends(get_db),
):
		new_item = ELibrary(judul=judul, kategori=kategori, deskripsi=deskripsi)
		db.add(new_item)
		db.commit()
		return RedirectResponse(url="/admin/elibrary", status_code=303)
```

### 3) EDIT (ambil data untuk form)

```python
@router.get("/admin/elibrary/edit/{item_id}")
def admin_elibrary_edit(item_id: int, request: Request, db: Session = Depends(get_db)):
		items = db.query(ELibrary).order_by(ELibrary.id.desc()).all()
		edit_item = db.query(ELibrary).filter(ELibrary.id == item_id).first()
		return templates.TemplateResponse(
				"admin/elibrary_form.html",
				{"request": request, "items": items, "edit_item": edit_item},
		)
```

### 4) UPDATE (simpan perubahan)

```python
@router.post("/admin/elibrary/edit/{item_id}")
def admin_elibrary_update(
		item_id: int,
		judul: str = Form(...),
		kategori: str = Form(...),
		deskripsi: str = Form(""),
		db: Session = Depends(get_db),
):
		item = db.query(ELibrary).filter(ELibrary.id == item_id).first()
		if not item:
				return RedirectResponse(url="/admin/elibrary", status_code=303)

		item.judul = judul
		item.kategori = kategori
		item.deskripsi = deskripsi
		db.commit()
		return RedirectResponse(url="/admin/elibrary?updated=1", status_code=303)
```

### 5) DELETE (hapus data)

```python
@router.post("/admin/elibrary/delete/{item_id}")
def admin_elibrary_delete(item_id: int, db: Session = Depends(get_db)):
		item = db.query(ELibrary).filter(ELibrary.id == item_id).first()
		if item:
				db.delete(item)
				db.commit()
		return RedirectResponse(url="/admin/elibrary", status_code=303)
```

## G. Contoh Template Form Admin

Contoh pola untuk tambah + edit di satu halaman (`admin/elibrary_form.html`):

```html
<h1>Kelola E-Library</h1>

{% if edit_item %}
	<h2>Edit Data</h2>
	<form method="post" action="/admin/elibrary/edit/{{ edit_item.id }}">
		<input type="text" name="judul" value="{{ edit_item.judul }}" required />
		<input type="text" name="kategori" value="{{ edit_item.kategori }}" required />
		<textarea name="deskripsi">{{ edit_item.deskripsi }}</textarea>
		<button type="submit">Update</button>
		<a href="/admin/elibrary">Batal</a>
	</form>
{% else %}
	<h2>Tambah Data</h2>
	<form method="post" action="/admin/elibrary">
		<input type="text" name="judul" placeholder="Judul" required />
		<input type="text" name="kategori" placeholder="Kategori" required />
		<textarea name="deskripsi" placeholder="Deskripsi"></textarea>
		<button type="submit">Simpan</button>
	</form>
{% endif %}

<table>
	<tr>
		<th>No</th>
		<th>Judul</th>
		<th>Kategori</th>
		<th>Aksi</th>
	</tr>
	{% for item in items %}
	<tr>
		<td>{{ loop.index }}</td>
		<td>{{ item.judul }}</td>
		<td>{{ item.kategori }}</td>
		<td>
			<a href="/admin/elibrary/edit/{{ item.id }}">Edit</a>
			<form method="post" action="/admin/elibrary/delete/{{ item.id }}" style="display:inline">
				<button type="submit">Hapus</button>
			</form>
		</td>
	</tr>
	{% endfor %}
</table>
```

## H. Kunci Jawaban per Modul Admin

### 1) Modul Login Admin

Target:
- Form username/password.
- Validasi sederhana.
- Redirect ke dashboard jika sukses.

Kunci poin:
- Route GET `/admin/login` untuk tampil form.
- Route POST `/admin/login` untuk cek kredensial.
- Simpan status login di session.

### 2) Modul Dashboard Admin

Target:
- Menampilkan ringkasan jumlah data.

Kunci poin:
- Hitung total ELibrary, Dokumentasi, Artikel dari database.
- Kirim hasil count ke template dashboard.

### 3) Modul E-Library

Target:
- CRUD lengkap untuk materi e-library.

Kunci poin:
- Tabel list data.
- Form tambah/edit pada halaman yang sama atau terpisah.
- Redirect setelah create/update/delete.
- Aturan khusus: bila tipe internal PDF dikunci saat edit file, jelaskan di UI.

### 4) Modul Dokumentasi

Target:
- CRUD dokumentasi kegiatan per kategori program.

Kunci poin:
- Field utama: judul, kategori, deskripsi, gambar/video.
- Filter kategori bisa ditambahkan bertahap.
- Tombol aksi edit/hapus wajib ada.

### 5) Modul Artikel

Target:
- CRUD artikel untuk Tunas/Karya/Cakra/Kersa.

Kunci poin:
- Field utama: judul, kategori, deskripsi, gambar, PDF.
- Gunakan empty state jika belum ada artikel.
- Terapkan informasi status file (misal PDF terkunci) saat mode edit.

### 6) Modul Settings

Target:
- Ubah pengaturan website dari panel admin.

Kunci poin:
- Form: nama situs, tagline, WhatsApp, alamat, email, maps.
- Simpan 1 record setting aktif.
- Tampilkan pesan berhasil setelah update.

## I. Rubrik Penilaian

Skor 1-4 per aspek:

1. Kelengkapan route CRUD tiap modul.
2. Kebenaran alur GET/POST dan redirect.
3. Kerapian template form + tabel.
4. Validasi dasar field penting.
5. Konsistensi UI admin (aksi edit/hapus/simpan jelas).

Nilai akhir = rata-rata 5 aspek.

## J. Tugas Praktik Siswa

1. Tambahkan 2 data baru di modul E-Library.
2. Edit 1 data Dokumentasi lalu verifikasi perubahan tampil di tabel.
3. Hapus 1 data Artikel dan pastikan jumlah dashboard berubah.
4. Ubah 2 field pada Settings dan cek tampil di halaman publik.

## K. Penutup

Setelah Pembelajaran 7:

- Siswa menguasai dasar CRUD berbasis web.
- Siswa siap lanjut ke Pembelajaran 8: validasi lebih kuat, upload file aman, dan manajemen role admin.


## L. Isi File HTML

Berikut contoh script minimal yang bisa langsung dipakai siswa.

### 1) `login.html`

```html
{% extends "base.html" %}
{% block content %}
<section>
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
</section>
{% endblock %}
```

### 2) `dashboard.html`

```html
{% extends "base.html" %}
{% block content %}
<section>
	<h1>Dashboard Admin</h1>
	<p>Ringkasan data website.</p>
</section>

<section>
	<article>
		<h2>Total E-Library</h2>
		<p>{{ total_elibrary }}</p>
	</article>
	<article>
		<h2>Total Dokumentasi</h2>
		<p>{{ total_dokumentasi }}</p>
	</article>
	<article>
		<h2>Total Artikel</h2>
		<p>{{ total_artikel }}</p>
	</article>
</section>

<section>
	<a href="/admin/elibrary">Kelola E-Library</a> |
	<a href="/admin/dokumentasi">Kelola Dokumentasi</a> |
	<a href="/admin/artikel">Kelola Artikel</a> |
	<a href="/admin/settings">Settings</a>
</section>
{% endblock %}
```

### 3) `elibrary_form.html`

```html
{% extends "base.html" %}
{% block content %}
<h1>Kelola E-Library</h1>

{% if request.query_params.get('updated') == '1' %}
	<p style="color: #166534;">Data berhasil diperbarui.</p>
{% endif %}

{% if edit_item %}
	<h2>Edit Data</h2>
	<form method="post" action="/admin/elibrary/edit/{{ edit_item.id }}" enctype="multipart/form-data">
		<input type="text" name="judul" value="{{ edit_item.judul }}" required />
		<input type="text" name="kategori" value="{{ edit_item.kategori }}" required />
		<textarea name="deskripsi">{{ edit_item.deskripsi }}</textarea>

		{% if edit_item.link_type == 'internal' %}
			<p><strong>PDF terkunci</strong> - file PDF tidak diubah pada mode edit.</p>
		{% else %}
			<input type="url" name="link" value="{{ edit_item.link }}" placeholder="https://..." />
		{% endif %}

		<button type="submit">Update</button>
		<a href="/admin/elibrary">Batal</a>
	</form>
{% else %}
	<h2>Tambah Data</h2>
	<form method="post" action="/admin/elibrary" enctype="multipart/form-data">
		<input type="text" name="judul" placeholder="Judul" required />
		<input type="text" name="kategori" placeholder="Kategori" required />
		<textarea name="deskripsi" placeholder="Deskripsi"></textarea>

		<select name="link_type" required>
			<option value="external">External URL</option>
			<option value="internal">Internal PDF</option>
		</select>

		<input type="url" name="link" placeholder="https://... (jika external)" />
		<input type="file" name="file_pdf" accept="application/pdf" />
		<button type="submit">Simpan</button>
	</form>
{% endif %}

<table>
	<tr>
		<th>No</th>
		<th>Judul</th>
		<th>Kategori</th>
		<th>Tipe</th>
		<th>Aksi</th>
	</tr>
	{% for item in items %}
	<tr>
		<td>{{ loop.index }}</td>
		<td>{{ item.judul }}</td>
		<td>{{ item.kategori }}</td>
		<td>{{ item.link_type }}</td>
		<td>
			<a href="/admin/elibrary/edit/{{ item.id }}">Edit</a>
			<form method="post" action="/admin/elibrary/delete/{{ item.id }}" style="display:inline;">
				<button type="submit">Hapus</button>
			</form>
		</td>
	</tr>
	{% endfor %}
</table>
{% endblock %}
```

### 4) `dokumentasi_form.html`

```html
{% extends "base.html" %}
{% block content %}
<h1>Kelola Dokumentasi</h1>

{% if edit_item %}
	<h2>Edit Dokumentasi</h2>
	<form method="post" action="/admin/dokumentasi/edit/{{ edit_item.id }}" enctype="multipart/form-data">
		<input type="text" name="judul" value="{{ edit_item.judul }}" required />
		<input type="text" name="kategori" value="{{ edit_item.kategori }}" required />
		<textarea name="deskripsi">{{ edit_item.deskripsi }}</textarea>
		<input type="url" name="link_video" value="{{ edit_item.link_video or '' }}" placeholder="Link video" />
		<input type="file" name="gambar" accept="image/*" />
		<button type="submit">Update</button>
		<a href="/admin/dokumentasi">Batal</a>
	</form>
{% else %}
	<h2>Tambah Dokumentasi</h2>
	<form method="post" action="/admin/dokumentasi" enctype="multipart/form-data">
		<input type="text" name="judul" placeholder="Judul" required />
		<select name="kategori" required>
			<option value="tunas">Tunas</option>
			<option value="karya">Karya</option>
			<option value="cakra">Cakra</option>
			<option value="kersa">Kersa</option>
		</select>
		<textarea name="deskripsi" placeholder="Deskripsi"></textarea>
		<input type="url" name="link_video" placeholder="Link video" />
		<input type="file" name="gambar" accept="image/*" />
		<button type="submit">Simpan</button>
	</form>
{% endif %}

<table>
	<tr><th>No</th><th>Judul</th><th>Kategori</th><th>Aksi</th></tr>
	{% for item in items %}
	<tr>
		<td>{{ loop.index }}</td>
		<td>{{ item.judul }}</td>
		<td>{{ item.kategori }}</td>
		<td>
			<a href="/admin/dokumentasi/edit/{{ item.id }}">Edit</a>
			<form method="post" action="/admin/dokumentasi/delete/{{ item.id }}" style="display:inline;">
				<button type="submit">Hapus</button>
			</form>
		</td>
	</tr>
	{% endfor %}
</table>
{% endblock %}
```

### 5) `artikel_form.html`

```html
{% extends "base.html" %}
{% block content %}
<h1>Kelola Artikel</h1>

{% if edit_item %}
	<h2>Edit Artikel</h2>
	<form method="post" action="/admin/artikel/edit/{{ edit_item.id }}" enctype="multipart/form-data">
		<input type="text" name="judul" value="{{ edit_item.judul }}" required />
		<select name="kategori" required>
			<option value="tunas" {% if edit_item.kategori == 'tunas' %}selected{% endif %}>Tunas</option>
			<option value="karya" {% if edit_item.kategori == 'karya' %}selected{% endif %}>Karya</option>
			<option value="cakra" {% if edit_item.kategori == 'cakra' %}selected{% endif %}>Cakra</option>
			<option value="kersa" {% if edit_item.kategori == 'kersa' %}selected{% endif %}>Kersa</option>
		</select>
		<textarea name="deskripsi">{{ edit_item.deskripsi }}</textarea>
		<input type="file" name="gambar" accept="image/*" />
		<p><strong>PDF terkunci</strong> - file PDF tidak diubah pada mode edit.</p>
		<button type="submit">Update</button>
		<a href="/admin/artikel">Batal</a>
	</form>
{% else %}
	<h2>Tambah Artikel</h2>
	<form method="post" action="/admin/artikel" enctype="multipart/form-data">
		<input type="text" name="judul" placeholder="Judul" required />
		<select name="kategori" required>
			<option value="tunas">Tunas</option>
			<option value="karya">Karya</option>
			<option value="cakra">Cakra</option>
			<option value="kersa">Kersa</option>
		</select>
		<textarea name="deskripsi" placeholder="Deskripsi"></textarea>
		<input type="file" name="gambar" accept="image/*" />
		<input type="file" name="file_pdf" accept="application/pdf" />
		<button type="submit">Simpan</button>
	</form>
{% endif %}

<table>
	<tr><th>No</th><th>Judul</th><th>Kategori</th><th>Status PDF</th><th>Aksi</th></tr>
	{% for item in items %}
	<tr>
		<td>{{ loop.index }}</td>
		<td>{{ item.judul }}</td>
		<td>{{ item.kategori }}</td>
		<td>{% if item.link_pdf %}PDF terkunci{% else %}-{% endif %}</td>
		<td>
			<a href="/admin/artikel/edit/{{ item.id }}">Edit</a>
			<form method="post" action="/admin/artikel/delete/{{ item.id }}" style="display:inline;">
				<button type="submit">Hapus</button>
			</form>
		</td>
	</tr>
	{% endfor %}
</table>
{% endblock %}
```

### 6) `settings.html`

```html
{% extends "base.html" %}
{% block content %}
<h1>Settings Website</h1>

{% if saved %}
	<p style="color: #166534;">Pengaturan berhasil disimpan.</p>
{% endif %}

<form method="post" action="/admin/settings">
	<label>Nama Situs</label>
	<input type="text" name="site_name" value="{{ settings.site_name if settings else '' }}" required />

	<label>Tagline</label>
	<input type="text" name="tagline" value="{{ settings.tagline if settings else '' }}" required />

	<label>WhatsApp</label>
	<input type="text" name="whatsapp" value="{{ settings.whatsapp if settings else '' }}" />

	<label>Alamat</label>
	<textarea name="alamat">{{ settings.alamat if settings else '' }}</textarea>

	<label>Email</label>
	<input type="email" name="email" value="{{ settings.email if settings else '' }}" />

	<label>Embed Maps</label>
	<textarea name="maps_embed">{{ settings.maps_embed if settings else '' }}</textarea>

	<button type="submit">Simpan Pengaturan</button>
</form>
{% endblock %}
```
