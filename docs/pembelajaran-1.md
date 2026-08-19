# Tahapan Pembelajaran Web FastAPI untuk Siswa SMA

Dokumen ini berisi alur belajar bertahap untuk siswa yang sudah memahami dasar HTML, FastAPI, dan SQLite. Fokusnya adalah proses yang visual, mudah diikuti, dan menghasilkan produk nyata.

## Tujuan Umum

Siswa mampu membangun web sederhana dari mockup sampai CRUD terhubung ke halaman HTML, lalu memahami hubungan antara:

- struktur halaman (HTML),
- tampilan (CSS),
- logika backend (FastAPI),
- data (SQLite).

## Alur Tahapan + Perkiraan Waktu

Estimasi dibuat untuk 1 pertemuan = 90 menit.

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

### 2. HTML Tanpa CSS (Kerangka/Layout)

Tujuan:
- Siswa membangun struktur halaman dengan benar.
- Siswa memahami section, form, table, dan navigasi.

Aktivitas:
- Membuat halaman HTML dasar.
- Menyusun layout konten sesuai mockup.

Output:
- Semua halaman bisa dibuka dengan struktur lengkap, walau belum menarik.

Waktu:
- 1 sampai 2 pertemuan (90–180 menit).

### 3. HTML + CSS (Visual dan Responsif)

Tujuan:
- Siswa memahami pemisahan fungsi HTML dan CSS.
- Siswa bisa membuat tampilan desktop + mobile yang rapi.

Aktivitas:
- Menambahkan style kartu, grid, tombol, jarak, warna, tipografi.
- Uji responsive di viewport mobile.

Output:
- Halaman tampak rapi dan nyaman dibaca.

Waktu:
- 1 sampai 2 pertemuan (90–180 menit).

### 4. Mockup -> Object -> Page HTML

Tujuan:
- Siswa mengubah data dummy menjadi model objek aplikasi.
- Siswa paham pemetaan objek ke komponen halaman.

Aktivitas:
- Definisikan objek inti: `ELibrary`, `Dokumentasi`, `Artikel`.
- Petakan atribut objek ke elemen HTML (judul, deskripsi, gambar, link).

Output:
- Dokumen mapping object-field ke komponen halaman.

Waktu:
- 1 pertemuan (90 menit).

### 5. Database SQLite (Skema dan Tabel)

Tujuan:
- Siswa memahami penyimpanan data permanen.
- Siswa mengenal konsep tabel, kolom, id, tipe data.

Aktivitas:
- Buat skema model di SQLAlchemy.
- Generate dan isi data awal (seed).

Output:
- Database SQLite aktif dengan tabel inti.

Waktu:
- 1 pertemuan (90 menit).

### 6. CRUD SQLite (Backend)

Tujuan:
- Siswa bisa membuat alur tambah, baca, ubah, hapus data.
- Siswa memahami route FastAPI untuk operasi data.

Aktivitas:
- Buat endpoint CRUD untuk objek utama.
- Uji fungsi create/read/update/delete dari admin.

Output:
- CRUD berjalan dan data berubah di database.

Waktu:
- 2 pertemuan (180 menit).

### 7. Menghubungkan HTML dengan CRUD

Tujuan:
- Siswa melihat alur penuh: input admin -> simpan DB -> tampil di halaman publik.

Aktivitas:
- Hubungkan form admin ke endpoint CRUD.
- Render data DB ke template Jinja2.
- Uji skenario nyata (tambah artikel, edit, hapus, cek halaman publik).

Output:
- Website dinamis end-to-end.

Waktu:
- 2 pertemuan (180 menit).

## Total Estimasi

- Minimal: 9 pertemuan x 90 menit.
- Aman/ideal: 10 sampai 11 pertemuan x 90 menit (termasuk review dan perbaikan).

## Contoh Jadwal Ringkas Kelas

1. Pertemuan 1: Mockup data semua halaman.
2. Pertemuan 2-3: HTML layout tanpa CSS.
3. Pertemuan 4-5: Styling CSS + responsive.
4. Pertemuan 6: Object mapping dari mockup.
5. Pertemuan 7: SQLite dan model data.
6. Pertemuan 8-9: CRUD backend.
7. Pertemuan 10-11: Integrasi HTML + CRUD + pengujian.

## Kenapa Alur Ini Cocok untuk SMA?

- Dimulai dari yang terlihat dulu (mockup dan halaman) sehingga tidak menakutkan.
- Konsep abstrak (database dan CRUD) masuk setelah siswa punya gambaran visual.
- Setiap tahap punya output nyata, jadi siswa merasa progresnya jelas.
- Mudah dibuat kerja kelompok: satu tim publik page, satu tim admin, lalu digabung.

## Tambahan Agar Menjadi Web Seperti Sekarang

Setelah 7 tahap dasar selesai, ada beberapa lapisan lanjutan agar hasilnya setara dengan web yang sudah berjalan saat ini.

### 8. Arsitektur Route dan Template yang Rapi

Tujuan:
- Kode mudah dirawat saat halaman bertambah.

Aktivitas:
- Pisah route per modul (landing, tunas, karya, cakra, kersa, admin).
- Gunakan template dasar bersama (navbar, footer, layout section).

Output:
- Struktur backend dan template lebih terorganisir.

Waktu:
- 1 pertemuan (90 menit).

### 9. Login Admin dan Proteksi Halaman

Tujuan:
- Halaman kelola tidak bisa diakses pengguna umum.

Aktivitas:
- Implementasi login/logout admin.
- Proteksi route admin dengan token/cookie.

Output:
- CMS admin aman secara dasar.

Waktu:
- 1 pertemuan (90 menit).

### 10. Upload File yang Aman (Gambar/PDF)

Tujuan:
- Siswa paham alur file upload dan kebersihan file server.

Aktivitas:
- Validasi ukuran/format file.
- Simpan path file ke database.
- Hapus file lama saat record dihapus atau saat gambar diganti.
- Terapkan aturan: PDF yang sudah di-upload tidak diedit langsung agar tidak jadi file sampah.

Output:
- Sistem upload stabil dan tidak menghasilkan banyak file sisa.

Waktu:
- 1 sampai 2 pertemuan (90-180 menit).

### 11. Fitur Konten Lanjutan (Edit, Detail, Filter, Pagination)

Tujuan:
- Website nyaman dipakai pengguna dan admin.

Aktivitas:
- Tambah fitur edit data admin.
- Tambah halaman detail konten.
- Tambah filter kategori dan pagination.

Output:
- Data lebih mudah dikelola dan dibaca.

Waktu:
- 2 pertemuan (180 menit).

### 12. Konsistensi UI/UX dan Responsif Mobile

Tujuan:
- Tampilan konsisten antar halaman di desktop dan mobile.

Aktivitas:
- Samakan komponen card, section, tombol, spacing.
- Perbaiki rasio gambar, ringkasan teks, dan area aksi di mobile.

Output:
- Pengalaman pengguna lebih rapi, visual, dan mudah dipahami.

Waktu:
- 1 sampai 2 pertemuan (90-180 menit).

### 13. Settings Dinamis + Dokumentasi + Deployment Dasar

Tujuan:
- Website siap dipelihara dan dipresentasikan.

Aktivitas:
- Buat halaman pengaturan situs (nama, kontak, maps).
- Lengkapi dokumentasi + capture tampilan.
- Siapkan docker/deployment dasar.

Output:
- Aplikasi lebih siap pakai di lingkungan nyata.

Waktu:
- 2 pertemuan (180 menit).

## Estimasi Tambahan Waktu (Lanjutan)

- Minimal tambahan: 8 pertemuan x 90 menit.
- Ideal tambahan: 9 sampai 10 pertemuan x 90 menit.

## Total Keseluruhan Program

- Tahap dasar (1-7): 9 sampai 11 pertemuan.
- Tahap lanjutan (8-13): 8 sampai 10 pertemuan.
- Total realistis: 17 sampai 21 pertemuan (masing-masing 90 menit).

## Catatan Implementasi untuk Kelas SMA

- Gunakan pola "lihat hasil dulu -> pahami kode -> praktik kecil -> evaluasi".
- Setiap pertemuan wajib ada output visual (halaman, tabel, form, atau fitur berjalan).
- Bagi peran kelompok: tim frontend, tim backend, tim data, lalu integrasi bersama.





Landing/Beranda
- Navbar
logo| beranda | visi | profil aksara | profil kelurahan | e-library | tunas | karya | cakra | kersa | hubungi kami 

- Hero 

BUKU UNTUK SEMUA GENERASI
PPK ORMAWA 2026
E-LIBRARY PPK ORMAWA
NGREMBAKA AKSARA
Ngrembaka Aksara adalah program penguatan literasi dan edupreneur skill lintas generasi yang hadir di Kelurahan Podorejo, Kecamatan Ngaliyan, Kota Semarang. Digagas oleh mahasiswa SGL PGSD Universitas Negeri Semarang melalui PPK ORMAWA tahun 2026.
(Selengkapnya)
(E-Library)

--------------------

AKSES CEPAT
Baca, jelajahi, dan temukan program
Portal Literasi
Baca lebih mudah
Koleksi belajar, program, dan pojok literasi dalam satu ruang yang rapi, ringan, dan mudah dijelajahi.

E-Library
Pojok Literasi
Artikel
E-LIBRARY
5 artikel
POJOK LITERASI
3 artikel
Literasi Lintas Generasi
Tumbuh cerdas, mandiri, dan berdaya lewat bacaan yang berkelanjutan.
Modul Pembelajaran
Materi belajar utama dan panduan pembaca
Buku Cerita
Cerita lokal, karakter, dan imajinasi
Tunas Ngrembaka
Literasi anak, numerasi, dan budaya
"Tumbuh dan berkembangnya ilmu pengetahuan"



- Buku untuk semua : 
- Kenapa Terasa mudah:
- Ringkasan Program
- PERTANYAAN YANG SERING DITANYAKAN
- KATALOG UNGGULAN
- KOLEKSI DIGITAL
- PROGRAM LINTAS GENERASI
- Footer
