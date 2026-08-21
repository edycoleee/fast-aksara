### 7.7 Section FAQ

#### Tujuan section
Section FAQ berfungsi untuk menjawab pertanyaan-pertanyaan umum yang sering muncul di benak pengunjung. Dengan FAQ, user bisa memahami isi website tanpa harus membaca semua halaman.

Pada halaman referensi, FAQ biasanya terdiri dari:
- judul section,
- deskripsi singkat,
- daftar pertanyaan,
- jawaban yang muncul saat user mengklik pertanyaan,
- tampilan interaktif dengan JavaScript.

---

#### Konsep dasar FAQ

FAQ adalah kombinasi antara HTML, CSS, dan JavaScript:
- HTML: membuat daftar pertanyaan dan jawaban
- CSS: membuat tampilan accordion dan hover
- JavaScript: membuka dan menutup jawaban saat diklik

Contoh struktur dasar:

```text
+-------------------------------------------+
| FAQ singkat                               |
| ----------------------------------------- |
| Apa isi utama website ini?      +           |
|   Website ini memuat ...                   |
| Bagaimana cara membuka koleksi buku? +    |
| Apakah kontennya bisa diperbarui admin? + |
+-------------------------------------------+
```

Ini adalah pola accordion: satu pertanyaan bisa dibuka atau ditutup.

---

#### 1) Script mudah: HTML dasar tanpa interaksi

```html
<section>
  <div>
    <div>Pertanyaan yang sering ditanyakan</div>
    <h2>FAQ singkat</h2>
    <p>Bagian ini membantu pengunjung baru memahami cara memakai portal dan isi setiap halaman dengan cepat.</p>
  </div>

  <div>
    <div>
      <h3>Apa isi utama website ini?</h3>
      <p>Website ini memuat E-Library, profil program, profil wilayah, dan empat Pojok Literasi yang ditujukan untuk lintas generasi.</p>
    </div>

    <div>
      <h3>Bagaimana cara membuka koleksi buku?</h3>
      <p>Pengunjung dapat masuk ke menu E-Library atau halaman utama untuk memilih kategori buku yang ingin dibaca.</p>
    </div>

    <div>
      <h3>Apakah kontennya bisa diperbarui admin?</h3>
      <p>Ya, admin dapat menambah atau mengubah konten melalui panel admin yang tersedia di sistem.</p>
    </div>
  </div>
</section>
```

Keterangan:
- HTML dasar ini sudah cukup untuk menampilkan daftar FAQ.
- Semua pertanyaan dan jawaban dibuat secara berurutan.
- Saat ini, semua jawaban tetap terlihat, karena belum ada interaksi JS.

Tujuan tahap ini:
- siswa memahami struktur FAQ,
- memahami cara menuliskan pertanyaan dan jawaban,
- memahami bahwa FAQ adalah daftar item yang disusun dalam urutan logis.

---

#### 2) Script menengah: HTML + CSS untuk tampilan accordion yang lebih rapi

```html
<section class="faq-wrap">
  <div class="container">
    <div class="faq-header">
      <div class="section-kicker">Pertanyaan yang sering ditanyakan</div>
      <h2 class="section-title">FAQ singkat</h2>
      <p>Bagian ini membantu pengunjung baru memahami cara memakai portal dan isi setiap halaman dengan cepat.</p>
    </div>

    <div class="faq-list">
      <div class="faq-item">
        <button class="faq-question">Apa isi utama website ini?</button>
        <div class="faq-answer">
          Website ini memuat E-Library, profil program, profil wilayah, dan empat Pojok Literasi yang ditujukan untuk lintas generasi.
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-question">Bagaimana cara membuka koleksi buku?</button>
        <div class="faq-answer">
          Pengunjung dapat membuka halaman E-Library dan memilih kategori yang diinginkan, lalu klik judul atau kartu untuk membaca isinya.
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-question">Apakah kontennya bisa diperbarui admin?</button>
        <div class="faq-answer">
          Ya, admin dapat menambah, mengedit, dan menghapus konten melalui panel admin agar website selalu up to date.
        </div>
      </div>
    </div>
  </div>
</section>
```

```css
.faq-wrap {
  padding: 4rem 0;
  background: #f7faf7;
}

.faq-header {
  margin-bottom: 2rem;
}

.faq-list {
  display: grid;
  gap: 1rem;
}

.faq-item {
  background: #ffffff;
  border: 1px solid rgba(18, 48, 26, 0.08);
  border-radius: 1rem;
  overflow: hidden;
}

.faq-question {
  width: 100%;
  text-align: left;
  border: none;
  background: transparent;
  padding: 1rem 1.25rem;
  font-size: 1rem;
  font-weight: 700;
  color: #12301a;
  cursor: pointer;
}

.faq-answer {
  padding: 0 1.25rem 1.25rem;
  color: #4f5d57;
  line-height: 1.7;
}
```

Keterangan:
- `faq-item` membuat tiap pertanyaan menjadi blok yang terpisah.
- `button` dipakai agar item bisa diklik.
- `faq-answer` dibuat dengan padding dan warna yang nyaman dibaca.
- pada tahap ini, semua jawaban masih bisa terlihat atau belum bisa ditutup, karena belum ada JavaScript.

Tujuan tahap ini:
- siswa mulai belajar membedakan struktur dan styling,
- memahami cara CSS membuat item FAQ terlihat modern.

---

#### 3) Script menengah-ke-mahir: menambahkan interaksi JavaScript sederhana

```html
<section class="faq-wrap">
  <div class="container">
    <div class="faq-header">
      <div class="section-kicker">Pertanyaan yang sering ditanyakan</div>
      <h2 class="section-title">FAQ singkat</h2>
      <p>Bagian ini membantu pengunjung baru memahami cara memakai portal dan isi setiap halaman dengan cepat.</p>
    </div>

    <div class="faq-list">
      <div class="faq-item active">
        <button class="faq-question" type="button">
          Apa isi utama website ini?
        </button>
        <div class="faq-answer" style="display:block;">
          Website ini memuat E-Library, profil program, profil wilayah, dan empat Pojok Literasi yang ditujukan untuk lintas generasi.
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-question" type="button">
          Bagaimana cara membuka koleksi buku?
        </button>
        <div class="faq-answer">
          Pengunjung dapat membuka halaman E-Library dan memilih kategori yang diinginkan, lalu klik judul atau kartu untuk membaca isinya.
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-question" type="button">
          Apakah kontennya bisa diperbarui admin?
        </button>
        <div class="faq-answer">
          Ya, admin dapat menambah, mengedit, dan menghapus konten melalui panel admin agar website selalu up to date.
        </div>
      </div>
    </div>
  </div>
</section>
```

```css
.faq-wrap {
  padding: 4rem 0;
  background: #f7faf7;
}

.faq-list {
  display: grid;
  gap: 1rem;
}

.faq-item {
  background: #fff;
  border: 1px solid rgba(18, 48, 26, 0.08);
  border-radius: 1rem;
  overflow: hidden;
}

.faq-question {
  width: 100%;
  background: transparent;
  border: none;
  text-align: left;
  padding: 1rem 1.25rem;
  font-weight: 700;
  color: #12301a;
  cursor: pointer;
}

.faq-answer {
  display: none;
  padding: 0 1.25rem 1.25rem;
  color: #4f5d57;
  line-height: 1.7;
}

.faq-item.active .faq-answer {
  display: block;
}
```

```javascript
const faqItems = document.querySelectorAll('.faq-item');

faqItems.forEach((item) => {
  const button = item.querySelector('.faq-question');

  button.addEventListener('click', () => {
    const isOpen = item.classList.contains('active');

    faqItems.forEach((faq) => {
      faq.classList.remove('active');
    });

    if (!isOpen) {
      item.classList.add('active');
    }
  });
});
```

Keterangan:
- JavaScript menambahkan behavior klik.
- Ketika tombol diklik, semua item ditutup dulu.
- Kemudian item yang diklik dibuka jika sebelumnya tertutup.
- `classList` dipakai untuk menambah atau menghapus class `active`.

Tujuan tahap ini:
- siswa mulai memahami hubungan HTML + CSS + JS,
- mengetahui bahwa interaksi bisa dibuat dengan event click,
- dan bahwa JavaScript dapat mengubah tampilan di browser tanpa mereload halaman.

---

#### 4) Script mahir: versi final HTML + CSS + JS yang mirip halaman nyata

```html
<section class="faq-wrap">
  <div class="container">
    <div class="d-flex flex-column flex-lg-row align-items-lg-end justify-content-between gap-2 mb-4">
      <div>
        <div class="section-kicker mb-2">Pertanyaan yang sering ditanyakan</div>
        <h2 class="section-title mb-2">FAQ singkat</h2>
      </div>
      <p class="text-muted mb-0" style="max-width: 42rem;">
        Bagian ini membantu pengunjung baru memahami cara memakai portal dan isi setiap halaman dengan cepat.
      </p>
    </div>

    <div class="faq-list">
      <div class="faq-item active">
        <button class="faq-question" type="button" aria-expanded="true">
          Apa isi utama website ini?
        </button>
        <div class="faq-answer">
          Website ini memuat E-Library, profil program, profil wilayah, dan empat Pojok Literasi yang ditujukan untuk lintas generasi.
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-question" type="button" aria-expanded="false">
          Bagaimana cara membuka koleksi buku?
        </button>
        <div class="faq-answer">
          Pengunjung dapat membuka halaman E-Library dan memilih kategori yang diinginkan, lalu klik judul atau kartu untuk membaca isinya.
        </div>
      </div>

      <div class="faq-item">
        <button class="faq-question" type="button" aria-expanded="false">
          Apakah kontennya bisa diperbarui admin?
        </button>
        <div class="faq-answer">
          Ya, admin dapat menambah, mengedit, dan menghapus konten melalui panel admin agar website selalu up to date.
        </div>
      </div>
    </div>
  </div>
</section>
```

```css
.faq-wrap {
  padding: 4rem 0;
  background: #f7faf7;
}

.faq-list {
  display: grid;
  gap: 1rem;
}

.faq-item {
  background: #ffffff;
  border: 1px solid rgba(18, 48, 26, 0.08);
  border-radius: 1rem;
  overflow: hidden;
  box-shadow: 0 8px 22px rgba(18, 48, 26, 0.04);
}

.faq-question {
  width: 100%;
  border: none;
  background: transparent;
  color: #12301a;
  text-align: left;
  font-size: 1.05rem;
  font-weight: 700;
  padding: 1rem 1.25rem;
  cursor: pointer;
  position: relative;
}

.faq-question::after {
  content: '+';
  position: absolute;
  right: 1.25rem;
  top: 50%;
  transform: translateY(-50%);
  font-size: 1.3rem;
  color: #4f7a4e;
}

.faq-item.active .faq-question::after {
  content: '-';
}

.faq-answer {
  display: none;
  padding: 0 1.25rem 1.25rem;
  color: #4f5d57;
  line-height: 1.7;
}

.faq-item.active .faq-answer {
  display: block;
}
```

```javascript
const faqItems = document.querySelectorAll('.faq-item');

faqItems.forEach((item) => {
  const button = item.querySelector('.faq-question');

  button.addEventListener('click', () => {
    const isOpen = item.classList.contains('active');

    faqItems.forEach((faq) => {
      faq.classList.remove('active');
      faq.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
    });

    if (!isOpen) {
      item.classList.add('active');
      button.setAttribute('aria-expanded', 'true');
    }
  });
});
```

Keterangan final:
- `+` dan `-` pada tombol pertanyaan memberi indikator visual.
- `aria-expanded` membantu aksesibilitas.
- JavaScript tetap sederhana, tetapi sudah cukup untuk membuat accordion yang berfungsi dengan baik.
- CSS membuat tampilannya lebih modern dan rapi.

---

#### Mengapa FAQ penting?
FAQ membantu user mendapatkan jawaban cepat tanpa membaca semua halaman. Untuk website seperti ini, FAQ sangat penting karena:
- mengurangi kebingungan pengunjung baru,
- mempercepat pemahaman isi website,
- membantu menjelaskan poin utama seperti halaman buku, profil, dan admin,
- memperlihatkan bahwa website dibuat dengan fokus pada user experience.

---

#### Tutorial belajar dari mudah ke mahir

1. Tahap mudah
   - buat daftar FAQ dengan HTML saja,
   - fokus pada struktur, judul, dan jawaban,
   - pastikan urutan pertanyaan masuk akal.

2. Tahap menengah
   - buat tiap item FAQ dalam blok yang terlihat rapi,
   - gunakan CSS untuk memberi border, padding, dan background,
   - tampilkan pertanyaan dan jawaban dengan jarak yang nyaman.

3. Tahap mahir
   - gunakan JavaScript untuk membuka dan menutup jawaban,
   - tambahkan `aria-expanded` agar lebih ramah aksesibilitas,
   - beri indikator `+` dan `-` agar user tahu item bisa diklik.

4. Tahap final
   - kombinasikan semua elemen agar terlihat bersih dan konsisten dengan landing page,
   - pastikan layout tetap nyaman di layar kecil.

---

#### Kunci pembelajaran

FAQ adalah latihan terbaik untuk memahami 3 konsep penting JavaScript web:
- DOM selection (`querySelectorAll`)
- event handling (`addEventListener`)
- class manipulation (`classList.add`, `classList.remove`)

Dengan kata lain, FAQ bukan hanya bagian dekoratif. Ia adalah contoh nyata penggunaan JavaScript untuk membuat halaman lebih interaktif.

---

#### Latihan kecil
Coba buat FAQ Anda sendiri dengan tema berikut:
- tentang sekolah
- tentang kelas online
- tentang program literasi
- tentang pengelolaan konten

Setiap item harus memiliki:
- judul pertanyaan,
- jawaban singkat,
- interaksi klik,
- dan warna yang konsisten dengan tema website.

Tujuan latihan:
- siswa belajar cara membangun accordion dari nol,
- memahami perbedaan HTML, CSS, dan JS,
- dan melihat bagaimana interaksi user di browser bisa dibuat dengan code yang sederhana.
