### 7.4 Section Buku untuk Semua

#### Struktur Section
Section ini berfungsi sebagai pembuktian bahwa portal ini tidak hanya indah secara visual, tetapi juga punya nilai manfaat nyata. Bagian ini menampilkan pesan utama: portal ini memudahkan akses belajar di mana pun dan kapan pun.

Komponen utama section ini:
- Kicker: "Buku untuk semua"
- Judul: "Akses di mana pun, kapan pun"
- Deskripsi panjang: menjelaskan bahwa portal adalah pintu masuk ke koleksi belajar, pojok literasi, dan program yang terintegrasi
- Statistik ringkas:
  - Koleksi E-Library: {{ elibrary_total }}
  - Pojok Literasi: {{ pojok_total }}
  - Program Inti: 4
  - Kategori Buku: 5

#### Desain Visual dalam tabel

| b/k | kolom1 | kolom2 |
|---|---|---|
| baris1 | Kicker + Judul + Deskripsi | Statistik 4 kotak |

Catatan layout:
- Sisi kiri berisi narasi utama.
- Sisi kanan berisi angka-angka penting untuk menegaskan skala dan manfaat.
- Kombinasi ini membuat section terasa seimbang: ada teks dan ada bukti data.

---

#### Implementasi HTML tanpa CSS

```html
<section>
  <div>
    <div>
      <div>Buku untuk semua</div>
      <h2>Akses di mana pun, kapan pun</h2>
      <p>
        Ngrembaka Aksara merangkum koleksi belajar, pojok literasi lintas usia,
        dan konten program dalam satu portal yang ringan dan mudah dijelajahi.
      </p>
    </div>

    <div>
      <div>
        <div>Koleksi E-Library</div>
        <div>{{ elibrary_total }}</div>
      </div>
      <div>
        <div>Pojok Literasi</div>
        <div>{{ pojok_total }}</div>
      </div>
      <div>
        <div>Program Inti</div>
        <div>4</div>
      </div>
      <div>
        <div>Kategori Buku</div>
        <div>5</div>
      </div>
    </div>
  </div>
</section>
```

Keterangan dasar HTML:
- `<section>`: membungkus satu bagian penting dari halaman.
- `div` pertama: container utama untuk bagian ini.
- `h2`: judul utama section.
- `p`: paragraf deskripsi.
- Elemen angka di sisi kanan dibuat dalam bentuk kotak kecil agar lebih mudah dibaca.

---

#### Versi HTML yang mirip halaman referensi

```html
<section class="py-4">
  <div class="container">
    <div class="card card-soft p-4 p-lg-5">
      <div class="row g-4 align-items-center">
        <div class="col-lg-7">
          <div class="section-kicker mb-2">Buku untuk semua</div>
          <h2 class="section-title mb-3">Akses di mana pun, kapan pun</h2>
          <p class="mb-0 text-muted" style="max-width: 42rem;">
            Ngrembaka Aksara merangkum koleksi belajar, pojok literasi lintas usia,
            dan konten program dalam satu portal yang ringan dan mudah dijelajahi.
          </p>
        </div>

        <div class="col-lg-5">
          <div class="row g-3">
            <div class="col-6 col-md-3 col-lg-6">
              <div class="hero-metric h-100">
                <div class="label">Koleksi E-Library</div>
                <div class="value">{{ elibrary_total }}</div>
              </div>
            </div>
            <div class="col-6 col-md-3 col-lg-6">
              <div class="hero-metric h-100">
                <div class="label">Pojok Literasi</div>
                <div class="value">{{ pojok_total }}</div>
              </div>
            </div>
            <div class="col-6 col-md-3 col-lg-6">
              <div class="hero-metric h-100">
                <div class="label">Program Inti</div>
                <div class="value">4</div>
              </div>
            </div>
            <div class="col-6 col-md-3 col-lg-6">
              <div class="hero-metric h-100">
                <div class="label">Kategori Buku</div>
                <div class="value">5</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

Penjelasan struktur:
- `col-lg-7` = area kiri yang lebih lebar untuk teks
- `col-lg-5` = area kanan untuk data statistik
- `row g-3` = grid kecil berisi 4 kotak kecil
- `hero-metric` = kelas khusus untuk card angka

---

#### Implementasi CSS

```css
.card-soft {
  background: #f7faf7;
  border: 1px solid rgba(18, 48, 26, 0.08);
  border-radius: 1.5rem;
  box-shadow: 0 12px 28px rgba(18, 48, 26, 0.05);
}

.section-kicker {
  color: #4f7a4e;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  font-size: 0.75rem;
}

.section-title {
  color: #12301a;
  font-size: clamp(1.8rem, 3vw, 2.8rem);
  font-weight: 800;
  line-height: 1.2;
}

.hero-metric {
  background: linear-gradient(180deg, #ffffff, #eef6ee);
  border: 1px solid rgba(18, 48, 26, 0.08);
  border-radius: 1rem;
  padding: 1rem;
  text-align: center;
}

.hero-metric .label {
  font-size: 0.72rem;
  color: #5e7862;
  margin-bottom: 0.4rem;
  line-height: 1.5;
}

.hero-metric .value {
  font-size: 1.5rem;
  font-weight: 800;
  color: #12301a;
}

@media (max-width: 991px) {
  .hero-metric {
    min-height: 120px;
  }
}
```

---

#### Keterangan CSS per bagian

1. `card-soft`
- memberi latar putih lembut agar section terlihat terpisah dari background utama.
- border tipis membuat section terlihat rapi.
- box-shadow memberi kesan ringan tetapi clean.

2. `section-kicker`
- biasanya digunakan untuk label kecil di bagian atas.
- huruf kapital dan letter spacing membuat label tampak seperti kategori atau label yang formal.

3. `section-title`
- ukuran besar agar judul langsung terlihat sebagai fokus.
- `line-height: 1.2` agar judul nyaman dibaca.

4. `hero-metric`
- dibuat dengan latar terang agar tampak seperti kartu statistik.
- angka besar di tengah memudahkan pembaca menangkap informasi penting.
- `text-align: center` membuat card terlihat lebih rapi dan fokus.

5. Responsif
- ketika layar mengecil, ukuran card tetap masuk ke grid dan tidak terlalu sempit.
- ini penting karena section ini biasanya dibaca dari mobile.

---

#### Mengapa section ini penting?
Section ini berperan sebagai bukti bahwa website bukan hanya tampilan, tetapi juga punya data yang valid. Data seperti jumlah artikel, program, dan kategori berfungsi untuk:
- menegaskan skala program,
- menunjukkan aktivitas nyata,
- memberi rasa percaya diri kepada pengguna,
- dan membuat halaman terasa lebih profesional.

Ini adalah pola yang umum dipakai di landing page modern: teks + data = tampilan yang kuat.

---

#### Langkah belajar bertahap

1. Buat section dengan dua kolom.
2. Kolom kiri berisi judul dan deskripsi.
3. Kolom kanan berisi 4 kartu angka.
4. Beri background putih lembut agar tampak terpisah.
5. Sesuaikan ukuran font dan margin agar lebih rapi.
6. Atur responsif untuk mobile agar kartu tetap rapi.

---

#### Ringkasan singkat
Section "Buku untuk semua" adalah contoh bagian landing page yang menggabungkan:
- narasi manfaat,
- bukti data,
- dan visual statis yang mudah dibaca.

Fungsi utamanya adalah memberi kejelasan: portal ini tidak hanya informatif, tetapi juga aktif, terstruktur, dan cukup luas untuk kebutuhan pembaca.

---

#### Latihan kecil
Coba buat section serupa dengan tema berikut:
- Kicker: "Belajar untuk semua"
- Judul: "Belajar lebih mudah, lebih cepat, lebih terarah"
- Deskripsi: singkat tentang program belajar digital
- Statistik: jumlah modul, mentor, kelas, dan proyek

Tujuan latihan:
- bangun section dengan 2 bagian utama,
- pastikan teks tetap jelas,
- dan buat 4 statistik yang rapi dan konsisten.

Latihan ini melatih kemampuan Anda dalam membangun section yang seimbang antara narasi dan data.
