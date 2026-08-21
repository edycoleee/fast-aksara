### 7.8 Section Katalog Buku

#### Tujuan section
Section katalog buku berfungsi untuk menampilkan koleksi konten dalam bentuk card atau item yang rapi. Tujuan utamanya adalah membantu user melihat kategori utama dari website dengan cepat, lalu memilih konten yang ingin dibaca.

Pada halaman referensi, katalog buku biasanya berisi:
- judul section,
- deskripsi singkat,
- beberapa card kategori,
- tiap card berisi ikon, judul, jumlah artikel, deskripsi, dan tombol lihat koleksi.

---

#### Konsep dasar katalog buku

Katalog buku adalah kombinasi antara:
- HTML untuk membuat daftar card,
- CSS untuk mengatur layout dan styling,
- JavaScript untuk interaksi jika diperlukan, misalnya hover, filter, atau tombol lanjut.

Secara umum, sebuah item katalog buku memiliki struktur:
- ikon
- label jumlah artikel
- judul
- deskripsi singkat
- tombol atau link ke halaman detail

---

#### 1) Script mudah: HTML dasar tanpa styling

```html
<section>
  <div>
    <div>Katalog unggulan</div>
    <h2>Buku terpilih untuk mulai membaca</h2>
    <p>Section ini menonjolkan koleksi dan program yang paling dekat dengan kebutuhan pembaca.</p>
  </div>

  <div>
    <div>
      <div>1 artikel</div>
      <h3>Modul Pembelajaran</h3>
      <p>Koleksi materi belajar utama untuk pembaca muda dan pendamping belajar.</p>
      <a href="/elibrary/modul-pembelajaran">Lihat koleksi</a>
    </div>

    <div>
      <div>0 artikel</div>
      <h3>Buku Cerita</h3>
      <p>Ruang baca untuk cerita anak, budaya lokal, dan imajinasi yang tumbuh.</p>
      <a href="/elibrary/buku-cerita">Lihat koleksi</a>
    </div>

    <div>
      <div>2 artikel</div>
      <h3>Tunas Ngrembaka</h3>
      <p>Program literasi dasar untuk balita dan anak-anak dengan pendekatan bermain.</p>
      <a href="/pojok-literasi/tunas">Lihat program</a>
    </div>
  </div>
</section>
```

Keterangan:
- HTML dasar sudah dapat menampilkan katalog yang mudah dibaca.
- tiap card dibagi menurut kategori,
- tiap item punya judul, deskripsi, dan tombol.

Tujuan tahap ini:
- siswa memahami struktur item katalog,
- memahami urutan tiap bagian dalam card.

---

#### 2) Script menengah: HTML + CSS untuk layout card yang rapi

```html
<section class="catalog-wrap">
  <div class="container">
    <div class="catalog-header">
      <div class="section-kicker">Katalog unggulan</div>
      <h2 class="section-title">Buku terpilih untuk mulai membaca</h2>
      <p>Section ini menonjolkan koleksi dan program yang paling dekat dengan kebutuhan pembaca.</p>
    </div>

    <div class="catalog-grid">
      <article class="catalog-card">
        <div class="catalog-meta">1 artikel</div>
        <h3>Modul Pembelajaran</h3>
        <p>Koleksi materi belajar utama untuk pembaca muda dan pendamping belajar.</p>
        <a href="/elibrary/modul-pembelajaran">Lihat koleksi</a>
      </article>

      <article class="catalog-card">
        <div class="catalog-meta">0 artikel</div>
        <h3>Buku Cerita</h3>
        <p>Ruang baca untuk cerita anak, budaya lokal, dan imajinasi yang tumbuh.</p>
        <a href="/elibrary/buku-cerita">Lihat koleksi</a>
      </article>

      <article class="catalog-card">
        <div class="catalog-meta">2 artikel</div>
        <h3>Tunas Ngrembaka</h3>
        <p>Program literasi dasar untuk balita dan anak-anak dengan pendekatan bermain.</p>
        <a href="/pojok-literasi/tunas">Lihat program</a>
      </article>
    </div>
  </div>
</section>
```

```css
.catalog-wrap {
  padding: 4rem 0;
  background: #f7faf7;
}

.catalog-header {
  margin-bottom: 2rem;
}

.catalog-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1.5rem;
}

.catalog-card {
  background: #ffffff;
  border: 1px solid rgba(18, 48, 26, 0.08);
  border-radius: 1.2rem;
  padding: 1.25rem;
  box-shadow: 0 10px 22px rgba(18, 48, 26, 0.04);
}

.catalog-meta {
  display: inline-block;
  background: #edf7ee;
  color: #12301a;
  border-radius: 999px;
  padding: 0.35rem 0.7rem;
  font-size: 0.72rem;
  font-weight: 700;
  margin-bottom: 0.8rem;
}

.catalog-card h3 {
  margin: 0 0 0.6rem;
  color: #12301a;
}

.catalog-card p {
  color: #53665d;
  line-height: 1.7;
}

.catalog-card a {
  display: inline-block;
  margin-top: 0.75rem;
  font-weight: 700;
  color: #12301a;
  text-decoration: none;
}

@media (max-width: 767px) {
  .catalog-grid {
    grid-template-columns: 1fr;
  }
}
```

Keterangan:
- `grid-template-columns: repeat(3, ...)` membuat 3 card sejajar di desktop.
- `catalog-card` dibuat dengan border, radius, dan shadow agar tampil seperti card modern.
- `catalog-meta` berfungsi sebagai label jumlah artikel.
- pada mobile, layout berubah menjadi satu kolom agar nyaman dibaca.

Tujuan tahap ini:
- siswa belajar membuat layout katalog dengan grid,
- memahami spacing dan ukuran card,
- melihat pentingnya keteraturan visual dalam website.

---

#### 3) Script mahir: HTML + CSS + JavaScript final yang mirip halaman nyata

```html
<section class="catalog-wrap">
  <div class="container">
    <div class="d-flex flex-column flex-lg-row align-items-lg-end justify-content-between gap-2 mb-4">
      <div>
        <div class="section-kicker mb-2">Katalog unggulan</div>
        <h2 class="section-title mb-0">Buku terpilih untuk mulai membaca</h2>
      </div>
      <p class="text-muted mb-0" style="max-width: 42rem;">
        Section ini menonjolkan koleksi dan program yang paling dekat dengan kebutuhan pembaca.
      </p>
    </div>

    <div class="catalog-grid">
      <article class="catalog-card">
        <div class="catalog-header-row">
          <div class="catalog-ico"><i class="fa-solid fa-book-open"></i></div>
          <span class="catalog-meta">1 artikel</span>
        </div>
        <h3>Modul Pembelajaran</h3>
        <p>Koleksi materi belajar utama untuk pembaca muda dan pendamping belajar.</p>
        <a href="/elibrary/modul-pembelajaran">
          Lihat koleksi <i class="fa-solid fa-arrow-right"></i>
        </a>
      </article>

      <article class="catalog-card">
        <div class="catalog-header-row">
          <div class="catalog-ico"><i class="fa-solid fa-book"></i></div>
          <span class="catalog-meta">0 artikel</span>
        </div>
        <h3>Buku Cerita</h3>
        <p>Ruang baca untuk cerita anak, budaya lokal, dan imajinasi yang tumbuh.</p>
        <a href="/elibrary/buku-cerita">
          Lihat koleksi <i class="fa-solid fa-arrow-right"></i>
        </a>
      </article>

      <article class="catalog-card">
        <div class="catalog-header-row">
          <div class="catalog-ico"><i class="fa-solid fa-seedling"></i></div>
          <span class="catalog-meta">2 artikel</span>
        </div>
        <h3>Tunas Ngrembaka</h3>
        <p>Program literasi dasar untuk balita dan anak-anak dengan pendekatan bermain.</p>
        <a href="/pojok-literasi/tunas">
          Lihat program <i class="fa-solid fa-arrow-right"></i>
        </a>
      </article>
    </div>
  </div>
</section>
```

```css
.catalog-wrap {
  padding: 4rem 0;
  background: #f7faf7;
}

.catalog-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1.5rem;
}

.catalog-card {
  position: relative;
  background: #ffffff;
  border: 1px solid rgba(18, 48, 26, 0.08);
  border-radius: 1.25rem;
  padding: 1.25rem;
  box-shadow: 0 16px 30px rgba(18, 48, 26, 0.05);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.catalog-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 18px 34px rgba(18, 48, 26, 0.08);
}

.catalog-header-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  margin-bottom: 0.8rem;
}

.catalog-ico {
  width: 42px;
  height: 42px;
  border-radius: 12px;
  background: #edf7ee;
  color: #12301a;
  display: flex;
  align-items: center;
  justify-content: center;
}

.catalog-meta {
  display: inline-block;
  padding: 0.35rem 0.7rem;
  border-radius: 999px;
  font-size: 0.72rem;
  font-weight: 700;
  background: #edf7ee;
  color: #12301a;
}

.catalog-card h3 {
  margin: 0 0 0.7rem;
  color: #12301a;
  font-size: 1.3rem;
}

.catalog-card p {
  color: #53665d;
  line-height: 1.7;
  margin-bottom: 1rem;
}

.catalog-card a {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: #12301a;
  text-decoration: none;
  font-weight: 700;
}

.catalog-card a:hover {
  text-decoration: underline;
}

@media (max-width: 767px) {
  .catalog-grid {
    grid-template-columns: 1fr;
  }
}
```

```javascript
const catalogCards = document.querySelectorAll('.catalog-card');

catalogCards.forEach((card) => {
  card.addEventListener('mouseenter', () => {
    card.style.transform = 'translateY(-4px)';
  });

  card.addEventListener('mouseleave', () => {
    card.style.transform = 'translateY(0)';
  });
});
```

Keterangan final:
- `hover` effect memberi feedback visual saat user mengarahkan mouse.
- JavaScript menambahkan interaksi sederhana yang membuat card terasa hidup.
- layout grid membuat katalog mudah dibaca.
- tiap card tetap fokus pada fungsi: memberi info dan mengarahkan user ke halaman detail.

---

#### Mengapa section katalog buku penting?
Katalog buku adalah bagian yang paling penting setelah user memahami apa website itu. Bagian ini membantu user untuk:
- melihat kategori utama,
- memilih konten yang paling relevan,
- memahami ruang belajar yang ada,
- dan memulai aktivitas membaca dengan cepat.

Jadi, katalog buku bukan sekadar daftar. Ia adalah navigasi menuju konten.

---

#### Tutorial belajar dari mudah ke mahir

1. Tahap mudah
   - buat struktur dasar item katalog,
   - susun 3 kartu secara berurutan,
   - pastikan tiap card punya judul dan link.

2. Tahap menengah
   - atur grid agar card dibuat berurutan dan rapi,
   - tambahkan label jumlah artikel,
   - berikan jarak dan style agar card tampil lebih modern.

3. Tahap mahir
   - tambahkan hover effect,
   - berikan ikon pada header card,
   - gunakan JavaScript agar card terasa lebih interaktif.

---

#### Kunci pembelajaran

Section katalog buku membantu siswa memahami beberapa konsep penting:
- grid layout,
- reusable card component,
- hover state,
- dan navigation link.

Ini adalah pola yang sering digunakan di banyak website modern, termasuk e-commerce, portal berita, dan aplikasi edukasi.

---

#### Latihan kecil
Coba buat katalog dengan tema berikut:
- Kategori Buku
- Kategori Program
- Kategori Kegiatan

Setiap card harus memiliki:
- ikon,
- judul,
- jumlah item,
- deskripsi,
- tombol lihat lebih lanjut.

Tujuan latihan:
- siswa belajar membuat card reusable,
- menerapkan grid layout,
- dan membuat section katalog yang berfungsi sebagai navigasi konten.
