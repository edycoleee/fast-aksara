### 7.6 Section Profil Program

#### Tujuan section
Section profil program berfungsi untuk menjelaskan program secara lebih luas dan lebih lengkap dibandingkan hero atau fitur pendukung. Di sini, user mulai mendapatkan pemahaman tentang tujuan, latar belakang, dan konteks program.

Pada halaman ini, section profil program terdiri dari dua card utama:
- Profil Ngrembaka Aksara
- Profil Kelurahan Podorejo

Masing-masing card berisi:
- badge kecil kategorinya,
- judul,
- deskripsi singkat,
- tombol baca selengkapnya.

---

#### Konsep dasar section profil program

Bayangkan kita ingin membangun sebuah section seperti ini:

```text
+---------------------------------------------------------------+
| Ringkasan program        | Profil Program                     |
| ------------------------------------------------------------- |
| [Profil Program]   [Profil Wilayah]                           |
|  +--------+         +--------+                               |
|  | icon   |         | icon   |                               |
|  | judul  |         | judul  |                               |
|  | teks   |         | teks   |                               |
|  | tombol |         | tombol |                               |
|  +--------+         +--------+                               |
+---------------------------------------------------------------+
```

Artinya:
- section ini terdiri dari 2 area besar,
- tiap area berdiri sendiri namun seimbang,
- ada judul, teks, dan tombol aksi,
- layout dibuat seperti kartu.

---

#### 1) Script mudah: struktur dasar tanpa styling

```html
<section>
  <div>
    <div>Ringkasan program</div>
    <h2>Profil Program</h2>
  </div>

  <div>
    <div>
      <div>
        <div>icon</div>
        <div>
          <div>Profil Program</div>
          <h5>Profil Ngrembaka Aksara</h5>
        </div>
      </div>

      <p>
        Program Ngrembaka Aksara lahir dari hasil survei lapangan, observasi,
        wawancara mendalam, dan FGD yang dilaksanakan bersama masyarakat Kelurahan Podorejo...
      </p>

      <a href="/profil/ngrembaka-aksara">Baca Selengkapnya</a>
    </div>

    <div>
      <div>
        <div>icon</div>
        <div>
          <div>Profil Wilayah</div>
          <h5>Profil Kelurahan Podorejo</h5>
        </div>
      </div>

      <p>
        Kelurahan Podorejo merupakan salah satu kelurahan di Kecamatan Ngaliyan,
        Kota Semarang. Luas wilayah 605,349 Ha dengan 10.188 jiwa tersebar di 12 RW dan 61 RT...
      </p>

      <a href="/profil/kelurahan-podorejo">Baca Selengkapnya</a>
    </div>
  </div>
</section>
```

Keterangan:
- `section` menjadi pembungkus utama.
- ada heading kecil di atas `Profil Program`.
- tiap card memiliki `icon`, `badge`, `judul`, `deskripsi`, dan tombol.
- pada tahap ini, kita fokus pada struktur dan urutan konten, bukan desain yang terlalu detail.

---

#### 2) Script menengah: menambahkan layout dan tata ruang

```html
<section class="section-bg py-5">
  <div class="container">
    <div class="d-flex flex-column flex-lg-row align-items-lg-end justify-content-between gap-2 mb-4">
      <div>
        <div class="section-kicker mb-2">Ringkasan program</div>
        <h2 class="section-title mb-0">Profil Program</h2>
      </div>
      <p class="text-muted mb-0" style="max-width: 44rem;">
        Program ini dirancang sebagai ekosistem literasi yang menumbuhkan kebiasaan baca,
        kreativitas, dan daya saing melalui konten yang terkurasi.
      </p>
    </div>

    <div class="row g-4">
      <div class="col-md-6">
        <div class="card card-aksara h-100 p-4 access-card">
          <div class="d-flex align-items-center gap-3 mb-3">
            <div class="icon-wrap fs-5"><i class="fa-solid fa-users"></i></div>
            <div>
              <div class="badge-aksara mb-2 d-inline-block">Profil Program</div>
              <h5 class="fw-bold mb-0" style="color: var(--color-dark);">Profil Ngrembaka Aksara</h5>
            </div>
          </div>

          <p class="text-muted small">
            Program Ngrembaka Aksara lahir dari hasil survei lapangan, observasi,
            wawancara mendalam, dan FGD yang dilaksanakan bersama masyarakat Kelurahan Podorejo...
          </p>

          <a href="/profil/ngrembaka-aksara" class="btn-aksara d-inline-block mt-auto" style="width: fit-content;">
            <i class="fa-solid fa-arrow-right me-1"></i>Baca Selengkapnya
          </a>
        </div>
      </div>

      <div class="col-md-6">
        <div class="card card-aksara h-100 p-4 access-card">
          <div class="d-flex align-items-center gap-3 mb-3">
            <div class="icon-wrap fs-5"><i class="fa-solid fa-map-location-dot"></i></div>
            <div>
              <div class="badge-aksara mb-2 d-inline-block">Profil Wilayah</div>
              <h5 class="fw-bold mb-0" style="color: var(--color-dark);">Profil Kelurahan Podorejo</h5>
            </div>
          </div>

          <p class="text-muted small">
            Kelurahan Podorejo merupakan salah satu kelurahan di Kecamatan Ngaliyan,
            Kota Semarang. Luas wilayah 605,349 Ha dengan 10.188 jiwa tersebar di 12 RW dan 61 RT...
          </p>

          <a href="/profil/kelurahan-podorejo" class="btn-aksara d-inline-block mt-auto" style="width: fit-content;">
            <i class="fa-solid fa-arrow-right me-1"></i>Baca Selengkapnya
          </a>
        </div>
      </div>
    </div>
  </div>
</section>
```

Keterangan:
- `container` membatasi lebar section agar tidak terlalu lebar.
- `row` dan `col-md-6` membuat dua card rata dengan ukuran yang seimbang.
- `d-flex` dan `gap` membuat elemen di dalam kartu terorganisir.
- `btn-aksara` memastikan tombol terasa sebagai CTA yang jelas.

Pada tahap ini, siswa sudah mulai belajar bagaimana layout grid bekerja untuk membagi area dengan rapi.

---

#### 3) Script mahir: versi final yang mirip halaman nyata

```html
<section class="section-bg py-5">
  <div class="container">
    <div class="d-flex flex-column flex-lg-row align-items-lg-end justify-content-between gap-2 mb-4">
      <div>
        <div class="section-kicker mb-2">Ringkasan program</div>
        <h2 class="section-title mb-0">Profil Program</h2>
      </div>
      <p class="text-muted mb-0" style="max-width: 44rem;">
        Program ini dirancang sebagai ekosistem literasi yang menumbuhkan kebiasaan baca,
        kreativitas, dan daya saing melalui konten yang terkurasi.
      </p>
    </div>

    <div class="row g-4">
      <div class="col-md-6">
        <div class="card card-aksara h-100 p-4 access-card">
          <div class="d-flex align-items-center gap-3 mb-3">
            <div class="icon-wrap fs-5"><i class="fa-solid fa-users"></i></div>
            <div>
              <div class="badge-aksara mb-2 d-inline-block">Profil Program</div>
              <h5 class="fw-bold mb-0" style="color: var(--color-dark);">Profil Ngrembaka Aksara</h5>
            </div>
          </div>
          <p class="text-muted small">
            Program Ngrembaka Aksara lahir dari hasil survei lapangan, observasi,
            wawancara mendalam, dan FGD yang dilaksanakan bersama masyarakat Kelurahan Podorejo.
            Tujuan utamanya adalah membangun ekosistem literasi yang melibatkan lintas generasi.
          </p>
          <a href="/profil/ngrembaka-aksara" class="btn-aksara d-inline-block mt-auto" style="width: fit-content;">
            <i class="fa-solid fa-arrow-right me-1"></i>Baca Selengkapnya
          </a>
        </div>
      </div>

      <div class="col-md-6">
        <div class="card card-aksara h-100 p-4 access-card">
          <div class="d-flex align-items-center gap-3 mb-3">
            <div class="icon-wrap fs-5"><i class="fa-solid fa-map-location-dot"></i></div>
            <div>
              <div class="badge-aksara mb-2 d-inline-block">Profil Wilayah</div>
              <h5 class="fw-bold mb-0" style="color: var(--color-dark);">Profil Kelurahan Podorejo</h5>
            </div>
          </div>
          <p class="text-muted small">
            Kelurahan Podorejo merupakan salah satu kelurahan di Kecamatan Ngaliyan, Kota Semarang.
            Dengan luas wilayah 605,349 Ha dan jumlah penduduk 10.188 jiwa, wilayah ini menjadi ruang
            strategis untuk penguatan literasi dan pemberdayaan masyarakat berbasis budaya lokal.
          </p>
          <a href="/profil/kelurahan-podorejo" class="btn-aksara d-inline-block mt-auto" style="width: fit-content;">
            <i class="fa-solid fa-arrow-right me-1"></i>Baca Selengkapnya
          </a>
        </div>
      </div>
    </div>
  </div>
</section>
```

Versi ini mencakup semua prinsip desain professional:
- content hierarchy jelas,
- visual konsisten,
- card seimbang,
- tombol CTA terlihat jelas,
- layout responsif terhadap layar.

---

#### Keterangan tutorial: dari mudah ke mahir

1. Tahap mudah
   - Fokus pada struktur konten.
   - Pastikan ada judul, deskripsi, dan tombol.
   - Gunakan 2 kartu besar agar urutannya jelas.

2. Tahap menengah
   - Tambahkan layout grid agar dua card rata dan seimbang.
   - Gunakan `d-flex` untuk menata icon, badge, dan judul di satu baris.
   - Gunakan `btn-aksara` agar CTA tampil lebih profesional.

3. Tahap mahir
   - Perhatikan spacing, padding, warna, border, shadow, dan ukuran teks.
   - Pastikan content hierarchy jelas dari atas ke bawah.
   - Sesuaikan visual agar semua card punya keseimbangan visual.

---

#### Kunci belajar

Section profil program adalah latihan penting karena menggabungkan:
- layout card,
- hierarchy teks,
- content grouping,
- dan tombol CTA.

Ini adalah dasar dari banyak halaman landing page modern, dan sangat cocok untuk dipelajari berjenjang.

---

#### Latihan praktik

Coba buat versi Anda sendiri dengan tema:
- Profil Tim
- Profil Sekolah
- Profil Komunitas

Setiap card harus berisi:
- icon,
- title,
- paragraph,
- tombol.

Tujuan:
- siswa memahami cara membuat card yang konsisten,
- memahami cara menata layout dua kolom,
- dan membangun section yang informatif namun tetap rapi.
