### 7.3 Hero Kanan (Visual / Informasi Cepat)

#### Struktur Hero Kanan sesuai referensi halaman
Hero kanan pada halaman ini bukan hanya gambar dekoratif. Ia berfungsi sebagai panel visual yang menampilkan informasi cepat dan memperkuat tema utama di sisi kiri.

Komponen utama hero kanan pada referensi halaman aktif:
- header atas: "Akses cepat" dan judul "Baca, jelajahi, dan temukan program"
- panel utama besar: area ilustrasi atau visual utama
- dua card samping: metric / informasi cepat seperti E-Library dan Pojok Literasi
- blok teks kecil: "Literasi Lintas Generasi"
- beberapa tile kecil di bawah: Modul Pembelajaran, Buku Cerita, Tunas Ngrembaka
- quote di bawah: "Tumbuh dan berkembangnya ilmu pengetahuan"

#### Desain Visual dalam tabel

| b/k | kolom1 | kolom2 | kolom3 |
|---|---|---|---|
| baris1 | Header | Icon |  |
| baris2 | Visual utama | metric 1 | metric 2 |
| baris3 | tile 1 | tile 2 | tile 3 |
| baris4 | quote |  |  |

Catatan layout:
- Hero kanan dibuat sebagai kumpulan blok yang saling melengkapi.
- Panel utama paling besar sebagai fokus visual.
- Metric kecil berada di samping untuk memberi info cepat.
- Tile kecil di bawah memperjelas kategori program.

---

#### Struktur HTML yang sesuai dengan referensi

Berikut struktur inti yang kira-kira sama dengan halaman referensi.

```html
<div class="hero-cover">
  <div class="cover-header d-flex align-items-center justify-content-between">
    <div>
      <div class="section-kicker text-white-50">Akses cepat</div>
      <h2 class="h4 fw-bold mb-0 text-white">Baca, jelajahi, dan temukan program</h2>
    </div>
    <div class="icon-wrap fs-4 bg-white">
      <i class="fa-solid fa-book-open-reader"></i>
    </div>
  </div>

  <div class="cover-body">
    <div class="cover-art">
      <div class="cover-visual">
        <div class="visual-badge"><i class="fa-solid fa-circle-play"></i> Portal Literasi</div>
        <div class="visual-title">Baca lebih mudah</div>
        <p class="visual-sub">
          Koleksi belajar, program, dan pojok literasi dalam satu ruang yang rapi, ringan, dan mudah dijelajahi.
        </p>
        <div class="visual-chiprow">
          <span class="visual-chip">E-Library</span>
          <span class="visual-chip">Pojok Literasi</span>
          <span class="visual-chip">Artikel</span>
        </div>
      </div>

      <div class="cover-side">
        <div class="hero-metric h-100">
          <div class="label">E-Library</div>
          <div class="value">{{ elibrary_total }} artikel</div>
        </div>
        <div class="hero-metric h-100">
          <div class="label">Pojok Literasi</div>
          <div class="value">{{ pojok_total }} artikel</div>
        </div>
        <div class="side-block">
          <div class="side-title">Literasi Lintas Generasi</div>
          <div class="side-meta">Tumbuh cerdas, mandiri, dan berdaya lewat bacaan yang berkelanjutan.</div>
        </div>
      </div>
    </div>

    <div class="book-stack">
      <div class="book-tile">
        <div class="mini-title">Modul Pembelajaran</div>
        <div class="mini-meta">Materi belajar utama dan panduan pembaca</div>
      </div>
      <div class="book-tile">
        <div class="mini-title">Buku Cerita</div>
        <div class="mini-meta">Cerita lokal, karakter, dan imajinasi</div>
      </div>
      <div class="book-tile">
        <div class="mini-title">Tunas Ngrembaka</div>
        <div class="mini-meta">Literasi anak, numerasi, dan budaya</div>
      </div>
    </div>

    <div class="hero-quote">
      "Tumbuh dan berkembangnya ilmu pengetahuan"
    </div>
  </div>
</div>
```

Penjelasan struktur:
- `.hero-cover` = kartu besar yang menjadi panel kanan hero
- `.cover-header` = bagian atas dengan teks dan ikon
- `.cover-art` = area visual utama yang berisi teks dan chips
- `.cover-side` = kolom samping berisi dua metric dan satu blok informasi
- `.book-stack` = kumpulan tile kecil yang menunjukkan kategori konten
- `.hero-quote` = kalimat penutup yang memberi feel edukasi dan inspiratif

---

#### Implementasi CSS yang mirip dengan referensi

```css
.hero-cover {
  position: relative;
  background: linear-gradient(180deg, rgba(19,48,26,0.95), rgba(25,58,34,0.9));
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 1.5rem;
  padding: 1.25rem;
  box-shadow: 0 30px 50px rgba(13, 29, 18, 0.18);
}

.cover-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 1rem;
}

.icon-wrap {
  width: 52px;
  height: 52px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255,255,255,0.9);
  color: var(--color-dark);
}

.cover-body {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.cover-art {
  display: grid;
  grid-template-columns: 1.5fr 1fr;
  gap: 0.85rem;
}

.cover-visual {
  background: linear-gradient(160deg, rgba(255,255,255,0.13), rgba(255,255,255,0.04));
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 1.2rem;
  padding: 1rem;
  min-height: 220px;
}

.visual-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  background: rgba(255,255,255,0.08);
  color: #ebf7ec;
  padding: 0.35rem 0.7rem;
  border-radius: 999px;
  font-size: 0.72rem;
  font-weight: 700;
}

.visual-title {
  margin-top: 1rem;
  font-size: 1.5rem;
  font-weight: 800;
  color: #ffffff;
}

.visual-sub {
  margin-top: 0.75rem;
  color: rgba(255,255,255,0.82);
  line-height: 1.6;
  font-size: 0.95rem;
}

.visual-chiprow {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 1rem;
}

.visual-chip {
  display: inline-block;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.08);
  color: #ebf7ec;
  border-radius: 999px;
  padding: 0.38rem 0.7rem;
  font-size: 0.72rem;
}

.cover-side {
  display: grid;
  gap: 0.75rem;
}

.hero-metric {
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 1rem;
  padding: 0.9rem 1rem;
  color: #ffffff;
}

.hero-metric .label {
  font-size: 0.72rem;
  color: rgba(255,255,255,0.72);
  margin-bottom: 0.4rem;
}

.hero-metric .value {
  font-size: 1.05rem;
  font-weight: 700;
}

.side-block {
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 1rem;
  padding: 0.9rem 1rem;
  color: #ffffff;
}

.side-title {
  font-size: 0.82rem;
  font-weight: 700;
  margin-bottom: 0.45rem;
  color: #dff4e1;
}

.side-meta {
  color: rgba(255,255,255,0.76);
  line-height: 1.5;
  font-size: 0.8rem;
}

.book-stack {
  display: grid;
  gap: 0.7rem;
}

.book-tile {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 0.9rem;
  padding: 0.8rem 0.9rem;
  color: #ffffff;
}

.mini-title {
  font-size: 0.82rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
}

.mini-meta {
  font-size: 0.72rem;
  color: rgba(255,255,255,0.7);
  line-height: 1.5;
}

.hero-quote {
  background: rgba(255,255,255,0.04);
  border-left: 3px solid rgba(255,255,255,0.45);
  padding: 0.8rem 0.9rem;
  color: rgba(255,255,255,0.82);
  font-style: italic;
  border-radius: 0.6rem;
}

@media (max-width: 991px) {
  .cover-art {
    grid-template-columns: 1fr;
  }

  .cover-side {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .side-block {
    grid-column: 1 / -1;
  }
}
```

---

#### Keterangan CSS berdasarkan referensi

1. Header hero kanan
- `display: flex; justify-content: space-between;` membuat judul dan ikon terpisah secara rapi.
- `icon-wrap` dibuat kotak kecil supaya ada elemen visual pendukung yang relevan dengan tema buku.

2. Panel utama visual
- `background: linear-gradient(...)` memberi efek gelap yang berani tapi tetap premium.
- `border-radius` membuat panel bulat dan modern.
- `box-shadow` menambah efek kedalaman sehingga panel terlihat lebih menonjol.

3. Grid di dalam cover
- `grid-template-columns: 1.5fr 1fr;` membuat area visual utama lebih lebar dari area informasi samping.
- ketika layar kecil, grid berubah menjadi satu kolom agar tetap rapi.

4. Metric card
- `hero-metric` dibuat mirip dengan kartu informasi statis, seperti E-Library dan Pojok Literasi.
- `value` dibuat lebih besar agar terlihat sebagai angka penting.

5. Tile kategori
- `book-stack` menampilkan tiga item kategori di bawah visual utama.
- masing-masing `book-tile` ringkas, mudah dibaca, dan membantu pengguna langsung mengenali program.

6. Quote
- `hero-quote` dibuat dengan border kiri dan italic untuk memberi nilai branding dan estetika editorial.

---

#### Kenapa struktur ini lebih cocok dengan halaman yang aktif?
Karena referensi halaman ini bukan hanya menampilkan satu ilustrasi sederhana, tetapi menggabungkan beberapa pola desain yang sering dipakai di landing page modern:
- header info,
- visual utama,
- card statistik,
- blok kategori,
- dan elemen support text.

Jadi, cara belajar yang benar adalah bukan hanya membuat kotak besar, tetapi memahami bagaimana beberapa blok kecil bekerja bersama untuk membentuk satu panel yang kuat.

---

#### Langkah belajar bertahap

1. Buat container utama `hero-cover`.
2. Buat `cover-header` untuk judul dan ikon.
3. Buat `cover-art` dan `cover-side` agar visual utama dan informasi samping terpisah.
4. Tambahkan `book-stack` untuk kategori program.
5. Tambahkan `hero-quote` untuk memperkuat citra edukasi.
6. Gunakan media query agar layout tetap rapi di mobile.

---

#### Ringkasan singkat
Hero kanan yang terlihat di referensi ini adalah contoh panel informasi visual yang dibuat dari beberapa elemen kecil yang digabung menjadi satu blok besar. Struktur utamanya:
- header,
- visual utama,
- metric samping,
- list kategori,
- quote final.

Ini adalah pola yang bagus untuk belajar layout landing page karena menunjukkan bagaimana desain web bukan hanya soal satu elemen, tetapi soal komposisi dan keseimbangan antar blok.

---

#### Latihan kecil
Coba buat versi sendiri dari hero kanan dengan tema berikut:
- header: "Akses cepat"
- judul: "Baca, jelajahi, dan temukan program"
- visual utama: area putih/green dengan teks singkat
- metric: "E-Library", "Pojok Literasi"
- card bawah: "Modul Pembelajaran", "Buku Cerita", "Tunas Ngrembaka"

Tujuan latihan:
- menjaga layout tetap seimbang,
- membedakan area visual utama dan informasi pendukung,
- memahami bahwa setiap blok harus punya fungsi, bukan sekadar dekorasi.
