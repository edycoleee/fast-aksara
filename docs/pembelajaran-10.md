# Pembelajaran 10 - Unit Test API dengan Pytest

Pembelajaran ini melanjutkan Pembelajaran 9.
Setelah siswa belajar auth dan keamanan dasar, tahap berikutnya adalah memastikan fitur API selalu benar lewat pengujian otomatis.

## A. Tujuan

- Siswa memahami konsep unit test API.
- Siswa bisa menjalankan test otomatis dengan Pytest.
- Siswa bisa menguji endpoint CRUD (create, read, update, delete).
- Siswa bisa menguji skenario sukses dan gagal.

## B. Hasil Akhir

Di akhir pembelajaran, siswa mampu:

1. Menyiapkan folder test.
2. Membuat test client FastAPI.
3. Menguji endpoint utama dengan data uji.
4. Membaca hasil test dan memperbaiki bug dari output test.

## C. Estimasi Waktu

- 3 sampai 4 pertemuan (270-360 menit).

## D. Konsep Dasar (Bahasa Sederhana)

1. Unit test: tes kecil untuk memeriksa satu perilaku program.
2. API test: kirim request ke endpoint, lalu cek response.
3. Otomatis: sekali jalankan `pytest`, semua test diperiksa sekaligus.
4. Manfaat utama: bug terdeteksi lebih cepat sebelum deploy.

## E. Alur Belajar

### Tahap 1 - Menyiapkan Tools (30-45 menit)

Aktivitas:
- Install `pytest` dan `httpx`.
- Kenali struktur folder test.

Output:
- Environment siap untuk test.

### Tahap 2 - Membuat Test Dasar GET (45-60 menit)

Aktivitas:
- Uji endpoint list data.
- Cek status code dan bentuk data JSON.

Output:
- Siswa bisa menulis test pertama.

### Tahap 3 - Menguji CRUD API (90-120 menit)

Aktivitas:
- Test create, read, update, delete.
- Tambahkan skenario id tidak ditemukan.

Output:
- Endpoint CRUD tervalidasi.

### Tahap 4 - Menjalankan Semua Test + Evaluasi (45-60 menit)

Aktivitas:
- Jalankan `pytest -q`.
- Baca test yang gagal dan analisis penyebab.

Output:
- Siswa bisa debugging berbasis hasil test.

## F. Instalasi Paket Test

Jalankan dari folder [backend/](backend/):

```powershell
pip install pytest httpx
```

Opsional simpan ke requirements:

```powershell
pip freeze > requirements.txt
```

## G. Struktur File yang Disarankan

```text
backend/
|-- app/
|   |-- main.py
|   |-- database.py
|   |-- models.py
|   |-- routers/
|       |-- elibrary.py
|-- tests/
|   |-- conftest.py
|   |-- test_health.py
|   |-- test_elibrary_api.py
|-- pytest.ini
```

## H. Detail per File (Jawaban Praktik)

### 1) [backend/pytest.ini](backend/pytest.ini)

```ini
[pytest]
pythonpath = .
testpaths = tests
```

### 2) [backend/tests/conftest.py](backend/tests/conftest.py)

```python
from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app

# Database test terpisah agar tidak merusak database utama.
TEST_DATABASE_URL = "sqlite:///./test_fast_aksara.db"

engine_test = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)


def override_get_db() -> Generator:
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def client() -> Generator[TestClient, None, None]:
    Base.metadata.drop_all(bind=engine_test)
    Base.metadata.create_all(bind=engine_test)

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()
```

### 3) [backend/tests/test_health.py](backend/tests/test_health.py)

Gunakan endpoint paling sederhana yang sudah ada (misalnya landing page).

```python
def test_landing_page_ok(client):
    response = client.get("/")
    assert response.status_code == 200
```

Jika proyek punya endpoint health JSON (contoh `/health`), bisa pakai:

```python
def test_health_json(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
```

### 4) [backend/tests/test_elibrary_api.py](backend/tests/test_elibrary_api.py)

Contoh berikut memakai endpoint API contoh:
- `GET /api/elibrary`
- `POST /api/elibrary`
- `PUT /api/elibrary/{item_id}`
- `DELETE /api/elibrary/{item_id}`

Sesuaikan path jika di proyekmu berbeda.

```python
def test_get_elibrary_list(client):
    response = client.get("/api/elibrary")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_elibrary_item(client):
    payload = {
        "judul": "Belajar Aksara Jawa",
        "kategori": "Budaya",
        "penulis": "Tim Aksara",
        "ringkasan": "Materi dasar aksara jawa",
    }

    response = client.post("/api/elibrary", json=payload)
    assert response.status_code in [200, 201]

    data = response.json()
    assert data["judul"] == payload["judul"]
    assert "id" in data


def test_update_elibrary_item(client):
    create_payload = {
        "judul": "Draft Lama",
        "kategori": "Budaya",
        "penulis": "Admin",
        "ringkasan": "Ringkasan lama",
    }
    created = client.post("/api/elibrary", json=create_payload).json()
    item_id = created["id"]

    update_payload = {
        "judul": "Draft Baru",
        "kategori": "Sejarah",
        "penulis": "Admin",
        "ringkasan": "Ringkasan baru",
    }

    response = client.put(f"/api/elibrary/{item_id}", json=update_payload)
    assert response.status_code == 200
    assert response.json()["judul"] == "Draft Baru"


def test_delete_elibrary_item(client):
    create_payload = {
        "judul": "Akan Dihapus",
        "kategori": "Arsip",
        "penulis": "Admin",
        "ringkasan": "Data sementara",
    }
    created = client.post("/api/elibrary", json=create_payload).json()
    item_id = created["id"]

    response = client.delete(f"/api/elibrary/{item_id}")
    assert response.status_code in [200, 204]


def test_update_not_found(client):
    update_payload = {
        "judul": "Tidak Ada",
        "kategori": "X",
        "penulis": "Y",
        "ringkasan": "Z",
    }

    response = client.put("/api/elibrary/99999", json=update_payload)
    assert response.status_code in [404, 400]
```

## I. Menjalankan Test

Dari folder [backend/](backend/):

```powershell
pytest -q
```

Jika ingin detail lebih lengkap:

```powershell
pytest -v
```

## J. Cara Baca Hasil Test

1. `.` berarti test lulus.
2. `F` berarti test gagal.
3. Bagian bawah output menunjukkan file dan baris assertion yang gagal.

Contoh:

```text
E       assert 404 == 200
```

Artinya endpoint mengembalikan 404 padahal test berharap 200.

## K. Checklist Praktik Siswa

1. Folder `tests` berhasil dibuat.
2. `conftest.py` bisa membuat test client.
3. Minimal 3 test API berjalan.
4. Ada test sukses dan test gagal (not found/invalid).
5. Semua test lulus setelah perbaikan kode.

## L. Rubrik Penilaian

Skor 1-4 per aspek:

1. Struktur test project rapi.
2. Ketepatan assertion status code.
3. Cakupan skenario CRUD.
4. Kemampuan membaca error test.
5. Kemandirian debugging sampai test hijau.

Nilai akhir = rata-rata 5 aspek.

## M. Tantangan Lanjutan (Opsional)

1. Tambahkan test autentikasi endpoint admin (unauthorized vs authorized).
2. Tambahkan test validasi upload file (tipe file salah harus ditolak).
3. Tambahkan test pagination dan filter query.
4. Buat CI sederhana agar test berjalan otomatis saat push.

## N. Catatan Guru

- Mulai dari endpoint paling mudah dulu agar siswa tidak takut.
- Saat ada test gagal, fokuskan pada satu gagal dulu sampai selesai.
- Biasakan siswa menulis test sebelum ubah fitur besar.

## O. Penutup

Setelah Pembelajaran 10:

- Siswa mampu menjaga kualitas API dengan pengujian otomatis.
- Siswa siap lanjut ke Pembelajaran 11 untuk integrasi test, audit log, atau pipeline deployment sederhana.

