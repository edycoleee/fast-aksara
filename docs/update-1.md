Prioritas tinggi (isi yang tidak sinkron)

*1. Data dummy masih tampil*
* Nomor WhatsApp `+6281234567890` jelas placeholder. Tombol "Hubungi Kami" di navbar dan footer mengarah ke nomor itu.
* Embed Google Maps tampak belum menunjuk lokasi yang benar (parameter place-nya kosong). Ganti dengan embed dari pencarian "Balai Kelurahan Podorejo".

*2. Navigasi dan label tidak cocok*
* Menu "Visi" mengarah ke `/beranda`, padahal "Beranda" mengarah ke `/`. Tombol "Selengkapnya" di hero juga ke `/beranda`. Kalau itu halaman visi, rapikan URL-nya (`/visi`) dan ubah tombolnya menjadi "Lihat Visi & Program".
* Menu "Profil" dan "Pojok Literasi" memakai `#` sebagai dropdown. Pastikan keduanya bisa dibuka di mobile.

*3. Dua dari empat program masih kosong*
* Karya Ngrembaka dan Cakra Ngrembaka berisi 0 artikel, tapi tampil setara dengan yang berisi. Pengunjung yang klik akan menemukan halaman kosong.
* Beri status "Segera hadir" yang jelas, atau sembunyikan angka "0 artikel" sampai kontennya ada.

*4. Istilah "artikel" untuk semuanya*
* Modul, e-book, dan buku cerita semuanya disebut "artikel". "Buku Cerita: 1 artikel" terasa janggal. Pakai "modul", "buku", atau "bacaan".
* Nama kategori campur: "Life Skills" (Inggris) di samping "Literasi Digital", dengan slug yang beda lagi (`buku-keterampilan`). Samakan bahasa dan slug-nya.

*5. Nama institusi tidak konsisten*
* Hero menulis "SGL PGSD Universitas Negeri Semarang", footer menulis "Sub Gugus Latih PGSD UNNES". Pilih satu format dan jelaskan singkatannya sekali.

## Konten dan copywriting

* **Kalimat berulang.** "Ringan dan mudah dijelajahi" muncul sekitar 4 kali, ditambah "rapi" dan "satu portal". Terasa seperti template. Ganti dengan hal konkret, misalnya "14 modul gratis untuk anak, remaja, dan lansia".
* **Angka yang sama muncul tiga kali:** chip di hero, kotak statistik, dan "Total isi" di bagian E-Library. Cukup satu tempat.
* **Bagian "Katalog unggulan" dan "E-Library" menampilkan kartu yang hampir sama.** Gabungkan, atau jadikan "unggulan" benar-benar berisi 3 buku pilihan dengan cover.
* *FAQ untuk admin, bukan pengunjung.** Pertanyaan "Apakah kontennya bisa diperbarui admin?" tidak relevan bagi pembaca. Ganti dengan: Apakah gratis? Bisa diunduh? Cocok untuk usia berapa? Bagaimana ikut kegiatan Pojok Literasi?
* **Arti "Ngrembaka Aksara" belum dijelaskan.** Satu kalimat tentang maknanya akan memperkuat identitas.
* Kutipan "Tumbuh dan berkembangnya ilmu pengetahuan" tidak ada keterangan sumbernya.** Bisa dijadikan tagline resmi atau dihapus.
* Sebutkan juga dampak program,** misalnya jumlah warga terlibat atau kegiatan yang sudah berjalan.

## Desain (perlu dicek visual)

* **Emoji sebagai ikon** (🌱🎨⚙️🌿) di menu dan kartu bisa tampil beda di tiap perangkat dan terlihat kurang profesional. Ganti dengan ikon SVG satu set, misalnya Lucide atau Phosphor.
* **Beri warna identitas untuk tiap program** (hijau untuk Tunas, dan seterusnya), dipakai konsisten di kartu, badge, dan halaman detailnya.
* **Kartu buku sebaiknya punya cover.** Katalog yang hanya berisi teks dan angka terasa seperti daftar, bukan perpustakaan.
* **Hierarki tombol di hero.** "Selengkapnya" dan "E-Library" tampak sama bobotnya. Jadikan "Mulai Membaca" sebagai tombol utama dan yang lain tombol sekunder.
* **Tipografi.** Struktur heading melompat dari H2 ke H5/H6, dan pertanyaan FAQ memakai H2. Rapikan jadi H1 → H2 → H3, dan buat FAQ berbentuk accordion.
* **Fitur E-Library yang belum ada:** kolom pencarian, filter usia atau kategori, dan keterangan format file serta cara membacanya (online atau unduh).
* **Footer:** tambahkan logo UNNES/PGSD/Kelurahan, tautan Instagram atau YouTube program, dan tanggal pembaruan terakhir.

## Teknis dan SEO

* Yang terbaca dari halaman hanya `title` dan `viewport`. Pastikan ada `meta description`, gambar Open Graph untuk preview saat dibagikan di WhatsApp, dan favicon.
* Judul tab "E-Library PPK ORMAWA Ngrembaka Aksara" cukup panjang. Coba "Ngrembaka Aksara — E-Library Literasi Podorejo".
* Cek alt text gambar, kontras warna, dan tampilan di layar HP kecil. Pengguna utamanya kemungkinan besar membuka lewat HP.

## Urutan pengerjaan yang saya sarankan

1. Ganti nomor WA dan peta, perbaiki tautan "Visi".
2. Tangani halaman program yang kosong dan seragamkan istilah "artikel".
3. Buang bagian yang duplikat dan tulis ulang FAQ.
4. Ganti emoji dengan ikon, tambahkan cover buku, dan rapikan hierarki heading.
5. Tambahkan pencarian, SEO, dan footer yang lengkap.
6. ganti nomor wa menjadi email: ppkosglpgsdunnes@gmail.com 
7. menambahkan link Instagram  ppko_sglpgsdunnes

Kalau Anda mau, kirim screenshot tampilan desktop dan HP supaya saya bisa menilai bagian visualnya. Saya juga bisa membuka halaman E-Library atau halaman profil untuk review lanjutan, atau menulis ulang copy bagian hero dan FAQ-nya.

## Update yang sudah dikerjakan (17 Oktober 2026)

### Prioritas tinggi

1. Data dummy dan kontak
- Tombol kontak di navbar dan footer sudah dialihkan dari WhatsApp ke email `ppkosglpgsdunnes@gmail.com`.
- Link Instagram `ppko_sglpgsdunnes` sudah ditambahkan di footer.
- Default Google Maps sudah diarahkan ke Balai Kelurahan Podorejo.

2. Navigasi dan label
- Menu Visi sudah dirapikan ke URL `/visi`.
- Tombol hero sudah diubah menjadi **Lihat Visi & Program** ke `/visi`.
- Route `/visi` sudah aktif (dengan kompatibilitas route lama `/beranda`).
- Dropdown Profil dan Pojok Literasi sudah diuji di tampilan mobile dan dapat dibuka.

3. Program kosong
- Karya Ngrembaka dan Cakra Ngrembaka yang masih kosong kini menampilkan status **Segera hadir** di landing.
- Pada halaman detail Karya/Cakra juga ditampilkan notifikasi **Segera hadir** saat konten belum tersedia.
- Di kartu agregasi landing, jika jumlah konten = 0 kini ditampilkan badge **Segera hadir** (termasuk kategori E-Library dan semua program Pojok Literasi), serta CTA berubah menjadi **Lihat Rencana Program**.

4. Istilah dan kategori
- Istilah jumlah konten sudah dirapikan: `modul`, `buku`, `koleksi`, dan `konten` (tidak disamaratakan sebagai `artikel`).
- Label kategori `Life Skills` sudah diubah menjadi `Keterampilan Hidup`.
- Slug baru kategori: `/elibrary/keterampilan-hidup`.
- Slug lama `/elibrary/buku-keterampilan` tetap didukung dan otomatis redirect.

5. Nama institusi
- Footer sudah diseragamkan ke format: **SGL PGSD UNNES (Sub Gugus Latih PGSD UNNES)**.

6. Form kirim email
- Halaman publik **/kirim-email** sudah ditambahkan untuk kirim pesan dari pengunjung.
- Form sudah memuat identitas pengirim (nama, email, nomor, instansi) dan isi pesan.
- Setelah kirim, sistem menampilkan konfirmasi sukses jika email terkirim, atau pesan gagal yang informatif jika konfigurasi SMTP belum lengkap.

7. Pengaturan SMTP di CMS
- Pengaturan SMTP sudah tersedia di halaman **/admin/settings** (`smtp_host`, `smtp_port`, `smtp_username`, `smtp_password`, `smtp_use_tls`, `email_to`).
- Pengiriman email memakai prioritas pengaturan dari CMS, dengan fallback ke environment variable bila diperlukan.

### Konten dan copywriting

- Kalimat repetitif pada hero/section landing sudah dirapikan.
- Blok duplikat statistik dan blok “Katalog unggulan” yang tumpang tindih sudah dihapus agar tidak mengulang informasi.
- FAQ sudah ditulis ulang untuk pengunjung:
	- Apakah gratis?
	- Bisa diunduh?
	- Cocok untuk usia berapa?
	- Bagaimana ikut kegiatan?
- Arti “Ngrembaka Aksara” sudah ditambahkan ke narasi hero.
- Kutipan “Tumbuh dan berkembangnya ilmu pengetahuan” sudah diposisikan sebagai tagline resmi.

### Desain

- Emoji pada menu/kartu/hero program sudah diganti dengan ikon Font Awesome agar konsisten lintas perangkat.
- Warna identitas per program sudah diterapkan pada kartu/badge (Tunas, Karya, Cakra, Kersa).
- Hirarki tombol hero sudah diperjelas:
	- Tombol utama: **Mulai Membaca**
	- Tombol sekunder: **Lihat Visi & Program**
- FAQ sudah berbentuk accordion.
- Fitur E-Library yang diminta sudah ditambahkan:
	- kolom pencarian,
	- filter usia,
	- keterangan format dan mode akses (online/unduh).
- Footer sudah dilengkapi:
	- logo UNNES/PGSD/Kelurahan,
	- Instagram,
	- YouTube (opsional via settings),
	- tanggal pembaruan terakhir.
- Ukuran logo mitra di footer saat ini sudah diseragamkan (tanpa class khusus per logo).

### Teknis dan SEO

- Meta description sudah ada.
- Open Graph image sudah ditambahkan.
- Favicon sudah ditambahkan.
- Judul tab landing sudah diperbarui menjadi **Ngrembaka Aksara — E-Library Literasi Podorejo**.
- Audit alt text gambar utama sudah dilakukan dan aman.
- Pengecekan tampilan mobile sudah dilakukan pada titik-titik kritis (navbar dropdown, footer, landing, E-Library).

### Catatan

- Logo institusi saat ini menggunakan placeholder SVG yang rapi dan sudah bisa langsung diganti ke logo resmi melalui settings (`logo_unnes_url`, `logo_pgsd_url`, `logo_kelurahan_url`).
- Selain URL, logo institusi sekarang juga bisa diupload langsung dari halaman settings. File upload akan otomatis di-resize ke **96x96 px** saat disimpan agar konsisten.