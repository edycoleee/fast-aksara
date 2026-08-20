**Cheat Sheet CSS Layout **  

# 🟩 0. **Template** — halaman minimal html
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

---

# 🟩 1. **Display** — dasar semua layout

### Jenis utama:
- **block** — turun baris, bisa width/height  
- **inline** — sebaris, tidak bisa width/height  
- **inline-block** — sebaris + bisa width/height  
- **flex** — layout baris/kolom modern  
- **grid** — layout kompleks  
- **none** — sembunyikan elemen  
- **contents** — wrapper hilang, isi tetap tampil  

---

# 🟦 2. **Flexbox** — layout paling sering dipakai

### Properti penting:
- `flex-direction: row | column`  
- `justify-content: center | space-between | flex-end`  
- `align-items: center | flex-start | stretch`  
- `flex-wrap: wrap`  
- `gap: 10px`  

### Contoh dasar:
```css
.container {
  display: flex;
  flex-direction: row;
  gap: 10px;
}
```

**5 contoh Flexbox dari dasar sampai mahir**
---

# 🟩 1) **Dasar: Susunan Baris**  
Tujuan: Elemen tersusun **horizontal** dengan jarak rapi.

### HTML
```html
<div class="container">
  <div class="box">A</div>
  <div class="box">B</div>
  <div class="box">C</div>
</div>
```

### CSS
```css
.container {
  display: flex;        /* aktifkan flexbox */
  flex-direction: row;  /* susunan ke samping */
  gap: 10px;            /* jarak antar elemen */
}

.box {
  background: lightblue;
  padding: 20px;
}
```

### Keterangan  
- `display: flex` = mengubah container jadi flexbox  
- `flex-direction: row` = anak-anaknya tersusun ke samping  
- `gap` = jarak otomatis antar elemen  

---

# 🟩 2) **Responsif: Baris → Kolom**  
Tujuan: Menu bar berubah jadi **tumpukan vertikal** saat layar kecil.

### HTML
```html
<div class="nav">
  <a>Home</a>
  <a>About</a>
  <a>Contact</a>
</div>
```

### CSS
```css
.nav {
  display: flex;
  flex-direction: row;
  gap: 15px;
}

@media (max-width: 600px) {
  .nav {
    flex-direction: column; /* berubah jadi vertikal */
  }
}
```

### Keterangan  
- Flexbox bisa digabung dengan **media query** untuk responsif.  
- Di layar kecil, menu otomatis jadi vertikal.

---

# 🟩 3) **Centering: Tengah Horizontal + Vertikal**  
Tujuan: Kotak berada **tepat di tengah** (paling sering dipakai).

### HTML
```html
<div class="wrapper">
  <div class="box">Tengah</div>
</div>
```

### CSS
```css
.wrapper {
  display: flex;
  justify-content: center; /* tengah horizontal */
  align-items: center;     /* tengah vertikal */
  height: 300px;
  background: #eee;
}

.box {
  padding: 20px;
  background: orange;
}
```

### Keterangan  
- `justify-content` = mengatur posisi horizontal  
- `align-items` = mengatur posisi vertikal  
- Kombinasi keduanya = elemen benar-benar di tengah

---

# 🟩 4) **Wrap: Grid Otomatis**  
Tujuan: Elemen otomatis turun ke baris berikutnya jika penuh.

### HTML
```html
<div class="gallery">
  <div class="item">1</div>
  <div class="item">2</div>
  <div class="item">3</div>
  <div class="item">4</div>
  <div class="item">5</div>
</div>
```

### CSS
```css
.gallery {
  display: flex;
  flex-wrap: wrap; /* turun ke baris berikutnya */
  gap: 10px;
}

.item {
  width: 120px;
  height: 80px;
  background: lightgreen;
  display: flex;
  justify-content: center;
  align-items: center;
}
```

### Keterangan  
- `flex-wrap: wrap` = elemen tidak dipaksa satu baris  
- Cocok untuk **gallery**, **produk**, **kartu-kartu**

---

# 🟩 5) **Mahir: Header dengan 3 Bagian**  
Tujuan: Logo kiri, menu tengah, tombol kanan.

### HTML
```html
<div class="header">
  <div class="logo">LOGO</div>
  <div class="menu">
    <a>Home</a>
    <a>Services</a>
    <a>Contact</a>
  </div>
  <div class="action">
    <button>Login</button>
  </div>
</div>
```

### CSS
```css
.header {
  display: flex;
  justify-content: space-between; /* jarak otomatis */
  align-items: center;            /* rata tengah vertikal */
  padding: 15px;
  background: #f5f5f5;
}

.logo { flex: 1; }

.menu {
  flex: 2;
  display: flex;
  gap: 20px;
}

.action {
  flex: 1;
  text-align: right;
}
```

### Keterangan  
- `space-between` = elemen kiri–tengah–kanan otomatis merenggang  
- `flex: 1 / 2 / 1` = pembagian ruang  
- Teknik ini dipakai di **navbar modern**

---

---

# 🟧 3. **Grid** — layout paling kuat

### Properti penting:
- `grid-template-columns: repeat(3, 1fr)`  
- `grid-template-rows`  
- `gap`  
- `place-items: center`  

### Contoh:
```css
.grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 20px;
}
```

**5 contoh CSS Grid dari dasar → mahir**

---

# 🟩 1) **Dasar: 3 kolom sama rata**  
Tujuan: Membuat layout 3 kolom sederhana.

### HTML
```html
<div class="grid">
  <div class="item">A</div>
  <div class="item">B</div>
  <div class="item">C</div>
</div>
```

### CSS
```css
.grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr; /* 3 kolom */
  gap: 20px;
}

.item {
  background: lightblue;
  padding: 20px;
}
```

### Keterangan  
- `1fr` = membagi ruang sama rata  
- Cocok untuk layout card sederhana  

---

# 🟩 2) **Grid dengan repeat()**  
Tujuan: Membuat kolom otomatis tanpa menulis 1fr berkali-kali.

### HTML
```html
<div class="grid">
  <div class="item">1</div>
  <div class="item">2</div>
  <div class="item">3</div>
  <div class="item">4</div>
</div>
```

### CSS
```css
.grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* 4 kolom otomatis */
  gap: 10px;
}

.item {
  background: salmon;
  padding: 20px;
}
```

### Keterangan  
- `repeat(4, 1fr)` = 4 kolom dengan ukuran sama  
- Lebih rapi dan mudah dibaca  

---

# 🟩 3) **Centering dengan place-items**  
Tujuan: Elemen di dalam grid berada tepat di tengah.

### HTML
```html
<div class="center-grid">
  <div class="box">Tengah</div>
</div>
```

### CSS
```css
.center-grid {
  display: grid;
  place-items: center; /* tengah horizontal + vertikal */
  height: 300px;
  background: #eee;
}

.box {
  background: orange;
  padding: 20px;
}
```

### Keterangan  
- `place-items: center` = gabungan `justify-items` + `align-items`  
- Cara paling cepat untuk centering  

---

# 🟩 4) **Grid otomatis responsif (auto-fit)**  
Tujuan: Card otomatis menyesuaikan ukuran layar.

### HTML
```html
<div class="auto-grid">
  <div class="card">1</div>
  <div class="card">2</div>
  <div class="card">3</div>
  <div class="card">4</div>
</div>
```

### CSS
```css
.auto-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 15px;
}

.card {
  background: lightgreen;
  padding: 20px;
}
```

### Keterangan  
- `auto-fit` = jumlah kolom menyesuaikan layar  
- `minmax(150px, 1fr)` = ukuran minimum 150px, maksimum fleksibel  
- Cocok untuk gallery, produk, dashboard  

---

# 🟩 5) **Mahir: Layout website lengkap**  
Tujuan: Membuat layout website dengan header, sidebar, content, footer.

### HTML
```html
<div class="layout">
  <header class="header">Header</header>
  <aside class="sidebar">Sidebar</aside>
  <main class="content">Content</main>
  <footer class="footer">Footer</footer>
</div>
```

### CSS
```css
.layout {
  display: grid;
  grid-template-columns: 200px 1fr; /* sidebar + konten */
  grid-template-rows: 80px 1fr 60px; /* header, isi, footer */
  gap: 10px;
  height: 100vh;
}

.header {
  grid-column: 1 / 3; /* melebar 2 kolom */
  background: #ddd;
}

.sidebar {
  background: #ccc;
}

.content {
  background: #eee;
}

.footer {
  grid-column: 1 / 3; /* melebar 2 kolom */
  background: #ddd;
}
```

### Keterangan  
- `grid-column: 1 / 3` = elemen melebar dari kolom 1 sampai 2  
- Teknik ini dipakai untuk layout website modern  
- Grid sangat cocok untuk struktur halaman besar  

---

---

# 🟥 4. **Positioning** — mengatur posisi elemen

### Jenis:
- **static** — default  
- **relative** — bisa digeser  
- **absolute** — posisi relatif ke parent  
- **fixed** — menempel di layar  
- **sticky** — nempel saat scroll  

### Contoh:
```css
.box {
  position: absolute;
  top: 20px;
  left: 10px;
}
```
---

# 🟩 1) **Dasar: Position static (default)**  
Tujuan: Elemen mengikuti alur normal halaman.

### HTML
```html
<div class="box">Static Position</div>
```

### CSS
```css
.box {
  position: static; /* default */
  background: lightblue;
  padding: 20px;
}
```

### Keterangan  
- Tidak bisa digeser dengan `top`, `left`, dll.  
- Semua elemen HTML default-nya static.

---

# 🟩 2) **Relative: Bisa digeser sedikit**  
Tujuan: Menggeser elemen dari posisi normalnya.

### HTML
```html
<div class="box">Relative</div>
```

### CSS
```css
.box {
  position: relative;
  top: 10px;   /* geser ke bawah */
  left: 20px;  /* geser ke kanan */
  background: salmon;
  padding: 20px;
}
```

### Keterangan  
- Elemen tetap “ada di tempatnya”, tapi digeser sedikit.  
- Sering dipakai sebagai **parent** untuk absolute.

---

# 🟩 3) **Absolute: Posisi bebas relatif ke parent**  
Tujuan: Elemen bisa ditempatkan di mana saja dalam parent.

### HTML
```html
<div class="parent">
  <div class="child">Absolute</div>
</div>
```

### CSS
```css
.parent {
  position: relative; /* wajib untuk referensi */
  width: 300px;
  height: 200px;
  background: #eee;
}

.child {
  position: absolute;
  top: 20px;
  right: 20px;
  background: lightgreen;
  padding: 10px;
}
```

### Keterangan  
- `absolute` akan mengikuti **parent yang relative**.  
- Cocok untuk badge, popup kecil, label, dll.

---

# 🟩 4) **Fixed: Menempel di layar saat scroll**  
Tujuan: Elemen tetap terlihat walaupun halaman di-scroll.

### HTML
```html
<div class="fixed-box">Fixed</div>
```

### CSS
```css
.fixed-box {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background: orange;
  padding: 15px;
}
```

### Keterangan  
- Selalu berada di posisi yang sama di layar.  
- Dipakai untuk tombol **chat**, **back to top**, **floating button**.

---

# 🟩 5) **Sticky: Nempel saat scroll, tapi tidak selalu**  
Tujuan: Elemen menempel di atas saat melewati batas tertentu.

### HTML
```html
<div class="sticky-header">Sticky Header</div>

<p>Konten panjang...</p>
<p>Konten panjang...</p>
<p>Konten panjang...</p>
```

### CSS
```css
.sticky-header {
  position: sticky;
  top: 0; /* batas nempel */
  background: #333;
  color: white;
  padding: 15px;
}
```

### Keterangan  
- Sticky hanya aktif **saat elemen mencapai posisi top**.  
- Cocok untuk header, menu kategori, filter produk.

---

## 🟪 Ringkasan Level Positioning
- **Static** → default  
- **Relative** → geser sedikit  
- **Absolute** → posisi bebas dalam parent  
- **Fixed** → selalu menempel di layar  
- **Sticky** → menempel saat scroll  

---

---

# 🟪 5. **Border** — garis luar elemen

### Komponen:
- `border-width`  
- `border-style`  
- `border-color`  
- `border-radius`  

### Contoh:
```css
.card {
  border: 3px solid blue;
  border-radius: 10px;
}
```
**5 contoh Border dari dasar → mahir**

---

# 🟩 1) **Dasar: Border sederhana**  
Tujuan: Membuat garis luar dasar.

### HTML
```html
<div class="box">Border Dasar</div>
```

### CSS
```css
.box {
  border: 2px solid black; /* tebal + style + warna */
  padding: 20px;
}
```

### Keterangan  
- `solid` = garis penuh  
- Cocok untuk card sederhana  

---

# 🟩 2) **Border warna + tebal**  
Tujuan: Mengatur warna dan ketebalan secara terpisah.

### HTML
```html
<div class="box2">Border Warna</div>
```

### CSS
```css
.box2 {
  border-width: 5px;
  border-style: dashed;
  border-color: red;
  padding: 20px;
}
```

### Keterangan  
- `dashed` = garis putus-putus  
- Bisa diganti `dotted`, `double`, dll.

---

# 🟩 3) **Border per sisi**  
Tujuan: Mengatur border hanya di sisi tertentu.

### HTML
```html
<div class="box3">Border Sisi Tertentu</div>
```

### CSS
```css
.box3 {
  border-top: 4px solid blue;
  border-bottom: 4px solid green;
  padding: 20px;
}
```

### Keterangan  
- Bisa pakai `border-left` dan `border-right`  
- Cocok untuk desain garis header atau section

---

# 🟩 4) **Border radius: sudut melengkung**  
Tujuan: Membuat elemen lebih halus dan modern.

### HTML
```html
<div class="box4">Rounded</div>
```

### CSS
```css
.box4 {
  border: 3px solid purple;
  border-radius: 15px; /* sudut melengkung */
  padding: 20px;
}
```

### Keterangan  
- `border-radius` bisa angka kecil (kotak) atau besar (oval)  
- Dipakai untuk tombol, card, foto profil

---

# 🟩 5) **Mahir: Card modern dengan shadow + radius**  
Tujuan: Membuat card modern seperti UI website.

### HTML
```html
<div class="card">
  <h3>Judul Card</h3>
  <p>Ini contoh card modern.</p>
</div>
```

### CSS
```css
.card {
  border: 2px solid #ddd;
  border-radius: 12px;
  padding: 20px;
  background: white;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1); /* bayangan */
  width: 250px;
}
```

### Keterangan  
- `border-radius` = sudut lembut  
- `box-shadow` = efek bayangan modern  
- Dipakai untuk UI dashboard, profile card, produk

---

## 🟪 Ringkasan Border
- **Width** → ketebalan  
- **Style** → jenis garis  
- **Color** → warna  
- **Radius** → sudut melengkung  

---

---

# 🟩 6. **Gap** — jarak antar elemen (flex & grid)

```css
.container {
  display: flex;
  gap: 15px;
}
```
**5 contoh penggunaan `gap` dari dasar → mahir**

---

# 🟩 1) **Dasar: Gap pada Flexbox**  
Tujuan: Membuat jarak antar elemen flex tanpa margin.

### HTML
```html
<div class="container">
  <div class="item">A</div>
  <div class="item">B</div>
  <div class="item">C</div>
</div>
```

### CSS
```css
.container {
  display: flex;
  gap: 15px; /* jarak antar elemen */
}

.item {
  background: lightblue;
  padding: 20px;
}
```

### Keterangan  
- `gap` bekerja otomatis untuk semua anak elemen  
- Lebih rapi daripada pakai `margin-right`

---

# 🟩 2) **Gap pada Grid**  
Tujuan: Memberi jarak antar kolom dan baris grid.

### HTML
```html
<div class="grid">
  <div class="box">1</div>
  <div class="box">2</div>
  <div class="box">3</div>
</div>
```

### CSS
```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px; /* jarak antar kolom & baris */
}

.box {
  background: salmon;
  padding: 20px;
}
```

### Keterangan  
- `gap` di grid mengatur **kolom dan baris sekaligus**

---

# 🟩 3) **Row-gap & Column-gap**  
Tujuan: Mengatur jarak baris dan kolom secara terpisah.

### HTML
```html
<div class="grid2">
  <div class="box">A</div>
  <div class="box">B</div>
  <div class="box">C</div>
  <div class="box">D</div>
</div>
```

### CSS
```css
.grid2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  row-gap: 30px;     /* jarak antar baris */
  column-gap: 10px;  /* jarak antar kolom */
}

.box {
  background: lightgreen;
  padding: 20px;
}
```

### Keterangan  
- Cocok untuk layout yang jarak barisnya lebih besar dari kolom.

---

# 🟩 4) **Gap pada Flex Wrap**  
Tujuan: Membuat jarak rapi pada elemen yang turun ke baris berikutnya.

### HTML
```html
<div class="wrap">
  <div class="item">1</div>
  <div class="item">2</div>
  <div class="item">3</div>
  <div class="item">4</div>
  <div class="item">5</div>
</div>
```

### CSS
```css
.wrap {
  display: flex;
  flex-wrap: wrap;
  gap: 15px; /* jarak antar elemen di semua baris */
}

.item {
  width: 100px;
  height: 60px;
  background: #ddd;
  display: flex;
  justify-content: center;
  align-items: center;
}
```

### Keterangan  
- `gap` tetap bekerja walaupun elemen pindah baris  
- Lebih bersih daripada margin yang sering bikin layout “geser”

---

# 🟩 5) **Mahir: Gap + Grid Auto-fit (responsif)**  
Tujuan: Membuat gallery responsif dengan jarak rapi.

### HTML
```html
<div class="gallery">
  <div class="pic">Foto 1</div>
  <div class="pic">Foto 2</div>
  <div class="pic">Foto 3</div>
  <div class="pic">Foto 4</div>
</div>
```

### CSS
```css
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 20px; /* jarak antar card */
}

.pic {
  background: #eee;
  padding: 30px;
  text-align: center;
}
```

### Keterangan  
- `auto-fit` membuat jumlah kolom menyesuaikan layar  
- `gap` menjaga jarak tetap konsisten di semua ukuran layar  
- Dipakai untuk gallery, produk, dashboard modern

---

## 🟪 Ringkasan Gap
- **Flexbox** → jarak antar item horizontal/vertical  
- **Grid** → jarak antar kolom & baris  
- **Row-gap / Column-gap** → jarak spesifik  
- **Wrap** → tetap rapi walau turun baris  
- **Auto-fit + gap** → layout responsif modern  

---

---

# 🟦 7. **Margin & Padding** — jarak luar & dalam

### Margin (luar)
```css
.box {
  margin: 20px;
}
```

### Padding (dalam)
```css
.box {
  padding: 20px;
}
```

**5 contoh Margin & Padding dari dasar → mahir**

---

# 🟩 1) **Dasar: Margin & Padding sederhana**  
Tujuan: Memahami perbedaan jarak luar dan dalam.

### HTML
```html
<div class="box">Isi Box</div>
```

### CSS
```css
.box {
  margin: 20px;   /* jarak luar */
  padding: 20px;  /* jarak dalam */
  background: lightblue;
}
```

### Keterangan  
- Margin = jarak antara elemen dengan elemen lain  
- Padding = jarak antara isi dengan batas elemen  

---

# 🟩 2) **Margin per sisi**  
Tujuan: Mengatur margin atas, kanan, bawah, kiri secara terpisah.

### HTML
```html
<div class="box2">Margin Per Sisi</div>
```

### CSS
```css
.box2 {
  margin-top: 30px;
  margin-right: 10px;
  margin-bottom: 20px;
  margin-left: 5px;
  background: salmon;
  padding: 10px;
}
```

### Keterangan  
- Cocok untuk mengatur jarak elemen yang tidak simetris  

---

# 🟩 3) **Padding per sisi**  
Tujuan: Mengatur ruang dalam secara detail.

### HTML
```html
<div class="box3">Padding Per Sisi</div>
```

### CSS
```css
.box3 {
  padding-top: 20px;
  padding-right: 40px;
  padding-bottom: 10px;
  padding-left: 5px;
  background: lightgreen;
}
```

### Keterangan  
- Dipakai untuk membuat isi elemen lebih “lega”  

---

# 🟩 4) **Margin auto untuk center**  
Tujuan: Membuat elemen berada di tengah secara otomatis.

### HTML
```html
<div class="center-box">Center</div>
```

### CSS
```css
.center-box {
  width: 200px;
  margin: 0 auto; /* center horizontal */
  padding: 20px;
  background: orange;
}
```

### Keterangan  
- `margin: auto` = cara paling mudah untuk center elemen blok  

---

# 🟩 5) **Mahir: Card modern dengan padding + margin**  
Tujuan: Membuat card modern seperti UI website.

### HTML
```html
<div class="card">
  <h3>Judul Card</h3>
  <p>Ini contoh card modern dengan margin & padding.</p>
</div>
```

### CSS
```css
.card {
  margin: 30px auto;        /* jarak luar + center */
  padding: 25px;            /* ruang dalam */
  width: 300px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}
```

### Keterangan  
- Margin untuk jarak antar card  
- Padding untuk ruang dalam card  
- Kombinasi radius + shadow = tampilan modern  

---

## 🟪 Ringkasan Margin & Padding
- **Margin** → jarak luar  
- **Padding** → jarak dalam  
- Bisa per sisi: top/right/bottom/left  
- `margin: auto` → center elemen  
- Kombinasi margin + padding = layout rapi & modern  

---

---

# 🟧 8. **Color** — warna teks & background

### Warna teks:
```css
p {
  color: red;
}
```

### Background:
```css
div {
  background-color: #f0f0f0;
}
```

### Format warna:
- Nama: `red`, `blue`  
- Hex: `#ff0000`  
- RGB: `rgb(255, 0, 0)`  
- RGBA: `rgba(255, 0, 0, 0.5)`  
- HSL: `hsl(0, 100%, 50%)`

---

**5 contoh dari dasar → mahir**

---

# 🟩 1) **Dasar: Warna teks**  
Tujuan: Mengubah warna teks sederhana.

### HTML
```html
<p class="text">Ini warna merah.</p>
```

### CSS
```css
.text {
  color: red; /* warna teks */
}
```

### Keterangan  
- `color` hanya mengubah **teks**, bukan background.

---

# 🟩 2) **Background-color dasar**  
Tujuan: Memberi warna latar belakang elemen.

### HTML
```html
<div class="box">Background abu-abu</div>
```

### CSS
```css
.box {
  background-color: #f0f0f0; /* warna background */
  padding: 20px;
}
```

### Keterangan  
- Hex (`#f0f0f0`) adalah format warna paling umum di UI modern.

---

# 🟩 3) **RGB & RGBA (warna + transparansi)**  
Tujuan: Membuat warna dengan nilai angka + transparansi.

### HTML
```html
<div class="rgba-box">RGBA Transparan</div>
```

### CSS
```css
.rgba-box {
  background-color: rgba(255, 0, 0, 0.4); /* merah transparan */
  padding: 20px;
}
```

### Keterangan  
- `rgba` = red, green, blue, alpha (transparansi)  
- Alpha 0.0 = transparan, 1.0 = solid

---

# 🟩 4) **HSL: Hue, Saturation, Lightness**  
Tujuan: Mengatur warna berdasarkan sudut warna.

### HTML
```html
<div class="hsl-box">HSL Color</div>
```

### CSS
```css
.hsl-box {
  background-color: hsl(200, 80%, 50%); /* biru cerah */
  padding: 20px;
}
```

### Keterangan  
- HSL lebih mudah untuk membuat **tema warna**  
- Hue = 0–360 derajat (merah → hijau → biru)

---

# 🟩 5) **Mahir: Tema warna gelap & terang**  
Tujuan: Membuat mode gelap & terang dengan variable CSS.

### HTML
```html
<div class="card">
  <h3>Judul</h3>
  <p>Contoh tema warna.</p>
</div>
```

### CSS
```css
:root {
  --bg-light: #ffffff;
  --text-light: #333;
  --bg-dark: #1e1e1e;
  --text-dark: #f5f5f5;
}

.card {
  background: var(--bg-light);
  color: var(--text-light);
  padding: 20px;
  border-radius: 10px;
}

/* Mode gelap */
body.dark .card {
  background: var(--bg-dark);
  color: var(--text-dark);
}
```

### Keterangan  
- `var(--nama)` = variable warna  
- Dipakai untuk **dark mode**, **theme switcher**, **UI modern**

---

## 🟪 Ringkasan Color
- `color` → warna teks  
- `background-color` → warna latar  
- Format warna: **nama**, **hex**, **rgb**, **rgba**, **hsl**  
- RGBA = transparansi  
- HSL = mudah untuk membuat tema warna  
- Variable CSS = dasar untuk dark mode

---

# 🟥 9. **Width & Height**

```css
.box {
  width: 200px;
  height: 100px;
}
```

### Satuan:
- px  
- %  
- rem  
- vh / vw  

---

**5 contoh dari dasar → mahir**

---

# 🟩 1) **Dasar: Width & Height px**  
Tujuan: Mengatur ukuran elemen secara tetap.

### HTML
```html
<div class="box">Kotak</div>
```

### CSS
```css
.box {
  width: 200px;
  height: 100px;
  background: lightblue;
}
```

### Keterangan  
- `px` = ukuran tetap  
- Cocok untuk elemen yang tidak perlu responsif  

---

# 🟩 2) **Persentase: Width % mengikuti parent**  
Tujuan: Membuat elemen fleksibel mengikuti lebar parent.

### HTML
```html
<div class="parent">
  <div class="child">Persen</div>
</div>
```

### CSS
```css
.parent {
  width: 400px;
  background: #eee;
}

.child {
  width: 50%; /* setengah dari parent */
  height: 80px;
  background: salmon;
}
```

### Keterangan  
- `%` = relatif terhadap ukuran parent  
- Cocok untuk layout responsif  

---

# 🟩 3) **rem: ukuran berdasarkan font root**  
Tujuan: Ukuran konsisten di seluruh website.

### HTML
```html
<div class="rem-box">REM</div>
```

### CSS
```css
.rem-box {
  width: 20rem;  /* 20 × ukuran font root */
  height: 10rem;
  background: lightgreen;
}
```

### Keterangan  
- 1 rem = ukuran font `<html>` (biasanya 16px)  
- Dipakai untuk desain yang konsisten  

---

# 🟩 4) **Viewport: vw & vh**  
Tujuan: Ukuran mengikuti layar (viewport).

### HTML
```html
<div class="viewport-box">Viewport</div>
```

### CSS
```css
.viewport-box {
  width: 50vw;  /* 50% dari lebar layar */
  height: 30vh; /* 30% dari tinggi layar */
  background: orange;
}
```

### Keterangan  
- `vw` = viewport width  
- `vh` = viewport height  
- Cocok untuk hero section, banner, fullscreen layout  

---

# 🟩 5) **Mahir: Min/Max Width & Height**  
Tujuan: Membuat elemen responsif tapi tetap punya batas ukuran.

### HTML
```html
<div class="card">
  <p>Card dengan min/max width</p>
</div>
```

### CSS
```css
.card {
  min-width: 200px;  /* batas minimum */
  max-width: 500px;  /* batas maksimum */
  height: auto;      /* tinggi mengikuti isi */
  padding: 20px;
  background: #fff;
  border: 1px solid #ccc;
}
```

### Keterangan  
- `min-width` mencegah elemen terlalu kecil  
- `max-width` mencegah elemen terlalu besar  
- Dipakai untuk card, artikel, container layout  

---

## 🟪 Ringkasan Width & Height
- **px** → ukuran tetap  
- **%** → mengikuti parent  
- **rem** → konsisten berdasarkan font root  
- **vw/vh** → mengikuti ukuran layar  
- **min/max-width** → kontrol responsif modern  

---

# 🟪 10. **Typography**

```css
.text {
  font-size: 18px;
  font-weight: bold;
  line-height: 1.5;
  text-align: center;
}
```
---

**5 contoh dari dasar → mahir**

---

# 🟩 1) **Dasar: Font-size, weight, line-height**  
Tujuan: Mengatur ukuran, ketebalan, dan jarak antar baris.

### HTML
```html
<p class="text">Ini contoh teks dasar.</p>
```

### CSS
```css
.text {
  font-size: 18px;     /* ukuran teks */
  font-weight: bold;   /* ketebalan */
  line-height: 1.5;    /* jarak antar baris */
  text-align: center;  /* rata tengah */
}
```

### Keterangan  
- `font-size` = ukuran huruf  
- `font-weight` = ketebalan (normal, bold, 100–900)  
- `line-height` = jarak antar baris  

---

# 🟩 2) **Font-family: memilih jenis font**  
Tujuan: Mengubah gaya huruf.

### HTML
```html
<p class="font">Font Family</p>
```

### CSS
```css
.font {
  font-family: "Arial", sans-serif;
  font-size: 20px;
}
```

### Keterangan  
- `sans-serif` = modern  
- `serif` = klasik  
- Bisa pakai Google Fonts juga  

---

# 🟩 3) **Text-transform: uppercase, lowercase, capitalize**  
Tujuan: Mengatur gaya huruf otomatis.

### HTML
```html
<p class="transform">contoh text transform</p>
```

### CSS
```css
.transform {
  text-transform: uppercase; /* jadi huruf besar semua */
}
```

### Keterangan  
- `uppercase` → BESAR  
- `lowercase` → kecil  
- `capitalize` → Huruf Awal Besar  

---

# 🟩 4) **Letter-spacing & word-spacing**  
Tujuan: Mengatur jarak antar huruf dan kata.

### HTML
```html
<p class="spacing">Jarak huruf dan kata</p>
```

### CSS
```css
.spacing {
  letter-spacing: 2px; /* jarak antar huruf */
  word-spacing: 10px;  /* jarak antar kata */
}
```

### Keterangan  
- Cocok untuk judul, banner, desain modern  

---

# 🟩 5) **Mahir: Heading hierarchy + line-height + weight**  
Tujuan: Membuat struktur teks profesional seperti website.

### HTML
```html
<div class="article">
  <h1>Judul Utama</h1>
  <h2>Subjudul</h2>
  <p>Ini adalah paragraf dengan typografi yang nyaman dibaca.</p>
</div>
```

### CSS
```css
.article h1 {
  font-size: 32px;
  font-weight: 700;
  line-height: 1.2;
}

.article h2 {
  font-size: 24px;
  font-weight: 600;
  margin-top: 10px;
}

.article p {
  font-size: 16px;
  line-height: 1.6;
  color: #444;
}
```

### Keterangan  
- Heading punya **hierarki** (H1 > H2 > H3)  
- Paragraf dibuat nyaman dengan `line-height`  
- Warna teks sedikit gelap (`#444`) lebih enak dibaca  

---

## 🟪 Ringkasan Typography
- **font-size** → ukuran huruf  
- **font-weight** → ketebalan  
- **line-height** → kenyamanan membaca  
- **font-family** → jenis font  
- **text-transform** → gaya huruf otomatis  
- **letter/word-spacing** → jarak huruf & kata  
- **hierarki heading** → struktur teks profesional  

---

# 🟩 11. **Overflow**

```css
.box {
  overflow: hidden; /* scroll, auto */
}
```
---

# 1️⃣ **Latihan Overflow Hidden**  
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Overflow Hidden</title>
  <style>
    .box {
      width: 250px;
      height: 100px;
      border: 2px solid #333;
      padding: 10px;
      overflow: hidden;
      background: #fff;
    }
  </style>
</head>
<body>
  <h2>1. Overflow: hidden</h2>

  <div class="box">
    Ini teks sangat panjang yang akan terpotong karena overflow hidden.
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore.
  </div>
</body>
</html>
```

---

# 2️⃣ **Latihan Overflow Scroll**  
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Overflow Scroll</title>
  <style>
    .box {
      width: 250px;
      height: 100px;
      border: 2px solid #333;
      padding: 10px;
      overflow: scroll;
      background: #fff;
    }
  </style>
</head>
<body>
  <h2>2. Overflow: scroll</h2>

  <div class="box">
    Ini teks panjang yang memaksa scrollbar muncul meskipun tidak diperlukan.
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore.
  </div>
</body>
</html>
```

---

# 3️⃣ **Latihan Overflow Auto**  
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Overflow Auto</title>
  <style>
    .box {
      width: 250px;
      height: 100px;
      border: 2px solid #333;
      padding: 10px;
      overflow: auto;
      background: #fff;
    }
  </style>
</head>
<body>
  <h2>3. Overflow: auto</h2>

  <div class="box">
    Scrollbar hanya muncul jika konten benar-benar panjang.
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore.
  </div>
</body>
</html>
```

---

# 4️⃣ **Latihan Overflow-x & Overflow-y**  
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Overflow X & Y</title>
  <style>
    .box {
      width: 250px;
      height: 100px;
      border: 2px solid #333;
      padding: 10px;
      overflow-x: scroll;
      overflow-y: hidden;
      white-space: nowrap;
      background: #fff;
    }
  </style>
</head>
<body>
  <h2>4. Overflow-x scroll & overflow-y hidden</h2>

  <div class="box">
    Ini contoh teks panjang horizontal → → → → → → → → → → → → → → → → → → → →
  </div>
</body>
</html>
```

---

# 5️⃣ **Latihan Scroll Snap (Level Mahir)**  
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Scroll Snap</title>
  <style>
    .container {
      width: 100%;
      height: 200px;
      overflow-x: auto;
      display: flex;
      gap: 20px;
      scroll-snap-type: x mandatory;
      border: 2px solid #333;
      padding: 10px;
      background: #fff;
    }

    .item {
      flex: 0 0 200px;
      height: 180px;
      background: #4caf50;
      border-radius: 10px;
      scroll-snap-align: start;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-size: 24px;
    }
  </style>
</head>
<body>
  <h2>5. Scroll Snap (mahir)</h2>

  <div class="container">
    <div class="item">1</div>
    <div class="item">2</div>
    <div class="item">3</div>
    <div class="item">4</div>
  </div>
</body>
</html>
```


---

# 🟦 12. **Z-index** — urutan lapisan

```css
.modal {
  position: absolute;
  z-index: 999;
}
```
Keren, kita naik ke **z-index**—ini konsep “lapisan” yang sering bikin orang bingung. Aku buat **5 script HTML terpisah**, dari **dasar → mahir**, plus keterangan detail tiap latihan.

---

### 1️⃣ Dasar: z-index tanpa `position` (tidak berfungsi)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 1 - Z-index tanpa position</title>
  <style>
    .box {
      width: 150px;
      height: 150px;
      position: static; /* default */
    }

    .red {
      background: red;
      z-index: 10; /* TIDAK berpengaruh karena tidak positioned */
    }

    .blue {
      background: blue;
      margin-top: -100px;
    }
  </style>
</head>
<body>
  <h2>1. Z-index tanpa position (tidak bekerja)</h2>
  <p>Di sini, <strong>z-index tidak berfungsi</strong> karena elemen tidak punya posisi selain default (static).</p>

  <div class="box red"></div>
  <div class="box blue"></div>
</body>
</html>
```

**Penjelasan singkat:**  
`z-index` hanya bekerja pada elemen yang punya `position: relative | absolute | fixed | sticky`. Latihan ini untuk menunjukkan “kenapa kok z-index kadang nggak ngaruh”.

---

### 2️⃣ Dasar: z-index dengan `position: relative`

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 2 - Z-index dengan position relative</title>
  <style>
    .box {
      width: 150px;
      height: 150px;
      position: relative;
    }

    .red {
      background: red;
      z-index: 1;
    }

    .blue {
      background: blue;
      margin-top: -100px;
      z-index: 2; /* biru di atas merah */
    }
  </style>
</head>
<body>
  <h2>2. Z-index dengan position: relative</h2>
  <p>Di sini, <strong>kotak biru</strong> muncul di atas kotak merah karena z-index lebih besar.</p>

  <div class="box red"></div>
  <div class="box blue"></div>
</body>
</html>
```

**Penjelasan:**  
Begitu elemen diberi `position: relative`, `z-index` mulai berfungsi. Urutan lapisan ditentukan oleh angka—semakin besar, semakin “di depan”.

---

### 3️⃣ Menengah: modal di atas overlay

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 3 - Modal dan Overlay</title>
  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
    }

    .content {
      padding: 20px;
    }

    .overlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.5);
      z-index: 10;
    }

    .modal {
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 300px;
      padding: 20px;
      background: white;
      z-index: 20; /* di atas overlay */
      box-shadow: 0 0 10px rgba(0,0,0,0.5);
    }
  </style>
</head>
<body>
  <h2 style="padding:20px;">3. Modal di atas overlay</h2>

  <div class="content">
    <p>Ini konten halaman di belakang.</p>
  </div>

  <div class="overlay"></div>

  <div class="modal">
    <h3>Modal</h3>
    <p>Modal ini berada di atas overlay karena z-index lebih besar.</p>
  </div>
</body>
</html>
```

**Penjelasan:**  
- **Overlay**: menutupi halaman, z-index `10`.  
- **Modal**: kotak dialog di atas overlay, z-index `20`.  
Ini pola klasik di UI: overlay + modal.

---

### 4️⃣ Lanjutan: z-index dan stacking context (parent mempengaruhi)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 4 - Stacking Context</title>
  <style>
    .parent-a, .parent-b {
      position: relative;
      width: 200px;
      height: 200px;
      margin: 20px;
      display: inline-block;
    }

    .parent-a {
      background: #eee;
      z-index: 5; /* parent A di depan parent B */
    }

    .parent-b {
      background: #ddd;
      z-index: 1;
    }

    .child-a {
      position: absolute;
      width: 100px;
      height: 100px;
      background: red;
      top: 50px;
      left: 50px;
      z-index: 1; /* anak A */
    }

    .child-b {
      position: absolute;
      width: 100px;
      height: 100px;
      background: blue;
      top: -30px;
      left: 100px;
      z-index: 999; /* besar, tapi tetap kalah kalau parent di belakang */
    }
  </style>
</head>
<body>
  <h2>4. Z-index & Stacking Context (parent berpengaruh)</h2>
  <p>Perhatikan: meskipun child biru punya z-index besar, ia tetap di belakang jika parent-nya punya z-index kecil.</p>

  <div class="parent-a">
    Parent A (z-index: 5)
    <div class="child-a">A</div>
  </div>

  <div class="parent-b">
    Parent B (z-index: 1)
    <div class="child-b">B</div>
  </div>
</body>
</html>
```

**Penjelasan penting:**  
- Setiap elemen dengan `position` + `z-index` bisa membuat **stacking context**.  
- Anak tidak bisa “menembus” parent lain yang punya z-index lebih tinggi.  
- Ini sering jadi sumber bug: “kok z-index 999 masih kalah?”—karena parent-nya.

---

### 5️⃣ Mahir: navbar sticky + dropdown + modal (multi-layer)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 5 - Z-index Level Mahir</title>
  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
    }

    /* Navbar sticky di atas konten */
    .navbar {
      position: sticky;
      top: 0;
      background: #2196f3;
      color: white;
      padding: 10px 20px;
      z-index: 50;
    }

    .dropdown {
      position: relative;
      display: inline-block;
    }

    .dropdown-menu {
      position: absolute;
      top: 30px;
      left: 0;
      background: white;
      color: black;
      padding: 10px;
      border: 1px solid #ccc;
      z-index: 60; /* di atas navbar */
    }

    .content {
      padding: 20px;
      height: 800px;
      background: #f5f5f5;
    }

    /* Overlay & modal di atas semuanya */
    .overlay {
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.5);
      z-index: 90;
    }

    .modal {
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background: white;
      padding: 20px;
      z-index: 100; /* paling depan */
      box-shadow: 0 0 10px rgba(0,0,0,0.5);
    }
  </style>
</head>
<body>
  <div class="navbar">
    Navbar (z-index: 50)
    <div class="dropdown">
      <span>Menu ▼</span>
      <div class="dropdown-menu">
        Dropdown (z-index: 60)
      </div>
    </div>
  </div>

  <div class="content">
    <h2>5. Multi-layer: navbar, dropdown, modal</h2>
    <p>Scroll halaman ini, lihat bagaimana navbar tetap di atas konten.</p>
    <p>Dropdown berada di atas navbar, dan modal + overlay di atas semuanya.</p>
  </div>

  <div class="overlay"></div>
  <div class="modal">
    <h3>Modal Paling Depan</h3>
    <p>Modal ini mengalahkan navbar dan dropdown karena z-index paling tinggi.</p>
  </div>
</body>
</html>
```

**Konsep yang dipakai di sini:**

- **Navbar sticky**: `position: sticky`, z-index `50`.  
- **Dropdown**: `position: absolute` di atas navbar, z-index `60`.  
- **Overlay + modal**: `fixed`, z-index `90` dan `100`, mengalahkan semua.

---

# 🟧 13. **Box Shadow**

```css
.card {
  box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}
```
---

# 1️⃣ **Dasar: Box Shadow sederhana**  
Tujuan: memahami bentuk dasar `box-shadow`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 1 - Box Shadow Dasar</title>
  <style>
    .card {
      width: 200px;
      padding: 20px;
      background: white;
      border: 1px solid #ccc;
      box-shadow: 0 4px 10px rgba(0,0,0,0.2); 
      /* x-offset | y-offset | blur | warna */
    }
  </style>
</head>
<body>
  <h2>1. Box Shadow Dasar</h2>
  <p>Shadow muncul di bawah elemen, lembut dan natural.</p>

  <div class="card">
    Shadow dasar
  </div>
</body>
</html>
```

**Keterangan:**  
- `0` → tidak geser ke kanan/kiri  
- `4px` → geser ke bawah  
- `10px` → blur  
- `rgba(0,0,0,0.2)` → warna hitam transparan  

---

# 2️⃣ **Menengah: Shadow tebal + warna**  
Tujuan: membuat shadow lebih dramatis dan berwarna.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 2 - Shadow Warna</title>
  <style>
    .card {
      width: 200px;
      padding: 20px;
      background: white;
      border-radius: 10px;
      box-shadow: 0 8px 20px rgba(255,0,0,0.4); 
      /* shadow merah */
    }
  </style>
</head>
<body>
  <h2>2. Shadow Warna</h2>
  <p>Shadow bisa berwarna, cocok untuk desain neon atau gaming.</p>

  <div class="card">
    Shadow merah
  </div>
</body>
</html>
```

**Keterangan:**  
- Blur besar → shadow makin lembut  
- Opacity besar → shadow makin terlihat  

---

# 3️⃣ **Lanjutan: Multiple shadow (lebih dari satu)**  
Tujuan: membuat efek glow atau layer shadow.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 3 - Multiple Shadow</title>
  <style>
    .card {
      width: 200px;
      padding: 20px;
      background: white;
      border-radius: 10px;
      box-shadow:
        0 4px 10px rgba(0,0,0,0.2),   /* shadow utama */
        0 0 15px rgba(0,150,255,0.5); /* glow biru */
    }
  </style>
</head>
<body>
  <h2>3. Multiple Shadow</h2>
  <p>Shadow bisa lebih dari satu untuk efek glow atau depth.</p>

  <div class="card">
    Glow + shadow
  </div>
</body>
</html>
```

**Keterangan:**  
- Pisahkan dengan koma  
- Bisa bikin efek neon, glow, depth UI modern  

---

# 4️⃣ **Advance: Inset shadow (shadow di dalam elemen)**  
Tujuan: membuat efek cekung, seperti input field ditekan.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 4 - Inset Shadow</title>
  <style>
    .card {
      width: 200px;
      padding: 20px;
      background: #f0f0f0;
      border-radius: 10px;
      box-shadow: inset 0 4px 10px rgba(0,0,0,0.3);
      /* inset = shadow masuk ke dalam */
    }
  </style>
</head>
<body>
  <h2>4. Inset Shadow</h2>
  <p>Shadow masuk ke dalam, cocok untuk efek cekung.</p>

  <div class="card">
    Inset shadow
  </div>
</body>
</html>
```

**Keterangan:**  
- `inset` → shadow berada di dalam elemen  
- Dipakai untuk efek “pressed”, “inner depth”, atau UI glass  

---

# 5️⃣ **Mahir: Card modern + hover shadow animasi**  
Tujuan: membuat card modern seperti UI dashboard.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 5 - Shadow Modern Hover</title>
  <style>
    .card {
      width: 220px;
      padding: 20px;
      background: white;
      border-radius: 12px;
      transition: box-shadow 0.3s ease, transform 0.3s ease;
      box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }

    .card:hover {
      transform: translateY(-5px);
      box-shadow: 
        0 10px 25px rgba(0,0,0,0.25),
        0 0 20px rgba(0,150,255,0.3);
    }
  </style>
</head>
<body>
  <h2>5. Shadow Modern + Hover</h2>
  <p>Efek card modern: naik sedikit + shadow lebih besar saat hover.</p>

  <div class="card">
    Hover saya
  </div>
</body>
</html>
```

**Keterangan:**  
- `transition` → animasi halus  
- `transform: translateY(-5px)` → card naik  
- Multiple shadow → efek depth + glow  
---

# 🟥 14. **Transition** — animasi halus

```css
.btn {
  transition: 0.3s;
}
```
---

# 1️⃣ **Dasar: Transition tanpa properti (default)**  
Tujuan: memahami bahwa `transition: 0.3s` berarti *semua perubahan* akan dianimasikan.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 1 - Transition Dasar</title>
  <style>
    .btn {
      padding: 15px 25px;
      background: #ff5252;
      color: white;
      border-radius: 8px;
      display: inline-block;
      transition: 0.3s; /* semua perubahan akan halus */
    }

    .btn:hover {
      background: #d50000;
    }
  </style>
</head>
<body>
  <h2>1. Transition Dasar</h2>
  <p>Hover tombol untuk melihat perubahan warna yang halus.</p>

  <div class="btn">Hover saya</div>
</body>
</html>
```

**Keterangan:**  
- Tidak menyebut properti → semua perubahan (warna, ukuran, border) akan dianimasikan.  

---

# 2️⃣ **Menengah: Transition property tertentu**  
Tujuan: mengatur animasi hanya pada properti tertentu.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 2 - Transition Property</title>
  <style>
    .box {
      width: 150px;
      height: 150px;
      background: #2196f3;
      transition: background 0.4s, transform 0.4s;
    }

    .box:hover {
      background: #0d47a1;
      transform: scale(1.1);
    }
  </style>
</head>
<body>
  <h2>2. Transition Property</h2>
  <p>Hanya background dan transform yang dianimasikan.</p>

  <div class="box"></div>
</body>
</html>
```

**Keterangan:**  
- Bisa memilih properti mana yang dianimasikan.  
- Lebih efisien daripada `transition: all`.

---

# 3️⃣ **Lanjutan: Transition + delay**  
Tujuan: membuat animasi yang *tertunda* sebelum berjalan.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 3 - Transition Delay</title>
  <style>
    .card {
      width: 200px;
      padding: 20px;
      background: #fff;
      border-radius: 10px;
      border: 1px solid #ccc;
      transition: transform 0.5s ease 0.3s; 
      /* durasi 0.5s, delay 0.3s */
    }

    .card:hover {
      transform: translateY(-10px);
    }
  </style>
</head>
<body>
  <h2>3. Transition Delay</h2>
  <p>Animasi baru berjalan setelah 0.3 detik.</p>

  <div class="card">Hover saya</div>
</body>
</html>
```

**Keterangan:**  
Format lengkap:  
`transition: property duration timing-function delay;`

---

# 4️⃣ **Advance: Transition + hover keluar (reverse animation)**  
Tujuan: membuat animasi halus saat hover masuk **dan** keluar.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 4 - Transition Reverse</title>
  <style>
    .box {
      width: 150px;
      height: 150px;
      background: #4caf50;
      border-radius: 10px;
      transition: transform 0.4s ease, border-radius 0.4s ease;
    }

    .box:hover {
      transform: rotate(10deg) scale(1.1);
      border-radius: 30px;
    }
  </style>
</head>
<body>
  <h2>4. Transition Reverse</h2>
  <p>Animasi halus saat hover masuk dan keluar.</p>

  <div class="box"></div>
</body>
</html>
```

**Keterangan:**  
Transition otomatis bekerja dua arah:  
- Hover masuk → animasi  
- Hover keluar → animasi balik  

---

# 5️⃣ **Mahir: Transition + dropdown menu animasi**  
Tujuan: membuat dropdown yang muncul halus tanpa JavaScript.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 5 - Transition Dropdown</title>
  <style>
    .menu {
      position: relative;
      display: inline-block;
    }

    .menu-btn {
      padding: 10px 20px;
      background: #ff9800;
      color: white;
      border-radius: 8px;
      cursor: pointer;
    }

    .dropdown {
      position: absolute;
      top: 45px;
      left: 0;
      background: white;
      border: 1px solid #ccc;
      padding: 10px;
      width: 150px;
      opacity: 0;
      transform: translateY(-10px);
      pointer-events: none;
      transition: opacity 0.3s ease, transform 0.3s ease;
    }

    .menu:hover .dropdown {
      opacity: 1;
      transform: translateY(0);
      pointer-events: auto;
    }
  </style>
</head>
<body>
  <h2>5. Dropdown dengan Transition</h2>
  <p>Dropdown muncul halus tanpa JS.</p>

  <div class="menu">
    <div class="menu-btn">Menu ▼</div>
    <div class="dropdown">
      <p>Item 1</p>
      <p>Item 2</p>
      <p>Item 3</p>
    </div>
  </div>
</body>
</html>
```

**Keterangan:**  
- `opacity` + `transform` → animasi paling halus untuk dropdown.  
- `pointer-events: none` → mencegah klik saat belum muncul.  

---

# 🟪 15. **Transform**

```css
.box:hover {
  transform: scale(1.1);
}
```
---

# 1️⃣ **Transform Dasar: Scale (membesar)**  
Transform Scale

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 1 - Transform Scale</title>
  <style>
    .box {
      width: 150px;
      height: 150px;
      background: #4caf50;
      border-radius: 10px;
      transition: 0.3s;
    }

    .box:hover {
      transform: scale(1.1); /* membesar 10% */
    }
  </style>
</head>
<body>
  <h2>1. Transform: scale()</h2>
  <p>Hover untuk melihat elemen membesar.</p>

  <div class="box"></div>
</body>
</html>
```

**Keterangan:**  
- `scale(1.1)` → ukuran naik 10%  
- Tidak mempengaruhi layout, hanya transform visual  

---

# 2️⃣ **Transform Translate: Geser X/Y**  
Transform Translate

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 2 - Transform Translate</title>
  <style>
    .box {
      width: 150px;
      height: 150px;
      background: #2196f3;
      border-radius: 10px;
      transition: 0.3s;
    }

    .box:hover {
      transform: translate(20px, -20px); 
      /* geser kanan 20px, naik 20px */
    }
  </style>
</head>
<body>
  <h2>2. Transform: translate()</h2>
  <p>Hover untuk melihat elemen bergeser.</p>

  <div class="box"></div>
</body>
</html>
```

**Keterangan:**  
- `translate(x, y)` → geser horizontal & vertikal  
- Tidak mengubah posisi asli di layout  

---

# 3️⃣ **Transform Rotate: Putar elemen**  
Transform Rotate

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 3 - Transform Rotate</title>
  <style>
    .box {
      width: 150px;
      height: 150px;
      background: #ff9800;
      border-radius: 10px;
      transition: 0.3s;
    }

    .box:hover {
      transform: rotate(15deg); /* putar 15 derajat */
    }
  </style>
</head>
<body>
  <h2>3. Transform: rotate()</h2>
  <p>Hover untuk melihat elemen berputar.</p>

  <div class="box"></div>
</body>
</html>
```

**Keterangan:**  
- `rotate(15deg)` → memutar searah jarum jam  
- Bisa pakai `deg`, `rad`, atau `turn`  

---

# 4️⃣ **Transform Skew: Miringkan elemen**  
Transform Skew

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 4 - Transform Skew</title>
  <style>
    .box {
      width: 150px;
      height: 150px;
      background: #e91e63;
      border-radius: 10px;
      transition: 0.3s;
    }

    .box:hover {
      transform: skew(10deg, 5deg); 
      /* miring horizontal 10°, vertikal 5° */
    }
  </style>
</head>
<body>
  <h2>4. Transform: skew()</h2>
  <p>Hover untuk melihat elemen menjadi miring.</p>

  <div class="box"></div>
</body>
</html>
```

**Keterangan:**  
- `skew(x, y)` → memiringkan elemen  
- Cocok untuk efek kartun, efek dinamis  

---

# 5️⃣ **Mahir: Gabungan Transform (scale + rotate + translate)**  
Transform Gabungan

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 5 - Transform Gabungan</title>
  <style>
    .box {
      width: 150px;
      height: 150px;
      background: #9c27b0;
      border-radius: 10px;
      transition: 0.4s ease;
    }

    .box:hover {
      transform: 
        scale(1.1)
        rotate(10deg)
        translate(10px, -10px);
      /* gabungan transform */
    }
  </style>
</head>
<body>
  <h2>5. Transform Gabungan</h2>
  <p>Hover untuk melihat efek gabungan: membesar + berputar + bergeser.</p>

  <div class="box"></div>
</body>
</html>
```

**Keterangan:**  
- Transform bisa digabung dalam satu baris  
- Urutan transform mempengaruhi hasil  
- Ini teknik umum untuk animasi modern UI  

---

# 🟩 16. **Media Query** — responsif

```css
@media (max-width: 600px) {
  .menu {
    flex-direction: column;
  }
}
```
---

# 1️⃣ **Dasar: Mengubah warna saat layar kecil**  
**Tujuan:** memahami konsep paling dasar media query.

**Media Query Dasar**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 1 - Media Query Dasar</title>
  <style>
    .box {
      width: 200px;
      height: 100px;
      background: #4caf50;
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    @media (max-width: 600px) {
      .box {
        background: #d32f2f; /* berubah saat layar kecil */
      }
    }
  </style>
</head>
<body>
  <h2>1. Media Query Dasar</h2>
  <p>Resize layar: warna berubah saat lebar ≤ 600px.</p>

  <div class="box">Ubah ukuran layar</div>
</body>
</html>
```

**Keterangan:**  
- Jika layar ≤ 600px → warna berubah merah.  
- Cocok untuk latihan awal responsif.

---

# 2️⃣ **Menengah: Menu horizontal → vertikal**  
**Tujuan:** memahami perubahan layout dengan `flex-direction`.

**Menu Responsif**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 2 - Menu Responsif</title>
  <style>
    .menu {
      display: flex;
      gap: 10px;
      background: #2196f3;
      padding: 10px;
    }

    .menu div {
      background: white;
      padding: 10px;
      border-radius: 5px;
    }

    @media (max-width: 600px) {
      .menu {
        flex-direction: column; /* jadi vertikal */
      }
    }
  </style>
</head>
<body>
  <h2>2. Menu Responsif</h2>
  <p>Resize layar: menu berubah dari horizontal → vertikal.</p>

  <div class="menu">
    <div>Home</div>
    <div>About</div>
    <div>Contact</div>
  </div>
</body>
</html>
```

**Keterangan:**  
- Desktop → horizontal  
- Mobile → vertikal  

---

# 3️⃣ **Lanjutan: Grid berubah jumlah kolom**  
**Tujuan:** membuat layout grid responsif.

**Grid Responsif**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 3 - Grid Responsif</title>
  <style>
    .grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
    }

    .item {
      background: #ff9800;
      padding: 20px;
      border-radius: 8px;
      color: white;
      text-align: center;
    }

    @media (max-width: 800px) {
      .grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (max-width: 500px) {
      .grid {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>
  <h2>3. Grid Responsif</h2>
  <p>Resize layar: kolom berubah 3 → 2 → 1.</p>

  <div class="grid">
    <div class="item">A</div>
    <div class="item">B</div>
    <div class="item">C</div>
    <div class="item">D</div>
    <div class="item">E</div>
    <div class="item">F</div>
  </div>
</body>
</html>
```

**Keterangan:**  
- ≥ 800px → 3 kolom  
- ≤ 800px → 2 kolom  
- ≤ 500px → 1 kolom  

---

# 4️⃣ **Advance: Hide & Show elemen di mobile**  
**Tujuan:** membuat elemen tertentu hanya muncul di mobile.

**Hide Show Mobile**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 4 - Hide Show Mobile</title>
  <style>
    .desktop {
      background: #4caf50;
      padding: 20px;
      color: white;
      border-radius: 8px;
    }

    .mobile {
      background: #e91e63;
      padding: 20px;
      color: white;
      border-radius: 8px;
      display: none; /* default: sembunyi */
    }

    @media (max-width: 600px) {
      .desktop {
        display: none;
      }
      .mobile {
        display: block; /* muncul di mobile */
      }
    }
  </style>
</head>
<body>
  <h2>4. Hide & Show Elemen</h2>
  <p>Desktop: hijau. Mobile: merah.</p>

  <div class="desktop">Ini tampilan desktop</div>
  <div class="mobile">Ini tampilan mobile</div>
</body>
</html>
```

**Keterangan:**  
- Desktop → elemen hijau  
- Mobile → elemen merah  

---

# 5️⃣ **Mahir: Navbar responsif + hamburger tanpa JS**  
**Tujuan:** membuat navbar yang berubah total di mobile.

**Navbar Responsif Mahir**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 5 - Navbar Responsif Mahir</title>
  <style>
    body {
      margin: 0;
      font-family: Arial;
    }

    .navbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #3f51b5;
      padding: 10px 20px;
      color: white;
    }

    .menu {
      display: flex;
      gap: 15px;
    }

    .hamburger {
      display: none;
      font-size: 24px;
      cursor: pointer;
    }

    @media (max-width: 600px) {
      .menu {
        display: none; /* sembunyikan menu */
      }
      .hamburger {
        display: block; /* tampilkan tombol H */
      }
    }
  </style>
</head>
<body>
  <h2 style="padding:20px;">5. Navbar Responsif Mahir</h2>
  <p>Resize layar: menu hilang, tombol hamburger muncul.</p>

  <div class="navbar">
    <div class="logo">LOGO</div>

    <div class="menu">
      <div>Home</div>
      <div>About</div>
      <div>Contact</div>
    </div>

    <div class="hamburger">☰</div>
  </div>
</body>
</html>
```

**Keterangan:**  
- Desktop → menu lengkap  
- Mobile → menu hilang, tombol hamburger muncul  
- Ini pondasi navbar responsif modern  

---

## Mau lanjut ke materi berikutnya?  
Pilih:

- **CSS Animation**  
- **CSS Filter**  
- **CSS Flexbox lanjutan**  

Atau lanjut ke **materi #17** dari cheat sheet kamu.
---

# 🟦 17. **Cursor**

```css
button {
  cursor: pointer;
}
```
## 🟦 17. **Cursor** — 5 script dari **dasar → mahir**  
Kita lanjut Edy — tetap dengan format **5 file HTML terpisah**, lengkap, jelas, dan bisa langsung diuji.  
Materi ini sederhana tapi penting untuk UX: mengubah bentuk cursor saat pengguna berinteraksi.

---

# 1️⃣ **Dasar: Cursor Pointer (tangan)**  
**Tujuan:** memahami penggunaan paling umum — tombol jadi “klik-able”.

**Cursor Pointer**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 1 - Cursor Pointer</title>
  <style>
    button {
      padding: 12px 20px;
      background: #4caf50;
      color: white;
      border: none;
      border-radius: 6px;
      cursor: pointer; /* tangan */
    }
  </style>
</head>
<body>
  <h2>1. Cursor Pointer</h2>
  <p>Hover tombol: cursor berubah menjadi tangan.</p>

  <button>Klik Saya</button>
</body>
</html>
```

**Keterangan:**  
- `cursor: pointer` → tanda bahwa elemen bisa diklik.

---

# 2️⃣ **Menengah: Cursor Not-Allowed (dilarang)**  
**Tujuan:** memberi sinyal bahwa tombol tidak bisa dipakai.

**Cursor Not Allowed**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 2 - Cursor Not Allowed</title>
  <style>
    .btn {
      padding: 12px 20px;
      background: #9e9e9e;
      color: white;
      border-radius: 6px;
      cursor: not-allowed; /* tanda larangan */
      opacity: 0.7;
    }
  </style>
</head>
<body>
  <h2>2. Cursor Not Allowed</h2>
  <p>Hover tombol: cursor jadi tanda larangan.</p>

  <div class="btn">Tidak Bisa Diklik</div>
</body>
</html>
```

**Keterangan:**  
- Cocok untuk tombol disabled.  
- Memberi feedback visual yang jelas.

---

# 3️⃣ **Lanjutan: Cursor Text (I-beam)**  
**Tujuan:** menunjukkan area yang bisa diketik atau diseleksi.

**Cursor Text**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 3 - Cursor Text</title>
  <style>
    .text-area {
      width: 300px;
      padding: 15px;
      background: #f5f5f5;
      border-radius: 6px;
      cursor: text; /* I-beam */
    }
  </style>
</head>
<body>
  <h2>3. Cursor Text</h2>
  <p>Hover area: cursor berubah menjadi I-beam.</p>

  <div class="text-area">Area ini bisa diseleksi seperti teks.</div>
</body>
</html>
```

**Keterangan:**  
- Dipakai untuk input, textarea, atau elemen yang berisi teks.

---

# 4️⃣ **Advance: Cursor Move (geser)**  
**Tujuan:** memberi sinyal bahwa elemen bisa dipindah/drag.

**Cursor Move**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 4 - Cursor Move</title>
  <style>
    .drag {
      width: 150px;
      height: 150px;
      background: #2196f3;
      border-radius: 10px;
      cursor: move; /* tanda bisa digeser */
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-size: 18px;
    }
  </style>
</head>
<body>
  <h2>4. Cursor Move</h2>
  <p>Hover kotak: cursor berubah menjadi ikon “pindah”.</p>

  <div class="drag">Drag</div>
</body>
</html>
```

**Keterangan:**  
- Cocok untuk elemen draggable.  
- Memberi sinyal bahwa elemen bisa dipindahkan.

---

# 5️⃣ **Mahir: Custom Cursor (pakai gambar sendiri)**  
**Tujuan:** membuat cursor unik untuk game, aplikasi, atau branding.

**Cursor Custom**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 5 - Custom Cursor</title>
  <style>
    .area {
      width: 300px;
      height: 200px;
      background: #ff9800;
      border-radius: 10px;
      cursor: url('https://icons.iconarchive.com/icons/custom-icon-design/flatastic-2/32/arrow-right-icon.png'), auto;
      /* cursor custom + fallback */
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-size: 20px;
    }
  </style>
</head>
<body>
  <h2>5. Custom Cursor</h2>
  <p>Hover area: cursor berubah menjadi gambar khusus.</p>

  <div class="area">Custom Cursor</div>
</body>
</html>
```

**Keterangan:**  
- Bisa pakai `.png`, `.cur`, `.svg`.  
- Selalu beri fallback: `auto` atau `pointer`.  
- Cocok untuk game UI, aplikasi kreatif, atau efek unik.

---

# 🟧 18. **Opacity**

```css
img {
  opacity: 0.7;
}
```
---

# 1️⃣ **Dasar: Opacity pada gambar**  
**Tujuan:** memahami efek paling dasar opacity.

**Opacity Dasar**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 1 - Opacity Dasar</title>
  <style>
    img {
      width: 250px;
      opacity: 0.7; /* 70% terlihat */
    }
  </style>
</head>
<body>
  <h2>1. Opacity Dasar</h2>
  <p>Gambar menjadi sedikit transparan.</p>

  <img src="https://picsum.photos/300/200" alt="demo">
</body>
</html>
```

**Keterangan:**  
- `opacity: 0.7` → gambar terlihat 70%, transparan 30%.

---

# 2️⃣ **Menengah: Opacity + hover (fade-in)**  
**Tujuan:** membuat efek fade saat hover.

**Opacity Hover**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 2 - Opacity Hover</title>
  <style>
    img {
      width: 250px;
      opacity: 0.5;
      transition: opacity 0.3s;
    }

    img:hover {
      opacity: 1; /* kembali solid */
    }
  </style>
</head>
<body>
  <h2>2. Opacity Hover</h2>
  <p>Hover gambar: opacity naik dari 0.5 → 1.</p>

  <img src="https://picsum.photos/300/200" alt="demo">
</body>
</html>
```

**Keterangan:**  
- Efek fade-in sangat umum untuk UI modern.

---

# 3️⃣ **Lanjutan: Overlay hitam dengan opacity**  
**Tujuan:** membuat overlay gelap untuk teks di atas gambar.

**Opacity Overlay**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 3 - Overlay Opacity</title>
  <style>
    .container {
      position: relative;
      width: 300px;
    }

    img {
      width: 100%;
      display: block;
    }

    .overlay {
      position: absolute;
      inset: 0;
      background: black;
      opacity: 0.4; /* overlay gelap */
    }

    .text {
      position: absolute;
      bottom: 10px;
      left: 10px;
      color: white;
      font-size: 20px;
    }
  </style>
</head>
<body>
  <h2>3. Overlay dengan Opacity</h2>

  <div class="container">
    <img src="https://picsum.photos/300/200" alt="demo">
    <div class="overlay"></div>
    <div class="text">Judul Foto</div>
  </div>
</body>
</html>
```

**Keterangan:**  
- Teknik umum untuk card, banner, hero section.

---

# 4️⃣ **Advance: Opacity pada seluruh elemen (anak ikut transparan)**  
**Tujuan:** memahami bahwa opacity mempengaruhi *semua* isi elemen.

**Opacity Parent**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 4 - Opacity Parent</title>
  <style>
    .box {
      width: 300px;
      padding: 20px;
      background: #4caf50;
      color: white;
      opacity: 0.5; /* semua isi ikut transparan */
    }
  </style>
</head>
<body>
  <h2>4. Opacity Parent</h2>
  <p>Perhatikan: teks juga ikut transparan.</p>

  <div class="box">
    Ini teks ikut transparan karena opacity diterapkan ke parent.
  </div>
</body>
</html>
```

**Keterangan:**  
- Opacity mempengaruhi seluruh elemen termasuk anak-anaknya.  
- Jika ingin hanya background yang transparan → gunakan `rgba()`.

---

# 5️⃣ **Mahir: Fade-in animasi saat halaman dibuka**  
**Tujuan:** membuat animasi masuk halus menggunakan opacity + keyframes.

**Opacity Fade-in**

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 5 - Fade In Animation</title>
  <style>
    .card {
      width: 300px;
      padding: 20px;
      background: white;
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.2);
      opacity: 0;
      animation: fadeIn 1s ease forwards;
    }

    @keyframes fadeIn {
      from {
        opacity: 0;
        transform: translateY(20px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }
  </style>
</head>
<body>
  <h2>5. Fade-in Animation</h2>
  <p>Card muncul dengan animasi halus saat halaman dibuka.</p>

  <div class="card">
    Animasi Fade-in
  </div>
</body>
</html>
```

**Keterangan:**  
- `opacity` + `translateY` → animasi modern ala UI dashboard.  
- `forwards` → animasi berhenti di kondisi akhir.

---

# 🟪 19. **Object-fit** — gambar rapi

```css
img {
  object-fit: cover;
}
```
---

# 1️⃣ **Dasar: object-fit cover (gambar memenuhi kotak)**  
Object-fit Cover

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 1 - Object-fit Cover</title>
  <style>
    .box {
      width: 300px;
      height: 200px;
      border: 2px solid #333;
      overflow: hidden;
    }

    img {
      width: 100%;
      height: 100%;
      object-fit: cover; /* isi penuh, crop bagian luar */
    }
  </style>
</head>
<body>
  <h2>1. object-fit: cover</h2>
  <p>Gambar memenuhi kotak tanpa distorsi.</p>

  <div class="box">
    <img src="https://picsum.photos/400/300" alt="">
  </div>
</body>
</html>
```

**Keterangan:**  
- Gambar tetap proporsional.  
- Bagian yang tidak muat akan terpotong (crop).  
- Cocok untuk thumbnail, card, banner.

---

# 2️⃣ **Contain: gambar selalu utuh (tidak terpotong)**  
Object-fit Contain

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 2 - Object-fit Contain</title>
  <style>
    .box {
      width: 300px;
      height: 200px;
      border: 2px solid #333;
      background: #eee;
    }

    img {
      width: 100%;
      height: 100%;
      object-fit: contain; /* gambar utuh, mungkin ada ruang kosong */
    }
  </style>
</head>
<body>
  <h2>2. object-fit: contain</h2>
  <p>Gambar tidak terpotong, tapi bisa ada ruang kosong.</p>

  <div class="box">
    <img src="https://picsum.photos/400/300" alt="">
  </div>
</body>
</html>
```

**Keterangan:**  
- Gambar selalu utuh.  
- Cocok untuk logo, ilustrasi, icon.

---

# 3️⃣ **Fill: gambar dipaksa memenuhi kotak (bisa distorsi)**  
Object-fit Fill

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 3 - Object-fit Fill</title>
  <style>
    .box {
      width: 300px;
      height: 200px;
      border: 2px solid #333;
    }

    img {
      width: 100%;
      height: 100%;
      object-fit: fill; /* gambar dipaksa memenuhi kotak */
    }
  </style>
</head>
<body>
  <h2>3. object-fit: fill</h2>
  <p>Gambar memenuhi kotak, tapi bisa gepeng atau melebar.</p>

  <div class="box">
    <img src="https://picsum.photos/400/300" alt="">
  </div>
</body>
</html>
```

**Keterangan:**  
- Tidak menjaga proporsi.  
- Cocok untuk background dekoratif yang tidak butuh akurasi bentuk.

---

# 4️⃣ **None: gambar tampil ukuran asli (bisa keluar kotak)**  
Object-fit None

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 4 - Object-fit None</title>
  <style>
    .box {
      width: 300px;
      height: 200px;
      border: 2px solid #333;
      overflow: hidden;
    }

    img {
      width: 100%;
      height: 100%;
      object-fit: none; /* pakai ukuran asli */
      object-position: center; /* fokus tengah */
    }
  </style>
</head>
<body>
  <h2>4. object-fit: none</h2>
  <p>Gambar pakai ukuran asli, bisa keluar kotak.</p>

  <div class="box">
    <img src="https://picsum.photos/400/300" alt="">
  </div>
</body>
</html>
```

**Keterangan:**  
- Cocok untuk cropping manual.  
- `object-position` mengatur bagian mana yang ditampilkan.

---

# 5️⃣ **Mahir: Card responsif dengan object-fit cover + hover zoom**  
Object-fit Mahir

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 5 - Object-fit Mahir</title>
  <style>
    .card {
      width: 300px;
      border-radius: 10px;
      overflow: hidden;
      box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }

    .card img {
      width: 100%;
      height: 200px;
      object-fit: cover;
      transition: transform 0.4s ease;
    }

    .card:hover img {
      transform: scale(1.1); /* zoom halus */
    }

    .content {
      padding: 15px;
      font-family: Arial;
    }
  </style>
</head>
<body>
  <h2>5. Card Responsif + Hover Zoom</h2>
  <p>Teknik modern untuk UI card seperti marketplace atau blog.</p>

  <div class="card">
    <img src="https://picsum.photos/400/300" alt="">
    <div class="content">
      <h3>Judul Card</h3>
      <p>Deskripsi singkat card.</p>
    </div>
  </div>
</body>
</html>
```

**Keterangan:**  
- `object-fit: cover` → gambar rapi.  
- `transform: scale(1.1)` → efek zoom modern.  
- Cocok untuk card produk, artikel, galeri.

---


# 🟩 20. **White-space** — kontrol spasi teks

```css
p {
  white-space: nowrap;
}
```
---

# 1️⃣ **Dasar: `white-space: nowrap` (teks tidak turun baris)**  
White-space Nowrap

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 1 - White-space Nowrap</title>
  <style>
    p {
      width: 200px;
      border: 2px solid #333;
      white-space: nowrap; /* teks tidak boleh turun baris */
    }
  </style>
</head>
<body>
  <h2>1. white-space: nowrap</h2>
  <p>Ini adalah contoh teks yang sangat panjang dan tidak akan turun baris.</p>
</body>
</html>
```

**Keterangan:**  
- Cocok untuk label, tombol panjang, atau teks yang harus tetap satu baris.

---

# 2️⃣ **Menengah: `white-space: normal` (default, teks wrap biasa)**  
White-space Normal

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 2 - White-space Normal</title>
  <style>
    p {
      width: 200px;
      border: 2px solid #333;
      white-space: normal; /* wrap seperti biasa */
    }
  </style>
</head>
<body>
  <h2>2. white-space: normal</h2>
  <p>Ini adalah contoh teks panjang yang akan turun baris secara normal sesuai lebar elemen.</p>
</body>
</html>
```

**Keterangan:**  
- Ini adalah perilaku default browser.

---

# 3️⃣ **Lanjutan: `white-space: pre` (menghormati spasi & enter)**  
White-space Pre

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 3 - White-space Pre</title>
  <style>
    .box {
      width: 300px;
      border: 2px solid #333;
      white-space: pre; /* spasi & enter dipertahankan */
    }
  </style>
</head>
<body>
  <h2>3. white-space: pre</h2>

  <div class="box">
Teks ini
    punya spasi      dan enter
yang dipertahankan persis seperti aslinya.
  </div>
</body>
</html>
```

**Keterangan:**  
- Mirip `<pre>` tag.  
- Cocok untuk menampilkan kode, puisi, atau teks format khusus.

---

# 4️⃣ **Advance: `white-space: pre-wrap` (enter dihormati, wrap tetap jalan)**  
White-space Pre-wrap

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 4 - White-space Pre-wrap</title>
  <style>
    .box {
      width: 250px;
      border: 2px solid #333;
      white-space: pre-wrap; 
      /* enter dihormati, tapi tetap wrap jika kepanjangan */
    }
  </style>
</head>
<body>
  <h2>4. white-space: pre-wrap</h2>

  <div class="box">
Teks ini punya enter
dan akan tetap turun baris
jika terlalu panjang untuk kotaknya.
  </div>
</body>
</html>
```

**Keterangan:**  
- Kombinasi `pre` + `normal`.  
- Cocok untuk chat bubble, komentar, input multiline.

---

# 5️⃣ **Mahir: `white-space: break-spaces` (spasi beruntun tetap tampil)**  
White-space Break-spaces

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 5 - White-space Break-spaces</title>
  <style>
    .box {
      width: 300px;
      border: 2px solid #333;
      white-space: break-spaces; 
      /* spasi beruntun tidak digabung */
    }
  </style>
</head>
<body>
  <h2>5. white-space: break-spaces</h2>

  <div class="box">
Teks ini punya spasi       yang sangat banyak
dan semuanya akan tetap muncul.
  </div>
</body>
</html>
```

**Keterangan:**  
- Spasi beruntun tidak diringkas jadi satu.  
- Cocok untuk teks yang butuh presisi spacing (ASCII art, format khusus).

---

# 🟦 21. **Overflow-wrap** — pecah kata panjang

```css
p {
  overflow-wrap: break-word;
}
```
---

# 1️⃣ **Dasar: `overflow-wrap: break-word` (pecah kata panjang)**  
Overflow-wrap Break-word

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 1 - Overflow-wrap Break-word</title>
  <style>
    p {
      width: 200px;
      border: 2px solid #333;
      overflow-wrap: break-word; /* pecah kata panjang */
    }
  </style>
</head>
<body>
  <h2>1. overflow-wrap: break-word</h2>

  <p>
    IniKataSuperPanjangBangetYangBiasanyaKeluarKotakTapiSekarangDipecah.
  </p>
</body>
</html>
```

**Keterangan:**  
- Kata super panjang akan dipotong otomatis.  
- Cocok untuk teks user-generated (komentar, chat).

---

# 2️⃣ **Menengah: `overflow-wrap: anywhere` (lebih agresif)**  
Overflow-wrap Anywhere

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 2 - Overflow-wrap Anywhere</title>
  <style>
    p {
      width: 200px;
      border: 2px solid #333;
      overflow-wrap: anywhere; /* pecah di mana saja */
    }
  </style>
</head>
<body>
  <h2>2. overflow-wrap: anywhere</h2>

  <p>
    KataSuperPanjangBangetYangTidakAdaSpasinyaAkanDipaksaPecahDimanaSaja.
  </p>
</body>
</html>
```

**Keterangan:**  
- Mirip `break-word`, tapi lebih agresif.  
- Cocok untuk data teknis: URL, hash, ID panjang.

---

# 3️⃣ **Lanjutan: Perbandingan tanpa overflow-wrap (keluar kotak)**  
Overflow-wrap Comparison

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 3 - Tanpa Overflow-wrap</title>
  <style>
    .box {
      width: 200px;
      border: 2px solid #333;
      margin-bottom: 20px;
    }

    .no-wrap {
      white-space: nowrap; /* tidak turun baris */
    }
  </style>
</head>
<body>
  <h2>3. Tanpa overflow-wrap (keluar kotak)</h2>

  <div class="box no-wrap">
    KataSuperPanjangBangetYangAkanKeluarKotakKarenaTidakAdaWrap
  </div>

  <p>Perhatikan: teks keluar kotak karena tidak ada wrap.</p>
</body>
</html>
```

**Keterangan:**  
- Tanpa overflow-wrap → teks bisa keluar kotak.  
- Latihan ini untuk melihat perbedaannya.

---

# 4️⃣ **Advance: Overflow-wrap + word-break (kombinasi kuat)**  
Overflow-wrap + Word-break

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 4 - Kombinasi Wrap</title>
  <style>
    p {
      width: 200px;
      border: 2px solid #333;
      overflow-wrap: break-word;
      word-break: break-all; /* paksa pecah semua karakter */
    }
  </style>
</head>
<body>
  <h2>4. Kombinasi overflow-wrap + word-break</h2>

  <p>
    KataSuperPanjangBangetYangTidakAdaSpasinyaDanHarusDipaksaPecah.
  </p>
</body>
</html>
```

**Keterangan:**  
- `word-break: break-all` → memecah karakter satu per satu.  
- Cocok untuk data ekstrem: hash, token, kode unik.

---

# 5️⃣ **Mahir: Chat bubble responsif (wrap otomatis)**  
Overflow-wrap Chat Bubble

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 5 - Chat Bubble Responsif</title>
  <style>
    .chat {
      max-width: 250px;
      padding: 15px;
      background: #4caf50;
      color: white;
      border-radius: 10px;
      font-family: Arial;
      overflow-wrap: break-word; /* pecah kata panjang */
    }
  </style>
</head>
<body>
  <h2>5. Chat Bubble Responsif</h2>
  <p>Bubble chat otomatis memecah kata panjang.</p>

  <div class="chat">
    Halo! Ini contoh chat dengan kataSuperPanjangBangetYangBiasanyaBikinLayoutRusak.
  </div>
</body>
</html>
```

**Keterangan:**  
- Teknik wajib untuk UI chat, komentar, forum.  
- Mencegah bubble melebar tidak terkontrol.

---

# 🟧 22. **Pointer-events**

```css
div {
  pointer-events: none;
}
```

---

# 🟪 23. **Filter** — efek visual

```css
img {
  filter: blur(5px);
}
```

---

# 1️⃣ **Dasar: pointer-events: none (elemen tidak bisa diklik)**  
Pointer-events None

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 1 - Pointer-events None</title>
  <style>
    .box {
      width: 200px;
      padding: 20px;
      background: #4caf50;
      color: white;
      border-radius: 8px;
      pointer-events: none; /* tidak bisa diklik */
    }
  </style>
</head>
<body>
  <h2>1. pointer-events: none</h2>
  <p>Elemen hijau tidak bisa diklik.</p>

  <div class="box" onclick="alert('Tidak akan jalan')">
    Saya tidak bisa diklik
  </div>
</body>
</html>
```

**Keterangan:**  
- Semua event mouse **dimatikan**.  
- Cocok untuk elemen dekoratif atau disabled.

---

# 2️⃣ **Menengah: pointer-events: auto (default, bisa diklik)**  
Pointer-events Auto

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 2 - Pointer-events Auto</title>
  <style>
    .box {
      width: 200px;
      padding: 20px;
      background: #2196f3;
      color: white;
      border-radius: 8px;
      pointer-events: auto; /* bisa diklik */
      cursor: pointer;
    }
  </style>
</head>
<body>
  <h2>2. pointer-events: auto</h2>
  <p>Elemen biru bisa diklik.</p>

  <div class="box" onclick="alert('Berhasil diklik!')">
    Klik saya
  </div>
</body>
</html>
```

**Keterangan:**  
- Ini adalah perilaku default browser.

---

# 3️⃣ **Lanjutan: pointer-events none pada overlay (klik tembus ke belakang)**  
Pointer-events Overlay

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 3 - Pointer-events Overlay</title>
  <style>
    .container {
      position: relative;
      width: 300px;
      height: 200px;
      background: #eee;
      border: 2px solid #333;
    }

    .overlay {
      position: absolute;
      inset: 0;
      background: rgba(0,0,0,0.3);
      pointer-events: none; /* klik tembus */
    }

    .btn {
      position: absolute;
      bottom: 10px;
      left: 10px;
      background: #4caf50;
      color: white;
      padding: 10px;
      border-radius: 6px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <h2>3. Overlay klik tembus</h2>
  <p>Overlay tidak menghalangi klik tombol di bawahnya.</p>

  <div class="container">
    <div class="overlay"></div>
    <div class="btn" onclick="alert('Tombol tetap bisa diklik!')">Klik tombol</div>
  </div>
</body>
</html>
```

**Keterangan:**  
- Teknik penting untuk efek visual overlay yang **tidak mengganggu interaksi**.

---

# 4️⃣ **Advance: pointer-events none hanya saat hover (disable sementara)**  
Pointer-events Hover

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 4 - Pointer-events Hover</title>
  <style>
    .box {
      width: 250px;
      padding: 20px;
      background: #ff9800;
      color: white;
      border-radius: 8px;
      transition: 0.3s;
    }

    .box:hover {
      pointer-events: none; /* saat hover jadi tidak bisa diklik */
      opacity: 0.6;
    }
  </style>
</head>
<body>
  <h2>4. pointer-events saat hover</h2>
  <p>Hover elemen → tidak bisa diklik sementara.</p>

  <div class="box" onclick="alert('Klik berhasil!')">
    Hover saya untuk menonaktifkan klik
  </div>
</body>
</html>
```

**Keterangan:**  
- Berguna untuk animasi atau loading state sementara.

---

# 5️⃣ **Mahir: Tooltip tidak menghalangi klik elemen di bawahnya**  
Pointer-events Tooltip

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 5 - Tooltip Pointer-events</title>
  <style>
    .wrapper {
      position: relative;
      width: 300px;
      padding: 20px;
      background: #4caf50;
      color: white;
      border-radius: 10px;
      cursor: pointer;
    }

    .tooltip {
      position: absolute;
      top: -40px;
      left: 0;
      background: #333;
      color: white;
      padding: 8px 12px;
      border-radius: 6px;
      pointer-events: none; /* tooltip tidak menghalangi klik */
      opacity: 0;
      transform: translateY(10px);
      transition: 0.3s;
    }

    .wrapper:hover .tooltip {
      opacity: 1;
      transform: translateY(0);
    }
  </style>
</head>
<body>
  <h2>5. Tooltip tidak menghalangi klik</h2>
  <p>Tooltip muncul, tapi klik tetap masuk ke elemen utama.</p>

  <div class="wrapper" onclick="alert('Elemen utama diklik!')">
    Hover saya
    <div class="tooltip">Tooltip muncul</div>
  </div>
</body>
</html>
```

**Keterangan:**  
- Tooltip hanya visual, tidak mengganggu interaksi.  
- Teknik wajib untuk UI modern (dashboard, form, card info).

---

# 🟩 24. **Aspect-ratio**

```css
.box {
  aspect-ratio: 16 / 9;
}
```
---

# 1️⃣ **Dasar: aspect-ratio 16/9 (video style)**  
Aspect-ratio 16:9

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 1 - Aspect Ratio 16:9</title>
  <style>
    .box {
      width: 300px;
      background: #4caf50;
      aspect-ratio: 16 / 9; /* rasio video */
      border-radius: 10px;
    }
  </style>
</head>
<body>
  <h2>1. aspect-ratio: 16 / 9</h2>
  <p>Elemen otomatis mengikuti rasio 16:9.</p>

  <div class="box"></div>
</body>
</html>
```

**Keterangan:**  
- Rasio standar video YouTube.  
- Tinggi otomatis dihitung dari lebar.

---

# 2️⃣ **Menengah: aspect-ratio 1/1 (kotak sempurna)**  
Aspect-ratio 1:1

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 2 - Aspect Ratio 1:1</title>
  <style>
    .box {
      width: 200px;
      background: #2196f3;
      aspect-ratio: 1 / 1; /* kotak */
      border-radius: 10px;
    }
  </style>
</head>
<body>
  <h2>2. aspect-ratio: 1 / 1</h2>
  <p>Kotak sempurna tanpa hitung manual.</p>

  <div class="box"></div>
</body>
</html>
```

**Keterangan:**  
- Cocok untuk avatar, thumbnail, icon.

---

# 3️⃣ **Lanjutan: aspect-ratio pada gambar (crop otomatis)**  
Aspect-ratio Image

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 3 - Aspect Ratio pada Gambar</title>
  <style>
    .box {
      width: 300px;
      aspect-ratio: 16 / 9;
      overflow: hidden;
      border-radius: 10px;
    }

    img {
      width: 100%;
      height: 100%;
      object-fit: cover; /* gambar rapi */
    }
  </style>
</head>
<body>
  <h2>3. Aspect Ratio + Object-fit</h2>
  <p>Gambar otomatis mengikuti rasio 16:9.</p>

  <div class="box">
    <img src="https://picsum.photos/400/300" alt="">
  </div>
</body>
</html>
```

**Keterangan:**  
- Kombinasi paling umum untuk card, banner, thumbnail.

---

# 4️⃣ **Advance: Grid responsif dengan aspect-ratio**  
Aspect-ratio Grid

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 4 - Grid Aspect Ratio</title>
  <style>
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
      gap: 15px;
    }

    .item {
      background: #ff9800;
      aspect-ratio: 4 / 3; /* rasio foto klasik */
      border-radius: 10px;
    }
  </style>
</head>
<body>
  <h2>4. Grid dengan Aspect Ratio</h2>
  <p>Semua item punya rasio seragam meskipun ukuran grid berubah.</p>

  <div class="grid">
    <div class="item"></div>
    <div class="item"></div>
    <div class="item"></div>
    <div class="item"></div>
  </div>
</body>
</html>
```

**Keterangan:**  
- Cocok untuk galeri foto responsif.  
- Tidak perlu padding‑hack lagi.

---

# 5️⃣ **Mahir: Card produk responsif (rasio tetap + hover zoom)**  
Aspect-ratio Card Produk

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 5 - Card Produk</title>
  <style>
    .card {
      width: 280px;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 4px 10px rgba(0,0,0,0.2);
      font-family: Arial;
    }

    .image {
      aspect-ratio: 1 / 1; /* kotak */
      overflow: hidden;
    }

    .image img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.4s ease;
    }

    .card:hover img {
      transform: scale(1.1); /* zoom */
    }

    .content {
      padding: 15px;
    }
  </style>
</head>
<body>
  <h2>5. Card Produk Responsif</h2>
  <p>Teknik modern untuk marketplace, katalog, dan UI e-commerce.</p>

  <div class="card">
    <div class="image">
      <img src="https://picsum.photos/400/400" alt="">
    </div>
    <div class="content">
      <h3>Nama Produk</h3>
      <p>Deskripsi singkat produk.</p>
    </div>
  </div>
</body>
</html>
```

**Keterangan:**  
- Rasio gambar tetap rapi.  
- Hover zoom membuat card lebih hidup.  
- Cocok untuk UI modern marketplace.

---

# 🟦 25. **Backdrop-filter** — efek kaca

```css
.glass {
  backdrop-filter: blur(10px);
}
```

---

# 1️⃣ **Dasar: blur background di belakang elemen**  
Backdrop Blur Dasar

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 1 - Backdrop Blur Dasar</title>
  <style>
    body {
      background: url('https://picsum.photos/800/600') no-repeat center/cover;
      height: 100vh;
    }

    .glass {
      width: 300px;
      padding: 20px;
      margin: 40px;
      background: rgba(255,255,255,0.3);
      backdrop-filter: blur(10px); /* efek kaca */
      border-radius: 12px;
      color: white;
    }
  </style>
</head>
<body>
  <h2 style="color:white;">1. Backdrop-filter: blur()</h2>

  <div class="glass">
    Efek kaca buram dasar.
  </div>
</body>
</html>
```

**Keterangan:**  
- Background di belakang elemen menjadi blur.  
- Elemen harus punya **background transparan** agar blur terlihat.

---

# 2️⃣ **Menengah: kombinasi blur + brightness**  
Backdrop Blur Brightness

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 2 - Blur + Brightness</title>
  <style>
    body {
      background: url('https://picsum.photos/800/600') no-repeat center/cover;
      height: 100vh;
    }

    .glass {
      width: 300px;
      padding: 20px;
      margin: 40px;
      background: rgba(255,255,255,0.25);
      backdrop-filter: blur(12px) brightness(1.2);
      border-radius: 12px;
      color: white;
    }
  </style>
</head>
<body>
  <h2 style="color:white;">2. Blur + Brightness</h2>

  <div class="glass">
    Efek kaca lebih terang.
  </div>
</body>
</html>
```

**Keterangan:**  
- `brightness(1.2)` → membuat area belakang lebih cerah.  
- Cocok untuk UI modern ala macOS.

---

# 3️⃣ **Lanjutan: card glassmorphism modern**  
Backdrop Glassmorphism

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 3 - Card Glassmorphism</title>
  <style>
    body {
      background: linear-gradient(135deg, #4a148c, #880e4f);
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .card {
      width: 320px;
      padding: 25px;
      background: rgba(255,255,255,0.15);
      backdrop-filter: blur(15px);
      border-radius: 15px;
      border: 1px solid rgba(255,255,255,0.3);
      color: white;
      font-family: Arial;
    }
  </style>
</head>
<body>
  <div class="card">
    <h2>Glassmorphism Card</h2>
    <p>Efek kaca modern ala UI 2024+</p>
  </div>
</body>
</html>
```

**Keterangan:**  
- Kombinasi blur + transparansi + border tipis → gaya glassmorphism.  
- Dipakai di dashboard, login page, hero section.

---

# 4️⃣ **Advance: navbar kaca transparan**  
Backdrop Navbar

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 4 - Navbar Kaca</title>
  <style>
    body {
      background: url('https://picsum.photos/900/600') no-repeat center/cover;
      height: 100vh;
      margin: 0;
    }

    .navbar {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      padding: 15px 30px;
      background: rgba(255,255,255,0.2);
      backdrop-filter: blur(12px);
      display: flex;
      gap: 20px;
      color: white;
      font-size: 18px;
    }
  </style>
</head>
<body>
  <div class="navbar">
    Home | About | Contact
  </div>
</body>
</html>
```

**Keterangan:**  
- Navbar tetap terlihat meski background berubah saat scroll.  
- Efek kaca membuat UI lebih elegan.

---

# 5️⃣ **Mahir: modal kaca + animasi fade-in**  
Backdrop Modal

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Latihan 5 - Modal Kaca Animasi</title>
  <style>
    body {
      background: url('https://picsum.photos/900/600') no-repeat center/cover;
      height: 100vh;
      margin: 0;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .modal {
      width: 350px;
      padding: 25px;
      background: rgba(255,255,255,0.25);
      backdrop-filter: blur(18px);
      border-radius: 15px;
      border: 1px solid rgba(255,255,255,0.4);
      color: white;
      font-family: Arial;
      opacity: 0;
      transform: translateY(20px);
      animation: fadeIn 0.6s ease forwards;
    }

    @keyframes fadeIn {
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }
  </style>
</head>
<body>
  <div class="modal">
    <h2>Modal Kaca</h2>
    <p>Efek kaca + animasi masuk halus.</p>
  </div>
</body>
</html>
```

**Keterangan:**  
- Efek kaca + animasi → UI premium.  
- Cocok untuk popup login, dialog, alert modern.

---

