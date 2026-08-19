# Pembelajaran 8 - Database SQLite (Skema dan Tabel)

Pembelajaran ini melanjutkan Pembelajaran 7.
Jika siswa sudah bisa CRUD admin, sekarang fokusnya adalah pondasi database: desain tabel yang benar, relasi data sederhana, dan data awal (seed).

## A. Tujuan

- Siswa memahami penyimpanan data permanen dengan SQLite.
- Siswa mengenal konsep tabel, kolom, id, tipe data, dan relasi sederhana.
- Siswa dapat membuat model SQLAlchemy yang rapi.
- Siswa dapat menyiapkan data awal untuk kebutuhan demo aplikasi.

## B. Hasil Akhir

Di akhir pembelajaran, siswa mampu:

1. Menyusun skema tabel inti proyek.
2. Menjalankan inisialisasi tabel dari SQLAlchemy.
3. Menambahkan data awal menggunakan script seed.
4. Mengecek data hasil seed dari halaman aplikasi atau query sederhana.

## C. Estimasi Waktu

- 2 sampai 3 pertemuan (180-270 menit).

## D. Tahap Belajar

### Tahap 1 - Konsep Skema Data (30-45 menit)

Aktivitas:
- Identifikasi entitas utama: E-Library, Dokumentasi, Artikel, Settings.
- Tentukan field wajib setiap entitas.

Output:
- Draft tabel dan kolom (manual di kertas/markdown).

### Tahap 2 - Implementasi Model SQLAlchemy (45-60 menit)

Aktivitas:
- Menulis class model Python untuk tiap tabel.
- Menentukan tipe data yang tepat (`Integer`, `String`, `Text`, `Boolean`, `DateTime`).

Output:
- File model siap dipakai untuk membuat tabel.

### Tahap 3 - Generate Tabel SQLite (30-45 menit)

Aktivitas:
- Jalankan `Base.metadata.create_all(bind=engine)`.
- Pastikan file `.db` terbentuk.

Output:
- Database SQLite aktif dengan tabel inti.

### Tahap 4 - Isi Data Awal (Seed) (45-60 menit)

Aktivitas:
- Buat script seed.
- Masukkan data contoh minimal untuk semua tabel inti.

Output:
- Aplikasi punya data awal untuk diuji dan didemokan.

### Tahap 5 - Validasi Data (30 menit)

Aktivitas:
- Cek data dari halaman publik/admin.
- Cek skenario tabel kosong vs ada data.

Output:
- Struktur data siap dipakai untuk pembelajaran lanjutan.

## E. Struktur File yang Dipakai

```text
backend/
|-- app/
|   |-- database.py
|   |-- models.py
|   |-- routers/
|   |   |-- admin.py
|   |   |-- elibrary.py
|   |   |-- tunas.py
|   |-- templates/
|-- seed.py
```

## F. Kunci Konfigurasi Database SQLite

Contoh konfigurasi `database.py`:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(
	DATABASE_URL,
	connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()
```

## G. Kunci Model Tabel Inti (Contoh)

Contoh ini mengikuti kebutuhan proyek literasi.

```python
from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text, func
from app.database import Base


class ELibrary(Base):
	__tablename__ = "elibrary"
	id = Column(Integer, primary_key=True, index=True)
	judul = Column(String(200), nullable=False)
	kategori = Column(String(100), nullable=False)
	deskripsi = Column(Text, nullable=True)
	link = Column(String(255), nullable=True)
	link_type = Column(String(20), default="external", nullable=False)
	created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class Dokumentasi(Base):
	__tablename__ = "dokumentasi"
	id = Column(Integer, primary_key=True, index=True)
	judul = Column(String(200), nullable=False)
	kategori = Column(String(50), nullable=False)
	deskripsi = Column(Text, nullable=True)
	link_gambar = Column(String(255), nullable=True)
	link_video = Column(String(255), nullable=True)
	created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class Artikel(Base):
	__tablename__ = "artikel"
	id = Column(Integer, primary_key=True, index=True)
	judul = Column(String(200), nullable=False)
	kategori = Column(String(50), nullable=False)
	deskripsi = Column(Text, nullable=True)
	gambar = Column(String(255), nullable=True)
	link_pdf = Column(String(255), nullable=True)
	is_published = Column(Boolean, default=True, nullable=False)
	created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class Settings(Base):
	__tablename__ = "settings"
	id = Column(Integer, primary_key=True, index=True)
	site_name = Column(String(150), nullable=False)
	tagline = Column(String(255), nullable=True)
	whatsapp = Column(String(30), nullable=True)
	alamat = Column(Text, nullable=True)
	email = Column(String(120), nullable=True)
	maps_embed = Column(Text, nullable=True)
```

## H. Kunci Generate Tabel

Tambahkan sementara di startup atau script init:

```python
from app.database import Base, engine
from app import models

Base.metadata.create_all(bind=engine)
```

Penjelasan:
- SQLAlchemy akan membaca class model dan membuat tabel jika belum ada.

## I. Kunci Script Seed (Data Awal)

Contoh `seed.py` minimal:

```python
from app.database import SessionLocal
from app.models import ELibrary, Dokumentasi, Artikel, Settings


def run_seed():
	db = SessionLocal()
	try:
		if db.query(ELibrary).count() == 0:
			db.add_all([
				ELibrary(judul="Panduan Menulis Cerita", kategori="Literasi", deskripsi="Materi dasar."),
				ELibrary(judul="Kelas Poster Digital", kategori="Keterampilan", deskripsi="Dasar desain."),
			])

		if db.query(Dokumentasi).count() == 0:
			db.add_all([
				Dokumentasi(judul="Kelas Membaca Ceria", kategori="tunas", deskripsi="Kegiatan anak-anak."),
				Dokumentasi(judul="Workshop Konten", kategori="karya", deskripsi="Kegiatan remaja."),
			])

		if db.query(Artikel).count() == 0:
			db.add_all([
				Artikel(judul="Langkah Awal Jualan Online", kategori="cakra", deskripsi="Pengenalan marketplace."),
				Artikel(judul="Senam Lansia Mingguan", kategori="kersa", deskripsi="Program kesehatan."),
			])

		if db.query(Settings).count() == 0:
			db.add(Settings(site_name="Ngrembaka Aksara", tagline="Literasi untuk Semua"))

		db.commit()
		print("Seed selesai.")
	finally:
		db.close()


if __name__ == "__main__":
	run_seed()
```

Jalankan:

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
python seed.py
```

## J. Contoh Validasi Field Dasar di CRUD

Contoh pada create artikel:

```python
if len(judul.strip()) < 5:
	raise ValueError("Judul minimal 5 karakter")

if kategori not in ["tunas", "karya", "cakra", "kersa"]:
	raise ValueError("Kategori tidak valid")
```

Catatan pengajaran:
- Jelaskan bahwa validasi backend wajib, walau frontend sudah punya `required`.

## K. Checklist Praktik Siswa

1. File `app.db` terbentuk.
2. Semua tabel inti terbentuk (`elibrary`, `dokumentasi`, `artikel`, `settings`).
3. Script seed berhasil menambah data awal.
4. Data muncul di halaman publik/admin.
5. Tambah data lewat admin benar-benar tersimpan (cek setelah restart server).

## L. Rubrik Penilaian

Skor 1-4 per aspek:

1. Ketepatan desain kolom tabel.
2. Kebenaran implementasi model SQLAlchemy.
3. Keberhasilan generate tabel dan seed.
4. Konsistensi data saat CRUD.
5. Penerapan validasi dasar.

Nilai akhir = rata-rata 5 aspek.

## M. Tugas Lanjutan

1. Tambahkan field `updated_at` pada tabel utama.
2. Tambahkan index pada kolom pencarian (`judul`, `kategori`).
3. Buat endpoint statistik sederhana untuk dashboard admin.
4. Coba ekspor isi tabel ke CSV.

## N. Penutup

Setelah Pembelajaran 8:

- Siswa memiliki pemahaman pondasi database yang solid.
- Siswa siap lanjut ke Pembelajaran 9: autentikasi, otorisasi role, dan keamanan input file.
