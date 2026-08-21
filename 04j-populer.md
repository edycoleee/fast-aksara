### 04j - Section Populer

#### Tujuan section
Section populer berfungsi untuk menampilkan konten atau program yang paling sering dibuka, paling menarik, atau paling relevan untuk dipelajari terlebih dahulu.

Biasanya section ini berisi:
- judul utama,
- beberapa card item,
- tag atau label seperti "Trending", "Terbaru", atau "Favorit",
- tombol aksi seperti "Baca sekarang".

Tujuan dari section ini adalah membuat pengunjung segera tertarik dan tahu konten apa yang paling penting untuk dibuka dulu.

---

#### Konsep dasar section populer
Section populer menggabungkan:
- HTML untuk menata daftar item,
- CSS untuk tampilan card dan hover,
- JavaScript untuk interaksi, seperti memilih item aktif atau menampilkan detail item.

Struktur umum item populer:
- gambar/ikon,
- label kategori,
- judul,
- ringkasan,
- tombol baca.

---

#### 1) Script mudah: HTML dasar

```html
<section>
  <div>
    <div>Populer</div>
    <h2>Konten favorit minggu ini</h2>
  </div>

  <div>
    <article>
      <span>Literasi Dasar</span>
      <h3>Belajar membaca anak</h3>
      <p>Latihan membaca sederhana untuk anak usia dini dan sekolah dasar.</p>
      <button>Baca sekarang</button>
    </article>

    <article>
      <span>Digital</span>
      <h3>Literasi media sosial</h3>
      <p>Belajar membedakan informasi yang bermanfaat dan aman di dunia digital.</p>
      <button>Baca sekarang</button>
    </article>

    <article>
      <span>Kreatif</span>
      <h3>Membuat cerita digital</h3>
      <p>Teknik menulis cerita singkat yang menarik dan bisa dibagikan ke teman.</p>
      <button>Baca sekarang</button>
    </article>
  </div>
</section>
```

Keterangan:
- HTML sederhana sudah cukup untuk membuat section populer.
- Setiap card dibuat secara terpisah agar mudah dibaca.
- Tiap item memiliki label, judul, deskripsi, dan tombol.

Tujuan tahap ini:
- siswa memahami struktur layout section,
- siswa belajar cara membagi konten menjadi item-item card,
- siswa fokus pada susunan HTML sebelum menambahkan style.

---

#### 2) Script mahir: HTML + CSS + JavaScript final

```html
<section class="popular-section">
  <div class="container">
    <div class="section-head">
      <div class="section-kicker">Populer</div>
      <h2>Konten favorit minggu ini</h2>
    </div>

    <div class="popular-grid" id="popularGrid">
      <article class="popular-card active" data-name="Belajar Membaca Anak" data-desc="Latihan membaca sederhana untuk membangun kebiasaan baca sejak dini.">
        <span class="tag">Literasi Dasar</span>
        <h3>Belajar membaca anak</h3>
        <p>Latihan membaca sederhana untuk anak usia dini dan sekolah dasar.</p>
        <button class="read-btn">Baca sekarang</button>
      </article>

      <article class="popular-card" data-name="Literasi Media Sosial" data-desc="Belajar membedakan konten yang bermanfaat, aman, dan sesuai kebutuhan.">
        <span class="tag">Digital</span>
        <h3>Literasi media sosial</h3>
        <p>Belajar membedakan informasi yang bermanfaat dan aman di dunia digital.</p>
        <button class="read-btn">Baca sekarang</button>
      </article>

      <article class="popular-card" data-name="Membuat Cerita Digital" data-desc="Mengembangkan ide cerita menjadi konten yang menarik dan mudah dibagikan.">
        <span class="tag">Kreatif</span>
        <h3>Membuat cerita digital</h3>
        <p>Teknik menulis cerita singkat yang menarik dan bisa dibagikan ke teman.</p>
        <button class="read-btn">Baca sekarang</button>
      </article>
    </div>

    <div class="popular-detail">
      <h4 id="detailTitle">Belajar Membaca Anak</h4>
      <p id="detailDesc">Latihan membaca sederhana untuk membangun kebiasaan baca sejak dini.</p>
    </div>
  </div>
</section>
```

```css
.popular-section {
  padding: 4rem 0;
  background: #f7faf7;
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

.popular-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1.5rem;
}

.popular-card {
  background: #fff;
  border: 1px solid rgba(17, 24, 39, 0.08);
  border-radius: 1rem;
  padding: 1.25rem;
  box-shadow: 0 10px 18px rgba(0, 0, 0, 0.04);
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
  cursor: pointer;
}

.popular-card:hover,
.popular-card.active {
  transform: translateY(-4px);
  border-color: rgba(47, 125, 74, 0.35);
  box-shadow: 0 16px 28px rgba(47, 125, 74, 0.08);
}

.tag {
  display: inline-block;
  background: #eaf6ee;
  color: #1f5f36;
  font-size: 0.72rem;
  font-weight: 700;
  border-radius: 999px;
  padding: 0.4rem 0.7rem;
  margin-bottom: 0.9rem;
}

.popular-card h3 {
  margin: 0 0 0.7rem;
  color: #12301a;
}

.popular-card p {
  color: #53665d;
  line-height: 1.7;
}

.read-btn {
  margin-top: 1rem;
  border: none;
  border-radius: 0.7rem;
  background: #12301a;
  color: #fff;
  padding: 0.75rem 1rem;
  font-weight: 700;
  cursor: pointer;
}

.popular-detail {
  margin-top: 2rem;
  background: #ffffff;
  border-radius: 1rem;
  padding: 1.25rem 1.5rem;
  border: 1px solid rgba(17, 24, 39, 0.08);
}

@media (max-width: 767px) {
  .popular-grid {
    grid-template-columns: 1fr;
  }
}
```

```javascript
const cards = document.querySelectorAll('.popular-card');
const detailTitle = document.getElementById('detailTitle');
const detailDesc = document.getElementById('detailDesc');

cards.forEach((card) => {
  card.addEventListener('click', () => {
    cards.forEach((item) => item.classList.remove('active'));
    card.classList.add('active');

    detailTitle.textContent = card.dataset.name;
    detailDesc.textContent = card.dataset.desc;
  });
});
```

Keterangan:
- `popular-grid` dibuat dengan CSS Grid agar card tampil rapi dan sejajar.
- `popular-card.active` memberi efek item yang sedang dipilih.
- JavaScript menambahkan interaksi: saat user klik card, judul dan deskripsi detail di bagian bawah berubah.
- Ini adalah contoh interaksi sederhana yang sering dipakai pada section populer di website modern.

Tujuan tahap ini:
- siswa belajar membuat layout card yang terlihat menarik,
- siswa melihat bagaimana hover, spacing, dan state aktif bekerja,
- siswa memahami cara menambahkan interaksi sederhana dengan JavaScript.

---

#### Tutorial belajar
1. Buat dulu struktur HTML dengan beberapa card.
2. Tambahkan CSS untuk mengatur ukuran, jarak, border, dan warna.
3. Gunakan `display: grid` supaya card tersebar rapi.
4. Tambahkan class `active` saat item dipilih.
5. Dengan JavaScript, ambil data dari `data-name` dan `data-desc` lalu tampilkan ke detail section.

Kesimpulan:
Section populer adalah cara agar website terlihat lebih hidup dan membantu pengguna langsung menemukan konten yang paling penting.

---

#### Latihan mandiri
Coba buat:
- 4 card populer,
- label warna berbeda untuk tiap kategori,
- efek hover yang lebih besar,
- tombol "Lihat semua" di bagian bawah section.

Jika kamu bisa membuat section ini dengan 2 sampai 3 card yang berfungsi, artinya kamu sudah paham konsep dasar section populer.
