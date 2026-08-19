### 1. Mockup Data per Page (Semua Halaman)

Tujuan:
- Siswa paham isi tiap halaman sebelum menulis kode.
- Siswa bisa membedakan halaman publik dan halaman admin.

Aktivitas:
- Menentukan daftar halaman: Landing, Beranda, E-Library, Tunas, Karya, Cakra, Kersa, Admin.
- Menulis data dummy per halaman (judul, deskripsi, gambar, tombol, tabel).

Output:
- Dokumen mockup data per halaman.

Waktu:
- 1 pertemuan (90 menit).

### MATERI

Tahap ini fokus ke "rencana isi halaman" sebelum coding. Siswa belum menulis HTML/CSS, tetapi sudah memetakan konten seperti web Ngrembaka Aksara.

## A. Konsep Inti (10 menit)

1. Mockup data adalah isi halaman dalam bentuk teks/objek sederhana.
2. Mockup membantu siswa tidak bingung saat mulai coding.
3. Urutan kerja: `Nama Halaman -> Tujuan Halaman -> Data yang Ditampilkan -> Aksi Tombol`.

## B. Daftar Halaman Acuan (Sesuai Web Ini)

### Halaman Publik

- Landing (`/`)
- Beranda (`/beranda`)
- Profil Aksara (`/profil/ngrembaka-aksara`)
- Profil Kelurahan (`/profil/kelurahan-podorejo`)
- E-Library (`/elibrary`)
- Tunas (`/pojok-literasi/tunas`)
- Karya (`/pojok-literasi/karya`)
- Cakra (`/pojok-literasi/cakra`)
- Kersa (`/pojok-literasi/kersa`)

### Halaman Admin

- Login (`/admin/login`)
- Dashboard (`/admin`)
- Kelola E-Library (`/admin/elibrary`)
- Kelola Dokumentasi (`/admin/dokumentasi`)
- Kelola Artikel (`/admin/artikel`)
- Settings (`/admin/settings`)

## C. Objek Data yang Dipakai

Gunakan 3 objek utama agar konsisten dengan implementasi web:

1. `ELibrary`
2. `Dokumentasi`
3. `Artikel`

Contoh atribut awal:

- `ELibrary`: `judul`, `kategori`, `deskripsi`, `link`, `link_type`, `gambar`
- `Dokumentasi`: `judul`, `kategori`, `deskripsi`, `link_gambar`, `link_video`
- `Artikel`: `judul`, `kategori`, `deskripsi`, `gambar`, `link_pdf`

## D. Template Mockup per Halaman (Langsung Isi)

Salin format ini untuk setiap halaman:

```markdown
Nama halaman:
Tujuan halaman:
Section utama:
1) ...
2) ...

Data yang tampil:
- Field 1:
- Field 2:
- Field 3:

Aksi pengguna:
- Tombol 1:
- Tombol 2:

Kondisi kosong:
- Jika data tidak ada, tampilkan:
```

## E. Folder HTML untuk Membuat Mockup (Praktik Siswa)

Bagian ini menjelaskan cara praktik dari nol: menyiapkan folder, membuat file HTML, lalu menjalankannya di browser.

### 1) Struktur Folder Latihan

Siswa membuat folder kerja sederhana seperti ini:

```text
latihan-mockup/
|-- index.html
|-- beranda.html
|-- elibrary.html
|-- tunas.html
|-- karya.html
|-- cakra.html
|-- kersa.html
|-- admin-login.html
|-- admin-dashboard.html
|-- admin-elibrary.html
|-- admin-dokumentasi.html
|-- admin-artikel.html
|-- admin-settings.html
```

Catatan:
- Satu file mewakili satu halaman mockup.
- Pada tahap ini, file boleh masih HTML dasar (tanpa CSS).

### 2) Cara Membuat File HTML (di VS Code)

Langkah:

1. Buat folder `latihan-mockup`.
2. Klik kanan folder -> `New File`.
3. Buat file pertama: `index.html`.
4. Ulangi sampai semua nama file di atas selesai.

Template isi awal tiap file:

```html
<!doctype html>
<html lang="id">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Nama Halaman</title>
</head>
<body>
	<h1>Nama Halaman</h1>
	<p>Isi mockup awal di sini.</p>
</body>
</html>
```

### 3) Cara Menjalankan HTML di Browser

#### Opsi A (paling cepat untuk siswa)

- Klik dua kali file `index.html`, lalu terbuka di browser.

#### Opsi B (disarankan agar semua link antar halaman berjalan rapi)

Jalankan server lokal dari folder `latihan-mockup`:

```bash
cd latihan-mockup
python -m http.server 5500
```

Lalu buka:

- `http://localhost:5500`

Keuntungan Opsi B:
- Navigasi antar file HTML lebih stabil.
- Simulasi lebih mirip website sungguhan.

### 4) Cara Menyambungkan Antar Halaman

Contoh menu sederhana di `index.html`:

```html
<nav>
	<a href="index.html">Landing</a>
	<a href="beranda.html">Beranda</a>
	<a href="elibrary.html">E-Library</a>
	<a href="tunas.html">Tunas</a>
	<a href="admin-dashboard.html">Admin</a>
</nav>
```

Minimal setiap file punya:
- Judul halaman (`h1`)
- Navigasi utama
- 2-3 section isi mockup

### 5) Checklist Praktik Siswa

1. Semua file HTML berhasil dibuat.
2. Semua file bisa dibuka di browser.
3. Link navigasi antar halaman tidak error.
4. Tiap halaman punya konten mockup sesuai rancangan.

### 6) Kapan Dipindah ke FastAPI Template?

Setelah mockup HTML selesai dan disetujui guru, file dipindah ke folder template proyek:

- dari: `latihan-mockup/*.html`
- ke: `backend/app/templates/`

Lalu tahap berikutnya mulai integrasi dengan route FastAPI dan data database.

## F. Contoh Mockup Detail (Siap Praktik)

### 1) Landing

- Tujuan: halaman pengenalan program.
- Section: hero, ringkasan program, CTA ke E-Library dan Pojok Literasi.
- Data tampil: nama program, tagline, jumlah program inti, tombol navigasi.
- Aksi: `Lihat E-Library`, `Lihat Pojok Literasi`.

#### Detail Mockup Landing (Langkah Praktik)

Tujuan bagian ini: siswa bisa mengubah ide halaman menjadi bentuk yang siap dikoding.

##### 1. Layout dalam Text (Wireframe Sederhana)

Minta siswa menulis susunan halaman pakai teks dulu (tanpa HTML):

```text
LAYOUT VISUAL (DESKTOP)
+--------------------------------------------------------------+
| LOGO: Ngrembaka Aksara | Beranda | Visi | Profil | E-Library |
|                        | Pojok Literasi | Hubungi Kami        |
+--------------------------------------------------------------+
| HERO                                                        |
| - Judul Program                                             |
| - Tagline                                                   |
| - Tombol: Lihat E-Library | Lihat Pojok Literasi           |
+--------------------------------------------------------------+
| RINGKASAN PROGRAM                                           |
| [Kartu 1: Profil Program]   [Kartu 2: Profil Wilayah]      |
+--------------------------------------------------------------+
| FOOTER: Lokasi | Kontak | Link Cepat                       |
+--------------------------------------------------------------+


LANDING PAGE
|-- Navbar
|   |-- Logo: Ngrembaka Aksara
|   |-- Menu: Beranda, Visi, Profil, E-Library, Pojok Literasi
|
|-- Hero Section
|   |-- Judul besar program
|   |-- Tagline
|   |-- Tombol: Lihat E-Library, Lihat Pojok Literasi
|
|-- Ringkasan Program
|   |-- Kartu 1: Profil Program
|   |-- Kartu 2: Profil Wilayah
|
|-- Footer
|   |-- Lokasi
|   |-- Kontak
```

Output langkah ini:
- Siswa paham urutan section dari atas ke bawah.
- Siswa tahu konten utama mana yang harus muncul duluan.

##### 2. Membuat HTML Layout (Kerangka)

Setelah wireframe teks selesai, ubah ke kerangka HTML sederhana:

```html
<body>
	<nav>
		<h1>Ngrembaka Aksara</h1>
		<ul>
			<li><a href="/">Beranda</a></li>
			<li><a href="/beranda">Visi</a></li>
			<li><a href="/profil/ngrembaka-aksara">Profil</a></li>
			<li><a href="/elibrary">E-Library</a></li>
			<li><a href="/pojok-literasi/tunas">Pojok Literasi</a></li>
		</ul>
	</nav>

	<main>
		<section id="hero">
			<h2>Ngrembaka Aksara</h2>
			<p>Tagline program</p>
			<a href="/elibrary">Lihat E-Library</a>
			<a href="/pojok-literasi/tunas">Lihat Pojok Literasi</a>
		</section>

		<section id="ringkasan-program">
			<article>
				<h3>Profil Program</h3>
				<p>Ringkasan singkat.</p>
			</article>
			<article>
				<h3>Profil Wilayah</h3>
				<p>Ringkasan singkat.</p>
			</article>
		</section>
	</main>

	<footer>
		<p>Lokasi dan kontak</p>
	</footer>
</body>
```

Catatan belajar untuk siswa:
- Fokus dulu ke tag struktur: `nav`, `main`, `section`, `article`, `footer`.
- Belum perlu styling CSS pada tahap ini.

##### 3. Mengisi HTML Layout dengan Konten Mockup

Isi teks nyata sesuai data mockup yang sudah dibuat:

- Ganti "Tagline program" dengan kalimat final.
- Isi judul kartu ringkasan dan deskripsinya.
- Pastikan link tombol mengarah ke route yang benar.

Contoh checklist validasi siswa:

1. Apakah halaman sudah punya 3 bagian utama: navbar, hero, ringkasan?
2. Apakah tombol CTA berfungsi (link tidak kosong)?
3. Apakah urutan informasi sudah nyaman dibaca dari atas ke bawah?
4. Apakah semua teks penting dari mockup sudah masuk ke HTML?

##### 4. Hasil Akhir yang Diharapkan dari Siswa

- 1 file layout teks (wireframe sederhana).
- 1 file HTML kerangka landing.
- 1 file HTML landing yang sudah berisi konten nyata.

Dengan alur ini, siswa tidak langsung "lompat coding". Mereka paham dulu rancangan, baru struktur, lalu isi konten.


### 2) E-Library

- Tujuan: menampilkan daftar sumber belajar.
- Section: filter kategori, daftar kartu konten, detail konten.
- Data tampil per kartu: judul, kategori, deskripsi ringkas, gambar, link.
- Aksi: `Detail`, `Tonton` atau `Unduh PDF`.
- Kondisi kosong: "Belum ada koleksi".

#### Detail Mockup E-Library (Langkah Praktik)

##### 1. Layout dalam Text (Wireframe Sederhana)

```text
E-LIBRARY PAGE
|-- Header
|   |-- Judul E-Library
|   |-- Ringkasan jumlah koleksi
|
|-- Filter Kategori
|   |-- Semua | Modul | E-Book | Buku Cerita | Literasi Digital | Life Skills
|
|-- Daftar Kartu Koleksi
|   |-- Kartu 1: Gambar | Judul | Kategori | Deskripsi Singkat | Tombol Detail
|   |-- Kartu 2: ...
|
|-- Empty State (jika kosong)
|   |-- Pesan: Belum ada koleksi
```

##### 2. Membuat HTML Layout (Kerangka)

```html
<main>
	<section id="elibrary-header">
		<h2>E-Library</h2>
		<p>Menampilkan X dari Y koleksi</p>
	</section>

	<section id="elibrary-filter">
		<button>Semua</button>
		<button>Modul</button>
		<button>E-Book</button>
	</section>

	<section id="elibrary-list">
		<article class="card">
			<img src="..." alt="judul" />
			<h3>Judul Konten</h3>
			<p>Kategori</p>
			<p>Deskripsi singkat</p>
			<a href="#">Detail</a>
		</article>
	</section>
</main>
```

##### 3. Mengisi HTML Layout dengan Konten Mockup

- Isi data dummy minimal 3 kartu.
- Minimal 1 kartu punya link YouTube, 1 kartu punya link PDF.
- Tambahkan 1 skenario kosong (list tidak ada data).

##### 4. Checklist Validasi

1. Apakah filter kategori terlihat jelas?
2. Apakah setiap kartu punya judul, kategori, deskripsi, tombol?
3. Apakah link aksi sesuai tipe konten (video/PDF)?
4. Apakah pesan empty state sudah disiapkan?

##### 5. Hasil Akhir

- 1 wireframe teks E-Library.
- 1 HTML kerangka E-Library.
- 1 HTML E-Library berisi konten mockup + skenario kosong.

### 3) Tunas/Karya/Cakra/Kersa

- Tujuan: menampilkan konten per program.
- Section umum: deskripsi program, daftar dokumentasi/artikel, pagination.
- Data tampil: judul item, deskripsi ringkas, gambar, kategori.
- Aksi: `Detail`, `PDF` (jika ada).

#### Detail Mockup Program (Tunas/Karya/Cakra/Kersa)

##### 1. Layout dalam Text (Wireframe Sederhana)

```text
PROGRAM PAGE (contoh: Tunas)
|-- Hero Program
|   |-- Nama Program
|   |-- Tagline
|
|-- Deskripsi Program
|   |-- Ringkasan tujuan
|
|-- Daftar Konten Program
|   |-- Item 1: Gambar | Judul | Deskripsi | Tombol Detail | Tombol PDF (opsional)
|   |-- Item 2: ...
|
|-- Pagination
|   |-- Prev | Halaman 1/3 | Next
```

##### 2. Membuat HTML Layout (Kerangka)

```html
<main>
	<section id="program-hero">
		<h1>Program Tunas</h1>
		<p>Tagline program</p>
	</section>

	<section id="program-description">
		<h2>Deskripsi Program</h2>
		<p>Ringkasan isi program...</p>
	</section>

	<section id="program-list">
		<article>
			<img src="..." alt="judul" />
			<h3>Judul Konten</h3>
			<p>Deskripsi ringkas</p>
			<a href="#">Detail</a>
			<a href="#">PDF</a>
		</article>
	</section>

	<nav aria-label="pagination">
		<a href="#">Prev</a>
		<span>Halaman 1/3</span>
		<a href="#">Next</a>
	</nav>
</main>
```

##### 3. Mengisi HTML Layout dengan Konten Mockup

- Buat 2 item konten untuk setiap program (Tunas/Karya/Cakra/Kersa).
- Salah satu item punya PDF, satu item tanpa PDF.
- Simulasikan teks panjang, lalu ringkas menjadi 2-3 kalimat.

##### 4. Checklist Validasi

1. Apakah ada pemisahan jelas antara deskripsi program dan daftar konten?
2. Apakah tombol `Detail` selalu ada?
3. Apakah tombol `PDF` hanya muncul jika data PDF tersedia?
4. Apakah pagination terlihat dan mudah dipahami?

##### 5. Hasil Akhir

- 4 wireframe teks (Tunas, Karya, Cakra, Kersa).
- 4 HTML kerangka program.
- 4 HTML berisi konten mockup.

### 4) Admin Dashboard

- Tujuan: ringkasan jumlah data + pintasan ke kelola konten.
- Data tampil: total elibrary, total dokumentasi, total artikel.
- Aksi: `Kelola` tiap modul.

#### Detail Mockup Admin Dashboard

##### 1. Layout dalam Text

```text
ADMIN DASHBOARD
|-- Header Admin
|   |-- Nama admin
|   |-- Tombol Logout
|
|-- Ringkasan Data
|   |-- Kartu: Total E-Library
|   |-- Kartu: Total Dokumentasi
|   |-- Kartu: Total Artikel
|
|-- Shortcut
|   |-- Kelola E-Library
|   |-- Kelola Dokumentasi
|   |-- Kelola Artikel
|   |-- Settings
```

##### 2. Kerangka HTML

```html
<main>
	<header>
		<h1>Dashboard Admin</h1>
		<a href="/admin/logout">Logout</a>
	</header>

	<section id="summary-cards">
		<article>Total E-Library: 12</article>
		<article>Total Dokumentasi: 8</article>
		<article>Total Artikel: 15</article>
	</section>

	<section id="admin-shortcuts">
		<a href="/admin/elibrary">Kelola E-Library</a>
		<a href="/admin/dokumentasi">Kelola Dokumentasi</a>
		<a href="/admin/artikel">Kelola Artikel</a>
		<a href="/admin/settings">Settings</a>
	</section>
</main>
```

##### 3. Checklist Validasi

1. Apakah 3 data ringkasan utama terlihat?
2. Apakah shortcut menuju modul admin lengkap?
3. Apakah tombol logout jelas?

##### 4. Hasil Akhir

- 1 wireframe dashboard admin.
- 1 HTML dashboard admin dengan data contoh.

### 5) Admin Kelola Data

- Tujuan: CRUD konten.
- Section: form tambah/edit + tabel data.
- Aksi tabel: `Edit`, `Hapus`.
- Catatan aturan bisnis: PDF yang sudah di-upload ditandai "terkunci" saat edit.

#### Detail Mockup Admin Kelola Data

##### 1. Layout dalam Text

```text
HALAMAN KELOLA DATA
|-- Form Tambah/Edit
|   |-- Field judul, kategori, deskripsi
|   |-- Field file (gambar/PDF sesuai modul)
|   |-- Tombol Simpan/Update
|
|-- Tabel Data
|   |-- Kolom: No, Judul, Kategori, Aksi
|   |-- Aksi: Edit | Hapus
|   |-- Badge: PDF terkunci (jika sudah upload)
```

##### 2. Kerangka HTML

```html
<main>
	<section id="form-kelola">
		<h2>Tambah Data</h2>
		<form>
			<input name="judul" placeholder="Judul" />
			<select name="kategori"><option>Kategori</option></select>
			<textarea name="deskripsi"></textarea>
			<button type="submit">Simpan</button>
		</form>
	</section>

	<section id="tabel-kelola">
		<table>
			<thead><tr><th>No</th><th>Judul</th><th>Kategori</th><th>Aksi</th></tr></thead>
			<tbody>
				<tr>
					<td>1</td><td>Contoh</td><td>Artikel</td>
					<td><button>Edit</button><button>Hapus</button></td>
				</tr>
			</tbody>
		</table>
	</section>
</main>
```

##### 3. Skenario Latihan CRUD (Manual)

1. Tambah 1 data baru.
2. Ubah judul data itu (simulasi edit).
3. Hapus data lain.
4. Tandai item PDF sebagai "PDF terkunci" saat mode edit.

##### 4. Checklist Validasi

1. Apakah form dan tabel tampil di halaman yang sama?
2. Apakah aksi `Edit` dan `Hapus` tersedia di setiap baris?
3. Apakah ada penanda untuk item PDF yang tidak boleh diganti?

##### 5. Hasil Akhir

- 1 wireframe kelola data.
- 1 HTML form + tabel.
- Dokumen alur CRUD sederhana (Tambah -> Edit -> Hapus).

---

Dengan pola detail seperti ini, siswa akan konsisten belajar dari:

1. Rancangan visual teks.
2. Struktur HTML.
3. Pengisian data mockup.
4. Validasi fungsi dasar.

## J. Layout Visual Semua Page (Desktop)

Bagian ini dipakai sebagai peta visual cepat sebelum siswa membuat HTML.

### 1) Landing (`/`)

```text
+--------------------------------------------------------------+
| LOGO | Beranda | Visi | Profil | E-Library | Pojok Literasi |
+--------------------------------------------------------------+
| HERO: Judul Program | Tagline | CTA 1 | CTA 2               |
+--------------------------------------------------------------+
| Ringkasan Program: [Kartu Profil] [Kartu Wilayah]           |
+--------------------------------------------------------------+
| Footer: Lokasi | Kontak | Link Cepat                        |
+--------------------------------------------------------------+
```

### 2) Beranda (`/beranda`)

```text
+--------------------------------------------------------------+
| Header Beranda: Visi & Tujuan Program                        |
+--------------------------------------------------------------+
| Kartu Visi                                                    |
| Kartu Tujuan (daftar poin)                                   |
+--------------------------------------------------------------+
| Footer                                                        |
+--------------------------------------------------------------+
```

### 3) Profil Aksara (`/profil/ngrembaka-aksara`)

```text
+--------------------------------------------------------------+
| Hero Profil Aksara                                            |
+--------------------------------------------------------------+
| Sejarah Terbentuk                                              |
| Latar Belakang (kartu masalah)                                |
| Sasaran Program (tabel)                                       |
| Struktur Tim (kartu + tabel anggota)                          |
+--------------------------------------------------------------+
| Footer                                                        |
+--------------------------------------------------------------+
```

### 4) Profil Kelurahan (`/profil/kelurahan-podorejo`)

```text
+--------------------------------------------------------------+
| Hero Profil Kelurahan                                          |
+--------------------------------------------------------------+
| Data Demografi/Wilayah                                         |
| Potensi Wilayah                                                |
| Fasilitas dan Ringkasan                                        |
+--------------------------------------------------------------+
| Footer                                                        |
+--------------------------------------------------------------+
```

### 5) E-Library (`/elibrary`)

```text
+--------------------------------------------------------------+
| Header E-Library: Judul + ringkasan jumlah koleksi           |
+--------------------------------------------------------------+
| Filter kategori                                               |
+--------------------------------------------------------------+
| Grid kartu koleksi (gambar, judul, kategori, aksi)           |
+--------------------------------------------------------------+
| Pagination / Empty state                                      |
+--------------------------------------------------------------+
| Footer                                                        |
+--------------------------------------------------------------+
```

### 6) Tunas (`/pojok-literasi/tunas`)

```text
+--------------------------------------------------------------+
| Hero Program Tunas                                             |
+--------------------------------------------------------------+
| Deskripsi Program + Sasaran                                    |
+--------------------------------------------------------------+
| Section Dokumentasi (list kartu + pagination)                 |
+--------------------------------------------------------------+
| Section Artikel (list kartu + pagination)                     |
+--------------------------------------------------------------+
| Footer                                                        |
+--------------------------------------------------------------+
```

### 7) Karya (`/pojok-literasi/karya`)

```text
+--------------------------------------------------------------+
| Hero Program Karya                                             |
+--------------------------------------------------------------+
| Deskripsi + Kader + Hasil Karya                               |
+--------------------------------------------------------------+
| Karya Digital (list)                                           |
| Karya Media Sosial (list)                                      |
| Hosting Library/Carousel (list)                                |
+--------------------------------------------------------------+
| Footer                                                        |
+--------------------------------------------------------------+
```

### 8) Cakra (`/pojok-literasi/cakra`)

```text
+--------------------------------------------------------------+
| Hero Program Cakra                                             |
+--------------------------------------------------------------+
| Deskripsi + Kader                                              |
| Materi Program (tabel)                                         |
+--------------------------------------------------------------+
| Artikel Terkait (list + pagination)                           |
+--------------------------------------------------------------+
| Footer                                                        |
+--------------------------------------------------------------+
```

### 9) Kersa (`/pojok-literasi/kersa`)

```text
+--------------------------------------------------------------+
| Hero Program Kersa                                             |
+--------------------------------------------------------------+
| Deskripsi + Kader + Mitra                                      |
+--------------------------------------------------------------+
| Program Kesehatan Lansia (list + pagination)                  |
| Program Keterampilan Produktif (list + pagination)            |
+--------------------------------------------------------------+
| Footer                                                        |
+--------------------------------------------------------------+
```

### 10) Login Admin (`/admin/login`)

```text
+---------------------------------------------+
| Card Login Admin                             |
| Username                                     |
| Password                                     |
| Tombol Masuk                                 |
+---------------------------------------------+
```

### 11) Dashboard Admin (`/admin`)

```text
+--------------------------------------------------------------+
| Header Admin: Nama user + Logout                             |
+--------------------------------------------------------------+
| Kartu ringkasan: E-Library | Dokumentasi | Artikel           |
+--------------------------------------------------------------+
| Shortcut: Kelola E-Library | Dokumentasi | Artikel | Settings|
+--------------------------------------------------------------+
| Footer                                                        |
+--------------------------------------------------------------+
```

### 12) Kelola E-Library (`/admin/elibrary`)

```text
+--------------------------------------------------------------+
| Form Tambah/Edit E-Library                                   |
+--------------------------------------------------------------+
| Tabel data E-Library: No | Judul | Kategori | Tipe | Aksi    |
+--------------------------------------------------------------+
```

### 13) Kelola Dokumentasi (`/admin/dokumentasi`)

```text
+--------------------------------------------------------------+
| Form Tambah/Edit Dokumentasi                                 |
+--------------------------------------------------------------+
| Tabel data Dokumentasi: No | Judul | Kategori | Aksi         |
+--------------------------------------------------------------+
```

### 14) Kelola Artikel (`/admin/artikel`)

```text
+--------------------------------------------------------------+
| Form Tambah/Edit Artikel                                     |
+--------------------------------------------------------------+
| Tabel data Artikel: No | Judul | Kategori | Aksi            |
| Catatan: badge PDF terkunci untuk item dengan file PDF       |
+--------------------------------------------------------------+
```

### 15) Settings (`/admin/settings`)

```text
+--------------------------------------------------------------+
| Form Pengaturan Situs: nama, tagline, WA, alamat, email     |
| maps embed, tombol simpan                                    |
+--------------------------------------------------------------+
| Preview Google Maps                                           |
+--------------------------------------------------------------+
```
