### 7.1 Navbar

#### Struktur Navigasi
- Logo: Ngrembaka Aksara.
- Menu utama:
	Beranda | Visi | Profil Aksara | Profil Kelurahan | E-Library | Tunas | Karya | Cakra | Kersa
- Tombol aksi kanan: Hubungi Kami (WhatsApp).
- Catatan konten:
	Gunakan istilah konsisten E-Library (bukan e-library/e library).

#### Desain Visual dalam tabel

| b/k | kolom1 | kolom2 | kolom3 | kolom4 | kolom5 | kolom6 | kolom7 | kolom8 | kolom9 | kolom10 | kolom11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| baris1 | Logo Ngrembaka Aksara | Beranda | Visi | Profil Aksara | Profil Kelurahan | E-Library | Tunas | Karya | Cakra | Kersa | Hubungi Kami (WhatsApp) |

Catatan layout konten:
- Kolom1 berfungsi sebagai brand/identitas.
- Kolom2 sampai kolom10 berfungsi sebagai navigasi utama.
- Kolom11 berfungsi sebagai CTA prioritas (kontak cepat WhatsApp).

#### Implementasi html tanpa CSS

```html
<nav>
	<div>
		<a href="/" aria-label="Ngrembaka Aksara">Logo Ngrembaka Aksara</a>
	</div>

	<ul>
		<li><a href="/">Beranda</a></li>
		<li><a href="/beranda">Visi</a></li>
		<li><a href="/profil/ngrembaka-aksara">Profil Aksara</a></li>
		<li><a href="/profil/kelurahan-podorejo">Profil Kelurahan</a></li>
		<li><a href="/elibrary">E-Library</a></li>
		<li><a href="/pojok-literasi/tunas">Tunas</a></li>
		<li><a href="/pojok-literasi/karya">Karya</a></li>
		<li><a href="/pojok-literasi/cakra">Cakra</a></li>
		<li><a href="/pojok-literasi/kersa">Kersa</a></li>
	</ul>

	<div>
		<a href="https://wa.me/6281234567890" target="_blank" rel="noopener noreferrer">
			Hubungi Kami (WhatsApp)
		</a>
	</div>
</nav>

```

Keterangan Dasar HTML:
- `<nav>`: elemen pembungkus navigasi utama.
	Alasan: karena bagian ini adalah menu utama situs, penggunaan `<nav>` membuat struktur HTML lebih semantik dan mudah dipahami browser maupun alat bantu aksesibilitas.

- `<div>`: elemen pembungkus umum untuk mengelompokkan konten.
	Contoh di sini: `<div>` pertama berisi logo/brand Ngrembaka Aksara.
	Alasan: logo bukan item daftar menu, jadi lebih tepat dibungkus dengan `<div>` agar mudah diatur posisinya.

- `<ul>`: wadah daftar (unordered list).
	Alasan: menu utama terdiri dari kumpulan tautan, sehingga tepat ditulis sebagai daftar agar struktur semantiknya jelas.

- `<li>`: item di dalam daftar.
	Alasan: setiap menu (Beranda, Visi, dan seterusnya) adalah satu item daftar, sehingga harus berada di dalam `<li>`.

- `<a>`: elemen tautan (link) ke halaman lain.
	Alasan: setiap menu perlu bisa diklik dan mengarah ke tujuan tertentu, jadi harus menggunakan `<a>`.

Referensi atribut pada elemen `<a>`:
- `href`: alamat tujuan tautan.
- `target`:
	- `_blank` membuka tautan di tab baru.
	- `_self` membuka tautan di tab yang sama.
- `rel`: contoh `noopener noreferrer`, dipakai saat `target="_blank"` untuk keamanan tambahan.
- `aria-label`: memberi deskripsi tambahan agar tautan lebih jelas bagi screen reader.



#### Implementasi CSS
```css
/* Wrapper utama navbar */
.na-navbar {
	display: flex;
	align-items: center;
	justify-content: space-between;
	gap: 1rem;
	padding: 0.75rem 1rem;
	background: #12301a;
	color: #ffffff;
}

/* Kolom 1: brand */
.na-brand {
	white-space: nowrap;
}

.na-brand a {
	color: #ffffff;
	text-decoration: none;
	font-weight: 700;
}

/* Kolom 2-10: menu utama */
.na-menu {
	list-style: none;
	display: flex;
	flex-wrap: wrap;
	align-items: center;
	justify-content: center;
	gap: 0.5rem 0.75rem;
	margin: 0;
	padding: 0;
	flex: 1;
}

.na-menu a {
	color: #e8f3e6;
	text-decoration: none;
	padding: 0.4rem 0.55rem;
	border-radius: 0.4rem;
	font-size: 0.95rem;
}

.na-menu a:hover,
.na-menu a:focus-visible {
	background: rgba(255, 255, 255, 0.14);
	color: #ffffff;
	outline: none;
}

/* Kolom 11: CTA WhatsApp */
.na-cta {
	white-space: nowrap;
}

.na-cta a {
	display: inline-block;
	text-decoration: none;
	background: #4f7a4e;
	color: #ffffff;
	padding: 0.5rem 0.85rem;
	border-radius: 999px;
	font-weight: 600;
}

.na-cta a:hover,
.na-cta a:focus-visible {
	background: #3f643e;
	outline: none;
}

/* Responsif: urutan vertikal di layar kecil */
@media (max-width: 991px) {
	.na-navbar {
		flex-direction: column;
		align-items: stretch;
	}

	.na-brand,
	.na-cta {
		text-align: center;
	}

	.na-menu {
		justify-content: center;
	}
}
```

```html
<nav class="na-navbar">

	<div class="na-brand">
		<a href="/" aria-label="Ngrembaka Aksara">Logo Ngrembaka Aksara</a>
	</div>

	<ul class="na-menu">
		<li><a href="/">Beranda</a></li>
		<li><a href="/beranda">Visi</a></li>
		<li><a href="/profil/ngrembaka-aksara">Profil Aksara</a></li>
		<li><a href="/profil/kelurahan-podorejo">Profil Kelurahan</a></li>
		<li><a href="/elibrary">E-Library</a></li>
		<li><a href="/pojok-literasi/tunas">Tunas</a></li>
		<li><a href="/pojok-literasi/karya">Karya</a></li>
		<li><a href="/pojok-literasi/cakra">Cakra</a></li>
		<li><a href="/pojok-literasi/kersa">Kersa</a></li>
	</ul>

	<div class="na-cta">
		<a href="https://wa.me/6281234567890" target="_blank" rel="noopener noreferrer">
			Hubungi Kami (WhatsApp)
		</a>
	</div>

</nav>
```


Keterangan CSS:

1. Wrapper utama navbar
Dalam satu blok `<nav>`, terdapat 3 bagian utama: `<div class="na-brand">`, `<ul class="na-menu">`, dan `<div class="na-cta">`.
Bagian ini ditata menggunakan Flexbox agar struktur navbar rapi dan mudah responsif.

- `display: flex;`
	Mengatur ketiga bagian utama agar tersusun dalam satu baris.
- `align-items: center;`
	Menyelaraskan semua elemen secara vertikal di tengah.
- `justify-content: space-between;`
	Memberi jarak antara elemen kiri (logo) dan kanan (CTA), sehingga keduanya berada di ujung.
- `gap: 1rem;`
	Memberi jarak antarblok di dalam navbar.
- `padding: 0.75rem 1rem;`
	Memberi ruang dalam navbar agar konten tidak menempel ke tepi.
- `background: #12301a;`
	Memberi warna latar navbar.
- `color: #ffffff;`
	Memberi warna teks default pada area navbar.

Catatan: satuan `rem` dipakai agar ukuran mengikuti font root (umumnya 16px), sehingga lebih fleksibel di berbagai ukuran layar.

2. Kolom 1: brand
- `white-space: nowrap;`
	Digunakan agar teks logo tetap satu baris dan tidak turun ke baris berikutnya.
- `.na-brand a`
	Digunakan untuk menata tautan logo agar tampil sebagai identitas utama:
	- `color: #ffffff;` memberi warna teks putih.
	- `text-decoration: none;` menghilangkan garis bawah tautan.
	- `font-weight: 700;` membuat teks logo lebih tebal.

3. Kolom 2-10: menu utama
- `list-style: none;`
	Menghilangkan bullet bawaan daftar pada elemen `<ul>`.
- `display: flex;`
	Menata item menu dalam satu baris horizontal.
- `flex-wrap: wrap;`
	Memungkinkan item pindah ke baris baru jika ruang tidak cukup.
- `align-items: center;`
	Menyelaraskan item menu secara vertikal di tengah.
- `justify-content: center;`
	Menyelaraskan item menu secara horizontal di tengah area menu.
- `gap: 0.5rem 0.75rem;`
	Memberi jarak antar item menu:
	- `0.5rem` untuk jarak vertikal.
	- `0.75rem` untuk jarak horizontal.
- `margin: 0;` dan `padding: 0;`
	Menghapus jarak bawaan elemen `<ul>` agar layout lebih presisi.
- `flex: 1;`
	Membuat area menu mengambil sisa ruang di antara logo (kiri) dan CTA (kanan), sehingga menu tetap berada di tengah.

Penjelasan singkat `display: flex` vs `flex: 1`:
- `display: flex` mengatur cara anak elemen disusun.
- `flex: 1` mengatur seberapa besar satu elemen mengambil ruang di dalam flex container.

4. Gaya tautan menu (`.na-menu a`)
- `color: #e8f3e6;` memberi warna teks hijau muda.
- `text-decoration: none;` menghilangkan garis bawah.
- `padding: 0.4rem 0.55rem;` memberi ruang klik yang lebih nyaman.
- `border-radius: 0.4rem;` membuat sudut tautan melengkung.
- `font-size: 0.95rem;` menyesuaikan ukuran teks menu.

5. State interaksi: `:hover` dan `:focus-visible`
- `:hover` aktif saat pointer/mouse berada di atas elemen.
- `:focus-visible` aktif saat elemen dipilih via keyboard (misalnya tombol Tab), penting untuk aksesibilitas.
- Pada keduanya, style dibuat sama agar konsisten:
```css
.na-menu a:hover,
.na-menu a:focus-visible {
	background: rgba(255, 255, 255, 0.14); // memberi latar belakang transparan putih saat hover/fokus
	color: #ffffff; // teks menjadi putih saat hover/fokus
	outline: none; // menghilangkan garis fokus default browser
}
```
6. Kolom 11: CTA WhatsApp
- `white-space: nowrap;` memastikan teks tombol tidak terpotong atau pindah baris.
- `.na-cta a` menata tombol CTA:
- `display: inline-block;` agar tombol bisa diberi padding dan ukuran.
- `text-decoration: none;` menghilangkan garis bawah.
- `background: #4f7a4e;` memberi warna hijau gelap.
- `color: #ffffff;` memberi warna teks putih.
- `padding: 0.5rem 0.85rem;` memberi ruang klik yang nyaman.
- `border-radius: 999px;` membuat tombol berbentuk kapsul.
- `font-weight: 600;` membuat teks tombol lebih tebal.  

7. Responsif: urutan vertikal di layar kecil
- `@media (max-width: 991px)` menargetkan layar dengan lebar maksimum 991px (umumnya tablet dan ponsel).
- Di dalam media query:
```css
.na-navbar {
    flex-direction: column; // mengubah arah flex menjadi vertikal
    align-items: stretch; // membuat semua elemen mengisi lebar penuh
}
.na-brand,.na-cta {
    text-align: center; // menengahkan teks logo dan tombol CTA
}
.na-menu {
    justify-content: center; // menengahkan menu utama
}                   
```

---

## 🟩 Pelajaran CSS yang harus dimengerti

### 1. **Flexbox**  
Properti penting: `display: flex`, `flex-direction`, `align-items`, `justify-content`, `flex-wrap`, `gap`.

**Arti:**  
Flexbox adalah cara modern untuk mengatur elemen agar rapi dalam baris atau kolom.

**Aturan:**  
- `display: flex` → mengaktifkan mode flex  
- `flex-direction: row` → elemen berbaris ke samping  
- `flex-direction: column` → elemen bertumpuk ke bawah  
- `justify-content` → mengatur posisi secara horizontal  
- `align-items` → mengatur posisi secara vertikal  
- `gap` → jarak antar elemen  

**Kenapa penting:**  
Flexbox membuat navbar bisa berubah otomatis:  
- **Layar lebar** → menu tampil **horizontal**  
- **Layar kecil** → menu tampil **vertikal**

Tanpa flexbox, kamu harus mengatur posisi satu per satu, jauh lebih sulit.

---

### 2. **Media Query**  
Contoh: `@media (max-width: 991px)`

**Arti:**  
Media query adalah aturan CSS yang hanya aktif pada ukuran layar tertentu.

**Aturan:**  
- `max-width: 991px` → aturan berlaku jika layar **lebih kecil dari 991px**  
- biasanya dipakai untuk mobile dan tablet  
- 991px dipilih karena standar Bootstrap: tablet < 992px

**Kenapa penting:**  
Supaya tampilan **responsif**, yaitu menyesuaikan ukuran layar.  
Contoh:  
- Desktop → menu horizontal  
- Mobile → menu vertikal agar tidak sempit

Tanpa media query, tampilan akan berantakan di HP.

---

### 3. **Pseudo-class**  
Contoh: `:hover`, `:focus-visible`

**Arti:**  
Pseudo-class adalah “keadaan khusus” pada elemen.

**Aturan:**  
- `:hover` → aktif saat mouse menyentuh elemen  
- `:focus-visible` → aktif saat elemen dipilih dengan keyboard (Tab)

**Kenapa harus ada hover?**  
Karena hover memberi **feedback visual**.  
Pengguna jadi tahu bahwa elemen itu **bisa diklik**.

**Tanpa hover boleh?**  
Boleh, tapi:  
- tampilan terasa kaku  
- pengguna tidak yakin link itu aktif  
- pengalaman pengguna lebih buruk

Hover = indikator bahwa tombol hidup.

---

### 4. **Box Model**  
Properti: `padding`, `margin`, `border-radius`

**Arti:**  
Box model menjelaskan bahwa setiap elemen adalah sebuah “kotak”.

**Aturan:**  
- `padding` → jarak dalam kotak  
- `margin` → jarak luar kotak  
- `border-radius` → sudut kotak dibuat melengkung

**Kenapa penting:**  
Tanpa box model, elemen akan menempel satu sama lain dan terlihat tidak rapi.

---

### 5. **Warna dan Kontras**  
**Arti:**  
Kontras adalah perbedaan warna antara teks dan latar belakang.

**Aturan:**  
- teks harus lebih terang atau lebih gelap dari background  
- hindari warna yang mirip (misal hijau tua di atas hijau tua)

**Kenapa penting:**  
Supaya teks **mudah dibaca**, terutama di layar kecil atau cahaya terang.

---

## 🟪 Ringkasan
- **Flexbox** → mengatur posisi elemen agar rapi  
- **Media query** → membuat tampilan responsif  
- **Hover & focus-visible** → efek interaksi pengguna  
- **Box model** → mengatur jarak dan bentuk elemen  
- **Kontras warna** → memastikan teks terbaca

---


#### Implementasi menu dinamis 
- (hamburger) untuk layar kecil, 
- submenu profil untuk menu Profil Aksara dan Profil Kelurahan,
- submenu untuk menu Pojok Literasi (Tunas, Karya, Cakra, Kersa).

Catatan perilaku:
- Desktop: menu tampil horizontal, submenu muncul saat hover atau fokus.
- Mobile: menu utama dibuka lewat tombol hamburger, submenu dibuka lewat tombol panah.
- Aksesibilitas: setiap tombol submenu menggunakan atribut aria-expanded.

```html
<!DOCTYPE html>
<html lang="id">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Navbar Dinamis Ngrembaka Aksara</title>

	<style>
		:root {
			--na-bg: #12301a;
			--na-bg-soft: #1b4625;
			--na-text: #ffffff;
			--na-text-soft: #e8f3e6;
			--na-accent: #4f7a4e;
			--na-accent-hover: #3f643e;
			--na-border: rgba(255, 255, 255, 0.15);
		}

		* { box-sizing: border-box; }

		body {
			margin: 0;
			font-family: Arial, sans-serif;
			background: #f5f8f4;
		}

		.na-navbar {
			background: var(--na-bg);
			color: var(--na-text);
			display: flex;
			align-items: center;
			justify-content: space-between;
			gap: 1rem;
			padding: 0.75rem 1rem;
			position: relative;
		}

		.na-brand a {
			color: var(--na-text);
			text-decoration: none;
			font-weight: 700;
			white-space: nowrap;
		}

		.na-toggle {
			display: none;
			border: 1px solid var(--na-border);
			background: transparent;
			color: var(--na-text);
			border-radius: 0.5rem;
			padding: 0.45rem 0.6rem;
			cursor: pointer;
			font-size: 1rem;
			line-height: 1;
		}

		.na-menu-wrap {
			display: flex;
			align-items: center;
			gap: 1rem;
			flex: 1;
			justify-content: space-between;
		}

		.na-menu {
			list-style: none;
			margin: 0;
			padding: 0;
			display: flex;
			align-items: center;
			gap: 0.3rem;
			flex-wrap: wrap;
		}

		.na-menu > li {
			position: relative;
		}

		.na-menu a,
		.na-subtoggle {
			color: var(--na-text-soft);
			text-decoration: none;
			display: inline-flex;
			align-items: center;
			gap: 0.35rem;
			padding: 0.45rem 0.6rem;
			border-radius: 0.4rem;
			border: 0;
			background: transparent;
			font: inherit;
			cursor: pointer;
		}

		.na-menu a:hover,
		.na-menu a:focus-visible,
		.na-subtoggle:hover,
		.na-subtoggle:focus-visible {
			background: rgba(255, 255, 255, 0.14);
			color: var(--na-text);
			outline: none;
		}

		.na-submenu {
			list-style: none;
			margin: 0;
			padding: 0.35rem;
			position: absolute;
			top: calc(100% + 0.25rem);
			left: 0;
			min-width: 220px;
			border-radius: 0.65rem;
			background: var(--na-bg-soft);
			border: 1px solid var(--na-border);
			display: none;
			z-index: 10;
		}

		.na-submenu a {
			width: 100%;
		}

		.na-item.has-submenu:hover > .na-submenu,
		.na-item.has-submenu:focus-within > .na-submenu,
		.na-item.has-submenu.open > .na-submenu {
			display: block;
		}

		.na-cta a {
			display: inline-block;
			text-decoration: none;
			color: var(--na-text);
			background: var(--na-accent);
			border-radius: 999px;
			padding: 0.5rem 0.9rem;
			font-weight: 600;
			white-space: nowrap;
		}

		.na-cta a:hover,
		.na-cta a:focus-visible {
			background: var(--na-accent-hover);
			outline: none;
		}

		@media (max-width: 991px) {
			.na-toggle {
				display: inline-flex;
			}

			.na-menu-wrap {
				display: none;
				position: absolute;
				top: 100%;
				left: 0;
				right: 0;
				background: var(--na-bg);
				border-top: 1px solid var(--na-border);
				padding: 0.8rem 1rem 1rem;
				flex-direction: column;
				align-items: stretch;
				gap: 0.75rem;
			}

			.na-menu-wrap.open {
				display: flex;
			}

			.na-menu {
				flex-direction: column;
				align-items: stretch;
			}

			.na-menu a,
			.na-subtoggle {
				width: 100%;
				justify-content: space-between;
			}

			.na-submenu {
				position: static;
				min-width: 0;
				margin-top: 0.35rem;
				background: rgba(255, 255, 255, 0.05);
			}

			.na-cta a {
				display: block;
				text-align: center;
			}
		}
	</style>
</head>

<body>

	<nav class="na-navbar" aria-label="Navigasi utama">
		<div class="na-brand">
			<a href="/" aria-label="Ngrembaka Aksara">Logo Ngrembaka Aksara</a>
		</div>

		<button class="na-toggle" type="button" aria-expanded="false" aria-controls="naMenuWrap">
			<span aria-hidden="true">☰</span>
			<span class="sr-only">Buka menu</span>
		</button>

		<div class="na-menu-wrap" id="naMenuWrap">
			<ul class="na-menu">
				<li><a href="/">Beranda</a></li>
				<li><a href="/beranda">Visi</a></li>

				<li class="na-item has-submenu">
					<button class="na-subtoggle" type="button" aria-expanded="false">
						Profil
						<span aria-hidden="true">▾</span>
					</button>
					<ul class="na-submenu">
						<li><a href="/profil/ngrembaka-aksara">Profil Aksara</a></li>
						<li><a href="/profil/kelurahan-podorejo">Profil Kelurahan</a></li>
					</ul>
				</li>

				<li><a href="/elibrary">E-Library</a></li>

				<li class="na-item has-submenu">
					<button class="na-subtoggle" type="button" aria-expanded="false">
						Pojok Literasi
						<span aria-hidden="true">▾</span>
					</button>
					<ul class="na-submenu">
						<li><a href="/pojok-literasi/tunas">Tunas</a></li>
						<li><a href="/pojok-literasi/karya">Karya</a></li>
						<li><a href="/pojok-literasi/cakra">Cakra</a></li>
						<li><a href="/pojok-literasi/kersa">Kersa</a></li>
					</ul>
				</li>
			</ul>

			<div class="na-cta">
				<a href="https://wa.me/6281234567890" target="_blank" rel="noopener noreferrer">
					Hubungi Kami (WhatsApp)
				</a>
			</div>
		</div>
	</nav>

	<script>
		// 1) Ambil elemen utama navbar
		const menuToggle = document.querySelector('.na-toggle');
		const menuWrap = document.querySelector('.na-menu-wrap');
		const submenuToggles = document.querySelectorAll('.na-subtoggle');

		// 2) Toggle menu utama saat tombol hamburger diklik
		menuToggle.addEventListener('click', () => {
			const isOpen = menuWrap.classList.toggle('open');
			menuToggle.setAttribute('aria-expanded', String(isOpen));
		});

		// 3) Toggle submenu (Profil dan Pojok Literasi)
		submenuToggles.forEach((button) => {
			button.addEventListener('click', () => {
				const parentItem = button.closest('.has-submenu');
				const isOpen = parentItem.classList.toggle('open');
				button.setAttribute('aria-expanded', String(isOpen));
			});
		});
	</script>
</body>
</html>

```

Keterangan script:
- `menuToggle`:
	Menyimpan referensi tombol hamburger (`.na-toggle`) yang dipakai untuk buka/tutup menu utama di layar kecil.
- `menuWrap`:
	Menyimpan elemen pembungkus menu (`.na-menu-wrap`) yang akan diberi class `open` saat menu dibuka.
- `submenuToggles`:
	Mengambil semua tombol submenu (`.na-subtoggle`) seperti tombol Profil dan Pojok Literasi.
- Event klik hamburger:
	`classList.toggle('open')` dipakai untuk mengubah status tampil/sembunyi menu utama.
	Nilai `aria-expanded` diubah ke `true/false` agar status menu terbaca oleh screen reader.
- Event klik submenu:
	Mencari parent `.has-submenu`, lalu toggle class `open` agar submenu muncul atau tertutup.
	`aria-expanded` pada tombol submenu juga ikut diperbarui.

