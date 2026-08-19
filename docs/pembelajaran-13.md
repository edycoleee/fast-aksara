# Pembelajaran 13 - Hosting, Domain, dan Cloudflare Tunnel

Pembelajaran ini membahas bagaimana aplikasi web yang sudah dibuat bisa diakses publik lewat internet tanpa harus membuka port aplikasi secara langsung.

## A. Tujuan

- Siswa memahami konsep hosting.
- Siswa memahami peran domain dan DNS.
- Siswa memahami cara kerja Cloudflare Tunnel.
- Siswa bisa menjelaskan alur publikasi aplikasi dari server lokal ke domain internet.

## B. Hasil Akhir

Di akhir pembelajaran, siswa mampu:

1. Menjelaskan arti hosting.
2. Menjelaskan fungsi domain dan DNS.
3. Menjelaskan alur request dari browser ke aplikasi server.
4. Memahami cara kerja Cloudflare Tunnel untuk keamanan.
5. Menyusun arsitektur sederhana aplikasi yang bisa diakses publik.

## C. Estimasi Waktu

- 2 sampai 3 pertemuan (180-270 menit).

## D. Konsep Dasar

### 1) Hosting
Hosting adalah tempat aplikasi disimpan dan dijalankan secara terus-menerus agar bisa diakses dari internet.

Contoh:
- laptop pribadi bisa digunakan sebagai server kecil,
- VPS bisa dipakai untuk aplikasi yang lebih stabil,
- cloud server bisa dipakai untuk kebutuhan produksi.

### 2) Domain
Domain adalah alamat yang mudah diingat, misalnya:
- `aksara.fun`
- `example.com`

Domain tidak menyimpan aplikasi, ia hanya mengarahkan user ke server yang benar.

### 3) DNS
DNS (Domain Name System) adalah sistem yang mengubah nama domain menjadi alamat IP server.

Contoh sederhananya:

```text
aksara.fun  ->  192.10.10.152
```

### 4) Cloudflare Tunnel
Cloudflare Tunnel adalah cara agar layanan di server lokal bisa diakses publik tanpa membuka port ke internet langsung.

Alurnya seperti ini:

```text
Browser -> Cloudflare Edge -> Tunnel -> Server lokal:3004
```

Yang penting:
- server lokal tetap aman,
- internet hanya melihat Cloudflare,
- aplikasi tetap berjalan di port internal.

## E. Arsitektur yang Dipelajari

```text
Browser
   |
   v
https://aksara.fun
   |
   v
Cloudflare
   |
   v
Tunnel
   |
   v
192.10.10.152:3004
   |
   v
Docker Compose container
   |
   v
FastAPI app
```

## F. Skema Praktik di Proyek Ini

Proyek FastAksara sudah memiliki:
- server lokal pada IP tertentu,
- aplikasi FastAPI berjalan di port `3004`,
- Docker Compose untuk menjalankan server.

Jadi, alur logisnya adalah:

1. Aplikasi berjalan di server lokal `192.10.10.152:3004`.
2. Cloudflare Tunnel menghubungkan domain ke server.
3. User mengakses `https://aksara.fun`.
4. Cloudflare meneruskan request ke server internal.

## G. Langkah Kerja Hosting

### Tahap 1 - Server siap
Pastikan server atau komputer sudah aktif.

```bash
curl -I http://127.0.0.1:3004/
```

Jika aplikasi sudah berjalan, server siap menerima request.

### Tahap 2 - Domain sudah di Cloudflare
Domain harus dikelola menggunakan Cloudflare agar dapat dibuat tunnel.

Cek hal berikut:
- domain aktif,
- nameserver sudah di Cloudflare,
- zone domain sudah terdaftar.

### Tahap 3 - Tunnel dibuat
Di Cloudflare Zero Trust, buat Tunnel baru.

Misalnya:
- nama tunnel: `aksara-tunnel`

### Tahap 4 - Connector diinstal di server
Di server Linux, install `cloudflared` dan ikuti token dari Cloudflare.

Contoh:

```bash
sudo cloudflared service install <TOKEN>
```

### Tahap 5 - Public hostname dibuat
Buat hostname publik:

```text
Hostname: aksara.fun
Service URL: http://192.10.10.152:3004
```

Maka browser membuka domain publik dan Cloudflare meneruskan ke server lokal.

## H. Dasar DNS dan Domain

### fungsi domain
- Nama yang mudah diingat.
- Berfungsi seperti alamat rumah.

### fungsi DNS
- Menerjemahkan domain ke IP.
- Agar browser tahu kemana harus pergi.

## I. Kenapa Pakai Cloudflare Tunnel?

Keuntungan utama:

1. Lebih aman
   - Port tidak dibuka ke internet secara langsung.
2. Lebih mudah
   - Domain publik langsung masuk ke server internal.
3. Stabil
   - Cloudflare membantu routing, caching, dan keamanan.
4. Praktis
   - Cocok untuk proyek sekolah dan demo publik.

## J. Contoh Alur Request

```text
Browser
  -> https://aksara.fun
  -> Cloudflare Edge
  -> Tunnel Connector
  -> 192.10.10.152:3004
  -> FastAPI app
  -> HTML / JSON response
  -> Browser menampilkan hasil
```

## K. Masalah yang Sering Terjadi

### 1) Domain tidak bisa dibuka
Kemungkinan:
- DNS belum aktif
- tunnel belum sehat
- public hostname tidak dibuat
- aplikasi lokal tidak running

### 2) Aplikasi belum jalan
Cek:

```bash
curl -i http://127.0.0.1:3004/
```

### 3) Port salah
Jika aplikasi sebenarnya berjalan di `3005`, tapi tunnel diarahkan ke `3004`, maka domain tidak akan bekerja.

### 4) Nama domain belum di Cloudflare
Domain harus dikelola oleh Cloudflare agar tunnel bisa bekerja dengan host alias.

## L. Diagram Sederhana Deployment

```text
Domain Cloudflare
   |
   v
Tunnel / Zero Trust
   |
   v
Server lokal (Docker Compose)
   |
   v
FastAPI + SQLite + Upload
```

## M. Checklist Praktik Siswa

1. Server lokal berjalan di port `3004`.
2. Aplikasi bisa diakses lewat localhost.
3. Tunnel dibuat di Cloudflare Zero Trust.
4. Public hostname dibuat untuk domain.
5. Browser bisa membuka domain publik dengan HTTPS.
6. Aplikasi tetap berjalan meskipun port internal tidak dibuka ke internet.

## N. Rubrik Penilaian

Skor 1-4 per aspek:

1. Pemahaman hosting.
2. Pemahaman domain dan DNS.
3. Pemahaman Cloudflare Tunnel.
4. Ketepatan menggambarkan arsitektur request.
5. Keberhasilan menjelaskan keamanan publikasi aplikasi.

Nilai akhir = rata-rata 5 aspek.

## O. Tugas Lanjutan

1. Buat diagram arsitektur hosting aplikasi kalian.
2. Jelaskan perbedaan hosting, domain, DNS, dan tunnel.
3. Coba dokumentasikan langkah deployment ke VPS lokal.
4. Bandingkan akses langsung vs akses lewat Cloudflare Tunnel.

## P. Catatan Guru

- Fokuskan konsep, bukan hanya langkah teknis.
- Siswa perlu memahami bahwa domain bukan aplikasi, hanya alamat yang mengarah ke server.
- Cloudflare Tunnel adalah solusi yang aman dan cocok untuk demo atau proyek sekolah.

## Q. Penutup

Setelah Pembelajaran 13:

- siswa memahami arti hosting, domain, DNS, dan Cloudflare Tunnel,
- siswa mampu menjelaskan alur aplikasi dari server lokal hingga publik melalui internet,
- siswa siap mengikuti tahap deployment atau pengelolaan aplikasi di server nyata.
