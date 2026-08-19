# Kunci Jawaban Pembelajaran 2

Dokumen ini berisi kunci jawaban untuk tugas mockup pada Pembelajaran 2, meliputi:

1. Struktur folder HTML latihan.
2. Kunci jawaban mockup semua halaman publik dan admin.
3. Kunci minimum isi HTML per halaman (kerangka yang benar).

## A. Struktur Folder Jawaban

Gunakan struktur ini saat siswa membuat mockup HTML:

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

## B. Template Kunci Jawaban Mockup

Format penilaian guru:

1. Tujuan halaman benar.
2. Section utama lengkap.
3. Data tampil sesuai kebutuhan halaman.
4. Aksi tombol sesuai alur user/admin.
5. Kondisi kosong (empty state) disiapkan.

## C. Kunci Jawaban Semua Halaman

### 1) Landing (`/`)

- Tujuan: memperkenalkan program Ngrembaka Aksara.
- Section utama: Navbar, Hero, Ringkasan Program, Footer.
- Data tampil: nama program, tagline, menu utama, CTA, ringkasan profil.
- Aksi: Lihat E-Library, Lihat Pojok Literasi.
- Empty state: tidak wajib (halaman informasi statis).

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
			<h2>Ringkasan Program</h2>
			<ul>
				<li>Tunas: literasi anak</li>
				<li>Karya: kreativitas remaja</li>
				<li>Cakra: edukasi produktif</li>
				<li>Kersa: lansia dan keterampilan</li>
			</ul>
		</section>
	</main>
	<footer>Kelurahan Podorejo</footer>
</body>
</html>
```

### 2) Beranda (`/beranda`)

- Tujuan: menampilkan visi dan tujuan program.
- Section utama: Judul halaman, Kartu Visi, Kartu Tujuan.
- Data tampil: teks visi, daftar tujuan program.
- Aksi: opsional tombol kembali ke landing atau navigasi utama.
- Empty state: jika data visi/tujuan kosong, tampilkan "Visi/tujuan belum diatur".

```html
<main>
	<section>
		<h1>Beranda Program</h1>
		<p>Selamat datang di Ngrembaka Aksara.</p>
	</section>

	<section>
		<h2>Visi</h2>
		<p>Terwujudnya masyarakat literat, kreatif, dan produktif.</p>
	</section>

	<section>
		<h2>Tujuan</h2>
		<ol>
			<li>Meningkatkan minat baca warga.</li>
			<li>Mendorong keterampilan digital.</li>
			<li>Menguatkan jejaring komunitas belajar.</li>
		</ol>
	</section>
</main>
```

### 3) Profil Aksara (`/profil/ngrembaka-aksara`)

- Tujuan: menjelaskan latar belakang dan struktur program.
- Section utama: Sejarah, Latar Belakang, Sasaran, Tim.
- Data tampil: narasi sejarah, daftar masalah, tabel sasaran, data tim.
- Aksi: navigasi antar section (opsional).
- Empty state: "Data profil belum lengkap".

```html
<main>
	<h1>Profil Ngrembaka Aksara</h1>

	<section>
		<h2>Sejarah</h2>
		<p>Program dimulai dari kebutuhan ruang literasi warga.</p>
	</section>

	<section>
		<h2>Latar Belakang</h2>
		<ul>
			<li>Minat baca rendah.</li>
			<li>Akses materi belajar terbatas.</li>
			<li>Perlu kegiatan lintas usia.</li>
		</ul>
	</section>

	<section>
		<h2>Sasaran</h2>
		<table>
			<tr><th>Kelompok</th><th>Fokus</th></tr>
			<tr><td>Anak</td><td>Literasi dasar</td></tr>
			<tr><td>Remaja</td><td>Karya digital</td></tr>
			<tr><td>Dewasa</td><td>Produktivitas</td></tr>
		</table>
	</section>
</main>
```

### 4) Profil Kelurahan (`/profil/kelurahan-podorejo`)

- Tujuan: memperlihatkan profil wilayah dampingan.
- Section utama: Ringkasan wilayah, data demografi, potensi wilayah.
- Data tampil: jumlah penduduk, luas, wilayah, potensi.
- Aksi: navigasi ke halaman program.
- Empty state: "Data kelurahan belum tersedia".

```html
<main>
	<h1>Profil Kelurahan Podorejo</h1>

	<section>
		<h2>Ringkasan Wilayah</h2>
		<p>Kelurahan dengan potensi UMKM dan komunitas aktif.</p>
	</section>

	<section>
		<h2>Data Demografi</h2>
		<ul>
			<li>Jumlah penduduk: 8.500 jiwa</li>
			<li>Luas wilayah: 3.2 km2</li>
			<li>Jumlah RW: 10</li>
		</ul>
	</section>

	<section>
		<h2>Potensi</h2>
		<p>Kerajinan, olahan pangan, dan komunitas belajar.</p>
	</section>
</main>
```

### 5) E-Library (`/elibrary`)

- Tujuan: menampilkan koleksi materi belajar.
- Section utama: Header koleksi, filter kategori, daftar kartu, pagination.
- Data tampil per kartu: judul, kategori, deskripsi, gambar, jenis link.
- Aksi: Detail, Tonton (external), Unduh PDF (internal).
- Empty state: "Belum ada koleksi".

```html
<main>
	<h1>E-Library</h1>

	<section>
		<label for="kategori">Filter kategori:</label>
		<select id="kategori">
			<option>Semua</option>
			<option>Literasi</option>
			<option>Keterampilan</option>
		</select>
	</section>

	<section>
		<article>
			<img src="img-elibrary-1.jpg" alt="cover" />
			<h2>Panduan Menulis Cerita</h2>
			<p>Kategori: Literasi</p>
			<p>Ringkasan materi untuk siswa SMP/SMA.</p>
			<a href="program_detail.html">Detail</a>
			<a href="#">Unduh PDF</a>
		</article>
	</section>

	<nav aria-label="pagination">
		<a href="#">Prev</a>
		<span>1</span>
		<a href="#">Next</a>
	</nav>
</main>
```

### 6) Tunas (`/pojok-literasi/tunas`)

- Tujuan: menampilkan konten program literasi anak.
- Section utama: Hero, deskripsi program, dokumentasi, artikel.
- Data tampil: judul item, deskripsi ringkas, gambar, tautan detail, PDF (jika ada).
- Aksi: Detail, PDF, pagination.
- Empty state: "Belum ada dokumentasi/artikel untuk kategori Tunas".

```html
<main>
	<h1>Pojok Literasi Tunas</h1>
	<section>
		<h2>Deskripsi Program</h2>
		<p>Program literasi anak dengan aktivitas membaca dan menulis.</p>
	</section>

	<section>
		<h2>Dokumentasi</h2>
		<article>
			<img src="tunas-dok-1.jpg" alt="dokumentasi tunas" />
			<h3>Kelas Membaca Ceria</h3>
			<p>Kegiatan membaca bersama di balai RW.</p>
			<a href="program_detail.html">Detail</a>
			<a href="#">PDF</a>
		</article>
	</section>
</main>
```

### 7) Karya (`/pojok-literasi/karya`)

- Tujuan: menampilkan karya dan aktivitas remaja.
- Section utama: Hero, deskripsi, karya digital, karya media sosial, carousel.
- Data tampil: judul karya, deskripsi, media, kategori.
- Aksi: Detail, pagination.
- Empty state: "Belum ada karya pada kategori ini".

```html
<main>
	<h1>Pojok Literasi Karya</h1>

	<section>
		<h2>Karya Digital</h2>
		<article>
			<img src="karya-1.jpg" alt="karya digital" />
			<h3>Poster Edukasi Lingkungan</h3>
			<p>Kategori: Desain Digital</p>
			<a href="program_detail.html">Detail</a>
		</article>
	</section>

	<section>
		<h2>Karya Media Sosial</h2>
		<article>
			<h3>Kampanye Baca 15 Menit</h3>
			<p>Konten edukasi singkat untuk remaja.</p>
		</article>
	</section>
</main>
```

### 8) Cakra (`/pojok-literasi/cakra`)

- Tujuan: menampilkan materi dan artikel program edukasi produktif.
- Section utama: Hero, deskripsi, materi program (tabel), artikel terkait.
- Data tampil: materi tabel, artikel list, gambar, deskripsi.
- Aksi: Detail, PDF, pagination.
- Empty state: "Belum ada artikel untuk kategori Cakra".

```html
<main>
	<h1>Pojok Literasi Cakra</h1>

	<section>
		<h2>Materi Program</h2>
		<table>
			<tr><th>No</th><th>Materi</th><th>Target</th></tr>
			<tr><td>1</td><td>Dasar Kewirausahaan</td><td>Remaja</td></tr>
			<tr><td>2</td><td>Perencanaan Usaha</td><td>Warga Umum</td></tr>
		</table>
	</section>

	<section>
		<h2>Artikel</h2>
		<article>
			<h3>Langkah Awal Jualan Online</h3>
			<p>Artikel pengenalan marketplace dan promosi.</p>
			<a href="program_detail.html">Detail</a>
			<a href="#">PDF</a>
		</article>
	</section>
</main>
```

### 9) Kersa (`/pojok-literasi/kersa`)

- Tujuan: menampilkan program lansia dan keterampilan produktif.
- Section utama: Hero, deskripsi, program kesehatan, program keterampilan.
- Data tampil: judul artikel, deskripsi, gambar, kategori.
- Aksi: Detail, PDF, pagination.
- Empty state: "Belum ada artikel kesehatan/keterampilan".

```html
<main>
	<h1>Pojok Literasi Kersa</h1>

	<section>
		<h2>Program Kesehatan Lansia</h2>
		<article>
			<img src="kersa-kesehatan.jpg" alt="kegiatan lansia" />
			<h3>Senam Lansia Mingguan</h3>
			<p>Pendampingan hidup sehat untuk warga lanjut usia.</p>
			<a href="program_detail.html">Detail</a>
		</article>
	</section>

	<section>
		<h2>Program Keterampilan Produktif</h2>
		<article>
			<h3>Pelatihan Kerajinan Rumah Tangga</h3>
			<p>Praktik membuat produk sederhana bernilai jual.</p>
			<a href="#">PDF</a>
		</article>
	</section>
</main>
```

### 10) Admin Login (`/admin/login`)

- Tujuan: autentikasi admin.
- Section utama: Form login.
- Data tampil: field username, password, pesan error.
- Aksi: Masuk.
- Empty state: tidak berlaku.

```html
<main>
	<h1>Login Admin</h1>
	<form method="post" action="#">
		<label>Username</label>
		<input type="text" name="username" required />

		<label>Password</label>
		<input type="password" name="password" required />

		<button type="submit">Masuk</button>
	</form>
	<p class="error" hidden>Username atau password salah.</p>
</main>
```

### 11) Admin Dashboard (`/admin`)

- Tujuan: ringkasan data dan shortcut pengelolaan.
- Section utama: Header admin, kartu statistik, shortcut modul.
- Data tampil: total elibrary, dokumentasi, artikel.
- Aksi: Kelola tiap modul, logout.
- Empty state: statistik 0 tetap tampil.

```html
<main>
	<h1>Dashboard Admin</h1>
	<section>
		<article><h2>Total E-Library</h2><p>12</p></article>
		<article><h2>Total Dokumentasi</h2><p>8</p></article>
		<article><h2>Total Artikel</h2><p>20</p></article>
	</section>

	<section>
		<a href="admin-elibrary.html">Kelola E-Library</a>
		<a href="admin-dokumentasi.html">Kelola Dokumentasi</a>
		<a href="admin-artikel.html">Kelola Artikel</a>
		<a href="admin-settings.html">Settings</a>
	</section>
</main>
```

### 12) Kelola E-Library (`/admin/elibrary`)

- Tujuan: CRUD data e-library.
- Section utama: Form tambah/edit, tabel data.
- Data tampil tabel: no, judul, kategori, tipe link, aksi.
- Aksi: Simpan, Edit, Hapus.
- Aturan: jika item tipe internal (PDF upload), tampilkan badge "PDF terkunci" saat edit.

```html
<main>
	<h1>Kelola E-Library</h1>

	<section>
		<h2>Form Tambah/Edit</h2>
		<form>
			<input type="text" placeholder="Judul" />
			<input type="text" placeholder="Kategori" />
			<select>
				<option>External URL</option>
				<option>Internal PDF</option>
			</select>
			<button type="submit">Simpan</button>
		</form>
	</section>

	<section>
		<table>
			<tr><th>No</th><th>Judul</th><th>Kategori</th><th>Tipe</th><th>Aksi</th></tr>
			<tr>
				<td>1</td>
				<td>Panduan Menulis</td>
				<td>Literasi</td>
				<td>Internal PDF <span>PDF terkunci</span></td>
				<td><button>Edit</button><button>Hapus</button></td>
			</tr>
		</table>
	</section>
</main>
```

### 13) Kelola Dokumentasi (`/admin/dokumentasi`)

- Tujuan: CRUD dokumentasi kegiatan.
- Section utama: Form tambah/edit, tabel data.
- Data tampil tabel: no, judul, kategori, aksi.
- Aksi: Simpan, Edit, Hapus.
- Empty state: "Belum ada data dokumentasi".

```html
<main>
	<h1>Kelola Dokumentasi</h1>

	<form>
		<input type="text" placeholder="Judul dokumentasi" />
		<select>
			<option>Tunas</option>
			<option>Karya</option>
			<option>Cakra</option>
			<option>Kersa</option>
		</select>
		<button type="submit">Simpan</button>
	</form>

	<table>
		<tr><th>No</th><th>Judul</th><th>Kategori</th><th>Aksi</th></tr>
		<tr>
			<td>1</td>
			<td>Kegiatan Membaca</td>
			<td>Tunas</td>
			<td><button>Edit</button><button>Hapus</button></td>
		</tr>
	</table>
</main>
```

### 14) Kelola Artikel (`/admin/artikel`)

- Tujuan: CRUD artikel program.
- Section utama: Form tambah/edit, tabel data.
- Data tampil tabel: no, judul, kategori, aksi.
- Aksi: Simpan, Edit, Hapus.
- Aturan: jika artikel memiliki PDF, beri badge "PDF terkunci" pada mode edit.

```html
<main>
	<h1>Kelola Artikel</h1>

	<form>
		<input type="text" placeholder="Judul artikel" />
		<textarea placeholder="Isi ringkas"></textarea>
		<select>
			<option>Tunas</option>
			<option>Karya</option>
			<option>Cakra</option>
			<option>Kersa</option>
		</select>
		<button type="submit">Simpan</button>
	</form>

	<table>
		<tr><th>No</th><th>Judul</th><th>Kategori</th><th>Aksi</th></tr>
		<tr>
			<td>1</td>
			<td>Tips Belajar Konsisten</td>
			<td>Tunas</td>
			<td><button>Edit</button><button>Hapus</button></td>
		</tr>
	</table>
	<p>Status file: PDF terkunci saat mode edit.</p>
</main>
```

### 15) Settings (`/admin/settings`)

- Tujuan: mengubah konfigurasi situs tanpa ubah kode.
- Section utama: Form setting + preview maps.
- Data tampil: nama situs, tagline, WA, alamat, email, embed maps.
- Aksi: Simpan Pengaturan.
- Empty state: jika kosong, gunakan nilai default.

```html
<main>
	<h1>Settings Website</h1>

	<form>
		<label>Nama Situs</label>
		<input type="text" value="Ngrembaka Aksara" />

		<label>Tagline</label>
		<input type="text" value="Literasi untuk Semua" />

		<label>WhatsApp</label>
		<input type="text" value="08123456789" />

		<label>Alamat</label>
		<textarea>Podorejo, Ngaliyan, Semarang</textarea>

		<label>Email</label>
		<input type="email" value="admin@example.com" />

		<label>Embed Maps</label>
		<textarea><iframe src="..."></iframe></textarea>

		<button type="submit">Simpan Pengaturan</button>
	</form>
</main>
```

## D. Kunci Kerangka HTML Minimal (Semua Halaman)

Semua halaman minimal harus memiliki:

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
	<footer>...</footer>
</body>
</html>
```

Khusus halaman admin login, `nav/footer` boleh tidak ditampilkan.

## E. Kunci Jalankan Praktik

Jalankan dari folder latihan:

```bash
cd latihan-mockup
python -m http.server 5500
```

Buka di browser:

- `http://localhost:5500`

## F. Rubrik Cek Cepat Guru

Skor 1-4 untuk tiap aspek:

1. Kelengkapan halaman: semua file HTML wajib ada.
2. Kesesuaian mockup: tujuan, section, data, aksi tepat.
3. Kerapian struktur HTML: tag utama benar (`nav/main/section/footer`).
4. Navigasi: link antar halaman bekerja.
5. Kesiapan lanjut: siap dipindah ke `backend/app/templates`.

Nilai akhir = rata-rata 5 aspek.
