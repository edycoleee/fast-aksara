# SEO Setup untuk aksara.fun agar lebih mudah ditemukan Google

Tujuan utama: mempermudah Google mengenali situs ini saat orang mencari kata kunci seperti:
- PPK ORMAWA
- Ngrembaka Aksara
- E-Library PPK ORMAWA
- Pojok Literasi semarang
- Kelurahan Podorejo literasi

---

## 1. Pastikan domain sudah aktif di Cloudflare

Langkah yang perlu dicek di Cloudflare:

1. Masuk ke dashboard Cloudflare.
2. Pilih domain aksara.fun.
3. Pastikan DNS sudah aktif untuk domain utama:
   - aksara.fun
   - www.aksara.fun (opsional)
4. Set SSL/TLS ke mode:
   - Full (Strict)
5. Pastikan proxy Cloudflare aktif untuk domain utama.
6. Jika ada pengaturan robots default dari Cloudflare, hapus/override agar situs dapat menggunakan file robots custom.

Catatan:
- File robots.txt di root website harus bisa dijangkau dari URL berikut:
  - https://aksara.fun/robots.txt
- File sitemap harus bisa dijangkau dari URL berikut:
  - https://aksara.fun/sitemap.xml

---

## 2. File yang harus di-upload ke root website

Buat file berikut di root publik website Anda.

### robots.txt

```txt
User-agent: *
Allow: /

Sitemap: https://aksara.fun/sitemap.xml
```

### sitemap.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://aksara.fun/</loc>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://aksara.fun/beranda</loc>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://aksara.fun/profil/ngrembaka-aksara</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://aksara.fun/profil/kelurahan-podorejo</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://aksara.fun/elibrary</loc>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://aksara.fun/pojok-literasi/tunas</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://aksara.fun/pojok-literasi/karya</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://aksara.fun/pojok-literasi/cakra</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://aksara.fun/pojok-literasi/kersa</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>
```

---

## 3. Pastikan metadata SEO di halaman utama sudah benar

Halaman utama sudah diberi metadata penting di file:
- backend/app/templates/base.html

Metadata yang perlu ada:
- title
- meta description
- meta keywords
- robots
- canonical
- Open Graph

Contoh metadata yang sudah diarahkan untuk kata kunci PPK ORMAWA:

```html
<meta name="description" content="Ngrembaka Aksara adalah portal E-Library dan Pojok Literasi PPK ORMAWA yang menghadirkan modul pembelajaran, buku cerita, dan program literasi di Kelurahan Podorejo, Semarang." />
<meta name="keywords" content="PPK ORMAWA, Ngrembaka Aksara, E-Library, pojok literasi, Kelurahan Podorejo, Semarang, literasi digital, modul pembelajaran" />
<meta name="robots" content="index,follow" />
<link rel="canonical" href="https://aksara.fun/" />
<meta property="og:title" content="Ngrembaka Aksara | E-Library & Pojok Literasi PPK ORMAWA" />
<meta property="og:description" content="Portal literasi dan E-Library PPK ORMAWA untuk masyarakat, siswa, dan pendamping belajar di Kelurahan Podorejo, Semarang." />
<meta property="og:url" content="https://aksara.fun/" />
```

---

## 4. Submit ke Google Search Console

Setelah file root aktif di website, lakukan langkah berikut:

1. Buka Google Search Console.
2. Pilih Add Property.
3. Masukkan domain: aksara.fun
4. Verifikasi ownership.
5. Setelah domain terverifikasi, buka menu Sitemaps.
6. Masukkan URL sitemap berikut:
   - https://aksara.fun/sitemap.xml
7. Klik Submit.

Jika muncul status error, cek apakah URL sitemap benar-benar mengembalikan file XML valid.

---

## 5. Verifikasi dari browser atau terminal

Cek URL ini dari browser atau curl:

```bash
curl -I https://aksara.fun/robots.txt
curl -I https://aksara.fun/sitemap.xml
curl -s https://aksara.fun/ | head
```

Harus ada hasil:
- robots.txt: 200 OK
- sitemap.xml: 200 OK
- halaman utama: HTML dengan meta SEO yang benar

---

## 6. Checklist akhir sebelum menunggu Google index

Pastikan sudah lengkap:

- [ ] DNS domain aktif di Cloudflare
- [ ] SSL/TLS Full (Strict)
- [ ] robots.txt ada di root website
- [ ] sitemap.xml ada di root website
- [ ] title dan description halaman utama jelas
- [ ] canonical link aktif
- [ ] domain sudah ditambah ke Google Search Console
- [ ] sitemap sudah disubmit
- [ ] Google sudah berhasil crawl minimal satu halaman

---

## 7. Catatan penting

Google biasanya tidak langsung menampilkan situs pada kata kunci tertentu dalam hitungan jam. Biasanya butuh waktu beberapa hari sampai beberapa minggu, tergantung:
- autoritas domain
- kualitas konten
- seberapa sering halaman di-crawl
- struktur SEO yang konsisten

Untuk kata kunci PPK ORMAWA, situs akan lebih mudah ditemukan jika terus memperbarui konten dan menjaga struktur URL serta metadata yang konsisten.

---

## 8. File pendukung yang sudah disiapkan di repo

Di repo ini sudah dibuat file pendukung untuk dipindahkan ke root domain website Anda:
- robots.txt
- sitemap.xml
- docs/SEO.md

Jika Anda ingin, langkah berikutnya bisa langsung dilakukan dengan cara:
- upload file robots.txt dan sitemap.xml ke root website Cloudflare / origin server
- lalu submit sitemap di Google Search Console

---

## 9. Saran lanjutan

Untuk optimasi selanjutnya, bisa ditambahkan:
- schema.org untuk organisasi / website
- breadcrumb structured data
- JSON-LD untuk profil organisasi
- artikel landing page berkualitas dengan keyword PPK ORMAWA
- menambahkan halaman konten baru yang relevan dengan kata kunci target

Tujuan akhir bukan hanya tampil di Google, tapi tampil pada hasil yang relevan dan dipercaya.
