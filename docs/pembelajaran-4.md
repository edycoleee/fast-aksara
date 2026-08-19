# Pembelajaran 4 - CSS Dasar sampai Layout Responsif

Dokumen ini melanjutkan Pembelajaran 3.
Jika pada Pembelajaran 3 siswa sudah punya 15 halaman HTML tanpa style, maka di Pembelajaran 4 siswa mulai mempercantik tampilan dengan CSS.

## A. Tujuan Pembelajaran

- Siswa memahami cara menghubungkan file CSS ke semua halaman HTML.
- Siswa mampu memberi warna, jarak, tipografi, dan kartu konten.
- Siswa mampu membuat layout responsive sederhana untuk mobile.
- Siswa menghasilkan tampilan web yang rapi dan konsisten di 15 halaman.

## B. Capaian Akhir

Di akhir Pembelajaran 4, siswa memiliki:

1. Folder HTML yang sama seperti Pembelajaran 3.
2. Tambahan 1 file CSS global: `style.css`.
3. Semua halaman publik dan admin sudah memiliki style dasar.
4. Tampilan masih sederhana, tetapi sudah enak dibaca dan tidak berantakan di HP.

## C. Struktur Folder Praktik

```text
latihan-mockup/
|-- index.html
|-- beranda.html
|-- profil-aksara.html
|-- profil-kelurahan.html
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
|-- style.css
```

## D. Tahapan Belajar (Step by Step)

### Tahap 1 - Hubungkan CSS ke Semua File (20-30 menit)

Aktivitas:
- Tambahkan tag CSS di bagian `<head>` semua file HTML.

Template yang ditambahkan:

```html
<link rel="stylesheet" href="style.css" />
```

Output:
- Semua halaman sudah membaca style dari satu file yang sama.

### Tahap 2 - Reset dan Style Dasar (30-45 menit)

Aktivitas:
- Buat aturan dasar untuk body, heading, paragraf, link, tombol.

Output:
- Semua halaman punya font, warna, dan spasi dasar yang seragam.

### Tahap 3 - Layout Navbar, Main, Footer (45-60 menit)

Aktivitas:
- Rapikan menu, area konten utama, dan footer.
- Batasi lebar konten agar nyaman dibaca.

Output:
- Struktur halaman tidak terlalu mepet layar.

### Tahap 4 - Kartu Konten dan Tabel (45-60 menit)

Aktivitas:
- Buat class kartu (`.card`) untuk artikel/daftar konten.
- Rapikan tabel admin.

Output:
- Halaman E-Library, Tunas, Karya, Cakra, Kersa, dan admin terlihat lebih terstruktur.

### Tahap 5 - Responsive Mobile (45-60 menit)

Aktivitas:
- Gunakan media query.
- Ubah menu dan grid agar nyaman di layar kecil.

Output:
- Tampilan tetap rapi di ukuran HP.

Total waktu rekomendasi:
- 3 sampai 4 pertemuan (270-360 menit).

## E. Kunci Jawaban `style.css` (Global)

Gunakan ini sebagai jawaban minimal yang bisa dipakai semua halaman:

```css
* {
	box-sizing: border-box;
}

body {
	margin: 0;
	font-family: Arial, sans-serif;
	background: #f5f7fb;
	color: #1f2937;
	line-height: 1.6;
}

nav {
	background: #0f172a;
	padding: 12px 16px;
	display: flex;
	gap: 12px;
	flex-wrap: wrap;
}

nav a {
	color: #ffffff;
	text-decoration: none;
	font-weight: 600;
}

main {
	max-width: 1000px;
	margin: 20px auto;
	padding: 0 16px;
}

section {
	background: #ffffff;
	border: 1px solid #e5e7eb;
	border-radius: 10px;
	padding: 16px;
	margin-bottom: 16px;
}

h1, h2, h3 {
	margin-top: 0;
}

article {
	border: 1px solid #e5e7eb;
	border-radius: 8px;
	padding: 12px;
	margin-bottom: 10px;
}

img {
	max-width: 100%;
	height: auto;
	border-radius: 8px;
}

table {
	width: 100%;
	border-collapse: collapse;
	background: #fff;
}

th,
td {
	border: 1px solid #e5e7eb;
	padding: 10px;
	text-align: left;
}

th {
	background: #eef2ff;
}

form {
	display: grid;
	gap: 10px;
}

input,
select,
textarea,
button {
	padding: 10px;
	border: 1px solid #cbd5e1;
	border-radius: 8px;
	font: inherit;
}

button {
	background: #1d4ed8;
	color: #fff;
	border: none;
	cursor: pointer;
	font-weight: 600;
}

button:hover {
	background: #1e40af;
}

footer {
	text-align: center;
	padding: 20px;
	color: #64748b;
}

@media (max-width: 768px) {
	nav {
		flex-direction: column;
		align-items: flex-start;
	}

	main {
		margin: 12px auto;
		padding: 0 12px;
	}

	section {
		padding: 12px;
	}

	table,
	thead,
	tbody,
	th,
	td,
	tr {
		display: block;
	}

	thead {
		display: none;
	}

	tr {
		margin-bottom: 10px;
		border: 1px solid #e5e7eb;
		border-radius: 8px;
		padding: 8px;
		background: #fff;
	}

	td {
		border: none;
		padding: 6px 0;
	}
}
```

## F. Kunci Jawaban Per File (Update dari Pembelajaran 3)

Inti Pembelajaran 4 bukan membuat HTML baru, tetapi menambahkan class agar style bisa diterapkan konsisten.

### 1) `index.html`

Tambahan minimal:
- Link ke `style.css` di `<head>`.
- Gunakan struktur `nav`, `main`, `section`, `footer`.

Contoh potongan:

```html
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Landing</title>
	<link rel="stylesheet" href="style.css" />
</head>
```

### 2) `beranda.html`

Tambahan minimal:
- Link CSS.
- Setiap blok visi/tujuan berada dalam `section`.

### 3) `profil-aksara.html`

Tambahan minimal:
- Link CSS.
- Tabel sasaran tetap pakai `<table>`, `<tr>`, `<th>`, `<td>` agar styling tabel aktif.

### 4) `profil-kelurahan.html`

Tambahan minimal:
- Link CSS.
- Data ringkasan dipisah per section.

### 5) `elibrary.html`

Tambahan minimal:
- Link CSS.
- Tiap item e-library dalam `article` agar tampil seperti kartu.

### 6) `tunas.html`

Tambahan minimal:
- Link CSS.
- Dokumentasi/artikel dibungkus `article`.

### 7) `karya.html`

Tambahan minimal:
- Link CSS.
- Karya digital dan media sosial dipisah section.

### 8) `cakra.html`

Tambahan minimal:
- Link CSS.
- Materi tetap dalam tabel.
- Artikel tetap dalam `article`.

### 9) `kersa.html`

Tambahan minimal:
- Link CSS.
- Program kesehatan dan keterampilan dipisah section.

### 10) `admin-login.html`

Tambahan minimal:
- Link CSS.
- Form tetap pakai elemen asli (`label`, `input`, `button`).

### 11) `admin-dashboard.html`

Tambahan minimal:
- Link CSS.
- Data ringkasan dalam `article`.

### 12) `admin-elibrary.html`

Tambahan minimal:
- Link CSS.
- Form input dan tabel tetap dipertahankan.

### 13) `admin-dokumentasi.html`

Tambahan minimal:
- Link CSS.
- Struktur form + tabel harus lengkap.

### 14) `admin-artikel.html`

Tambahan minimal:
- Link CSS.
- Gunakan `textarea` untuk ringkasan artikel.

### 15) `admin-settings.html`

Tambahan minimal:
- Link CSS.
- Form pengaturan berisi field nama situs, tagline, kontak, alamat.

## G. Checklist Penilaian Guru

Gunakan ceklis berikut:

1. Semua file HTML sudah terhubung ke `style.css`.
2. Tampilan tidak mepet dan mudah dibaca.
3. Form dan tabel admin sudah rapi.
4. Tampilan mobile masih nyaman dibuka.
5. Struktur HTML dari Pembelajaran 3 tidak rusak.

Skor tiap poin: 1-4.
Nilai akhir = rata-rata 5 poin.

## H. Penutup

Setelah Pembelajaran 4 selesai:

- Siswa sudah menguasai alur HTML + CSS dasar.
- Siswa siap lanjut ke Pembelajaran 5: komponen lebih lanjut, interaksi JavaScript sederhana, dan persiapan integrasi ke template FastAPI.
