### 04k - Section Program Literasi

#### Tujuan section
Section program literasi berfungsi untuk menampilkan berbagai program utama dari website. Section ini membantu pengunjung memahami bahwa website bukan hanya berisi buku, tetapi juga ada program dan kegiatan yang ditujukan untuk berbagai kelompok usia.

Biasanya section ini berisi:
- judul utama,
- beberapa card program,
- target sasaran seperti anak, remaja, dewasa, atau lansia,
- deskripsi singkat,
- tombol untuk melihat program lebih lanjut.

Pada proyek ini, section ini mirip dengan bagian Pojok Literasi yang ada di halaman landing page.

---

#### Konsep dasar program literasi
Program literasi biasanya dibuat dari:
- HTML untuk menyusun card program,
- CSS untuk layout dan warna,
- JavaScript untuk interaksi seperti filter atau pemilihan program aktif.

Setiap card program biasanya memiliki:
- ikon atau emoji,
- nama program,
- target sasaran,
- deskripsi,
- tombol lihat program.

---

#### 1) Script mudah: HTML dasar

```html
<section>
  <div>
    <div>Program lintas generasi</div>
    <h2>Pojok Literasi</h2>
  </div>

  <div>
    <article>
      <div>🌱</div>
      <h3>Tunas Ngrembaka</h3>
      <p>Untuk balita dan anak-anak</p>
      <a href="#">Lihat program</a>
    </article>

    <article>
      <div>🎨</div>
      <h3>Karya Ngrembaka</h3>
      <p>Untuk remaja</p>
      <a href="#">Lihat program</a>
    </article>

    <article>
      <div>⚙️</div>
      <h3>Cakra Ngrembaka</h3>
      <p>Untuk usia produktif</p>
      <a href="#">Lihat program</a>
    </article>
  </div>
</section>
```

Keterangan:
- HTML dasar sudah cukup untuk membuat daftar program.
- Masing-masing card diurutkan secara berurutan dan mudah dibaca.
- Teks menjelaskan siapa sasaran program dan apa fokusnya.

Tujuan tahap ini:
- siswa memahami bahwa satu section bisa berisi banyak card,
- siswa belajar menyusun informasi dengan struktur yang jelas,
- siswa melihat bahwa website tidak hanya berisi teks, tetapi juga kategori program.

---

#### 2) Script mahir: HTML + CSS + JavaScript final

```html
<section class="program-section">
  <div class="container">
    <div class="section-head">
      <div class="section-kicker">Program lintas generasi</div>
      <h2>Pojok Literasi</h2>
    </div>

    <div class="program-grid">
      <article class="program-card active" data-group="anak" data-name="Tunas Ngrembaka" data-desc="Program literasi dasar untuk anak usia dini dan anak sekolah melalui kegiatan membaca, bermain, dan menulis.">
        <div class="icon-wrap">🌱</div>
        <div class="program-badge">Anak</div>
        <h3>Tunas Ngrembaka</h3>
        <p>Literasi dasar, numerasi, karakter, dan budaya lokal.</p>
        <button class="program-btn">Lihat program</button>
      </article>

      <article class="program-card" data-group="remaja" data-name="Karya Ngrembaka" data-desc="Program untuk remaja agar lebih kreatif dalam literasi digital, desain, dan konten kreatif.">
        <div class="icon-wrap">🎨</div>
        <div class="program-badge">Remaja</div>
        <h3>Karya Ngrembaka</h3>
        <p>Literasi digital, desain visual, dan kreativitas berbasis teknologi.</p>
        <button class="program-btn">Lihat program</button>
      </article>

      <article class="program-card" data-group="dewasa" data-name="Cakra Ngrembaka" data-desc="Program untuk usia produktif yang fokus pada inovasi, branding, dan keterampilan usaha.">
        <div class="icon-wrap">⚙️</div>
        <div class="program-badge">Dewasa</div>
        <h3>Cakra Ngrembaka</h3>
        <p>Edupreneur skill, produk lokal, dan pemasaran digital.</p>
        <button class="program-btn">Lihat program</button>
      </article>

      <article class="program-card" data-group="lansia" data-name="Kersa Ngrembaka" data-desc="Program untuk lansia agar tetap sehat, produktif, dan aktif dalam kegiatan literasi komunitas.">
        <div class="icon-wrap">🌿</div>
        <div class="program-badge">Lansia</div>
        <h3>Kersa Ngrembaka</h3>
        <p>Kesehatan, TOGA, dan keterampilan produktif berbasis komunitas.</p>
        <button class="program-btn">Lihat program</button>
      </article>
    </div>

    <div class="program-detail">
      <p class="detail-label">Program terpilih</p>
      <h4 id="programTitle">Tunas Ngrembaka</h4>
      <p id="programDesc">Program literasi dasar untuk anak usia dini dan anak sekolah melalui kegiatan membaca, bermain, dan menulis.</p>
    </div>
  </div>
</section>
```

```css
.program-section {
  padding: 4rem 0;
  background: #f5f8f5;
}

.section-head {
  margin-bottom: 2rem;
}

.section-kicker {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #2f7d4a;
  font-weight: 700;
}

.program-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1.25rem;
}

.program-card {
  background: #fff;
  border: 1px solid rgba(18, 48, 26, 0.08);
  border-radius: 1rem;
  padding: 1.25rem;
  box-shadow: 0 10px 20px rgba(18, 48, 26, 0.04);
  transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
  cursor: pointer;
}

.program-card:hover,
.program-card.active {
  transform: translateY(-4px);
  border-color: rgba(47, 125, 74, 0.4);
  box-shadow: 0 18px 28px rgba(47, 125, 74, 0.08);
}

.icon-wrap {
  width: 3rem;
  height: 3rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 0.9rem;
  background: #edf8ef;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.program-badge {
  display: inline-block;
  background: #eaf6ee;
  color: #1d4d2d;
  font-size: 0.7rem;
  font-weight: 700;
  border-radius: 999px;
  padding: 0.35rem 0.7rem;
  margin-bottom: 0.8rem;
}

.program-card h3 {
  margin: 0 0 0.6rem;
  color: #12301a;
}

.program-card p {
  color: #53665d;
  line-height: 1.7;
}

.program-btn {
  margin-top: 1rem;
  border: none;
  border-radius: 0.7rem;
  background: #12301a;
  color: white;
  padding: 0.7rem 1rem;
  font-weight: 700;
  cursor: pointer;
}

.program-detail {
  margin-top: 2rem;
  background: #ffffff;
  border-radius: 1rem;
  padding: 1.25rem 1.5rem;
  border: 1px solid rgba(18, 48, 26, 0.08);
}

.detail-label {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #2f7d4a;
  font-weight: 700;
  margin: 0 0 0.5rem;
}

@media (max-width: 991px) {
  .program-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 575px) {
  .program-grid {
    grid-template-columns: 1fr;
  }
}
```

```javascript
const cards = document.querySelectorAll('.program-card');
const programTitle = document.getElementById('programTitle');
const programDesc = document.getElementById('programDesc');

cards.forEach((card) => {
  card.addEventListener('click', () => {
    cards.forEach((item) => item.classList.remove('active'));
    card.classList.add('active');

    programTitle.textContent = card.dataset.name;
    programDesc.textContent = card.dataset.desc;
  });
});
```

Keterangan:
- `grid-template-columns` diatur agar program tampil dalam 4 kolom di desktop.
- `program-card.active` digunakan untuk menunjukkan card yang dipilih.
- JavaScript mengambil nilai dari `data-name` dan `data-desc`, lalu menampilkan detail ke bagian bawah.
- Interaksi ini membuat section terasa lebih modern dan lebih mudah dipahami pengunjung.

Tujuan tahap ini:
- siswa belajar membangun section program dengan banyak kategori,
- siswa memahami cara menampilkan beberapa program sekaligus dengan struktur yang konsisten,
- siswa belajar mengombinasikan HTML, CSS, dan JavaScript untuk interaksi yang lebih hidup.

---

#### Tutorial belajar
1. Buat card program satu per satu.
2. Tambahkan ikon, judul, dan target sasaran.
3. Gunakan CSS Grid agar card rata dan tidak berantakan.
4. Beri efek hover dan active state agar user tahu card mana yang sedang dipilih.
5. Gunakan JavaScript untuk memperbarui detail program saat card diklik.

Kesimpulan:
Section program literasi membantu website menjelaskan bahwa program bukan hanya sekadar buku, tetapi juga kegiatan belajar yang disesuaikan dengan kebutuhan kelompok sasaran.

---

#### Latihan mandiri
Coba lanjutkan dengan:
- menambahkan filter "Semua | Anak | Remaja | Dewasa | Lansia",
- membuat tombol "Lihat semua program",
- menambahkan ikon yang lebih beragam,
- mengganti warna sesuai tema website.

Jika kamu bisa membuat section ini dengan 4 card dan interaksi klik, berarti kamu sudah mulai memahami pola kerja section yang dinamis.
