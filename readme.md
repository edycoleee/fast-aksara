# Branch Pembelajaran HTML & CSS

Branch ini dibuat khusus untuk belajar HTML dan CSS dari materi dasar sampai siap membuat layout web yang rapi dan responsif.

Referensi utama: [00-html.md](00-html.md)

## Tujuan branch ini

Tujuan dari pembelajaran ini adalah agar siswa mampu:
- memahami struktur dasar halaman HTML,
- menggunakan tag HTML yang sering dipakai,
- mengatur layout dengan CSS,
- memahami display, flexbox, grid, dan positioning,
- membuat navbar, card, hero section, dan halaman sederhana,
- membuat layout yang responsif untuk layar kecil dan besar.

---

## Urutan belajar yang disarankan

### 1. HTML dasar
Belajar tentang struktur dokumen HTML:
- `<!DOCTYPE html>`
- `<html>`, `<head>`, `<body>`
- judul halaman dengan `<title>`
- heading, paragraph, list, link, button, form

### 2. CSS dasar
Belajar cara menata tampilan:
- warna,
- font,
- margin,
- padding,
- border,
- background,
- width dan height.

### 3. Display dan layout
Pahami perbedaan jenis display:
- `block`
- `inline`
- `inline-block`
- `flex`
- `grid`
- `none`

### 4. Flexbox
Flexbox adalah teknik utama untuk membuat layout modern.

Contoh konsep yang dipelajari:
- `display: flex`
- `flex-direction`
- `justify-content: center | space-between`
- `align-items`
- `gap`
- `flex-wrap`

### 5. Responsive design
Belajar bagaimana tampilan berubah di layar kecil dengan media query:

```css
@media (max-width: 600px) {
  .nav {
    flex-direction: column;
  }
}
```

### 6. Komponen layout populer
Latihan membuat elemen web seperti:
- navbar,
- hero section,
- tombol CTA,
- card produk,
- gallery,
- footer,
- layout 2 kolom atau 3 kolom.

---

## Topik utama dari materi HTML/CSS

### 1. Template halaman minimal
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dasar HTML CSS</title>
</head>
<body>

</body>
</html>
```

### 2. Display
Jenis layout dasar:
- block = turun satu baris
- inline = sebaris
- inline-block = dapat ukuran tetap
- flex = layout modern
- grid = layout kompleks
- none = sembunyikan

### 3. Flexbox latihan
Contoh latihan dasar:
- baris horizontal,
- menu responsif,
- center layout,
- gallery wrap,
- header dengan logo-menu-aksi.

### 4. Box model
Pahami:
- margin,
- padding,
- border,
- width,
- height,
- box-sizing.

### 5. Positioning
Belajar konsep posisi elemen:
- static
- relative
- absolute
- fixed
- sticky

### 6. Typography dan spacing
Gunakan:
- font-size,
- font-weight,
- line-height,
- letter-spacing,
- text-align.

### 7. Styling visual
Gunakan:
- border-radius,
- box-shadow,
- background,
- gradient,
- hover effect.

---

## Rencana latihan

### Latihan 1: Struktur halaman sederhana
Buat satu halaman yang berisi:
- header,
- nav,
- main,
- section,
- footer.

### Latihan 2: Flexbox layout
Buat:
- 3 card berdampingan,
- navbar dengan logo dan menu,
- layout center.

### Latihan 3: Responsif
Ubah layout saat layar kecil menjadi:
- menu turun ke bawah,
- card berubah satu kolom,
- content rapi di layar mobile.

### Latihan 4: Project mini
Buat halaman seperti:
- landing page sekolah,
- halaman profil desa,
- halaman produk sederhana,
- halaman portofolio.

---

## Target akhir

Setelah mempelajari materi ini, siswa diharapkan bisa membuat halaman web sederhana yang rapi, responsif, dan siap dikembangkan ke tahap berikutnya seperti:
- JavaScript dasar,
- Jinja2,
- FastAPI + template,
- CRUD web app.

---

## Catatan

Branch ini adalah tahap awal sebelum masuk ke JavaScript dan Jinja2. Artinya, fokus utama sekarang adalah membangun fondasi HTML dan CSS dengan latihan yang praktis dan bertahap.

Jika ingin lanjut ke tahap berikutnya, langkah berikutnya adalah:
1. JavaScript dasar,
2. Jinja2 untuk FastAPI,
3. Integrasi HTML + CSS + JS + FastAPI.
