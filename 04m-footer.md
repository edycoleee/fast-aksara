### 04m - Section Footer

#### Tujuan section
Footer adalah bagian penutup halaman yang berisi informasi penting seperti lokasi, kontak, navigasi cepat, dan hak cipta.

Pada proyek ini, footer di template utama sudah berisi:
- lokasi (peta),
- kontak,
- link cepat ke halaman E-Library dan Pojok Literasi,
- copyright.

Section ini membantu pengguna menemukan informasi penting tanpa harus kembali ke atas halaman.

---

#### Konsep dasar footer
Footer biasanya memadukan:
- HTML untuk struktur kolom,
- CSS untuk warna kontras dan keterbacaan,
- JavaScript untuk interaksi kecil, misalnya menampilkan tahun otomatis atau tombol kembali ke atas.

---

#### 1) Script mudah: HTML dasar

```html
<footer>
  <div>
    <h3>Ngrembaka Aksara</h3>
    <p>Portal literasi untuk semua generasi.</p>
  </div>

  <div>
    <h4>Kontak</h4>
    <ul>
      <li>Email: admin@aksara.fun</li>
      <li>WhatsApp: +6281234567890</li>
      <li>Alamat: Podorejo, Semarang</li>
    </ul>
  </div>

  <div>
    <h4>Menu Cepat</h4>
    <ul>
      <li><a href="/elibrary">E-Library</a></li>
      <li><a href="/pojok-literasi/tunas">Tunas</a></li>
      <li><a href="/pojok-literasi/karya">Karya</a></li>
    </ul>
  </div>

  <p>Copyright 2026 Ngrembaka Aksara</p>
</footer>
```

Keterangan:
- Struktur footer dibagi menjadi beberapa kelompok informasi.
- Konten utama: identitas, kontak, dan link cepat.
- Tahap ini fokus pada isi, belum pada tampilan.

Tujuan tahap ini:
- memahami fungsi footer sebagai penutup,
- mampu menyusun informasi penting secara ringkas,
- belajar membagi informasi dalam blok.

---

#### 2) Script mahir: HTML + CSS + JavaScript final

```html
<footer class="footer-aksara">
  <div class="container">
    <div class="footer-grid">
      <div>
        <h3>Ngrembaka Aksara</h3>
        <p>Portal literasi untuk semua generasi. Koleksi belajar, program, dan konten komunitas dalam satu tempat.</p>
      </div>

      <div>
        <h4>Kontak</h4>
        <ul class="footer-list">
          <li>Email: admin@aksara.fun</li>
          <li>WhatsApp: +6281234567890</li>
          <li>Alamat: Podorejo, Semarang</li>
        </ul>
      </div>

      <div>
        <h4>Menu Cepat</h4>
        <ul class="footer-list">
          <li><a href="/elibrary">E-Library</a></li>
          <li><a href="/pojok-literasi/tunas">Tunas Ngrembaka</a></li>
          <li><a href="/pojok-literasi/karya">Karya Ngrembaka</a></li>
          <li><a href="/pojok-literasi/cakra">Cakra Ngrembaka</a></li>
        </ul>
      </div>
    </div>

    <button class="top-btn" id="topBtn" type="button">Kembali ke atas</button>

    <div class="footer-bottom">
      <small>&copy; <span id="yearNow"></span> PPK ORMAWA Ngrembaka Aksara. Hak cipta dilindungi.</small>
    </div>
  </div>
</footer>
```

```css
.footer-aksara {
  background: #102b18;
  color: #e8f2ec;
  padding: 3rem 0 1.5rem;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.4fr 1fr 1fr;
  gap: 1.5rem;
}

.footer-aksara h3,
.footer-aksara h4 {
  margin-top: 0;
  margin-bottom: 0.8rem;
  color: #ffffff;
}

.footer-aksara p {
  color: #b6c9be;
  line-height: 1.7;
}

.footer-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.footer-list li {
  margin-bottom: 0.55rem;
  color: #c4d5cc;
}

.footer-list a {
  color: #dff2e6;
  text-decoration: none;
}

.footer-list a:hover {
  text-decoration: underline;
}

.top-btn {
  margin-top: 1.5rem;
  border: 1px solid rgba(223, 242, 230, 0.35);
  background: transparent;
  color: #e6f3ea;
  border-radius: 0.7rem;
  padding: 0.6rem 0.9rem;
  cursor: pointer;
}

.footer-bottom {
  margin-top: 1.2rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(223, 242, 230, 0.2);
  color: #c0d2c7;
}

@media (max-width: 767px) {
  .footer-grid {
    grid-template-columns: 1fr;
  }
}
```

```javascript
const yearNow = document.getElementById('yearNow');
const topBtn = document.getElementById('topBtn');

yearNow.textContent = new Date().getFullYear();

topBtn.addEventListener('click', () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
});
```

Keterangan:
- Layout footer memakai grid 3 kolom di desktop, lalu 1 kolom di mobile.
- Warna footer dibuat kontras agar terpisah jelas dari isi utama halaman.
- JavaScript dipakai untuk dua hal praktis: tahun otomatis dan tombol kembali ke atas.

Tujuan tahap ini:
- membuat footer yang informatif dan rapi,
- memahami pentingnya navigasi penutup,
- menambahkan interaksi kecil yang berguna.

---

#### Tutorial belajar
1. Mulai dari 3 blok footer: identitas, kontak, menu cepat.
2. Atur warna latar footer agar berbeda dari section lain.
3. Gunakan CSS Grid untuk mengatur kolom.
4. Tambahkan garis pemisah dan baris copyright.
5. Tambahkan JavaScript tahun otomatis dan tombol kembali ke atas.

Kesimpulan:
Footer yang baik membuat website terlihat selesai, profesional, dan memudahkan pengguna mencari info penting dengan cepat.
