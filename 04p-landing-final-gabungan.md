### 04p - Landing Final Gabungan (04a sampai 04m)

#### Tujuan
File ini menggabungkan semua section pembelajaran 04a sampai 04m menjadi satu halaman landing utuh.

Urutan section yang digabung:
1. Navbar
2. Hero kiri + hero kanan
3. Buku untuk semua
4. Kenapa terasa mudah
5. Profil program
6. FAQ
7. Katalog buku
8. Program literasi
9. Testimoni
10. CTA akhir
11. Footer

Tujuan utamanya agar siswa bisa melihat alur lengkap dari halaman awal sampai akhir.

---

#### 1) Script mudah: HTML kerangka utuh

```html
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Landing Final Ngrembaka Aksara</title>
</head>
<body>
  <nav>
    <a href="#">Ngrembaka Aksara</a>
    <a href="#hero">Beranda</a>
    <a href="#katalog">Katalog</a>
    <a href="#program">Program</a>
    <a href="#kontak">Kontak</a>
  </nav>

  <header id="hero">
    <h1>E-Library PPK ORMAWA Ngrembaka Aksara</h1>
    <p>Portal literasi lintas generasi.</p>
    <a href="#katalog">Lihat Koleksi</a>
  </header>

  <section>
    <h2>Buku untuk semua</h2>
    <p>Akses di mana pun dan kapan pun.</p>
  </section>

  <section>
    <h2>Kenapa terasa mudah</h2>
    <p>Akses cepat, koleksi tertata, dan lintas generasi.</p>
  </section>

  <section>
    <h2>Profil Program</h2>
    <p>Ringkasan program Ngrembaka Aksara.</p>
  </section>

  <section>
    <h2>FAQ</h2>
    <p>Jawaban singkat untuk pertanyaan umum.</p>
  </section>

  <section id="katalog">
    <h2>Katalog Buku</h2>
    <p>Modul pembelajaran, buku cerita, dan literasi digital.</p>
  </section>

  <section id="program">
    <h2>Program Literasi</h2>
    <p>Tunas, Karya, Cakra, dan Kersa.</p>
  </section>

  <section>
    <h2>Testimoni</h2>
    <p>Pengalaman pengguna portal.</p>
  </section>

  <section>
    <h2>Siap mulai belajar?</h2>
    <a href="#">Lihat E-Library</a>
    <a href="#">Hubungi Kami</a>
  </section>

  <footer id="kontak">
    <p>Kontak dan informasi program.</p>
    <p>&copy; 2026 Ngrembaka Aksara</p>
  </footer>
</body>
</html>
```

Keterangan:
- Ini adalah kerangka lengkap satu halaman landing.
- Semua section utama sudah ada, walau masih sederhana.
- Cocok untuk memahami urutan layout sebelum desain detail.

---

#### 2) Script menengah: HTML + CSS (layout landing utuh)

```html
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Landing Final Ngrembaka Aksara</title>
  <style>
    :root {
      --bg: #f6faf7;
      --dark: #12301a;
      --muted: #557265;
      --card: #ffffff;
      --accent: #2f7d4a;
      --gold: #f4bf3a;
    }

    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: "Poppins", sans-serif;
      background: var(--bg);
      color: var(--dark);
      line-height: 1.6;
    }

    .container {
      width: min(1120px, 92%);
      margin: 0 auto;
    }

    nav {
      position: sticky;
      top: 0;
      z-index: 10;
      background: #102b18;
      color: #fff;
      padding: 0.8rem 0;
    }

    .nav-inner {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      flex-wrap: wrap;
    }

    .nav-links {
      display: flex;
      gap: 0.8rem;
      flex-wrap: wrap;
    }

    .nav-links a,
    .brand {
      color: #e6f2eb;
      text-decoration: none;
      font-weight: 600;
    }

    header {
      padding: 4.2rem 0 3.2rem;
      background: linear-gradient(140deg, #143521, #255b3a);
      color: #fff;
    }

    .hero-grid {
      display: grid;
      grid-template-columns: 1.2fr 1fr;
      gap: 1.2rem;
      align-items: center;
    }

    .hero-card {
      background: rgba(255, 255, 255, 0.11);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 1rem;
      padding: 1rem;
    }

    .btn {
      display: inline-block;
      text-decoration: none;
      font-weight: 700;
      border-radius: 0.75rem;
      padding: 0.7rem 1rem;
    }

    .btn-gold { background: var(--gold); color: #1f2b22; }
    .btn-outline { border: 1px solid #d3e8db; color: #f4fff8; }

    section {
      padding: 3.4rem 0;
    }

    .section-title {
      margin: 0 0 0.8rem;
      font-size: clamp(1.4rem, 2.2vw, 2rem);
    }

    .section-sub {
      margin: 0;
      color: var(--muted);
      max-width: 44rem;
    }

    .grid-3 {
      margin-top: 1.3rem;
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 1rem;
    }

    .grid-4 {
      margin-top: 1.3rem;
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 1rem;
    }

    .card {
      background: var(--card);
      border: 1px solid rgba(18, 48, 26, 0.08);
      border-radius: 1rem;
      padding: 1rem;
    }

    .cta-box {
      background: linear-gradient(135deg, #12301a, #2f7d4a);
      color: #fff;
      border-radius: 1rem;
      padding: 1.5rem;
      display: flex;
      justify-content: space-between;
      gap: 1rem;
      align-items: center;
      flex-wrap: wrap;
    }

    footer {
      background: #102b18;
      color: #d9ebdf;
      padding: 2.2rem 0 1.2rem;
      margin-top: 1.5rem;
    }

    .footer-grid {
      display: grid;
      grid-template-columns: 1.3fr 1fr 1fr;
      gap: 1rem;
    }

    @media (max-width: 900px) {
      .hero-grid, .grid-4, .footer-grid {
        grid-template-columns: 1fr 1fr;
      }
    }

    @media (max-width: 640px) {
      .hero-grid, .grid-3, .grid-4, .footer-grid {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>
  <nav>
    <div class="container nav-inner">
      <a class="brand" href="#">Ngrembaka Aksara</a>
      <div class="nav-links">
        <a href="#hero">Beranda</a>
        <a href="#faq">FAQ</a>
        <a href="#katalog">Katalog</a>
        <a href="#program">Program</a>
      </div>
    </div>
  </nav>

  <header id="hero">
    <div class="container hero-grid">
      <div>
        <h1>E-Library PPK ORMAWA Ngrembaka Aksara</h1>
        <p>Portal literasi lintas generasi untuk belajar, berkarya, dan bertumbuh bersama.</p>
        <a class="btn btn-gold" href="#katalog">Lihat E-Library</a>
        <a class="btn btn-outline" href="#program">Lihat Program</a>
      </div>
      <div class="hero-card">
        <h3>Akses cepat</h3>
        <p>E-Library, Pojok Literasi, Artikel, dan profil program dalam satu halaman.</p>
      </div>
    </div>
  </header>

  <section>
    <div class="container">
      <h2 class="section-title">Buku untuk semua</h2>
      <p class="section-sub">Koleksi belajar dapat diakses dari perangkat mana pun.</p>
      <div class="grid-3">
        <article class="card">Koleksi E-Library</article>
        <article class="card">Program Inti</article>
        <article class="card">Kategori Buku</article>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <h2 class="section-title">FAQ Singkat</h2>
      <div class="grid-3" id="faq">
        <article class="card">Apa isi utama website?</article>
        <article class="card">Bagaimana membuka koleksi?</article>
        <article class="card">Apakah konten bisa diperbarui?</article>
      </div>
    </div>
  </section>

  <section id="katalog">
    <div class="container">
      <h2 class="section-title">Katalog Buku</h2>
      <div class="grid-3">
        <article class="card">Modul Pembelajaran</article>
        <article class="card">Buku Cerita</article>
        <article class="card">Literasi Digital</article>
      </div>
    </div>
  </section>

  <section id="program">
    <div class="container">
      <h2 class="section-title">Program Literasi</h2>
      <div class="grid-4">
        <article class="card">Tunas</article>
        <article class="card">Karya</article>
        <article class="card">Cakra</article>
        <article class="card">Kersa</article>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <h2 class="section-title">Testimoni</h2>
      <div class="grid-3">
        <article class="card">"Anak saya lebih semangat membaca."</article>
        <article class="card">"Materi tersusun rapi dan mudah dipakai."</article>
        <article class="card">"Program remaja sangat membantu kreativitas."</article>
      </div>
    </div>
  </section>

  <section>
    <div class="container cta-box">
      <div>
        <h2>Siap mulai belajar hari ini?</h2>
        <p>Pilih jalur belajar sesuai kebutuhanmu.</p>
      </div>
      <div>
        <a class="btn btn-gold" href="#">Lihat E-Library</a>
      </div>
    </div>
  </section>

  <footer>
    <div class="container footer-grid">
      <div>Ngrembaka Aksara</div>
      <div>Kontak</div>
      <div>Menu Cepat</div>
    </div>
  </footer>
</body>
</html>
```

Keterangan:
- Semua section utama sudah membentuk landing page utuh.
- CSS dasar dipakai untuk grid, card, dan hero.
- Ini adalah jembatan sebelum masuk interaksi JavaScript.

---

#### 3) Script mahir: HTML + CSS + JavaScript final (gabungan 04a-04m)

```html
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Landing Final Gabungan</title>
  <style>
    :root {
      --bg: #f4f9f5;
      --dark: #12301a;
      --muted: #567063;
      --card: #ffffff;
      --line: rgba(18, 48, 26, 0.1);
      --accent: #2f7d4a;
      --gold: #f4bf3a;
    }

    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0;
      font-family: "Poppins", sans-serif;
      background: var(--bg);
      color: var(--dark);
      line-height: 1.65;
    }

    .container { width: min(1140px, 92%); margin: 0 auto; }

    .site-nav {
      position: sticky;
      top: 0;
      z-index: 20;
      background: #102b18;
      border-bottom: 1px solid rgba(223, 244, 232, 0.15);
    }

    .site-nav .inner {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      padding: 0.75rem 0;
      flex-wrap: wrap;
    }

    .brand,
    .nav-links a {
      color: #e9f5ee;
      text-decoration: none;
      font-weight: 600;
    }

    .nav-links { display: flex; gap: 0.75rem; flex-wrap: wrap; }

    .hero {
      padding: 4.4rem 0 3.2rem;
      background:
        radial-gradient(circle at 15% 10%, rgba(244, 191, 58, 0.16), transparent 35%),
        linear-gradient(140deg, #133520, #255b3a 70%);
      color: #fff;
    }

    .hero-grid {
      display: grid;
      grid-template-columns: 1.2fr 1fr;
      gap: 1.25rem;
      align-items: center;
    }

    .hero-card {
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 1rem;
      padding: 1rem;
    }

    .hero-stats { display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; margin-top: 0.9rem; }
    .hero-stat { background: rgba(255, 255, 255, 0.12); border-radius: 0.8rem; padding: 0.7rem; }

    .btn { display: inline-block; border-radius: 0.75rem; font-weight: 700; text-decoration: none; padding: 0.72rem 1rem; }
    .btn-main { background: var(--gold); color: #1f2d22; }
    .btn-sub { border: 1px solid rgba(225, 244, 233, 0.45); color: #eefaf2; }

    section { padding: 3.4rem 0; }
    .section-kicker {
      margin: 0 0 0.35rem;
      font-size: 0.74rem;
      text-transform: uppercase;
      letter-spacing: 0.13em;
      font-weight: 700;
      color: var(--accent);
    }

    .section-title { margin: 0 0 0.7rem; font-size: clamp(1.45rem, 2.2vw, 2rem); }
    .section-sub { margin: 0; color: var(--muted); max-width: 44rem; }

    .grid-2 { margin-top: 1.2rem; display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
    .grid-3 { margin-top: 1.2rem; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1rem; }
    .grid-4 { margin-top: 1.2rem; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 1rem; }

    .card {
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: 1rem;
      padding: 1rem;
      box-shadow: 0 10px 22px rgba(18, 48, 26, 0.05);
    }

    .card h3, .card h4 { margin: 0.2rem 0 0.5rem; }
    .chip {
      display: inline-block;
      background: #e8f4ec;
      color: #1f5f36;
      font-size: 0.72rem;
      border-radius: 999px;
      padding: 0.32rem 0.68rem;
      font-weight: 700;
    }

    .faq-item { cursor: pointer; }
    .faq-answer { margin-top: 0.55rem; color: var(--muted); display: none; }
    .faq-item.active .faq-answer { display: block; }

    .selectable.active {
      border-color: rgba(47, 125, 74, 0.5);
      transform: translateY(-2px);
    }

    .cta-wrap {
      background: linear-gradient(135deg, #12301a, #2f7d4a);
      border-radius: 1rem;
      color: #fff;
      padding: 1.45rem;
      display: flex;
      justify-content: space-between;
      gap: 1rem;
      align-items: center;
      flex-wrap: wrap;
    }

    .cta-note { color: #d2e8d9; margin: 0.45rem 0 0; font-size: 0.9rem; }

    .footer {
      background: #102b18;
      color: #d9ebdf;
      padding: 2.2rem 0 1.1rem;
      margin-top: 1.3rem;
    }

    .footer-grid { display: grid; grid-template-columns: 1.3fr 1fr 1fr; gap: 1rem; }
    .footer a { color: #e4f5eb; text-decoration: none; }

    .reveal {
      opacity: 0;
      transform: translateY(22px);
      transition: opacity 0.55s ease, transform 0.55s ease;
    }

    .reveal.show {
      opacity: 1;
      transform: translateY(0);
    }

    @media (max-width: 900px) {
      .hero-grid, .grid-4, .footer-grid { grid-template-columns: 1fr 1fr; }
    }

    @media (max-width: 640px) {
      .hero-grid, .grid-2, .grid-3, .grid-4, .footer-grid { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>
  <nav class="site-nav">
    <div class="container inner">
      <a class="brand" href="#hero">Ngrembaka Aksara</a>
      <div class="nav-links">
        <a href="#hero">Beranda</a>
        <a href="#faq">FAQ</a>
        <a href="#katalog">Katalog</a>
        <a href="#program">Program</a>
        <a href="#testimoni">Testimoni</a>
      </div>
    </div>
  </nav>

  <header id="hero" class="hero reveal" data-delay="0">
    <div class="container hero-grid">
      <div>
        <p class="section-kicker" style="color:#d7eedf;">Buku untuk semua generasi</p>
        <h1 style="margin:0 0 0.7rem;">E-Library PPK ORMAWA Ngrembaka Aksara</h1>
        <p style="max-width:42rem; color:#e1f2e8;">Portal literasi lintas generasi untuk belajar, berkarya, dan bertumbuh bersama melalui koleksi buku, program, dan konten komunitas.</p>
        <a class="btn btn-main" href="#katalog">Lihat E-Library</a>
        <a class="btn btn-sub" href="#program">Lihat Program</a>
      </div>
      <div class="hero-card">
        <h3 style="margin-top:0;">Akses cepat</h3>
        <p style="margin:0; color:#e5f5eb;">Baca, jelajahi, dan temukan program sesuai usia dan kebutuhan belajar.</p>
        <div class="hero-stats">
          <div class="hero-stat">E-Library: 5 kategori</div>
          <div class="hero-stat">Pojok Literasi: 4 program</div>
          <div class="hero-stat">Artikel: terus bertambah</div>
          <div class="hero-stat">Akses: mobile friendly</div>
        </div>
      </div>
    </div>
  </header>

  <section class="reveal" data-delay="60">
    <div class="container">
      <p class="section-kicker">Buku untuk semua</p>
      <h2 class="section-title">Akses di mana pun, kapan pun</h2>
      <p class="section-sub">Portal merangkum koleksi belajar, pojok literasi lintas usia, dan konten program dalam satu alur yang mudah dijelajahi.</p>
      <div class="grid-3">
        <article class="card">Koleksi E-Library</article>
        <article class="card">Program Inti</article>
        <article class="card">Kategori Buku</article>
      </div>
    </div>
  </section>

  <section class="reveal" data-delay="90">
    <div class="container">
      <p class="section-kicker">Kenapa terasa mudah</p>
      <h2 class="section-title">Portal fokus pada akses belajar</h2>
      <div class="grid-3">
        <article class="card"><h4>Akses cepat</h4><p>Semua menu penting ada dalam satu alur.</p></article>
        <article class="card"><h4>Koleksi tertata</h4><p>Kategori jelas untuk memudahkan pengguna baru.</p></article>
        <article class="card"><h4>Lintas generasi</h4><p>Dirancang untuk anak sampai lansia.</p></article>
      </div>
    </div>
  </section>

  <section class="reveal" data-delay="120">
    <div class="container">
      <p class="section-kicker">Ringkasan program</p>
      <h2 class="section-title">Profil Program</h2>
      <div class="grid-2">
        <article class="card selectable">
          <span class="chip">Profil Program</span>
          <h3>Profil Ngrembaka Aksara</h3>
          <p>Ekosistem literasi berbasis kebutuhan warga dan pendamping belajar.</p>
        </article>
        <article class="card selectable">
          <span class="chip">Profil Wilayah</span>
          <h3>Kelurahan Podorejo</h3>
          <p>Wilayah sasaran program dengan penguatan literasi lintas usia.</p>
        </article>
      </div>
    </div>
  </section>

  <section id="faq" class="reveal" data-delay="150">
    <div class="container">
      <p class="section-kicker">Pertanyaan umum</p>
      <h2 class="section-title">FAQ Singkat</h2>
      <div class="grid-3">
        <article class="card faq-item">
          <h4>Apa isi utama website?</h4>
          <p class="faq-answer">E-Library, profil, dan empat Pojok Literasi.</p>
        </article>
        <article class="card faq-item">
          <h4>Bagaimana cara membuka koleksi?</h4>
          <p class="faq-answer">Pilih kategori buku di section katalog.</p>
        </article>
        <article class="card faq-item">
          <h4>Apakah konten bisa diperbarui?</h4>
          <p class="faq-answer">Bisa, melalui panel admin CMS.</p>
        </article>
      </div>
    </div>
  </section>

  <section id="katalog" class="reveal" data-delay="180">
    <div class="container">
      <p class="section-kicker">Katalog unggulan</p>
      <h2 class="section-title">Buku terpilih untuk mulai membaca</h2>
      <div class="grid-3">
        <article class="card selectable">
          <span class="chip">1 artikel</span>
          <h3>Modul Pembelajaran</h3>
          <p>Koleksi materi belajar utama untuk pendamping dan siswa.</p>
        </article>
        <article class="card selectable">
          <span class="chip">0 artikel</span>
          <h3>Buku Cerita</h3>
          <p>Cerita anak, budaya lokal, dan imajinasi.</p>
        </article>
        <article class="card selectable">
          <span class="chip">2 artikel</span>
          <h3>Literasi Digital</h3>
          <p>Materi keterampilan digital yang relevan.</p>
        </article>
      </div>
    </div>
  </section>

  <section id="program" class="reveal" data-delay="210">
    <div class="container">
      <p class="section-kicker">Program lintas generasi</p>
      <h2 class="section-title">Pojok Literasi</h2>
      <div class="grid-4">
        <article class="card selectable"><h3>🌱 Tunas</h3><p>Anak</p></article>
        <article class="card selectable"><h3>🎨 Karya</h3><p>Remaja</p></article>
        <article class="card selectable"><h3>⚙️ Cakra</h3><p>Dewasa</p></article>
        <article class="card selectable"><h3>🌿 Kersa</h3><p>Lansia</p></article>
      </div>
    </div>
  </section>

  <section id="testimoni" class="reveal" data-delay="240">
    <div class="container">
      <p class="section-kicker">Suara pengguna</p>
      <h2 class="section-title">Testimoni Pengunjung</h2>
      <div class="grid-3">
        <article class="card selectable" data-quote="Anak saya jadi lebih semangat membaca."><p>"Anak saya jadi lebih semangat membaca."</p><strong>Rina - Orang Tua</strong></article>
        <article class="card selectable" data-quote="Materinya rapi dan mudah dipakai saat pendampingan."><p>"Materinya rapi dan mudah dipakai saat pendampingan."</p><strong>Pak Dimas - Pendamping</strong></article>
        <article class="card selectable" data-quote="Program remaja membuat saya berani membuat karya digital."><p>"Program remaja membuat saya berani membuat karya digital."</p><strong>Nisa - Siswa</strong></article>
      </div>
      <p id="quotePreview" style="margin-top:1rem; color:var(--muted);">Klik salah satu testimoni untuk melihat kutipan utama.</p>
    </div>
  </section>

  <section class="reveal" data-delay="270">
    <div class="container cta-wrap">
      <div>
        <p class="section-kicker" style="color:#d8efdf;">Langkah berikutnya</p>
        <h2 style="margin:0 0 0.5rem;">Siap mulai belajar hari ini?</h2>
        <p style="margin:0; color:#d8ecdf;">Mulai dari koleksi buku, lanjut program, lalu hubungi pendamping jika perlu bantuan.</p>
        <p class="cta-note" id="ctaStatus">Belum ada aksi dipilih.</p>
      </div>
      <div>
        <a class="btn btn-main cta-action" href="#katalog" data-label="E-Library">Lihat E-Library</a>
        <a class="btn btn-sub cta-action" href="#program" data-label="Program">Lihat Program</a>
      </div>
    </div>
  </section>

  <footer class="footer">
    <div class="container footer-grid">
      <div>
        <h4 style="margin-top:0; color:#fff;">Ngrembaka Aksara</h4>
        <p>Portal literasi untuk belajar dan bertumbuh bersama.</p>
      </div>
      <div>
        <h4 style="margin-top:0; color:#fff;">Kontak</h4>
        <p>Email: admin@aksara.fun</p>
        <p>WhatsApp: +6281234567890</p>
      </div>
      <div>
        <h4 style="margin-top:0; color:#fff;">Menu Cepat</h4>
        <p><a href="#hero">Beranda</a></p>
        <p><a href="#katalog">Katalog</a></p>
        <p><a href="#program">Program</a></p>
      </div>
    </div>
    <div class="container" style="margin-top:1rem; border-top:1px solid rgba(233,245,238,0.2); padding-top:0.8rem;">
      <small>&copy; <span id="yearNow"></span> PPK ORMAWA Ngrembaka Aksara</small>
    </div>
  </footer>

  <script>
    const revealElements = document.querySelectorAll('.reveal');
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const delay = Number(entry.target.dataset.delay || 0);
          setTimeout(() => entry.target.classList.add('show'), delay);
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.16 });

    revealElements.forEach((el) => revealObserver.observe(el));

    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach((item) => {
      item.addEventListener('click', () => {
        item.classList.toggle('active');
      });
    });

    const selectableCards = document.querySelectorAll('.selectable');
    selectableCards.forEach((card) => {
      card.addEventListener('click', () => {
        const siblings = card.parentElement.querySelectorAll('.selectable');
        siblings.forEach((sib) => sib.classList.remove('active'));
        card.classList.add('active');

        const quote = card.dataset.quote;
        if (quote) {
          document.getElementById('quotePreview').textContent = `Kutipan utama: "${quote}"`;
        }
      });
    });

    const ctaActions = document.querySelectorAll('.cta-action');
    const ctaStatus = document.getElementById('ctaStatus');
    ctaActions.forEach((btn) => {
      btn.addEventListener('click', () => {
        ctaStatus.textContent = `Aksi dipilih: ${btn.dataset.label}`;
      });
    });

    document.getElementById('yearNow').textContent = new Date().getFullYear();
  </script>
</body>
</html>
```

Keterangan:
- Script ini menggabungkan semua pembelajaran section 04a-04m dalam satu halaman final.
- Interaksi JavaScript yang dipakai:
  - reveal animation saat scroll,
  - FAQ toggle,
  - active card untuk katalog/program/testimoni,
  - status aksi pada CTA,
  - tahun footer otomatis.
- Layout sudah responsive dan bisa dijadikan dasar integrasi ke template Jinja2.

---

#### Tutorial belajar
1. Mulai dari script kerangka HTML penuh (tahap 1).
2. Tambahkan CSS grid, card, hero, dan footer (tahap 2).
3. Tambahkan class khusus untuk elemen interaktif: `faq-item`, `selectable`, `cta-action`, `reveal`.
4. Implementasikan JavaScript secara bertahap: FAQ dulu, lalu active card, lalu scroll animation.
5. Uji di desktop dan mobile agar urutan section tetap nyaman dibaca.

Kesimpulan:
Setelah menyelesaikan file ini, siswa sudah memahami cara membangun landing page utuh dari komponen kecil menjadi halaman final yang interaktif.

---

## Versi Integrasi Jinja2 Ke Struktur Proyek

Bagian ini mengubah landing final menjadi versi yang benar-benar terhubung ke FastAPI + Jinja2 pada struktur proyek:

- `backend/app/routers/landing.py`
- `backend/app/templates/landing.html`
- `backend/app/static/css/style.css`
- `backend/app/static/js/main.js`

Target belajar: dari template statis menuju template dinamis berbasis data backend.

---

### 1) Script awal: route FastAPI + render Jinja2 paling dasar

#### A. Router (`backend/app/routers/landing.py`)

```python
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.jinja import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def landing(request: Request):
    return templates.TemplateResponse(
        "landing.html",
        {
            "request": request,
            "judul": "E-Library PPK ORMAWA Ngrembaka Aksara",
            "subjudul": "Portal literasi lintas generasi",
        },
    )
```

#### B. Template (`backend/app/templates/landing.html`)

```html
{% extends "base.html" %}
{% block title %}{{ judul }}{% endblock %}

{% block content %}
<section class="py-5">
  <div class="container">
    <h1>{{ judul }}</h1>
    <p>{{ subjudul }}</p>
    <a href="/elibrary" class="btn-aksara">Lihat E-Library</a>
  </div>
</section>
{% endblock %}
```

Keterangan:
- Data dikirim dari Python ke HTML lewat dictionary context.
- `request` wajib disertakan agar `TemplateResponse` valid.
- Ini fondasi render Jinja2 paling dasar.

---

### 2) Script menengah: data list/dict + loop Jinja2 untuk section landing

#### A. Router (`backend/app/routers/landing.py`)

```python
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.jinja import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def landing(request: Request):
    hero = {
        "judul": "E-LIBRARY PPK ORMAWA NGREMBAKA AKSARA",
        "deskripsi": "Portal literasi lintas generasi untuk belajar, berkarya, dan bertumbuh bersama.",
    }

    metrics = [
        {"label": "Koleksi E-Library", "value": 5},
        {"label": "Program Inti", "value": 4},
        {"label": "Kategori Buku", "value": 5},
    ]

    katalog = [
        {
            "judul": "Modul Pembelajaran",
            "deskripsi": "Materi belajar utama untuk pendamping dan siswa.",
            "artikel": 1,
            "url": "/elibrary/modul-pembelajaran",
        },
        {
            "judul": "Buku Cerita",
            "deskripsi": "Cerita anak, budaya lokal, dan imajinasi.",
            "artikel": 0,
            "url": "/elibrary/buku-cerita",
        },
        {
            "judul": "Literasi Digital",
            "deskripsi": "Materi keterampilan digital yang relevan.",
            "artikel": 2,
            "url": "/elibrary/buku-literasi-digital",
        },
    ]

    return templates.TemplateResponse(
        "landing.html",
        {
            "request": request,
            "hero": hero,
            "metrics": metrics,
            "katalog": katalog,
        },
    )
```

#### B. Template (`backend/app/templates/landing.html`)

```html
{% extends "base.html" %}

{% block content %}
<section class="hero-aksara py-5">
  <div class="container">
    <h1>{{ hero.judul }}</h1>
    <p>{{ hero.deskripsi }}</p>
  </div>
</section>

<section class="py-4">
  <div class="container">
    <div class="row g-3">
      {% for item in metrics %}
      <div class="col-6 col-lg-4">
        <div class="hero-metric h-100">
          <div class="label">{{ item.label }}</div>
          <div class="value">{{ item.value }}</div>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</section>

<section class="section-bg py-5">
  <div class="container">
    <h2 class="section-title mb-4">Katalog Buku</h2>
    <div class="row g-4">
      {% for buku in katalog %}
      <div class="col-lg-4">
        <a href="{{ buku.url }}" class="text-decoration-none feature-link">
          <div class="highlight-card h-100 d-flex">
            <div class="rail"></div>
            <div class="p-4 flex-grow-1">
              <span class="badge-aksara">{{ buku.artikel }} artikel</span>
              <h5 class="title mt-3">{{ buku.judul }}</h5>
              <p class="meta mb-3">{{ buku.deskripsi }}</p>
              <span class="cta">Lihat koleksi</span>
            </div>
          </div>
        </a>
      </div>
      {% endfor %}
    </div>
  </div>
</section>
{% endblock %}
```

Keterangan:
- `for` loop Jinja2 dipakai untuk menghindari penulisan card berulang.
- Data list di Python jadi lebih mudah diubah tanpa edit HTML satu per satu.
- Sudah mulai mengikuti pola visual landing proyek.

---

### 3) Script mahir: integrasi penuh (router + template + css + js) sesuai proyek

#### A. Router (`backend/app/routers/landing.py`)

```python
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.jinja import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def landing(request: Request):
    elibrary_counts = {
        "modul-pembelajaran": 1,
        "ebook": 0,
        "buku-cerita": 0,
        "buku-literasi-digital": 2,
        "buku-keterampilan": 0,
    }

    pojok_counts = {
        "tunas": 2,
        "karya": 0,
        "cakra": 0,
        "kersa": 0,
    }

    faq_items = [
        {
            "q": "Apa isi utama website ini?",
            "a": "E-Library, profil program, profil wilayah, dan empat Pojok Literasi.",
        },
        {
            "q": "Bagaimana cara membuka koleksi buku?",
            "a": "Klik kartu kategori pada bagian E-Library di halaman utama.",
        },
        {
            "q": "Apakah kontennya bisa diperbarui admin?",
            "a": "Bisa, melalui panel pengelolaan admin CMS.",
        },
    ]

    testimoni = [
        {"nama": "Rina", "peran": "Orang Tua", "kutipan": "Anak saya jadi lebih semangat membaca."},
        {"nama": "Pak Dimas", "peran": "Pendamping", "kutipan": "Materi pembelajaran tersusun rapi."},
        {"nama": "Nisa", "peran": "Siswa", "kutipan": "Program remaja membuat saya berani berkarya."},
    ]

    elibrary_total = sum(elibrary_counts.values())
    pojok_total = sum(pojok_counts.values())

    return templates.TemplateResponse(
        "landing.html",
        {
            "request": request,
            "elibrary_counts": elibrary_counts,
            "pojok_counts": pojok_counts,
            "elibrary_total": elibrary_total,
            "pojok_total": pojok_total,
            "faq_items": faq_items,
            "testimoni": testimoni,
        },
    )
```

#### B. Template (`backend/app/templates/landing.html`)

```html
{% extends "base.html" %}

{% block content %}
<section class="hero-aksara">
  <div class="container py-5">
    <h1 class="display-5 fw-bold mb-3">E-Library PPK ORMAWA Ngrembaka Aksara</h1>
    <p class="lead text-white-50 mb-4">Portal literasi lintas generasi untuk belajar dan bertumbuh bersama.</p>
    <div class="d-flex gap-2 flex-wrap">
      <a href="/elibrary" class="btn-aksara">Lihat E-Library</a>
      <a href="/pojok-literasi/tunas" class="btn-aksara-outline">Lihat Program</a>
    </div>
  </div>
</section>

<section class="py-4 reveal" data-delay="40">
  <div class="container">
    <div class="row g-3">
      <div class="col-6 col-lg-3">
        <div class="hero-metric h-100"><div class="label">Koleksi E-Library</div><div class="value">{{ elibrary_total }}</div></div>
      </div>
      <div class="col-6 col-lg-3">
        <div class="hero-metric h-100"><div class="label">Pojok Literasi</div><div class="value">{{ pojok_total }}</div></div>
      </div>
      <div class="col-6 col-lg-3">
        <div class="hero-metric h-100"><div class="label">Program Inti</div><div class="value">4</div></div>
      </div>
      <div class="col-6 col-lg-3">
        <div class="hero-metric h-100"><div class="label">Kategori Buku</div><div class="value">5</div></div>
      </div>
    </div>
  </div>
</section>

<section class="section-white py-5 reveal" data-delay="80" id="faqLanding">
  <div class="container">
    <div class="section-kicker mb-2">FAQ singkat</div>
    <h2 class="section-title mb-4">Pertanyaan yang sering ditanyakan</h2>
    <div class="row g-3">
      {% for item in faq_items %}
      <div class="col-md-4">
        <article class="card card-aksara faq-item h-100 p-3">
          <h6 class="fw-bold mb-2">{{ item.q }}</h6>
          <p class="faq-answer mb-0 text-muted">{{ item.a }}</p>
        </article>
      </div>
      {% endfor %}
    </div>
  </div>
</section>

<section class="section-bg py-5 reveal" data-delay="120" id="testimoniLanding">
  <div class="container">
    <div class="section-kicker mb-2">Suara pengguna</div>
    <h2 class="section-title mb-4">Testimoni Pengunjung</h2>
    <div class="row g-3">
      {% for t in testimoni %}
      <div class="col-md-4">
        <article class="card card-aksara selectable h-100 p-3" data-quote="{{ t.kutipan }}">
          <p class="mb-2">"{{ t.kutipan }}"</p>
          <strong>{{ t.nama }}</strong>
          <div class="small text-muted">{{ t.peran }}</div>
        </article>
      </div>
      {% endfor %}
    </div>
    <p id="quotePreview" class="text-muted mt-3 mb-0">Klik testimoni untuk melihat kutipan utama.</p>
  </div>
</section>
{% endblock %}

{% block scripts %}
  {{ super() }}
  <script src="{{ url_for('static', path='js/main.js') }}"></script>
{% endblock %}
```

#### C. CSS (`backend/app/static/css/style.css`)

```css
.reveal {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.5s ease, transform 0.5s ease;
}

.reveal.show {
  opacity: 1;
  transform: translateY(0);
}

.faq-item {
  cursor: pointer;
}

.faq-item .faq-answer {
  display: none;
}

.faq-item.active .faq-answer {
  display: block;
}

.selectable.active {
  border-color: rgba(47, 125, 74, 0.4);
  box-shadow: 0 14px 24px rgba(47, 125, 74, 0.1);
}
```

#### D. JS (`backend/app/static/js/main.js`)

```javascript
document.addEventListener('DOMContentLoaded', () => {
  const revealElements = document.querySelectorAll('.reveal');

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const delay = Number(entry.target.dataset.delay || 0);
        setTimeout(() => entry.target.classList.add('show'), delay);
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.16 });

  revealElements.forEach((el) => revealObserver.observe(el));

  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach((item) => {
    item.addEventListener('click', () => {
      item.classList.toggle('active');
    });
  });

  const selectableCards = document.querySelectorAll('.selectable');
  const quotePreview = document.getElementById('quotePreview');

  selectableCards.forEach((card) => {
    card.addEventListener('click', () => {
      const siblings = card.parentElement.parentElement.querySelectorAll('.selectable');
      siblings.forEach((sib) => sib.classList.remove('active'));
      card.classList.add('active');

      if (quotePreview && card.dataset.quote) {
        quotePreview.textContent = `Kutipan utama: "${card.dataset.quote}"`;
      }
    });
  });
});
```

Keterangan:
- Tahap mahir memisahkan tanggung jawab file secara rapi: Python untuk data, Jinja untuk render, CSS untuk tampilan, JS untuk interaksi.
- Blok `{% block scripts %}` dipakai agar script landing bisa dipasang tanpa merusak `base.html`.
- Pola ini siap dikembangkan ke data database asli (`ELibrary`, artikel pojok, dan settings situs).

---

### Tutorial implementasi dari awal sampai mahir

1. Mulai dari script awal: pastikan route `/` merender `landing.html` dengan context sederhana (`judul`, `subjudul`).
2. Naik ke script menengah: pindahkan konten card ke list Python, render dengan `{% for %}`.
3. Naik ke script mahir: pecah data metrik/faq/testimoni di router, render semua section dinamis di Jinja2.
4. Pindahkan style ke `backend/app/static/css/style.css` dan logic interaksi ke `backend/app/static/js/main.js`.
5. Uji hasil render di browser lalu cek apakah setiap section masih responsif dan interaktif.

Kesimpulan:
Versi integrasi Jinja2 membuat landing final tidak lagi hardcoded, tetapi menjadi halaman dinamis yang siap tersambung ke database dan CMS admin.
