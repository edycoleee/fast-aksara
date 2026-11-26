# Fitur Private Chat

## Tujuan

Menambahkan layanan chat privat di:

- Halaman login: `https://aksara.fun/chat/login`
- Halaman chat: `https://aksara.fun/chat`

Halaman login menyediakan tombol **Call** yang membuka layanan:

```text
https://kos.sulfat.site/api/v1/messages/send?t=6285122769501&m=Halo&s=lumbungsari1
```

Tampilan mengikuti konsep sederhana:

```text
+--------------------------------------------------+
| Budi                                  Online     |
+--------------------------------------------------+
| Halo                                             |
|                                      Hai         |
| Bisa kirim file?                                 |
|                                      Ya, sebentar|
| [gambar.jpg]                                     |
|                                      [laporan.pdf]|
+--------------------------------------------------+
| Lampiran | Ketik pesan...               Kirim    |
+--------------------------------------------------+
```

## Batasan Versi Pertama

- Dua atau lebih pengguna dapat melakukan percakapan privat.
- Riwayat pesan tersimpan di SQLite.
- Pengguna hanya dapat melihat percakapan yang melibatkannya.
- Mendukung pesan teks, gambar, dan PDF.
- Pembaruan menggunakan HTTP polling setiap 4 detik.
- WebSocket tidak digunakan pada versi pertama.
- Status online ditentukan dari waktu aktivitas terakhir pengguna.
- Pengguna dianggap online jika aktif dalam 30 detik terakhir.
- Akun chat terpisah dari akun admin CMS.

## Struktur Implementasi

```text
backend/app/
├── chat.py                    # helper autentikasi dan session chat
├── models.py                  # model ChatUser, Conversation, Message
├── upload.py                  # validasi dan penyimpanan lampiran chat
├── routers/
│   └── chat.py                # halaman dan endpoint chat
├── static/
│   ├── css/chat.css
│   └── js/chat.js
└── templates/
    ├── chat_login.html
    └── chat.html
```

## Skema Database

### `chat_user`

| Kolom | Tipe | Keterangan |
|---|---|---|
| `id` | integer | Primary key |
| `username` | string(50) | Unik, digunakan untuk login |
| `display_name` | string(100) | Nama yang tampil |
| `hashed_password` | string(255) | Hash bcrypt |
| `is_active` | boolean | Akun dapat login |
| `last_seen_at` | datetime | Aktivitas terakhir |
| `created_at` | datetime | Waktu dibuat |

### `chat_conversation`

| Kolom | Tipe | Keterangan |
|---|---|---|
| `id` | integer | Primary key |
| `participant_one_id` | integer | Foreign key ke `chat_user.id` |
| `participant_two_id` | integer | Foreign key ke `chat_user.id` |
| `created_at` | datetime | Waktu percakapan dibuat |

Tambahkan unique constraint agar pasangan peserta tidak memiliki percakapan ganda.
Urutkan ID peserta sebelum menyimpan sehingga `A-B` dan `B-A` dianggap pasangan yang sama.

### `chat_message`

| Kolom | Tipe | Keterangan |
|---|---|---|
| `id` | integer | Primary key |
| `conversation_id` | integer | Foreign key ke percakapan |
| `sender_id` | integer | Foreign key ke pengirim |
| `content` | text | Isi pesan, boleh kosong jika ada lampiran |
| `attachment_path` | string(500) | Path file, bersifat opsional |
| `attachment_name` | string(255) | Nama file asli |
| `attachment_type` | string(50) | `image`, `pdf`, atau kosong |
| `created_at` | datetime | Waktu pesan dibuat |

Tambahkan index pada `conversation_id` dan `created_at` agar polling riwayat cepat.

## Autentikasi

Gunakan akun pada tabel `chat_user`, bukan `AdminUser`.

- Simpan password sebagai hash menggunakan `pwd_context`.
- Setelah login berhasil, simpan JWT dalam cookie `chat_token`.
- Cookie menggunakan `httponly=True` dan `samesite="lax"`.
- Set `secure=True` pada deployment HTTPS.
- Masa berlaku token 8 jam.
- Semua endpoint chat, kecuali halaman dan proses login, wajib memeriksa token.
- Saat pengguna tidak berhak mengakses percakapan, kirim `403 Forbidden`.

Cookie login chat tidak boleh memakai nama `admin_token`.

## Endpoint

### Halaman

```text
GET  /chat/login
POST /chat/login
GET  /chat/logout
GET  /chat
```

Perilaku:

- `/chat/login`: tampilkan form jika belum login.
- Jika sudah login, arahkan `/chat/login` ke `/chat`.
- `/chat`: wajib login; muat daftar lawan chat dan percakapan awal.
- `/chat/logout`: hapus `chat_token` dan kembali ke `/chat/login`.

### API

```text
GET  /chat/api/users
GET  /chat/api/conversations
POST /chat/api/conversations
GET  /chat/api/conversations/{conversation_id}/messages
POST /chat/api/conversations/{conversation_id}/messages
POST /chat/api/conversations/{conversation_id}/attachments
DELETE /chat/api/conversations/{conversation_id}/messages
POST /chat/api/heartbeat
```

### `GET /chat/api/conversations`

Mengembalikan daftar percakapan pengguna dengan:

```json
[
  {
    "id": 1,
    "partner_id": 2,
    "partner_name": "Budi",
    "last_message": "Bisa kirim file?",
    "last_message_at": "2026-11-26T01:20:00Z",
    "is_online": true
  }
]
```

### `POST /chat/api/conversations`

Input:

```json
{
  "partner_id": 2
}
```

Gunakan percakapan lama bila pasangan sudah pernah dibuat. Jika belum ada, buat
percakapan baru.

### `GET /chat/api/conversations/{id}/messages`

Parameter:

```text
after_id: optional, ID pesan terakhir yang sudah diterima
limit: optional, default 50, maksimum 100
```

Respons:

```json
{
  "messages": [
    {
      "id": 15,
      "sender_id": 2,
      "content": "Halo",
      "attachment": null,
      "created_at": "2026-11-26T01:20:00Z"
    }
  ],
  "last_message_id": 15,
  "server_time": "2026-11-26T01:20:04Z"
}
```

Jika tanpa `after_id`, kirim 50 pesan terbaru. Jika memakai `after_id`, hanya
kirim pesan yang ID-nya lebih besar.

### `POST /chat/api/conversations/{id}/messages`

Input:

```json
{
  "content": "Bisa kirim file?"
}
```

Aturan:

- Isi pesan harus berupa teks.
- Hapus spasi di awal dan akhir.
- Tolak pesan kosong.
- Batasi maksimum 4.000 karakter.
- Simpan ke database lalu kirim pesan yang baru dibuat sebagai respons `201`.

## Lampiran

### Batas validasi

- Gambar: JPG, PNG, WebP, maksimum 5 MB.
- PDF: maksimum 10 MB.
- Tolak tipe lain.
- Validasi MIME asli, bukan hanya nama ekstensi.
- Ubah gambar menjadi nama acak seperti file upload lain di aplikasi.
- Jangan melayani file dengan Content-Disposition inline jika tipe tidak valid.
- Simpan di bawah `app/private_uploads/chat/`, bukan direktori static.
- Simpan `created_at` pesan dalam UTC dan sertakan waktu ISO 8601 pada respons.

### `POST /chat/api/conversations/{id}/attachments`

Kirim memakai `multipart/form-data`:

```text
file: UploadFile
content: pesan opsional
```

Respons menggunakan bentuk `chat_message` yang sama dengan endpoint pesan teks.

### Clear Chat

Tambahkan tombol **Clear Chat** pada header percakapan aktif.

Fungsi ini menghapus seluruh pesan dalam percakapan secara permanen untuk kedua
pengguna. Tindakan tidak dapat dibatalkan.

```text
DELETE /chat/api/conversations/{conversation_id}/messages
```

Sebelum request dikirim, frontend menampilkan konfirmasi:

```text
Hapus semua pesan dalam percakapan ini untuk kedua pengguna?
Tindakan ini tidak dapat dibatalkan.
```

Aturan:

- Hanya peserta percakapan yang dapat menggunakan endpoint.
- Paling tidak satu pesan harus dihapus; percakapan kosong tetap dipertahankan.
- Hapus semua record `chat_message` pada percakapan.
- Hapus seluruh lampiran terkait setelah data pesan berhasil dihapus.
- Gagal menghapus file harus dicatat sebagai error, bukan mengembalikan status
  sukses palsu.
- Gunakan transaksi database agar riwayat tidak terhapus sebagian.
- Setelah berhasil, kosongkan area pesan tanpa refresh halaman.
- Tampilkan status "Belum ada pesan" pada kedua sisi.
- Pengguna lain akan melihat penghapusan pada polling berikutnya.
- Tombol dinonaktifkan ketika request berjalan atau percakapan sudah kosong.

Respons sukses:

```json
{
  "cleared": true,
  "conversation_id": 1
}
```

Jika riwayat percakapan telah berubah saat request berjalan, tetap gunakan
penghapusan terbaru berdasarkan `conversation_id`. Jangan mengandalkan ID pesan
terakhir yang dikirim browser.

Download hanya boleh dilakukan oleh peserta percakapan. Jangan memberi URL file
lama secara langsung jika lokasi tersebut belum lolos pemeriksaan kepemilikan.
Gunakan endpoint download terproteksi, misalnya:

```text
GET /chat/api/messages/{message_id}/attachment
```

## Polling Frontend

Polling dilakukan setiap 4 detik dan tidak memerlukan WebSocket.

```javascript
const pollingIntervalMs = 4000;
let activeConversationId = null;
let lastMessageId = 0;
let pollingTimer = null;
```

Setiap siklus:

1. Jangan polling jika tab sedang tersembunyi.
2. Panggil endpoint pesan dengan `after_id=lastMessageId`.
3. Tambahkan hanya pesan baru ke tampilan.
4. Perbarui `lastMessageId`.
5. Panggil heartbeat paling lama setiap 20 detik.
6. Refresh daftar percakapan dan status online setiap 20 detik.

Jika request gagal:

- Tampilkan indikator koneksi terputus.
- Jangan menghapus pesan yang sudah tampil.
- Coba lagi pada polling berikutnya.
- Biarkan pengguna tetap dapat mengganti percakapan.

Saat mengirim pesan:

1. Nonaktifkan tombol kirim sementara.
2. Kirim request.
3. Tampilkan pesan hasil respons.
4. Perbarui `lastMessageId`.
5. Aktifkan kembali input setelah berhasil atau gagal.
6. Jika gagal, tampilkan pesan kesalahan dan pertahankan isi input.

## Tampilan

Halaman chat harus responsif:

- Desktop: lebar percakapan sekitar 700 piksel, posisi tengah.
- Mobile: memenuhi lebar layar dan mengurangi padding.
- Area pesan: tinggi tetap, dapat di-scroll.
- Pesan sendiri rata kanan dengan warna hijau muda.
- Pesan pengguna lain rata kiri dengan latar abu-abu.
- Gambar dapat dibuka dalam ukuran lebih besar.
- Gambar langsung ditampilkan sebagai preview di dalam balon chat.
- PDF ditampilkan sebagai kartu tautan/download.
- Pesan baru otomatis men-scroll ke bawah.
- Pengguna yang membuka riwayat lama tidak dipaksa kembali ke bawah.
- Setiap pesan menampilkan waktu kirim, termasuk pesan teks, gambar, dan PDF.

### Tanggal dan Jam Pesan

Waktu pesan tampil pada bagian bawah balon:

```text
Halo
08.42
```

Gunakan format berikut:

- Pesan hari ini: tampilkan jam dan menit, misalnya `08.42`.
- Pesan kemarin: tampilkan `Kemarin, 08.42`.
- Pesan tahun yang sama: tampilkan tanggal singkat dan jam,
  misalnya `24 Nov, 08.42`.
- Pesan tahun berbeda: tampilkan tanggal lengkap dan jam,
  misalnya `24 Nov 2025, 08.42`.
- Tanggal pemisah dapat ditampilkan di tengah riwayat, misalnya
  `Hari ini`, `Kemarin`, atau `Senin, 23 November 2026`.

Aturan waktu:

- Backend menyimpan waktu pesan dalam UTC.
- API mengirim waktu ISO 8601 yang menyertakan offset atau akhiran `Z`.
- JavaScript mengubah waktu UTC menjadi zona waktu perangkat pengguna dengan
  `Date.toLocaleTimeString()` dan `Date.toLocaleDateString()`.
- Tampilan menggunakan locale Indonesia (`id-ID`).
- Jangan mengubah waktu database berdasarkan zona waktu server.
- Atribut `datetime` HTML menggunakan nilai ISO 8601 asli.
- Judul atau tooltip waktu dapat menampilkan tanggal dan jam lengkap.
- Pesan yang gagal terkirim tidak diberi waktu pengiriman permanen.

### Preview Foto

Lampiran dengan tipe `image` langsung ditampilkan di percakapan:

```text
┌────────────────────────┐
│    [Preview gambar]    │
│                        │
│ foto-kegiatan.jpg      │
└────────────────────────┘
```

Aturan preview:

- Ukuran preview maksimum lebar 280 piksel.
- Tinggi preview menyesuaikan gambar dan tidak memotong isi.
- Gunakan `loading="lazy"` untuk mengurangi penggunaan bandwidth.
- Klik preview untuk membuka gambar ukuran penuh.
- Jika preview gagal dimuat, tampilkan nama file dan tombol unduh.
- Gambar ditampilkan pada balon yang sama dengan pesan teks.
- File PDF tidak ditampilkan sebagai preview gambar.

URL preview dan gambar penuh memakai endpoint terproteksi:

```text
GET /chat/api/messages/{message_id}/attachment?preview=1
GET /chat/api/messages/{message_id}/attachment
```

Endpoint pertama mengembalikan thumbnail jika tersedia. Jika thumbnail belum
tersedia atau tidak dapat dibuat, endpoint dapat mengembalikan gambar asli
dengan ukuran download yang masih dibatasi server. Endpoint kedua mengembalikan
gambar atau PDF dengan header download sesuai kebutuhan.

## Pembuatan Akun Awal

Pada versi pertama belum memerlukan halaman pendaftaran publik.

Tambahkan data awal melalui:

```text
backend/seed.py
```

atau command administratif. Kredensial tidak boleh ditulis langsung di kode atau
di dokumentasi. Gunakan dua pasangan akun dari variabel environment:

```dotenv
CHAT_USER1_USERNAME=...
CHAT_USER1_PASSWORD=...
CHAT_USER2_USERNAME=...
CHAT_USER2_PASSWORD=...
```

Aturan seed akun:

- Baca `CHAT_USER1_USERNAME` dan `CHAT_USER1_PASSWORD`.
- Baca `CHAT_USER2_USERNAME` dan `CHAT_USER2_PASSWORD`.
- Buat kedua akun pada `chat_user` saat aplikasi pertama kali dijalankan.
- Jika username sudah ada, jangan membuat akun duplikat.
- Jangan menimpa password akun yang sudah ada.
- Password di environment di-hash dengan bcrypt sebelum disimpan ke database.
- Nama tampilan awal dapat disamakan dengan username.
- Jika salah satu pasangan username/password tidak lengkap, jangan membuat akun
  tersebut dan tampilkan peringatan startup yang jelas.
- Jangan pernah membalas atau mencatat password hasil pembacaan environment.
- Halaman `/chat/login` menerima kedua username tersebut beserta password
  pasangannya.

Versi pertama hanya mengizinkan kedua akun environment. Fitur menambah atau
menghapus akun melalui CMS admin dapat dikembangkan setelah fungsi chat dasar
selesai.

## Urutan Implementasi

### 1. Model dan autentikasi

- Tambahkan relasi dan model chat pada `models.py`.
- Buat helper `get_current_chat_user`.
- Buat login dan logout khusus chat.
- Tambahkan seed akun `CHAT_USER1_*` dan `CHAT_USER2_*` dari environment.

### 2. Halaman dan router

- Buat router `chat.py`.
- Buat `chat_login.html`.
- Buat layout dasar `chat.html`.
- Daftarkan router pada `main.py`.
- Pastikan `/chat` membalas redirect login jika token tidak ada.

### 3. Percakapan dan pesan

- Buat endpoint daftar pengguna dan percakapan.
- Buat percakapan unik antara dua pengguna.
- Buat endpoint pengiriman pesan.
- Buat endpoint polling berdasarkan `after_id`.
- Tambahkan pemeriksaan peserta pada setiap endpoint.

### 4. Frontend polling

- Buat `chat.js`.
- Muat percakapan, kirim pesan, dan lakukan polling setiap 4 detik.
- Tambahkan indikator loading, error, dan online/offline.
- Pastikan tab tersembunyi tidak melakukan request tiap 4 detik.

### 5. Lampiran

- Tambahkan validasi gambar/PDF.
- Buat endpoint upload dan download terproteksi.
- Tampilkan preview gambar dan tautan PDF.

### 6. Keamanan

- Batasi pesan dan ukuran upload.
- Verifikasi peserta percakapan pada pesan dan lampiran.
- Hindari membuka `attachment_path` langsung dari input pengguna.
- Gunakan nama file acak dan simpan metadata di database.
- Pastikan error upload dan autentikasi tidak membocorkan detail internal.

### 7. Pengujian

Minimal uji:

- Login benar dan salah.
- Pengguna tanpa login tidak dapat membuka `/chat`.
- Pengguna tidak dapat membaca percakapan orang lain.
- Pengguna tidak dapat mengunduh lampiran percakapan orang lain.
- Pesan kosong ditolak.
- Polling hanya mengembalikan pesan setelah `after_id`.
- Pesan muncul setelah login ulang.
- Gambar/PDF diterima dan tipe lain ditolak.
- File yang melebihi batas ditolak.
- Preview gambar muncul langsung pada balon chat.
- Preview gagal menampilkan nama file dan tombol unduh.
- Pengguna non-peserta tidak dapat membuka preview maupun gambar penuh.
- Clear Chat meminta konfirmasi sebelum menghapus.
- Clear Chat menghapus pesan dan lampiran untuk kedua peserta.
- Pengguna non-peserta tidak dapat melakukan Clear Chat.
- Setelah Clear Chat, polling tetap sinkron dan tidak memunculkan pesan lama.
- Polling berhenti saat tab disembunyikan.
- Waktu tampil pada seluruh tipe pesan dan menggunakan zona waktu perangkat.
- Pemisah tanggal berubah sesuai hari pengiriman.
- Status online berubah offline setelah 30 detik tanpa heartbeat.

## Keputusan Implementasi

Versi pertama memakai **HTTP polling selama 4 detik**, bukan WebSocket, karena:

- lebih sederhana untuk aplikasi FastAPI dan satu container;
- mudah di-deploy dengan Cloudflare Tunnel dan reverse proxy;
- cukup untuk jumlah pengguna kecil dan delay beberapa detik;
- tidak memerlukan penyimpanan koneksi aktif di memori;
- struktur API dan database dapat tetap digunakan jika WebSocket ditambahkan nanti.
