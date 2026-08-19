# Pembelajaran 12 - Docker Compose untuk Aplikasi FastAPI

Pembelajaran ini membahas cara menjalankan aplikasi dalam container agar lebih mudah dipindahkan, diulang, dan dipublish ke server.

## A. Tujuan

- Siswa memahami konsep container dan Docker.
- Siswa bisa menjalankan aplikasi FastAPI menggunakan Docker Compose.
- Siswa bisa melihat keunggulan deploy yang konsisten antar mesin.
- Siswa dapat memahami hubungan antara Dockerfile dan docker-compose.yml.

## B. Hasil Akhir

Di akhir pembelajaran, siswa mampu:

1. Menjelaskan fungsi Docker Compose.
2. Menjalankan aplikasi dari file Compose.
3. Mengatur port, volume, dan environment variable.
4. Menyimpan data SQLite tetap aman di volume Docker.

## C. Estimasi Waktu

- 2 sampai 3 pertemuan (180-270 menit).

## D. Konsep Dasar

### 1) Apa itu Docker?
Docker adalah alat untuk membungkus aplikasi beserta semua dependensinya ke dalam satu wadah yang bisa dijalankan di lingkungan mana saja.

### 2) Apa itu Docker Compose?
Docker Compose adalah alat untuk menjalankan beberapa container sekaligus dengan satu file konfigurasi.

Contoh di proyek ini:
- 1 container untuk aplikasi FastAPI
- 1 volume untuk database SQLite
- 1 volume untuk folder upload

## E. Kenapa Penting?

Docker membantu:
- konsisten saat develop dan deploy,
- tidak tergantung OS laptop,
- mudah di-copy ke server lain,
- memudahkan tim kerja kolaboratif.

## F. Struktur File Docker di Proyek

```text
backend/
|-- requirements.txt
|-- app/
|-- .env

docker/
|-- Dockerfile
|-- docker-compose.yml
```

## G. File Dockerfile

File [docker/Dockerfile](docker/Dockerfile) saat ini berisi:

```dockerfile
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 3004

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3004"]
```

Penjelasan:
- `FROM python:3.12-slim`: gunakan base image Python.
- `WORKDIR /app`: folder kerja di container.
- `COPY requirements.txt .`: salin dependency.
- `RUN pip install...`: install paket Python.
- `COPY . .`: salin aplikasi.
- `EXPOSE 3004`: menandai port yang dipakai.
- `CMD [...]`: perintah startup aplikasi.

## H. File Docker Compose

File [docker/docker-compose.yml](docker/docker-compose.yml) saat ini berisi:

```yaml
services:
  aksara:
    build:
      context: ../backend
      dockerfile: ../docker/Dockerfile
    container_name: aksara-app
    restart: unless-stopped
    ports:
      - "3004:3004"
    env_file:
      - ../backend/.env
    environment:
      DATABASE_URL: sqlite:////app/data/aksara.db
    volumes:
      - aksara_db:/app/data
      - aksara_uploads:/app/app/static/uploads
    command: ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3004"]

volumes:
  aksara_db:
  aksara_uploads:
```

## I. Penjelasan per Bagian

### 1) services
Bagian utama untuk mendefinisikan container yang dibuat.

```yaml
services:
  aksara:
```

Artinya kita membuat service bernama `aksara`.

### 2) build

```yaml
build:
  context: ../backend
  dockerfile: ../docker/Dockerfile
```

- `context`: folder source aplikasi
- `dockerfile`: lokasi Dockerfile

Di proyek ini, aplikasi ada di folder [backend/](backend/) dan Dockerfile ada di folder [docker/](docker/).

### 3) ports

```yaml
ports:
  - "3004:3004"
```

Artinya:
- port laptop/host: `3004`
- port di container: `3004`

Jadi kita bisa membuka browser ke:

```text
http://localhost:3004
```

### 4) env_file

```yaml
env_file:
  - ../backend/.env
```

Ini memuat variabel lingkungan dari file `.env` seperti:

```env
SECRET_KEY=rahasia
DEBUG=False
```

### 5) environment

```yaml
environment:
  DATABASE_URL: sqlite:////app/data/aksara.db
```

Ini mengatur database SQLite di dalam container. Jadi file database akan disimpan di folder `/app/data`.

### 6) volumes

```yaml
volumes:
  - aksara_db:/app/data
  - aksara_uploads:/app/app/static/uploads
```

Ini penting karena:
- data SQLite tidak ikut hilang saat container dihapus,
- file upload tetap ada meskipun container di-restart.

### 7) command

```yaml
command: ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3004"]
```

Perintah ini menjalankan server FastAPI saat container naik.

## J. Cara Menjalankan Docker Compose

Dari root project, jalankan:

```powershell
docker compose -f docker/docker-compose.yml up --build
```

Jika sudah dibangun dan ingin menjalankan ulang:

```powershell
docker compose -f docker/docker-compose.yml up
```

Untuk menghentikan:

```powershell
docker compose -f docker/docker-compose.yml down
```

## K. Menjalankan di Background

```powershell
docker compose -f docker/docker-compose.yml up -d
```

- `-d` artinya detached, aplikasi berjalan di background.

## L. Buka Aplikasi

Setelah container aktif, bukalah browser ke:

```text
http://localhost:3004
```

## M. Tips Jika Ada Error

### Error 1: Docker tidak terinstall
Install Docker Desktop lalu restart komputer.

### Error 2: Port sudah dipakai
Cek jika port 3004 digunakan aplikasi lain. Ubah menjadi port lain seperti `3005`.

Contoh:

```yaml
ports:
  - "3005:3004"
```

### Error 3: Database tidak muncul
Pastikan volume `aksara_db` dibuat dan folder `/app/data` benar.

### Error 4: Upload tidak tersimpan
Pastikan folder `static/uploads` ada di container dan volume map benar.

## N. Contoh Praktik Siswa

Tugas kelompok:

1. Jalankan aplikasi dengan Docker Compose.
2. Ubah port menjadi `3005` dan jalankan ulang.
3. Simpan file gambar ke upload form.
4. Restart container, lalu cek apakah file masih ada.
5. Catat apa yang berubah dan apa yang tetap bertahan.

## O. Checklist Praktik Siswa

1. Docker Compose berhasil menjalankan aplikasi.
2. Browser bisa mengakses halaman utama.
3. Port mapping bekerja.
4. Volume database tetap ada setelah restart container.
5. File upload tetap ada walau container dihapus dan dibuat ulang.

## P. Rubrik Penilaian

Skor 1-4 per aspek:

1. Pemahaman konsep container.
2. Kebenaran konfigurasi Dockerfile.
3. Kebenaran konfigurasi Compose.
4. Kemampuan menjalankan dan mengecek hasil.
5. Ketepatan troubleshooting error sederhana.

Nilai akhir = rata-rata 5 aspek.

## Q. Tugas Lanjutan

1. Tambahkan service database MySQL/PostgreSQL dalam Compose.
2. Buat file `.env.example` agar pengguna mudah setup.
3. Tambahkan `docker compose` untuk development dan production yang berbeda.
4. Uji aplikasi saat file upload dan SQLite data dipindah ke volume.

## R. Kesimpulan

Docker Compose memudahkan kita menjalankan aplikasi FastAPI dengan konfigurasi yang rapi dan repeatable.
Untuk proyek seperti FastAksara, Compose membantu kita memastikan aplikasi bisa dijalankan dengan cara yang sama di laptop, server, atau lingkungan pengembangan lain.

## S. Penutup

Setelah Pembelajaran 12:

- Siswa paham cara menjalankan aplikasi FastAPI dengan Docker Compose.
- Siswa siap lanjut ke deployment nyata ke server/VPS atau cloud.
