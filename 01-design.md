DESAIN PAGE NGREMBAKA AKSARA

Tahap saat ini: melengkapi data konten terlebih dahulu sebelum masuk detail CSS.

## 1. Struktur Halaman (Tree Diagram)

```text
Landing/Beranda
|- Visi
|- Profil Aksara
|- Profil Kelurahan
|- E-Library
|- Pojok Literasi
	|- Tunas
	|- Karya
	|- Cakra
	|- Kersa
```

## 2. Tujuan Halaman Utama

- Menjelaskan singkat apa itu Ngrembaka Aksara.
- Mengarahkan pengunjung ke konten inti: E-Library, profil, dan pojok literasi.
- Menampilkan ringkasan data agar pengunjung percaya dan paham skala program.
- Menjadi pintu masuk untuk lintas generasi: anak, remaja, orang tua, guru, pendamping.

## 3. Konten Wajib Landing/Beranda

### A. Hero Section
- Kicker: Buku untuk semua generasi.
- Headline utama: E-Library PPK ORMAWA Ngrembaka Aksara.
- Subheadline: deskripsi program, lokasi, dan penyelenggara.
- CTA 1: Selengkapnya (ke halaman Visi/Beranda).
- CTA 2: E-Library (ke halaman koleksi).

### B. Ringkasan Statistik
- Total koleksi E-Library.
- Total artikel Pojok Literasi.
- Jumlah program inti (4).
- Jumlah kategori buku (misal 5, sesuai data final).

### C. Nilai Utama (Why This Portal)
- Akses cepat.
- Koleksi tertata.
- Lintas generasi.

### D. Ringkasan Profil
- Card Profil Ngrembaka Aksara + tombol baca selengkapnya.
- Card Profil Kelurahan Podorejo + tombol baca selengkapnya.

### E. FAQ Singkat
- Apa isi utama website ini?
- Bagaimana cara membuka koleksi buku?
- Apakah konten bisa diperbarui admin?

## 4. Data Konten per Halaman

### 4.1 Visi
- Visi program.
- Misi (3-5 poin).
- Dampak yang diharapkan.
- Sasaran penerima manfaat.

### 4.2 Profil Aksara
- Latar belakang program.
- Permasalahan awal yang ditemukan.
- Metode pelaksanaan (survei, observasi, wawancara, FGD).
- Tujuan jangka pendek dan jangka panjang.

### 4.3 Profil Kelurahan
- Gambaran umum wilayah.
- Data kependudukan.
- Potensi lokal.
- Tantangan literasi setempat.

### 4.4 E-Library
- Daftar kategori.
- Kartu koleksi (judul, ringkasan, gambar, metadata).
- Aksi baca/unduh.
- Fitur pencarian atau filter (jika tersedia).

### 4.5 Tunas
- Konten literasi anak.
- Konten numerasi dasar.
- Aktivitas belajar menyenangkan.

### 4.6 Karya
- Konten kreativitas, seni, dan produk belajar.
- Dokumentasi hasil karya warga/siswa.

### 4.7 Cakra
- Konten teknologi terapan dan keterampilan.
- Materi alat, proses, atau praktik edukatif.

### 4.8 Kersa
- Konten karakter, budaya, dan pemberdayaan.
- Materi penguatan kebiasaan positif.

## 5. Checklist Data Sebelum Styling CSS

- Semua judul section sudah final.
- Copywriting headline dan deskripsi sudah disetujui.
- Data angka statistik sudah valid dan sinkron ke backend.
- Link tombol CTA sudah benar.
- FAQ sudah final minimal 3 pertanyaan.
- Placeholder gambar yang belum ada sudah ditandai.

## 6. Prioritas Eksekusi Konten

1. Finalisasi Hero + CTA + statistik.
2. Finalisasi ringkasan Profil Aksara dan Profil Kelurahan.
3. Finalisasi FAQ.
4. Review konsistensi istilah antar halaman (E-Library, Pojok Literasi, nama program).
5. Setelah konten final, lanjut tahap detail CSS.



## 7. Konten Detail Landing/Beranda
### 7.1 Navbar

### 7.2 Hero Kiri (Pesan Utama)

- Kicker: Buku untuk semua generasi.
- Badge: PPK ORMAWA 2026.
- Judul utama:
	E-LIBRARY PPK ORMAWA
	NGREMBAKA AKSARA
- Deskripsi:
	Ngrembaka Aksara adalah program penguatan literasi dan edupreneur skill lintas generasi
	yang hadir di Kelurahan Podorejo, Kecamatan Ngaliyan, Kota Semarang.
	Digagas oleh mahasiswa SGL PGSD Universitas Negeri Semarang melalui PPK ORMAWA tahun 2026.
- CTA utama: Selengkapnya (tujuan: /beranda).
- CTA sekunder: E-Library (tujuan: /elibrary).

### 7.3 Hero Kanan (Kartu Akses Cepat)

- Header kartu:
	Akses Cepat
	Baca, jelajahi, dan temukan program
- Blok visual:
	- Badge: Portal Literasi
	- Judul: Baca lebih mudah
	- Deskripsi: Koleksi belajar, program, dan pojok literasi dalam satu ruang yang rapi, ringan, dan mudah dijelajahi.
	- Chip: E-Library | Pojok Literasi | Artikel
- Metrik:
	- E-Library: {{ elibrary_total }} artikel
	- Pojok Literasi: {{ pojok_total }} artikel
- Highlight:
	- Judul: Literasi Lintas Generasi
	- Deskripsi: Tumbuh cerdas, mandiri, dan berdaya lewat bacaan yang berkelanjutan.
- Tile konten:
	- Modul Pembelajaran: Materi belajar utama dan panduan pembaca
	- Buku Cerita: Cerita lokal, karakter, dan imajinasi
	- Tunas Ngrembaka: Literasi anak, numerasi, dan budaya
- Quote:
	"Tumbuh dan berkembangnya ilmu pengetahuan"

### 7.4 Section Buku untuk Semua

- Kicker: Buku untuk semua.
- Judul: Akses di mana pun, kapan pun.
- Deskripsi:
	Ngrembaka Aksara merangkum koleksi belajar, pojok literasi lintas usia,
	dan konten program dalam satu portal yang ringan dan mudah dijelajahi.
- Statistik ringkas:
	- Koleksi E-Library: {{ elibrary_total }}
	- Pojok Literasi: {{ pojok_total }}
	- Program Inti: 4
	- Kategori Buku: 5

### 7.5 Section Kenapa Terasa Mudah

- Kicker: Kenapa terasa mudah.
- Judul: Portal yang fokus pada akses belajar.
- 3 nilai utama:
	- Akses cepat: Semua katalog, program, dan materi belajar ada dalam satu alur.
	- Koleksi tertata: Kategori jelas memudahkan pengunjung baru.
	- Lintas generasi: Cocok untuk anak, remaja, orang tua, dan pendamping belajar.

### 7.6 Section Ringkasan Program

- Kicker: Ringkasan program.
- Judul: Profil Program.
- Deskripsi section:
	Program ini dirancang sebagai ekosistem literasi yang menumbuhkan kebiasaan baca,
	kreativitas, dan daya saing melalui konten yang terkurasi.
- Card 1:
	- Label: Profil Program
	- Judul: Profil Ngrembaka Aksara
	- Ringkasan:
		Program Ngrembaka Aksara lahir dari hasil survei lapangan, observasi,
		wawancara mendalam, dan FGD bersama masyarakat Kelurahan Podorejo.
	- Tombol: Baca Selengkapnya (tujuan: /profil/ngrembaka-aksara)
- Card 2:
	- Label: Profil Wilayah
	- Judul: Profil Kelurahan Podorejo
	- Ringkasan:
		Kelurahan Podorejo merupakan salah satu kelurahan di Kecamatan Ngaliyan, Kota Semarang,
		dengan potensi wilayah dan masyarakat yang mendukung penguatan literasi.
	- Tombol: Baca Selengkapnya (tujuan: /profil/kelurahan-podorejo)

### 7.7 Section FAQ (Pertanyaan yang Sering Ditanyakan)

- Kicker: Pertanyaan yang sering ditanyakan.
- Judul: FAQ singkat.
- Intro:
	Bagian ini membantu pengunjung baru memahami cara memakai portal dengan cepat.
- Daftar FAQ:
	- Q: Apa isi utama website ini?
		A: Website memuat E-Library, profil program, profil wilayah, dan empat Pojok Literasi untuk lintas generasi.
	- Q: Bagaimana cara membuka koleksi buku?
		A: Klik menu E-Library atau masuk ke kategori yang diinginkan dari halaman utama.
	- Q: Apakah konten bisa diperbarui admin?
		A: Bisa. Admin dapat menambah artikel, dokumentasi, dan koleksi E-Library melalui panel CMS.

### 7.8 Section Katalog Unggulan

- Tujuan: menampilkan konten pilihan agar pengunjung langsung melihat kualitas koleksi.
- Jumlah awal: 3-6 kartu unggulan.
- Format kartu:
	- Judul buku/artikel
	- Ringkasan 1-2 kalimat
	- Kategori
	- Tombol baca detail
- Sumber data: E-Library (prioritas konten terbaru atau paling relevan).

### 7.9 Section Koleksi Digital

- Tujuan: menonjolkan bahwa materi dapat diakses digital.
- Isi:
	- Jenis file yang tersedia (PDF/gambar/teks).
	- Cara akses (baca online/unduh sesuai izin).
	- Catatan manfaat: hemat waktu dan mudah diakses dari perangkat apa pun.

### 7.10 Section Program Lintas Generasi

- Tujuan: mengikat semua pojok literasi dalam satu narasi program.
- Daftar program:
	- Tunas Ngrembaka: literasi anak dan numerasi dasar.
	- Karya Ngrembaka: kreativitas, seni, dan ekspresi karya.
	- Cakra Ngrembaka: teknologi terapan dan keterampilan.
	- Kersa Ngrembaka: karakter, budaya, dan pemberdayaan.
- CTA section:
	Jelajahi Program (menuju halaman daftar pojok literasi atau section program terkait).

### 7.11 Footer

- Kolom 1: Lokasi (embed peta).
- Kolom 2: Kontak (alamat, email, WhatsApp).
- Kolom 3: Tautan cepat (E-Library, Tunas, Karya, Cakra, Kersa).
- Copyright:
	2026 PPK ORMAWA Ngrembaka Aksara - Sub Gugus Latih PGSD UNNES.

### 7.12 Catatan Sinkronisasi Konten dengan Template

- Gunakan variabel dinamis untuk angka:
	{{ elibrary_total }} dan {{ pojok_total }}.
- Samakan penulisan nama menu dengan navbar aktual.
- Pastikan semua CTA memiliki tujuan URL final dan tidak ada tombol kosong.
- Jika section Katalog Unggulan, Koleksi Digital, dan Program Lintas Generasi belum tampil di template,
	pertahankan dulu sebagai backlog konten tahap berikutnya.
