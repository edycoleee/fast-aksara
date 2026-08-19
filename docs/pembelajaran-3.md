# Pembelajaran 3 - Implementasi HTML Per File (Lanjutan Pembelajaran 2)

Dokumen ini melanjutkan Pembelajaran 2.
Fokus Pembelajaran 3 adalah menulis file HTML satu per satu sampai semua halaman lengkap dan saling terhubung.

## A. Tujuan Pembelajaran

- Siswa mampu membuat 15 file HTML sesuai hasil mockup Pembelajaran 2.
- Siswa memahami struktur halaman publik dan admin.
- Siswa mampu menghubungkan navigasi antar halaman.
- Siswa siap masuk ke tahap styling CSS pada pembelajaran berikutnya.

## B. Alur Waktu dan Tahapan Belajar

### Tahap 1 - Setup Proyek HTML (20-30 menit)

Aktivitas:
- Membuat folder `latihan-mockup`.
- Membuat 15 file HTML kosong.
- Menjalankan server lokal.

Output:
- Semua file tersedia dan bisa diakses via browser.

Perintah jalankan:

```bash
cd latihan-mockup
python -m http.server 5500
```

### Tahap 2 - Halaman Publik Dasar (45-60 menit)

Aktivitas:
- Mengerjakan `index.html`, `beranda.html`, `profil-aksara.html`, `profil-kelurahan.html`.

Output:
- Halaman informasi utama lengkap (judul, isi, dan navigasi).

### Tahap 3 - Halaman Konten Program (60-90 menit)

Aktivitas:
- Mengerjakan `elibrary.html`, `tunas.html`, `karya.html`, `cakra.html`, `kersa.html`.

Output:
- Semua halaman program memiliki list konten dan tombol aksi.

### Tahap 4 - Halaman Admin (60-90 menit)

Aktivitas:
- Mengerjakan `admin-login.html`, `admin-dashboard.html`, `admin-elibrary.html`, `admin-dokumentasi.html`, `admin-artikel.html`, `admin-settings.html`.

Output:
- Semua halaman CRUD admin tersedia dalam bentuk HTML statis.

### Tahap 5 - Cek Integrasi (30-45 menit)

Aktivitas:
- Mengecek semua link menu.
- Mengecek struktur heading, section, form, dan table.

Output:
- Tidak ada halaman kosong atau link putus.

Total waktu rekomendasi:
- 3 sampai 5 pertemuan (270-450 menit), tergantung kecepatan kelas.

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
```

## D. Kunci Jawaban Setiap File (HTML Tanpa CSS)

Catatan:
- Semua contoh di bawah adalah jawaban minimal.
- Siswa boleh menambah elemen selama struktur utama tetap benar.

### 1) `index.html` (Landing)

```html
<!doctype html>
<html lang="id">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Landing</title></head>
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
	</main>
	<footer>Kelurahan Podorejo</footer>
</body>
</html>
```

### 2) `beranda.html`

```html
<!doctype html>
<html lang="id">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Beranda</title></head>
<body>
	<main>
		<section><h1>Beranda Program</h1><p>Selamat datang di Ngrembaka Aksara.</p></section>
		<section><h2>Visi</h2><p>Masyarakat literat, kreatif, produktif.</p></section>
		<section>
			<h2>Tujuan</h2>
			<ol><li>Meningkatkan minat baca.</li><li>Mendorong keterampilan digital.</li><li>Menguatkan komunitas belajar.</li></ol>
		</section>
	</main>
</body>
</html>
```

### 3) `profil-aksara.html`

```html
<!doctype html>
<html lang="id">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Profil Aksara</title></head>
<body>
	<main>
		<h1>Profil Ngrembaka Aksara</h1>
		<section><h2>Sejarah</h2><p>Program lahir dari kebutuhan literasi warga.</p></section>
		<section><h2>Latar Belakang</h2><ul><li>Minat baca rendah</li><li>Akses terbatas</li></ul></section>
		<section>
			<h2>Sasaran</h2>
			<table><tr><th>Kelompok</th><th>Fokus</th></tr><tr><td>Anak</td><td>Literasi dasar</td></tr></table>
		</section>
	</main>
</body>
</html>
```

### 4) `profil-kelurahan.html`

```html
<!doctype html>
<html lang="id">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Profil Kelurahan</title></head>
<body>
	<main>
		<h1>Profil Kelurahan Podorejo</h1>
		<section><h2>Ringkasan</h2><p>Kelurahan dengan potensi UMKM.</p></section>
		<section><h2>Demografi</h2><ul><li>Penduduk: 8.500 jiwa</li><li>RW: 10</li></ul></section>
		<section><h2>Potensi</h2><p>Kerajinan, pangan, komunitas belajar.</p></section>
	</main>
</body>
</html>
```

### 5) `elibrary.html`

```html
<!doctype html>
<html lang="id">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>E-Library</title></head>
<body>
	<main>
		<h1>E-Library</h1>
		<section><label>Kategori</label><select><option>Semua</option><option>Literasi</option></select></section>
		<section>
			<article>
				<h2>Panduan Menulis Cerita</h2>
				<p>Kategori: Literasi</p>
				<a href="#">Detail</a>
				<a href="#">Unduh PDF</a>
			</article>
		</section>
	</main>
</body>
</html>
```

### 6) `tunas.html`

```html
<!doctype html>
<html lang="id">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Tunas</title></head>
<body>
	<main>
		<h1>Pojok Literasi Tunas</h1>
		<section><h2>Deskripsi Program</h2><p>Literasi anak: baca, tulis, cerita.</p></section>
		<section><h2>Dokumentasi</h2><article><h3>Kelas Membaca Ceria</h3><a href="#">Detail</a></article></section>
	</main>
</body>
</html>
```

### 7) `karya.html`

```html
<!doctype html>
<html lang="id">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Karya</title></head>
<body>
	<main>
		<h1>Pojok Literasi Karya</h1>
		<section><h2>Karya Digital</h2><article><h3>Poster Edukasi</h3><a href="#">Detail</a></article></section>
		<section><h2>Karya Sosial Media</h2><article><h3>Kampanye Baca</h3></article></section>
	</main>
</body>
</html>
```

### 8) `cakra.html`

```html
<!doctype html>
<html lang="id">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Cakra</title></head>
<body>
	<main>
		<h1>Pojok Literasi Cakra</h1>
		<section>
			<h2>Materi Program</h2>
			<table><tr><th>No</th><th>Materi</th></tr><tr><td>1</td><td>Dasar Kewirausahaan</td></tr></table>
		</section>
		<section><h2>Artikel</h2><article><h3>Langkah Awal Jualan Online</h3><a href="#">PDF</a></article></section>
	</main>
</body>
</html>
```

### 9) `kersa.html`

```html
<!doctype html>
<html lang="id">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Kersa</title></head>
<body>
	<main>
		<h1>Pojok Literasi Kersa</h1>
		<section><h2>Program Kesehatan Lansia</h2><article><h3>Senam Lansia Mingguan</h3></article></section>
		<section><h2>Program Keterampilan Produktif</h2><article><h3>Pelatihan Kerajinan</h3></article></section>
	</main>
</body>
</html>
```

### 10) `admin-login.html`

```html
<!doctype html>
<html lang="id">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Login Admin</title></head>
<body>
	<main>
		<h1>Login Admin</h1>
		<form>
			<label>Username</label><input type="text" required>
			<label>Password</label><input type="password" required>
			<button type="submit">Masuk</button>
		</form>
	</main>
</body>
</html>
```

### 11) `admin-dashboard.html`

```html
<!doctype html>
<html lang="id">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Dashboard Admin</title></head>
<body>
	<main>
		<h1>Dashboard Admin</h1>
		<section><article><h2>Total E-Library</h2><p>12</p></article></section>
		<section>
			<a href="admin-elibrary.html">Kelola E-Library</a>
			<a href="admin-dokumentasi.html">Kelola Dokumentasi</a>
			<a href="admin-artikel.html">Kelola Artikel</a>
		</section>
	</main>
</body>
</html>
```

### 12) `admin-elibrary.html`

```html
<!doctype html>
<html lang="id">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Admin E-Library</title></head>
<body>
	<main>
		<h1>Kelola E-Library</h1>
		<form>
			<input type="text" placeholder="Judul">
			<select><option>External URL</option><option>Internal PDF</option></select>
			<button type="submit">Simpan</button>
		</form>
		<table>
			<tr><th>No</th><th>Judul</th><th>Aksi</th></tr>
			<tr><td>1</td><td>Panduan Menulis</td><td><button>Edit</button><button>Hapus</button></td></tr>
		</table>
	</main>
</body>
</html>
```

### 13) `admin-dokumentasi.html`

```html
<!doctype html>
<html lang="id">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Admin Dokumentasi</title></head>
<body>
	<main>
		<h1>Kelola Dokumentasi</h1>
		<form>
			<input type="text" placeholder="Judul dokumentasi">
			<select><option>Tunas</option><option>Karya</option><option>Cakra</option><option>Kersa</option></select>
			<button type="submit">Simpan</button>
		</form>
		<table>
			<tr><th>No</th><th>Judul</th><th>Kategori</th><th>Aksi</th></tr>
			<tr><td>1</td><td>Kegiatan Membaca</td><td>Tunas</td><td><button>Edit</button><button>Hapus</button></td></tr>
		</table>
	</main>
</body>
</html>
```

### 14) `admin-artikel.html`

```html
<!doctype html>
<html lang="id">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Admin Artikel</title></head>
<body>
	<main>
		<h1>Kelola Artikel</h1>
		<form>
			<input type="text" placeholder="Judul artikel">
			<textarea placeholder="Ringkasan"></textarea>
			<button type="submit">Simpan</button>
		</form>
		<table>
			<tr><th>No</th><th>Judul</th><th>Kategori</th><th>Aksi</th></tr>
			<tr><td>1</td><td>Tips Belajar Konsisten</td><td>Tunas</td><td><button>Edit</button><button>Hapus</button></td></tr>
		</table>
	</main>
</body>
</html>
```

### 15) `admin-settings.html`

```html
<!doctype html>
<html lang="id">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Settings</title></head>
<body>
	<main>
		<h1>Settings Website</h1>
		<form>
			<label>Nama Situs</label><input type="text" value="Ngrembaka Aksara">
			<label>Tagline</label><input type="text" value="Literasi untuk Semua">
			<label>WhatsApp</label><input type="text" value="08123456789">
			<label>Alamat</label><textarea>Podorejo, Ngaliyan, Semarang</textarea>
			<button type="submit">Simpan Pengaturan</button>
		</form>
	</main>
</body>
</html>
```

## E. Rubrik Penilaian Praktik

Gunakan skor 1-4 pada tiap kriteria:

1. Kelengkapan file 15 halaman.
2. Kebenaran struktur tag HTML.
3. Kesesuaian konten dengan fungsi halaman.
4. Keterhubungan link antar halaman.
5. Kerapian penulisan HTML.

Nilai akhir = rata-rata semua kriteria.

## F. Penutup untuk Guru

Setelah siswa selesai Pembelajaran 3:

- Siswa sudah memiliki mini website statis versi lengkap.
- Siswa siap masuk Pembelajaran 4 (CSS dasar: warna, spacing, tipografi, layout).