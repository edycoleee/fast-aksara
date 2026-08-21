### 04n - Section CTA Akhir

#### Tujuan section
Section CTA (Call To Action) akhir adalah ajakan penutup agar pengunjung melakukan aksi setelah membaca halaman landing.

Contoh aksi yang umum:
- Buka E-Library
- Lihat Program Literasi
- Hubungi admin melalui WhatsApp

CTA akhir biasanya diletakkan sebelum footer agar pengguna punya langkah lanjut yang jelas.

---

#### Konsep dasar CTA
Section CTA yang baik memadukan:
- judul yang kuat,
- deskripsi singkat,
- tombol aksi utama dan tombol pendukung,
- tampilan visual yang menonjol dibanding section lain.

Di tahap mahir, JavaScript dipakai untuk interaksi kecil seperti efek klik, analytics sederhana, atau notifikasi.

---

#### 1) Script mudah: HTML dasar

```html
<section>
  <div>
    <h2>Siap mulai belajar hari ini?</h2>
    <p>Buka koleksi bacaan dan program literasi sesuai kebutuhanmu.</p>
    <a href="/elibrary">Lihat E-Library</a>
    <a href="/pojok-literasi/tunas">Lihat Program Literasi</a>
  </div>
</section>
```

Keterangan:
- Struktur paling dasar hanya butuh judul, deskripsi, dan link.
- Belum ada style, jadi fokusnya memahami isi CTA.
- Dua tombol memberi pilihan aksi yang jelas.

Tujuan tahap ini:
- memahami fungsi CTA,
- belajar menyusun ajakan singkat,
- mengenal pola tombol aksi utama dan sekunder.

---

#### 2) Script menengah: HTML + CSS

```html
<section class="cta-final">
  <div class="container cta-box">
    <div class="cta-content">
      <p class="cta-kicker">Langkah berikutnya</p>
      <h2>Siap mulai belajar hari ini?</h2>
      <p class="cta-desc">Buka koleksi bacaan, jelajahi program literasi, lalu pilih materi yang paling sesuai untukmu.</p>
    </div>
    <div class="cta-actions">
      <a href="/elibrary" class="btn-primary">Lihat E-Library</a>
      <a href="/pojok-literasi/tunas" class="btn-secondary">Lihat Program Literasi</a>
    </div>
  </div>
</section>
```

```css
.cta-final {
  padding: 4rem 0;
  background: #f3f8f3;
}

.cta-box {
  background: linear-gradient(135deg, #12301a, #1f5f36);
  border-radius: 1.25rem;
  padding: 2rem;
  color: #ffffff;
  display: flex;
  justify-content: space-between;
  gap: 1.5rem;
  align-items: center;
}

.cta-kicker {
  margin: 0 0 0.5rem;
  font-size: 0.75rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #b9e2c6;
  font-weight: 700;
}

.cta-content h2 {
  margin: 0 0 0.7rem;
  font-size: clamp(1.5rem, 2.4vw, 2.2rem);
}

.cta-desc {
  margin: 0;
  color: #d7ebde;
  max-width: 38rem;
  line-height: 1.7;
}

.cta-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.7rem;
}

.btn-primary,
.btn-secondary {
  text-decoration: none;
  padding: 0.75rem 1rem;
  border-radius: 0.75rem;
  font-weight: 700;
}

.btn-primary {
  background: #f4bf3a;
  color: #1d2a20;
}

.btn-secondary {
  background: transparent;
  color: #e8f4ec;
  border: 1px solid rgba(232, 244, 236, 0.45);
}

@media (max-width: 768px) {
  .cta-box {
    flex-direction: column;
    align-items: flex-start;
  }
}
```

Keterangan:
- CSS membuat CTA tampil kontras dengan section sebelumnya.
- Tombol utama dan sekunder dibedakan agar prioritas aksi jelas.
- Responsive layout memastikan CTA tetap rapi di layar kecil.

Tujuan tahap ini:
- belajar membuat hierarchy visual,
- memahami pentingnya warna kontras pada CTA,
- melatih responsive layout.

---

#### 3) Script mahir: HTML + CSS + JavaScript final

```html
<section class="cta-final" id="ctaAkhir">
  <div class="container cta-box">
    <div class="cta-content">
      <p class="cta-kicker">Langkah berikutnya</p>
      <h2>Siap mulai belajar hari ini?</h2>
      <p class="cta-desc">Pilih jalur belajarmu: mulai dari E-Library, lanjut ke Pojok Literasi, atau hubungi pendamping melalui WhatsApp.</p>
    </div>

    <div class="cta-actions">
      <a href="/elibrary" class="btn-primary cta-btn" data-action="elibrary">Lihat E-Library</a>
      <a href="/pojok-literasi/tunas" class="btn-secondary cta-btn" data-action="program">Lihat Program Literasi</a>
      <a href="https://wa.me/6281234567890" target="_blank" class="btn-ghost cta-btn" data-action="whatsapp">Hubungi Kami</a>
    </div>
  </div>

  <p class="cta-note" id="ctaNote">Belum ada aksi yang dipilih.</p>
</section>
```

```css
.cta-final {
  padding: 4rem 0 3.5rem;
  background:
    radial-gradient(circle at 15% 15%, rgba(47, 125, 74, 0.16), transparent 42%),
    #f2f8f3;
}

.cta-box {
  background: linear-gradient(135deg, #0f2b18, #1f5f36 58%, #2f7d4a);
  border-radius: 1.25rem;
  padding: 2rem;
  color: #ffffff;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1.5rem;
  box-shadow: 0 18px 34px rgba(17, 53, 29, 0.24);
}

.cta-kicker {
  margin: 0 0 0.45rem;
  font-size: 0.74rem;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: #b8e4c7;
  font-weight: 700;
}

.cta-content h2 {
  margin: 0 0 0.6rem;
  font-size: clamp(1.55rem, 2.45vw, 2.25rem);
}

.cta-desc {
  margin: 0;
  max-width: 40rem;
  color: #dceee2;
  line-height: 1.7;
}

.cta-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
}

.cta-btn {
  text-decoration: none;
  border-radius: 0.8rem;
  padding: 0.78rem 1rem;
  font-weight: 700;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.cta-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.18);
}

.btn-primary {
  background: #f4bf3a;
  color: #1b2c20;
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.12);
  color: #f4fff7;
  border: 1px solid rgba(255, 255, 255, 0.34);
}

.btn-ghost {
  background: transparent;
  color: #dcf3e3;
  border: 1px dashed rgba(220, 243, 227, 0.55);
}

.cta-note {
  margin: 0.9rem auto 0;
  max-width: 72rem;
  font-size: 0.9rem;
  color: #325840;
}

@media (max-width: 768px) {
  .cta-box {
    flex-direction: column;
    align-items: flex-start;
  }
}
```

```javascript
const ctaButtons = document.querySelectorAll('.cta-btn');
const ctaNote = document.getElementById('ctaNote');

ctaButtons.forEach((btn) => {
  btn.addEventListener('click', (event) => {
    const action = btn.dataset.action;
    const label = btn.textContent.trim();

    ctaNote.textContent = `Aksi dipilih: ${label} (${action}).`;

    if (action !== 'whatsapp') {
      event.preventDefault();
      alert(`Simulasi: kamu memilih ${label}.`);
    }
  });
});
```

Keterangan:
- JavaScript membaca atribut `data-action` untuk mengetahui tombol mana yang diklik.
- Pesan status di bawah CTA membantu latihan event handling.
- Untuk latihan, link non-WhatsApp dibuat simulasi dengan `alert` agar perubahan terlihat jelas.

Tujuan tahap ini:
- memahami CTA modern yang menarik,
- belajar menghubungkan tombol dengan event JavaScript,
- membangun section penutup yang mendorong aksi.

---

#### Tutorial belajar
1. Mulai dari HTML sederhana: judul + 2 tombol.
2. Tambah CSS agar CTA menonjol dengan warna kontras.
3. Tambah tombol ketiga untuk opsi kontak.
4. Gunakan `data-action` untuk menandai fungsi tiap tombol.
5. Uji event klik dan tampilkan feedback ke pengguna.

Kesimpulan:
CTA akhir yang baik membuat pengunjung tidak berhenti di membaca, tetapi lanjut melakukan aksi nyata.
