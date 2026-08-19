# Pembelajaran 5 - Tahap 1

## Mockup -> Object -> Page HTML (Halaman Publik)

Tahap ini melanjutkan Pembelajaran 4.
Siswa tidak hanya membuat tampilan, tetapi mulai berpikir seperti developer: data disiapkan dalam bentuk objek, lalu dipetakan ke komponen halaman.

## A. Tujuan

- Siswa mengubah data dummy menjadi model objek aplikasi.
- Siswa memahami pemetaan objek ke komponen HTML.
- Siswa siap lanjut ke tahap template dinamis (Jinja/FastAPI).

## B. Aktivitas

- Definisikan objek inti: `ELibrary`, `Dokumentasi`, `Artikel`.
- Definisikan objek pendukung halaman profil.
- Petakan atribut objek ke elemen HTML: judul, deskripsi, gambar, link, tabel.

## C. Output

- Dokumen mapping object-field ke komponen halaman.
- 9 halaman publik memiliki struktur konten berbasis data objek.

## D. Waktu

- 1 sampai 2 pertemuan (90-180 menit).

## E. File yang Dibahas pada Tahap 1

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
```

## F. Objek Data Acuan

### 1) Objek `ELibrary`

```json
{
	"judul": "Panduan Menulis Cerita",
	"kategori": "Literasi",
	"deskripsi": "Materi dasar menulis cerita untuk remaja.",
	"gambar": "img-elibrary-1.jpg",
	"link": "panduan-menulis.pdf",
	"link_type": "internal"
}
```

### 2) Objek `Dokumentasi`

```json
{
	"judul": "Kelas Membaca Ceria",
	"kategori": "tunas",
	"deskripsi": "Kegiatan membaca bersama anak-anak.",
	"link_gambar": "tunas-dok-1.jpg",
	"link_video": "https://youtu.be/contoh"
}
```

### 3) Objek `Artikel`

```json
{
	"judul": "Langkah Awal Jualan Online",
	"kategori": "cakra",
	"deskripsi": "Pengenalan marketplace untuk pemula.",
	"gambar": "cakra-artikel-1.jpg",
	"link_pdf": "langkah-awal-jualan-online.pdf"
}
```

### 4) Objek `ProfilProgram`

```json
{
	"nama_program": "Ngrembaka Aksara",
	"tagline": "Gerakan literasi berbasis kampung belajar",
	"visi": "Masyarakat literat, kreatif, produktif",
	"tujuan": [
		"Meningkatkan minat baca",
		"Mendorong keterampilan digital",
		"Menguatkan komunitas belajar"
	]
}
```

### 5) Objek `ProfilKelurahan`

```json
{
	"nama_kelurahan": "Podorejo",
	"jumlah_penduduk": 8500,
	"jumlah_rw": 10,
	"potensi": ["UMKM", "Kerajinan", "Komunitas Belajar"]
}
```

## G. Detail Per File (Tahap 1)

Gunakan format ini saat membimbing siswa:

1. Tujuan file.
2. Objek yang dipakai.
3. Mapping object -> komponen HTML.
4. Contoh struktur HTML minimal.

### 1) `index.html`

Tujuan file:
- Halaman pengenalan utama program.

Objek yang dipakai:
- `ProfilProgram`.

Mapping object -> komponen HTML:
- `nama_program` -> `<h1>` hero.
- `tagline` -> `<p>` hero.
- daftar program inti (statis/array) -> `<ul>`.

Contoh minimal:

```html
<main>
	<section>
		<h1>Ngrembaka Aksara</h1>
		<p>Gerakan literasi berbasis kampung belajar</p>
		<a href="elibrary.html">Lihat E-Library</a>
		<a href="tunas.html">Lihat Pojok Literasi</a>
	</section>
</main>
```

### 2) `beranda.html`

Tujuan file:
- Menampilkan visi dan tujuan program.

Objek yang dipakai:
- `ProfilProgram`.

Mapping object -> komponen HTML:
- `visi` -> `<section>` visi.
- `tujuan[]` -> `<ol><li>...</li></ol>`.

Contoh minimal:

```html
<main>
	<section>
		<h2>Visi</h2>
		<p>Masyarakat literat, kreatif, produktif</p>
	</section>
	<section>
		<h2>Tujuan</h2>
		<ol>
			<li>Meningkatkan minat baca</li>
			<li>Mendorong keterampilan digital</li>
		</ol>
	</section>
</main>
```

### 3) `profil-aksara.html`

Tujuan file:
- Menjelaskan latar belakang dan sasaran program.

Objek yang dipakai:
- `ProfilProgram` + data tambahan `sasaran_program`.

Mapping object -> komponen HTML:
- deskripsi latar belakang -> `<p>`.
- sasaran (kelompok + fokus) -> `<table>`.

Contoh minimal:

```html
<main>
	<h1>Profil Ngrembaka Aksara</h1>
	<section>
		<h2>Latar Belakang</h2>
		<p>Program dibentuk untuk menguatkan literasi warga.</p>
	</section>
	<section>
		<h2>Sasaran</h2>
		<table>
			<tr><th>Kelompok</th><th>Fokus</th></tr>
			<tr><td>Anak</td><td>Literasi dasar</td></tr>
		</table>
	</section>
</main>
```

### 4) `profil-kelurahan.html`

Tujuan file:
- Menampilkan identitas wilayah dampingan.

Objek yang dipakai:
- `ProfilKelurahan`.

Mapping object -> komponen HTML:
- `nama_kelurahan` -> judul halaman.
- `jumlah_penduduk`, `jumlah_rw` -> daftar data.
- `potensi[]` -> list potensi.

Contoh minimal:

```html
<main>
	<h1>Profil Kelurahan Podorejo</h1>
	<section>
		<ul>
			<li>Penduduk: 8.500 jiwa</li>
			<li>RW: 10</li>
		</ul>
	</section>
	<section>
		<h2>Potensi</h2>
		<ul><li>UMKM</li><li>Kerajinan</li></ul>
	</section>
</main>
```

### 5) `elibrary.html`

Tujuan file:
- Menampilkan daftar materi belajar.

Objek yang dipakai:
- daftar `ELibrary[]`.

Mapping object -> komponen HTML:
- `judul` -> judul kartu.
- `kategori` -> label kategori.
- `deskripsi` -> ringkasan isi.
- `link`, `link_type` -> tombol `Unduh PDF` atau `Tonton`.

Contoh minimal:

```html
<section>
	<article>
		<h2>Panduan Menulis Cerita</h2>
		<p>Kategori: Literasi</p>
		<p>Materi dasar menulis cerita untuk remaja.</p>
		<a href="panduan-menulis.pdf">Unduh PDF</a>
	</article>
</section>
```

### 6) `tunas.html`

Tujuan file:
- Menampilkan dokumentasi dan artikel kategori Tunas.

Objek yang dipakai:
- filter `Dokumentasi[]` kategori `tunas`.
- filter `Artikel[]` kategori `tunas`.

Mapping object -> komponen HTML:
- `link_gambar` -> `<img>` dokumentasi.
- `judul`, `deskripsi` -> isi kartu.
- `link_pdf` (jika ada) -> tombol PDF.

Contoh minimal:

```html
<section>
	<h2>Dokumentasi Tunas</h2>
	<article>
		<img src="tunas-dok-1.jpg" alt="Dokumentasi Tunas" />
		<h3>Kelas Membaca Ceria</h3>
		<p>Kegiatan membaca bersama anak-anak.</p>
	</article>
</section>
```

### 7) `karya.html`

Tujuan file:
- Menampilkan karya digital dan publikasi remaja.

Objek yang dipakai:
- filter `Dokumentasi[]` kategori `karya`.
- filter `Artikel[]` kategori `karya`.

Mapping object -> komponen HTML:
- `judul` karya -> judul kartu.
- `deskripsi` -> ringkasan.
- `link_video` (jika ada) -> tombol video/tautan publikasi.

Contoh minimal:

```html
<section>
	<h2>Karya Digital</h2>
	<article>
		<h3>Poster Edukasi Lingkungan</h3>
		<p>Kampanye visual buatan remaja.</p>
		<a href="#">Detail</a>
	</article>
</section>
```

### 8) `cakra.html`

Tujuan file:
- Menampilkan materi edukasi produktif dan artikel pendukung.

Objek yang dipakai:
- data `materi_program[]`.
- filter `Artikel[]` kategori `cakra`.

Mapping object -> komponen HTML:
- `materi_program[]` -> tabel materi.
- `Artikel.judul/deskripsi/link_pdf` -> kartu artikel + tombol PDF.

Contoh minimal:

```html
<section>
	<h2>Materi Program</h2>
	<table>
		<tr><th>No</th><th>Materi</th><th>Target</th></tr>
		<tr><td>1</td><td>Dasar Kewirausahaan</td><td>Remaja</td></tr>
	</table>
</section>
```

### 9) `kersa.html`

Tujuan file:
- Menampilkan program lansia dan keterampilan produktif.

Objek yang dipakai:
- filter `Artikel[]` kategori `kersa`.
- data section statis: kesehatan + keterampilan.

Mapping object -> komponen HTML:
- judul artikel kesehatan -> kartu kesehatan.
- judul artikel keterampilan -> kartu keterampilan.
- `link_pdf` (jika ada) -> tombol PDF.

Contoh minimal:

```html
<section>
	<h2>Program Kesehatan Lansia</h2>
	<article>
		<h3>Senam Lansia Mingguan</h3>
		<p>Pendampingan hidup sehat untuk warga lanjut usia.</p>
	</article>
</section>
```

## H. Checklist Penilaian Tahap 1

1. Semua file publik tersedia (9 file).
2. Tiap file memiliki tujuan halaman yang tepat.
3. Mapping field objek ke elemen HTML sudah benar.
4. Halaman konten (`elibrary`, `tunas`, `karya`, `cakra`, `kersa`) sudah berbentuk list kartu/tabel.
5. Struktur HTML tetap rapi (`nav`, `main`, `section`, `article`, `table` bila perlu).

Skor per poin: 1-4.
Nilai akhir = rata-rata 5 poin.

## I. Lanjutan Tahap 2 (Preview)

Setelah Tahap 1 selesai, lanjut ke Tahap 2:
- objek data dipindah ke backend sederhana (Python dictionary/list),
- halaman mulai dirender dinamis dengan template,
- dan siswa mulai memahami alur data -> tampilan nyata.

## Kunci jawaban tahap 1

Gunakan kunci ini untuk mengecek hasil siswa dengan cepat.

### A. Jawaban Inti Per File

1. `index.html`
- Wajib ada: hero, nama program, tagline, CTA ke `elibrary.html` dan `tunas.html`.
- Objek utama: `ProfilProgram`.

2. `beranda.html`
- Wajib ada: section visi dan tujuan.
- Objek utama: `ProfilProgram` (`visi`, `tujuan[]`).

3. `profil-aksara.html`
- Wajib ada: latar belakang + tabel sasaran.
- Objek utama: `ProfilProgram` + `sasaran_program[]`.

4. `profil-kelurahan.html`
- Wajib ada: data penduduk, RW, dan potensi wilayah.
- Objek utama: `ProfilKelurahan`.

5. `elibrary.html`
- Wajib ada: list materi dalam bentuk kartu (`article`).
- Objek utama: `ELibrary[]`.
- Mapping penting: `judul`, `kategori`, `deskripsi`, `link`, `link_type`.

6. `tunas.html`
- Wajib ada: section dokumentasi/artikel kategori tunas.
- Objek utama: `Dokumentasi[]` + `Artikel[]` (filter `kategori=tunas`).

7. `karya.html`
- Wajib ada: section karya digital dan publikasi.
- Objek utama: `Dokumentasi[]` + `Artikel[]` (filter `kategori=karya`).

8. `cakra.html`
- Wajib ada: tabel materi + artikel pendukung.
- Objek utama: `materi_program[]` + `Artikel[]` (filter `kategori=cakra`).

9. `kersa.html`
- Wajib ada: section kesehatan lansia + keterampilan produktif.
- Objek utama: `Artikel[]` (filter `kategori=kersa`).

### B. Jawaban Struktur HTML Minimal (Wajib Konsisten)

Setiap file minimal mengikuti pola ini:

```html
<!doctype html>
<html lang="id">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Nama Halaman</title>
</head>
<body>
	<nav>...</nav>
	<main>
		<section>...</section>
	</main>
</body>
</html>
```

Catatan:
- File boleh berbeda isi, tetapi struktur semantik tetap dipertahankan.
- `table` wajib dipakai untuk data tabular (contoh: sasaran/materi).

### C. Kriteria Lulus Tahap 1

Siswa dinyatakan tuntas jika:

1. 9 file publik lengkap dan bisa dibuka.
2. Tiap file menampilkan data sesuai objek yang tepat.
3. Mapping objek ke elemen HTML benar.
4. Navigasi antar halaman utama berjalan.
5. Tidak ada file kosong.

### D. Skema Nilai Rekomendasi

- 86-100: Sangat Baik (struktur tepat, mapping kuat, konten lengkap)
- 76-85: Baik (struktur benar, ada sedikit bagian kurang detail)
- 66-75: Cukup (masih ada mapping/section yang hilang)
- <=65: Perlu bimbingan ulang (banyak komponen inti belum sesuai)


## JAWABAN DETAIL SETIAP FILE 

### 1) `index.html`

Tujuan:
- Menampilkan pintu masuk utama program.

Checklist isi:
- Navbar sederhana.
- Hero (`h1` + tagline).
- Ringkasan 4 program.
- Tombol ke `elibrary.html` dan `tunas.html`.

Kunci jawaban:

```html
<!doctype html>
<html lang="id">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Landing - Ngrembaka Aksara</title>
</head>
<body>
	<nav>
		<a href="index.html">Landing</a>
		<a href="beranda.html">Beranda</a>
		<a href="elibrary.html">E-Library</a>
	</nav>

	<main>
		<section>
			<h1>Ngrembaka Aksara</h1>
			<p>Gerakan literasi berbasis kampung belajar.</p>
			<a href="elibrary.html">Lihat E-Library</a>
			<a href="tunas.html">Lihat Pojok Literasi</a>
		</section>

		<section>
			<h2>Program Inti</h2>
			<ul>
				<li>Tunas</li>
				<li>Karya</li>
				<li>Cakra</li>
				<li>Kersa</li>
			</ul>
		</section>
	</main>
</body>
</html>
```

### 2) `beranda.html`

Tujuan:
- Menjelaskan visi dan tujuan program.

Checklist isi:
- Judul halaman.
- Section visi.
- Section tujuan (list).

Kunci jawaban:

```html
<!doctype html>
<html lang="id">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Beranda</title>
</head>
<body>
	<main>
		<section>
			<h1>Beranda Program</h1>
			<p>Selamat datang di Ngrembaka Aksara.</p>
		</section>

		<section>
			<h2>Visi</h2>
			<p>Masyarakat literat, kreatif, dan produktif.</p>
		</section>

		<section>
			<h2>Tujuan</h2>
			<ol>
				<li>Meningkatkan minat baca.</li>
				<li>Mendorong keterampilan digital.</li>
				<li>Menguatkan komunitas belajar.</li>
			</ol>
		</section>
	</main>
</body>
</html>
```

### 3) `profil-aksara.html`

Tujuan:
- Menampilkan latar belakang dan sasaran program.

Checklist isi:
- Judul profil.
- Latar belakang.
- Tabel sasaran.

Kunci jawaban:

```html
<!doctype html>
<html lang="id">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Profil Aksara</title>
</head>
<body>
	<main>
		<h1>Profil Ngrembaka Aksara</h1>

		<section>
			<h2>Latar Belakang</h2>
			<p>Program dibentuk untuk menguatkan budaya baca dan pembelajaran warga.</p>
		</section>

		<section>
			<h2>Sasaran</h2>
			<table>
				<tr><th>Kelompok</th><th>Fokus</th></tr>
				<tr><td>Anak</td><td>Literasi dasar</td></tr>
				<tr><td>Remaja</td><td>Kreativitas digital</td></tr>
			</table>
		</section>
	</main>
</body>
</html>
```

### 4) `profil-kelurahan.html`

Tujuan:
- Menampilkan data wilayah dampingan.

Checklist isi:
- Judul kelurahan.
- Data demografi utama.
- Potensi wilayah.

Kunci jawaban:

```html
<!doctype html>
<html lang="id">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Profil Kelurahan</title>
</head>
<body>
	<main>
		<h1>Profil Kelurahan Podorejo</h1>

		<section>
			<h2>Data Demografi</h2>
			<ul>
				<li>Jumlah penduduk: 8.500 jiwa</li>
				<li>Jumlah RW: 10</li>
			</ul>
		</section>

		<section>
			<h2>Potensi Wilayah</h2>
			<ul>
				<li>UMKM lokal</li>
				<li>Kerajinan rumah tangga</li>
				<li>Komunitas belajar</li>
			</ul>
		</section>
	</main>
</body>
</html>
```

### 5) `elibrary.html`

Tujuan:
- Menampilkan daftar materi belajar.

Checklist isi:
- Judul halaman.
- Filter kategori.
- Minimal 1 kartu materi.

Kunci jawaban:

```html
<!doctype html>
<html lang="id">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>E-Library</title>
</head>
<body>
	<main>
		<h1>E-Library</h1>

		<section>
			<label for="kategori">Kategori</label>
			<select id="kategori">
				<option>Semua</option>
				<option>Literasi</option>
				<option>Keterampilan</option>
			</select>
		</section>

		<section>
			<article>
				<h2>Panduan Menulis Cerita</h2>
				<p>Kategori: Literasi</p>
				<p>Materi dasar menulis cerita untuk remaja.</p>
				<a href="panduan-menulis.pdf">Unduh PDF</a>
			</article>
		</section>
	</main>
</body>
</html>
```

### 6) `tunas.html`

Tujuan:
- Menampilkan konten literasi anak.

Checklist isi:
- Deskripsi program.
- Dokumentasi kegiatan.
- Artikel pendukung (opsional minimal 1 item).

Kunci jawaban:

```html
<!doctype html>
<html lang="id">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Tunas</title>
</head>
<body>
	<main>
		<h1>Pojok Literasi Tunas</h1>

		<section>
			<h2>Deskripsi Program</h2>
			<p>Program literasi anak: membaca, menulis, dan bercerita.</p>
		</section>

		<section>
			<h2>Dokumentasi</h2>
			<article>
				<img src="tunas-dok-1.jpg" alt="Dokumentasi Tunas" />
				<h3>Kelas Membaca Ceria</h3>
				<p>Kegiatan membaca bersama di balai RW.</p>
			</article>
		</section>
	</main>
</body>
</html>
```

### 7) `karya.html`

Tujuan:
- Menampilkan karya dan publikasi remaja.

Checklist isi:
- Section karya digital.
- Section publikasi/medsos.
- Tombol detail.

Kunci jawaban:

```html
<!doctype html>
<html lang="id">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Karya</title>
</head>
<body>
	<main>
		<h1>Pojok Literasi Karya</h1>

		<section>
			<h2>Karya Digital</h2>
			<article>
				<h3>Poster Edukasi Lingkungan</h3>
				<p>Kampanye visual buatan remaja.</p>
				<a href="#">Detail</a>
			</article>
		</section>

		<section>
			<h2>Publikasi Media Sosial</h2>
			<article>
				<h3>Kampanye Baca 15 Menit</h3>
				<p>Konten edukasi singkat di media sosial.</p>
			</article>
		</section>
	</main>
</body>
</html>
```

### 8) `cakra.html`

Tujuan:
- Menampilkan materi program produktif + artikel.

Checklist isi:
- Tabel materi.
- 1 kartu artikel.
- Tombol PDF pada artikel.

Kunci jawaban:

```html
<!doctype html>
<html lang="id">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Cakra</title>
</head>
<body>
	<main>
		<h1>Pojok Literasi Cakra</h1>

		<section>
			<h2>Materi Program</h2>
			<table>
				<tr><th>No</th><th>Materi</th><th>Target</th></tr>
				<tr><td>1</td><td>Dasar Kewirausahaan</td><td>Remaja</td></tr>
			</table>
		</section>

		<section>
			<h2>Artikel</h2>
			<article>
				<h3>Langkah Awal Jualan Online</h3>
				<p>Pengenalan marketplace untuk pemula.</p>
				<a href="langkah-awal-jualan-online.pdf">PDF</a>
			</article>
		</section>
	</main>
</body>
</html>
```

### 9) `kersa.html`

Tujuan:
- Menampilkan program lansia dan keterampilan produktif.

Checklist isi:
- Section kesehatan lansia.
- Section keterampilan produktif.
- Minimal 1 artikel tiap section.

Kunci jawaban:

```html
<!doctype html>
<html lang="id">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Kersa</title>
</head>
<body>
	<main>
		<h1>Pojok Literasi Kersa</h1>

		<section>
			<h2>Program Kesehatan Lansia</h2>
			<article>
				<h3>Senam Lansia Mingguan</h3>
				<p>Pendampingan hidup sehat untuk warga lanjut usia.</p>
			</article>
		</section>

		<section>
			<h2>Program Keterampilan Produktif</h2>
			<article>
				<h3>Pelatihan Kerajinan Rumah Tangga</h3>
				<p>Praktik membuat produk sederhana bernilai jual.</p>
			</article>
		</section>
	</main>
</body>
</html>
```

