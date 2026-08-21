### 7.5 Section Kenapa Terasa Mudah

#### Struktur Section
Section ini menekankan nilai utama dari portal yang sedang dibangun: "mudah diakses, mudah dipahami, dan cocok untuk banyak kalangan." Bagian ini biasanya berisi 3 kolom fitur utama, masing-masing menjelaskan alasan portal terasa mudah digunakan.

Komponen utama section ini:
- Kicker: "Kenapa terasa mudah"
- Judul: "Portal yang fokus pada akses belajar"
- 3 kartu fitur:
  - Akses cepat
  - Koleksi tertata
  - Lintas generasi

#### Desain Visual dalam tabel

| b/k | kolom1 | kolom2 | kolom3 |
|---|---|---|---|
| baris1 | Kicker + Judul |  |  |
| baris2 | Akses cepat | Koleksi tertata | Lintas generasi |

Catatan layout:
- Judul berada di atas agar pembaca langsung tahu tema section.
- Tiga kartu fitur dibuat sejajar agar mudah dibaca.
- Setiap kartu berisi ikon, judul, dan deskripsi singkat.

---

#### Implementasi HTML tanpa CSS

```html
<section>
  <div>
    <div>Kenapa terasa mudah</div>
    <h2>Portal yang fokus pada akses belajar</h2>

    <div>
      <div>
        <div>ikon</div>
        <h6>Akses cepat</h6>
        <p>Semua katalog, program, dan materi belajar dibawa ke satu halaman yang ringan dan mudah dijelajahi.</p>
      </div>

      <div>
        <div>ikon</div>
        <h6>Koleksi tertata</h6>
        <p>Setiap kategori memiliki struktur jelas agar pengguna baru bisa langsung menemukan materi yang dibutuhkan.</p>
      </div>

      <div>
        <div>ikon</div>
        <h6>Lintas generasi</h6>
        <p>Portal ini dibuat untuk anak, orang tua, guru, dan pendamping belajar agar membaca tetap menyenangkan.</p>
      </div>
    </div>
  </div>
</section>
```

Keterangan dasar HTML:
- `<section>`: membungkus seluruh bagian fitur.
- `div` pertama: wrapper utama.
- tiga `div` yang berurutan: masing-masing adalah kartu fitur.
- `h6`: judul fitur.
- `p`: penjelasan singkat.
- ikon bisa dibuat dengan emoji, Font Awesome, atau elemen bentuk sederhana.

---

#### Versi HTML yang mirip halaman referensi

```html
<section class="section-white py-5">
  <div class="container">
    <div class="d-flex flex-column flex-lg-row align-items-lg-end justify-content-between gap-2 mb-4">
      <div>
        <div class="section-kicker mb-2">Kenapa terasa mudah</div>
        <h2 class="section-title mb-0">Portal yang fokus pada akses belajar</h2>
      </div>
    </div>

    <div class="row g-4">
      <div class="col-md-4">
        <div class="card card-aksara mini-feature-card h-100 p-4">
          <div class="icon-wrap mb-3"><i class="fa-solid fa-bolt"></i></div>
          <h6 class="fw-bold mb-2" style="color: var(--color-dark);">Akses cepat</h6>
          <p class="text-muted small mb-0">
            Semua katalog, program, dan materi belajar dibawa ke satu halaman yang ringan dan mudah dijelajahi.
          </p>
        </div>
      </div>

      <div class="col-md-4">
        <div class="card card-aksara mini-feature-card h-100 p-4">
          <div class="icon-wrap mb-3"><i class="fa-solid fa-layer-group"></i></div>
          <h6 class="fw-bold mb-2" style="color: var(--color-dark);">Koleksi tertata</h6>
          <p class="text-muted small mb-0">
            Setiap kategori memiliki struktur jelas agar pengguna baru bisa langsung menemukan materi yang dibutuhkan.
          </p>
        </div>
      </div>

      <div class="col-md-4">
        <div class="card card-aksara mini-feature-card h-100 p-4">
          <div class="icon-wrap mb-3"><i class="fa-solid fa-seedling"></i></div>
          <h6 class="fw-bold mb-2" style="color: var(--color-dark);">Lintas generasi</h6>
          <p class="text-muted small mb-0">
            Portal ini dibuat untuk anak, orang tua, guru, dan pendamping belajar agar membaca tetap menyenangkan.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>
```

Penjelasan struktur:
- `section-white` = background yang berbeda agar section terpisah dari area sebelumnya.
- `row g-4` = membuat 3 kartu rata dan berjarak.
- `col-md-4` = setiap kartu mengambil 1/3 lebar layar pada desktop.
- `card` = wadah kartu fitur.
- `icon-wrap` = area untuk ikon.

---

#### Implementasi CSS

```css
.section-white {
  background: #ffffff;
}

.mini-feature-card {
  border-radius: 1.25rem;
  border: 1px solid rgba(18, 48, 26, 0.08);
  background: #ffffff;
  box-shadow: 0 14px 28px rgba(18, 48, 26, 0.05);
}

.icon-wrap {
  width: 52px;
  height: 52px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #edf7ee;
  color: #12301a;
  font-size: 1.2rem;
}

.mini-feature-card h6 {
  font-size: 1rem;
  color: var(--color-dark);
}

.mini-feature-card p {
  line-height: 1.7;
}

@media (max-width: 767px) {
  .mini-feature-card {
    text-align: center;
  }

  .icon-wrap {
    margin-left: auto;
    margin-right: auto;
  }
}
```

---

#### Keterangan CSS per bagian

1. `section-white`
- background putih membuat section terasa bersih dan jelas.
- section yang berbeda background sering dipakai untuk membagi topik dalam landing page.

2. `mini-feature-card`
- border radius memberi bentuk yang modern.
- box-shadow membuat kartu terlihat lebih menonjol tapi tetap ringan.
- border tipis menjaga kesan elegan dan rapi.

3. `icon-wrap`
- kotak ikon dibuat agar visual terasa lebih konsisten.
- warna hijau lembut memberi kesan ramah dan edukatif.

4. `mini-feature-card p`
- `line-height: 1.7` membuat paragraf lebih nyaman dibaca.
- `text-muted` bisa diatur lagi sesuai warna tema.

5. Responsif
- pada mobile, ikon dan teks dapat dipusatkan agar lebih nyaman di layar kecil.

---

#### Mengapa tiga fitur ini penting?
Section ini menjelaskan alasan utama website terasa mudah digunakan. Alasan itu dijabarkan dalam 3 bentuk:
- Akses cepat: semua informasi mudah ditemukan.
- Koleksi tertata: kategori dibuat jelas dan terstruktur.
- Lintas generasi: situs bisa dipakai oleh anak, orang tua, guru, dan pendamping.

Artinya, section ini bukan sekadar menampilkan ikon. Ia mengomunikasikan nilai produk kepada pengguna.

---

#### Langkah belajar bertahap

1. Buat section dengan judul dan subjudul.
2. Buat 3 kartu fitur sebaris.
3. Isi tiap kartu dengan ikon, judul, dan satu paragraf penjelasan.
4. Atur spacing agar rapi dan seimbang.
5. Tambahkan media query agar layout tetap bagus di mobile.
6. Gunakan warna yang konsisten dengan brand.

---

#### Ringkasan singkat
Section "Kenapa terasa mudah" adalah pola yang sangat penting dalam landing page karena ia menjawab pertanyaan: "Kenapa website ini berguna bagi saya?"

Dengan 3 kartu fitur, kita bisa menampilkan nilai utama tanpa membuat halaman terasa terlalu panjang atau terlalu padat.

---

#### Latihan kecil
Coba buat versi section fitur Anda sendiri dengan tema berikut:
- Akses mudah
- Konten relevan
- Belajar sesuai kebutuhan

Masing-masing kartu harus berisi:
- ikon,
- judul,
- deskripsi singkat,
- dan warna yang konsisten.

Tujuan latihan:
- membuat kartu yang memiliki fungsi jelas,
- menjaga desain tetap rapi,
- dan belajar bagaimana menulis value proposition dalam layout web.
