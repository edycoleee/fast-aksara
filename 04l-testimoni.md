### 04l - Section Testimoni

#### Tujuan section
Section testimoni dipakai untuk menampilkan pengalaman pengguna setelah memakai portal literasi. Bagian ini penting untuk membangun kepercayaan dan menunjukkan dampak program.

Isi umum section testimoni:
- judul section,
- daftar testimoni,
- nama pemberi testimoni,
- peran atau asal (misal: siswa, orang tua, pendamping),
- kutipan singkat.

---

#### Konsep dasar testimoni
Section testimoni dibuat dengan:
- HTML untuk struktur quote,
- CSS untuk tampilan card agar nyaman dibaca,
- JavaScript untuk interaksi sederhana seperti mengganti testimoni aktif.

---

#### 1) Script mudah: HTML dasar

```html
<section>
  <div>
    <div>Suara Pengguna</div>
    <h2>Testimoni Pengunjung</h2>
    <p>Pengalaman nyata dari pengguna portal literasi.</p>
  </div>

  <div>
    <article>
      <p>"Anak saya jadi lebih semangat membaca karena pilihan bukunya banyak dan mudah dicari."</p>
      <h3>Rina</h3>
      <small>Orang Tua</small>
    </article>

    <article>
      <p>"Materi pembelajaran tersusun rapi, jadi saya lebih cepat menyiapkan kegiatan kelas."</p>
      <h3>Pak Dimas</h3>
      <small>Pendamping Belajar</small>
    </article>

    <article>
      <p>"Bagian pojok literasi remaja membuat saya tertarik membuat karya digital sendiri."</p>
      <h3>Nisa</h3>
      <small>Siswa</small>
    </article>
  </div>
</section>
```

Keterangan:
- Struktur dasar sudah memperlihatkan bentuk section testimoni.
- Setiap testimoni punya kutipan, nama, dan peran.
- Tahap ini fokus ke susunan konten sebelum styling.

Tujuan tahap ini:
- memahami struktur data testimoni,
- membiasakan menulis konten dalam card terpisah,
- melatih urutan informasi yang jelas.

---

#### 2) Script mahir: HTML + CSS + JavaScript final

```html
<section class="testimoni-section">
  <div class="container">
    <div class="section-head">
      <div class="section-kicker">Suara Pengguna</div>
      <h2>Testimoni Pengunjung</h2>
      <p>Pengalaman nyata dari pengguna portal literasi.</p>
    </div>

    <div class="testimoni-grid" id="testimoniGrid">
      <article class="testi-card active" data-name="Rina" data-role="Orang Tua" data-quote="Anak saya jadi lebih semangat membaca karena pilihan bukunya banyak dan mudah dicari.">
        <p>"Anak saya jadi lebih semangat membaca karena pilihan bukunya banyak dan mudah dicari."</p>
        <h3>Rina</h3>
        <small>Orang Tua</small>
      </article>

      <article class="testi-card" data-name="Pak Dimas" data-role="Pendamping Belajar" data-quote="Materi pembelajaran tersusun rapi, jadi saya lebih cepat menyiapkan kegiatan kelas.">
        <p>"Materi pembelajaran tersusun rapi, jadi saya lebih cepat menyiapkan kegiatan kelas."</p>
        <h3>Pak Dimas</h3>
        <small>Pendamping Belajar</small>
      </article>

      <article class="testi-card" data-name="Nisa" data-role="Siswa" data-quote="Bagian pojok literasi remaja membuat saya tertarik membuat karya digital sendiri.">
        <p>"Bagian pojok literasi remaja membuat saya tertarik membuat karya digital sendiri."</p>
        <h3>Nisa</h3>
        <small>Siswa</small>
      </article>
    </div>

    <div class="testi-highlight">
      <h4 id="testiName">Rina</h4>
      <p class="role" id="testiRole">Orang Tua</p>
      <p id="testiQuote">Anak saya jadi lebih semangat membaca karena pilihan bukunya banyak dan mudah dicari.</p>
    </div>
  </div>
</section>
```

```css
.testimoni-section {
  padding: 4rem 0;
  background: #f7faf7;
}

.section-kicker {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #2f7d4a;
  font-weight: 700;
}

.section-head {
  margin-bottom: 2rem;
}

.testimoni-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1.2rem;
}

.testi-card {
  background: #ffffff;
  border: 1px solid rgba(18, 48, 26, 0.08);
  border-radius: 1rem;
  padding: 1.25rem;
  box-shadow: 0 12px 22px rgba(18, 48, 26, 0.04);
  cursor: pointer;
  transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
}

.testi-card:hover,
.testi-card.active {
  transform: translateY(-4px);
  border-color: rgba(47, 125, 74, 0.35);
  box-shadow: 0 18px 30px rgba(47, 125, 74, 0.08);
}

.testi-card p {
  color: #44564d;
  line-height: 1.7;
}

.testi-card h3 {
  margin: 1rem 0 0.2rem;
  color: #12301a;
}

.testi-card small {
  color: #6a7d74;
}

.testi-highlight {
  margin-top: 1.5rem;
  background: #ffffff;
  border: 1px solid rgba(18, 48, 26, 0.08);
  border-radius: 1rem;
  padding: 1.25rem 1.5rem;
}

.testi-highlight .role {
  margin: 0.2rem 0 0.7rem;
  font-size: 0.9rem;
  color: #2f7d4a;
  font-weight: 600;
}

@media (max-width: 767px) {
  .testimoni-grid {
    grid-template-columns: 1fr;
  }
}
```

```javascript
const testiCards = document.querySelectorAll('.testi-card');
const testiName = document.getElementById('testiName');
const testiRole = document.getElementById('testiRole');
const testiQuote = document.getElementById('testiQuote');

testiCards.forEach((card) => {
  card.addEventListener('click', () => {
    testiCards.forEach((item) => item.classList.remove('active'));
    card.classList.add('active');

    testiName.textContent = card.dataset.name;
    testiRole.textContent = card.dataset.role;
    testiQuote.textContent = card.dataset.quote;
  });
});
```

Keterangan:
- Card testimoni ditata dengan grid agar rapi di desktop.
- State active membantu pengguna tahu testimoni yang sedang dipilih.
- JavaScript membaca data dari atribut data-* lalu menampilkan detail di area highlight.

Tujuan tahap ini:
- memahami cara membuat section testimoni yang interaktif,
- belajar menggabungkan layout, warna, dan state aktif,
- belajar update konten dinamis dengan JavaScript sederhana.

---

#### Tutorial belajar
1. Tulis 3 testimoni dulu dalam HTML dasar.
2. Tambahkan CSS card: border, radius, shadow, dan hover.
3. Buat area highlight untuk menampilkan testimoni terpilih.
4. Tambahkan JavaScript click event untuk mengganti isi highlight.
5. Uji di mobile agar card berubah jadi 1 kolom.

Kesimpulan:
Section testimoni membuat halaman lebih meyakinkan karena menampilkan pengalaman pengguna secara langsung.
