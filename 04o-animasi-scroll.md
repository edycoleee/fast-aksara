### 04o - Animasi Scroll

#### Tujuan section
Animasi scroll membuat halaman terasa hidup saat pengguna bergerak dari atas ke bawah.

Manfaatnya:
- meningkatkan fokus pengguna,
- membuat transisi antar section lebih halus,
- menonjolkan konten penting saat masuk viewport.

---

#### Konsep dasar animasi scroll
Alur paling umum:
1. Elemen diberi class awal (masih tersembunyi atau bergeser).
2. Saat elemen masuk area layar, class aktif ditambahkan.
3. CSS transition menjalankan animasi.

Di versi mahir, JavaScript memakai `IntersectionObserver` agar performa lebih baik.

---

#### 1) Script mudah: HTML dasar

```html
<section>
  <h2>Animasi Scroll Dasar</h2>
  <p>Scroll halaman untuk melihat bagian muncul satu per satu.</p>

  <div>Card 1 - Konten pertama</div>
  <div>Card 2 - Konten kedua</div>
  <div>Card 3 - Konten ketiga</div>
</section>
```

Keterangan:
- Tahap awal hanya menyiapkan elemen yang nanti dianimasikan.
- Fokusnya mengenali bagian mana yang akan diberi efek.

Tujuan tahap ini:
- memahami elemen target animasi,
- membiasakan membagi konten ke dalam blok.

---

#### 2) Script menengah: HTML + CSS

```html
<section class="scroll-demo">
  <h2>Animasi Scroll Dasar</h2>
  <p>Scroll halaman untuk melihat card bergerak masuk.</p>

  <div class="reveal-card">Card 1 - Konten pertama</div>
  <div class="reveal-card">Card 2 - Konten kedua</div>
  <div class="reveal-card">Card 3 - Konten ketiga</div>
</section>
```

```css
.scroll-demo {
  padding: 4rem 0;
  max-width: 760px;
  margin: 0 auto;
}

.reveal-card {
  background: #ffffff;
  border: 1px solid rgba(18, 48, 26, 0.08);
  border-radius: 1rem;
  padding: 1.1rem 1.2rem;
  margin-top: 1rem;

  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.5s ease, transform 0.5s ease;
}

.reveal-card.show {
  opacity: 1;
  transform: translateY(0);
}
```

Keterangan:
- Class awal `.reveal-card` dibuat transparan dan turun sedikit.
- Class `.show` akan menampilkan elemen secara halus.
- JavaScript nanti bertugas menambahkan class `.show`.

Tujuan tahap ini:
- memahami hubungan class awal dan class aktif,
- belajar menggunakan `transition` untuk efek ringan.

---

#### 3) Script mahir: HTML + CSS + JavaScript final

```html
<section class="scroll-demo">
  <div class="section-head">
    <p class="kicker">Interaksi Halaman</p>
    <h2>Animasi Scroll pada Landing</h2>
    <p>Setiap card akan muncul saat masuk viewport agar alur baca terasa progresif.</p>
  </div>

  <div class="reveal-card" data-delay="0">Card 1 - Ringkasan Program</div>
  <div class="reveal-card" data-delay="90">Card 2 - FAQ Singkat</div>
  <div class="reveal-card" data-delay="180">Card 3 - Katalog Unggulan</div>
  <div class="reveal-card" data-delay="270">Card 4 - CTA Akhir</div>
</section>
```

```css
.scroll-demo {
  padding: 4rem 1rem;
  max-width: 780px;
  margin: 0 auto;
}

.section-head {
  margin-bottom: 1rem;
}

.kicker {
  margin: 0 0 0.35rem;
  font-size: 0.74rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #2f7d4a;
  font-weight: 700;
}

.reveal-card {
  background: #ffffff;
  border: 1px solid rgba(18, 48, 26, 0.08);
  border-radius: 1rem;
  padding: 1.15rem 1.2rem;
  margin-top: 0.95rem;
  box-shadow: 0 10px 20px rgba(18, 48, 26, 0.05);

  opacity: 0;
  transform: translateY(24px) scale(0.98);
  transition: opacity 0.55s ease, transform 0.55s ease;
}

.reveal-card.show {
  opacity: 1;
  transform: translateY(0) scale(1);
}
```

```javascript
const revealItems = document.querySelectorAll('.reveal-card');

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const delay = Number(entry.target.dataset.delay || 0);

        setTimeout(() => {
          entry.target.classList.add('show');
        }, delay);

        observer.unobserve(entry.target);
      }
    });
  },
  {
    threshold: 0.2
  }
);

revealItems.forEach((item) => observer.observe(item));
```

Keterangan:
- `IntersectionObserver` mendeteksi elemen saat masuk viewport.
- `data-delay` dipakai untuk stagger animation (muncul bergantian).
- `unobserve` menghindari animasi berulang dan lebih hemat performa.

Tujuan tahap ini:
- mengenal teknik animasi scroll yang modern,
- memahami dasar optimasi performa,
- bisa menerapkan efek reveal ke banyak section landing page.

---

#### Tutorial belajar
1. Beri class target ke elemen yang akan dianimasikan.
2. Tulis state awal di CSS: `opacity: 0` dan `transform`.
3. Tulis state aktif `.show`.
4. Buat observer JavaScript untuk menambahkan `.show` saat elemen terlihat.
5. Tambahkan `data-delay` agar muncul bertahap.

Kesimpulan:
Animasi scroll yang ringan membuat halaman terlihat lebih profesional tanpa membebani pengguna.
