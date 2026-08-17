# Panduan Admin Ngrembaka Aksara

Dokumen ini menjelaskan cara memakai seluruh fitur admin dari awal sampai mahir.
Fokusnya adalah alur kerja harian, struktur menu, aturan upload, dan cara menjaga data tetap rapi.

## 1. Tujuan Admin CMS

Admin CMS dipakai untuk mengelola isi website tanpa mengubah kode aplikasi.

Fungsi utamanya:

1. Mengelola E-Library.
2. Mengelola Dokumentasi.
3. Mengelola Artikel.
4. Mengubah pengaturan situs seperti nama, kontak, dan peta.
5. Memastikan konten publik selalu terbarui.

## 2. Alur Kerja Awal

Saat pertama kali membuka admin, urutannya seperti ini:

1. Buka halaman login admin.
2. Masukkan username dan password admin.
3. Setelah berhasil login, masuk ke dashboard.
4. Dari dashboard, pilih menu yang ingin dikelola.
5. Tambah, edit, atau hapus data sesuai kebutuhan.
6. Cek hasilnya di halaman publik.

## 3. Login Admin

Halaman login ada di:

```text
https://aksara.fun/admin/login
```

### Langkah login

1. Buka `https://aksara.fun/admin/login`.
2. Masukkan `username` admin. >> admin
3. Masukkan `password` admin. >> Admin123!
4. Klik tombol login.

Jika login benar, Anda akan diarahkan ke dashboard admin.

### Jika login gagal

Periksa hal berikut:

- Username benar.
- Password benar.
- Akun admin sudah di-seed atau sudah dibuat di database.
- Browser tidak memblokir cookie.

## 4. Dashboard Admin

Halaman dashboard ada di:

```text
https://aksara.fun/admin
```

Dashboard dipakai sebagai pusat kontrol admin. Biasanya berisi:

- Ringkasan jumlah data.
- Menu ke E-Library.
- Menu ke Dokumentasi.
- Menu ke Artikel.
- Menu ke Settings.
- Menu dokumentasi admin.

### Kebiasaan yang baik di dashboard

1. Cek ringkasan data sebelum edit.
2. Buka menu yang sesuai, jangan masuk lewat halaman publik.
3. Setelah mengubah data, refresh halaman publik untuk verifikasi.

## 5. Mengelola E-Library

Menu E-Library digunakan untuk menyimpan materi bacaan, PDF, modul, ebook, atau resource digital lain.

Halaman admin E-Library biasanya di:

```text
https://aksara.fun/admin/elibrary
```

### Data yang diisi

Umumnya form E-Library berisi:

- Kategori.
- Judul.
- Deskripsi.
- Link file atau URL.
- Gambar thumbnail.

### Kategori yang umum dipakai

Contoh kategori:

- modul-pembelajaran
- ebook
- buku-cerita
- buku-literasi-digital
- buku-keterampilan

### Langkah menambah item E-Library

1. Buka menu E-Library.
2. Klik tambah data.
3. Isi kategori yang sesuai.
4. Isi judul yang jelas.
5. Tulis deskripsi singkat dan informatif.
6. Upload gambar jika tersedia.
7. Upload file PDF atau masukkan link jika dibutuhkan.
8. Simpan data.
9. Cek hasilnya di halaman publik `https://aksara.fun/elibrary`.

### Tips untuk E-Library

- Gunakan judul yang singkat dan mudah dicari.
- Deskripsi jangan terlalu panjang.
- Gambar thumbnail sebaiknya ringan agar halaman cepat dibuka.
- Jika file berupa PDF, pastikan nama file tidak membingungkan.

### Saat mengedit E-Library

1. Buka item yang ingin diubah.
2. Periksa apakah kategori masih tepat.
3. Perbaiki judul atau deskripsi bila perlu.
4. Ganti file atau gambar hanya jika memang perlu.
5. Simpan perubahan.

### Saat menghapus E-Library

1. Pastikan item benar-benar tidak dipakai lagi.
2. Cek apakah ada link publik yang masih mengarah ke item tersebut.
3. Hapus data jika sudah yakin.

## 6. Mengelola Dokumentasi

Menu Dokumentasi dipakai untuk mengelola dokumentasi kegiatan, foto acara, dan konten visual lain.

Halaman admin Dokumentasi biasanya di:

```text
https://aksara.fun/admin/dokumentasi
```

### Data yang diisi

Biasanya form dokumentasi berisi:

- Kategori.
- Judul kegiatan.
- Deskripsi singkat.
- Gambar dokumentasi.
- Link video opsional.

### Kategori dokumentasi yang umum

Contoh kategori:

- dokumentasi-tunas
- karya-digital
- karya-media-sosial
- gambar-carosel

### Langkah menambah dokumentasi

1. Buka menu Dokumentasi.
2. Klik tambah data.
3. Pilih kategori yang sesuai.
4. Isi judul kegiatan.
5. Tulis deskripsi ringkas.
6. Upload foto dokumentasi.
7. Tambahkan link video jika ada.
8. Simpan data.
9. Cek tampilannya di halaman publik.

### Tips untuk dokumentasi

- Gunakan foto yang jelas dan tidak terlalu berat.
- Pilih satu foto utama yang paling representatif.
- Jika ada video YouTube, pastikan link aktif.
- Judul sebaiknya menunjukkan kegiatan yang sebenarnya.

### Saat mengedit dokumentasi

1. Buka item yang akan diperbaiki.
2. Ganti deskripsi jika ada informasi yang salah.
3. Ganti gambar jika kualitasnya kurang baik.
4. Simpan dan cek hasilnya.

## 7. Mengelola Artikel

Menu Artikel dipakai untuk konten berbentuk artikel, berita, atau tulisan informatif.

Halaman admin Artikel biasanya di:

```text
https://aksara.fun/admin/artikel
```

### Data yang diisi

Biasanya form artikel berisi:

- Kategori artikel.
- Judul.
- Deskripsi.
- Gambar cover.
- PDF artikel jika ada.

### Kategori artikel yang umum

Contoh kategori:

- artikel-tunas
- artikel-cakra
- artikel-kersa-kesehatan
- artikel-kersa-keterampilan

### Langkah menambah artikel

1. Buka menu Artikel.
2. Klik tambah data.
3. Pilih kategori artikel.
4. Isi judul yang menarik dan jelas.
5. Tulis deskripsi singkat.
6. Upload gambar cover.
7. Upload PDF jika artikel memang tersedia dalam file.
8. Simpan data.
9. Cek hasilnya di halaman publik.

### Tips untuk artikel

- Gunakan judul yang informatif.
- Jangan duplikasi artikel yang sama di kategori berbeda tanpa alasan.
- Gambar cover harus relevan dengan isi artikel.
- PDF harus mudah dibaca dan ukurannya wajar.

## 8. Pengaturan Situs

Menu Settings dipakai untuk mengubah identitas website.

Halaman settings biasanya di:

```text
https://aksara.fun/admin/settings
```

### Data yang biasanya diatur

- Nama situs.
- Tagline.
- Nomor WhatsApp.
- Label WhatsApp.
- Alamat.
- Email.
- Embed Google Maps.

### Langkah mengubah settings

1. Buka menu Settings.
2. Ubah data sesuai kebutuhan.
3. Pastikan nama situs sesuai branding.
4. Pastikan nomor WhatsApp benar.
5. Pastikan embed maps valid.
6. Simpan perubahan.
7. Refresh halaman publik untuk mengecek hasilnya.

### Tips untuk settings

- Jangan sering mengubah identitas utama jika tidak perlu.
- Pastikan tautan peta masih aktif.
- Gunakan nomor WhatsApp yang benar-benar dipantau.

## 9. Dokumentasi Admin

Menu dokumentasi admin dipakai sebagai panduan singkat untuk operator situs.

Biasanya berisi:

- Cara memakai E-Library.
- Cara memakai Dokumentasi.
- Cara memakai Artikel.
- Cara mengubah settings.
- Catatan penting bagi admin.

Gunakan halaman ini sebagai pengingat bila admin baru bergabung.

## 10. Aturan Upload File

Jika sistem sudah mendukung upload file lokal, ikuti aturan ini:

### File gambar

- Format aman: `jpg`, `jpeg`, `png`, `webp`.
- Ukuran sebaiknya kecil agar cepat dimuat.
- Nama file sebaiknya otomatis atau unik.

### File PDF

- Pastikan file benar-benar PDF.
- Gunakan ukuran file yang wajar.
- Jangan upload file yang rusak atau terlalu besar.

### Aturan umum upload

1. Upload hanya file yang relevan.
2. Jangan upload file duplikat tanpa alasan.
3. Periksa hasil upload setelah simpan.
4. Hapus file lama jika sudah diganti.

## 11. Alur Kerja Harian Admin

Alur kerja yang paling aman untuk admin adalah:

1. Login.
2. Cek dashboard.
3. Tambah atau edit data yang perlu diperbarui.
4. Simpan perubahan.
5. Buka halaman publik untuk cek hasil.
6. Jika ada kesalahan, kembali ke admin dan perbaiki.

## 12. Alur Kerja Mingguan

Disarankan admin melakukan pengecekan rutin:

1. Cek apakah ada link mati.
2. Cek gambar yang rusak atau terlalu berat.
3. Cek apakah artikel masih relevan.
4. Cek apakah kontak dan peta masih valid.
5. Cek apakah halaman publik masih tampil benar di mobile.

## 13. Praktik Baik Saat Mengisi Konten

### Untuk judul

- Buat singkat.
- Langsung menjelaskan isi.
- Hindari judul yang terlalu panjang.

### Untuk deskripsi

- Tulis ringkas tapi cukup jelas.
- Jangan menyalin teks yang tidak diperlukan.
- Gunakan bahasa yang mudah dibaca publik.

### Untuk gambar

- Gunakan gambar yang fokus.
- Hindari gambar pecah.
- Jangan upload gambar terlalu besar.

### Untuk link eksternal

- Pastikan link masih aktif.
- Uji sebelum dipublikasikan.

## 14. Troubleshooting Singkat

### Tidak bisa login

- Cek username/password.
- Pastikan cookie browser aktif.
- Pastikan akun admin memang ada di database.

### Data tidak muncul di halaman publik

- Cek apakah data sudah disimpan.
- Cek apakah kategori sudah benar.
- Refresh browser.

### Gambar tidak tampil

- Cek path file.
- Cek apakah file benar-benar terunggah.
- Cek apakah file masih ada di folder upload.

### PDF tidak bisa dibuka

- Cek format file.
- Cek ukuran file.
- Cek apakah link/path PDF benar.

### Halaman admin tampil tapi perubahan tidak terlihat

- Pastikan data sudah disimpan.
- Pastikan browser tidak menampilkan cache lama.
- Cek halaman publik yang benar, bukan URL lama.

## 15. Urutan Belajar untuk Admin Baru

Kalau admin baru mau cepat paham, belajar dengan urutan ini:

1. Login admin.
2. Coba baca dashboard.
3. Tambah satu data E-Library.
4. Tambah satu dokumentasi.
5. Tambah satu artikel.
6. Ubah settings situs.
7. Hapus data percobaan jika tidak dipakai.
8. Cek semua hasil di halaman publik.

## 16. Ringkasan Cepat

- Login di `/admin/login`.
- Masuk dashboard di `/admin`.
- Kelola E-Library di `/admin/elibrary`.
- Kelola Dokumentasi di `/admin/dokumentasi`.
- Kelola Artikel di `/admin/artikel`.
- Kelola identitas situs di `/admin/settings`.
- Selalu cek hasil di halaman publik setelah update.

## 17. Tujuan Akhir Admin

Tujuan utama admin bukan hanya mengisi data, tetapi memastikan website:

- selalu rapi,
- selalu update,
- mudah dibaca,
- konsisten secara tampilan,
- dan mudah dipelihara.

Dengan alur di atas, admin baru bisa mulai dari nol lalu pelan-pelan menguasai semua fitur.
