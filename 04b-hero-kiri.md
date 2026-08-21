### 7.2 Hero Kiri (Pesan Utama)

#### Struktur Konten Hero
Bagian hero kiri adalah area paling penting di halaman landing. Di sini kita menyampaikan pesan utama, menggugah minat pengunjung, dan mengarahkan mereka ke halaman berikutnya.

Komponen utama hero kiri:
- Kicker: "Buku untuk semua generasi"
- Badge: "PPK ORMAWA 2026"
- Judul utama: "E-LIBRARY PPK ORMAWA NGREMBAKA AKSARA"
- Deskripsi singkat: menjelaskan program dan tujuan literasi
- CTA utama: "Selengkapnya" ke halaman /beranda
- CTA sekunder: "E-Library" ke halaman /elibrary

#### Desain Visual dalam tabel

| b/k | kolom1 | kolom2 |
|---|---|---|
| baris1 | Kicker | Badge |
| baris2 | Judul utama |  |
| baris3 | Deskripsi |  |
| baris4 | CTA utama | CTA sekunder |

Catatan layout:
- Kolom1 berfungsi sebagai area teks utama.
- Kicker berada di posisi paling atas agar pembaca langsung menangkap tema.
- Badge berada di bawah kicker sebagai label program.
- Judul utama adalah fokus utama yang ingin dibaca pertama kali.
- Deskripsi berfungsi sebagai penjelasan singkat tentang program.
- Dua tombol CTA membantu user bergerak ke halaman yang diinginkan.

---

#### Implementasi HTML tanpa CSS

```html
<section>
	<div>
		<p>Buku untuk semua generasi.</p>
		<span>PPK ORMAWA 2026</span>
		<h1>
			E-LIBRARY PPK ORMAWA
			NGREMBAKA AKSARA
		</h1>
		<p>
			Ngrembaka Aksara adalah program penguatan literasi dan edupreneur skill lintas generasi
			yang hadir di Kelurahan Podorejo, Kecamatan Ngaliyan, Kota Semarang.
			Digagas oleh mahasiswa SGL PGSD Universitas Negeri Semarang melalui PPK ORMAWA tahun 2026.
		</p>
		<div>
			<a href="/beranda">Selengkapnya</a>
			<a href="/elibrary">E-Library</a>
		</div>
	</div>
</section>
```

Keterangan dasar HTML:
- `<section>`: elemen pembungkus bagian utama pada halaman.
  Alasan: hero adalah bagian yang berdiri sendiri, jadi lebih semantik menggunakan `<section>`.

- `<div>`: pembungkus umum untuk kelompok isi hero.
  Alasan: bagian kiri memiliki beberapa elemen yang harus dikelompokkan agar mudah diatur layout dan styling.

- `<p>`: paragraf untuk kicker dan deskripsi.
  Alasan: teks pendek seperti slogan atau penjelasan lebih cocok ditulis dengan `<p>`.

- `<span>`: elemen inline untuk badge kecil.
  Alasan: badge biasanya singkat dan tidak perlu blok penuh, jadi `span` cocok.

- `<h1>`: judul utama halaman.
  Alasan: judul utama harus punya prioritas paling tinggi untuk SEO dan struktur dokumen.

- `<a>`: tombol link yang bisa diklik.
  Alasan: CTA harus mengarahkan user ke halaman lain.

Atribut penting pada link:
- `href`: tujuan halaman tujuan.
- `target="_blank"`: bila link dibuka di tab baru.
- `rel="noopener noreferrer"`: keamanan saat link dibuka di tab baru.

---

#### Implementasi CSS

```css
/* Wrapper utama hero */
.na-hero {
	display: flex;
	align-items: center;
	justify-content: space-between;
	gap: 2rem;
	padding: 4rem 1.5rem;
	background: linear-gradient(135deg, #f4f8f1 0%, #eaf5ea 100%);
	color: #12301a;
}

/* Kolom kiri: teks hero */
.na-hero-copy {
	max-width: 620px;
}

.na-kicker {
	margin: 0 0 0.75rem;
	font-size: 0.9rem;
	font-weight: 700;
	letter-spacing: 0.08em;
	text-transform: uppercase;
	color: #4f7a4e;
}

.na-badge {
	display: inline-block;
	margin-bottom: 1rem;
	padding: 0.45rem 0.8rem;
	background: #dfeee0;
	color: #12301a;
	border-radius: 999px;
	font-size: 0.8rem;
	font-weight: 700;
}

.na-title {
	margin: 0;
	font-size: clamp(2.2rem, 4vw, 4rem);
	line-height: 1.1;
	font-weight: 800;
	color: #12301a;
}

.na-title span {
	display: block;
}

.na-description {
	margin-top: 1.2rem;
	font-size: 1.05rem;
	line-height: 1.7;
	color: #2d4f2f;
}

/* Area tombol CTA */
.na-actions {
	display: flex;
	flex-wrap: wrap;
	gap: 0.85rem;
	margin-top: 1.6rem;
}

.na-btn {
	display: inline-block;
	padding: 0.85rem 1.35rem;
	border-radius: 999px;
	text-decoration: none;
	font-weight: 700;
	transition: all 0.2s ease;
}

.na-btn-primary {
	background: #12301a;
	color: #ffffff;
}

.na-btn-primary:hover,
.na-btn-primary:focus-visible {
	background: #1d4326;
	outline: none;
}

.na-btn-secondary {
	background: transparent;
	color: #12301a;
	border: 1px solid #12301a;
}

.na-btn-secondary:hover,
.na-btn-secondary:focus-visible {
	background: #12301a;
	color: #ffffff;
	outline: none;
}

/* Responsif */
@media (max-width: 991px) {
	.na-hero {
		flex-direction: column;
		align-items: flex-start;
	}

	.na-hero-copy {
		max-width: 100%;
	}

	.na-actions {
		flex-direction: column;
		align-items: stretch;
	}

	.na-btn {
		text-align: center;
	}
}
```

```html
<section class="na-hero">
	<div class="na-hero-copy">
		<p class="na-kicker">Buku untuk semua generasi.</p>
		<span class="na-badge">PPK ORMAWA 2026</span>

		<h1 class="na-title">
			<span>E-LIBRARY</span>
			<span>PPK ORMAWA</span>
			<span>NGREMBAKA AKSARA</span>
		</h1>

		<p class="na-description">
			Ngrembaka Aksara adalah program penguatan literasi dan edupreneur skill lintas generasi
			yang hadir di Kelurahan Podorejo, Kecamatan Ngaliyan, Kota Semarang.
			Digagas oleh mahasiswa SGL PGSD Universitas Negeri Semarang melalui PPK ORMAWA tahun 2026.
		</p>

		<div class="na-actions">
			<a href="/beranda" class="na-btn na-btn-primary">Selengkapnya</a>
			<a href="/elibrary" class="na-btn na-btn-secondary">E-Library</a>
		</div>
	</div>
</section>
```

---

#### Keterangan CSS per bagian

1. Wrapper utama hero
- `display: flex;`
  Mengatur bagian kiri dan kanan agar berdampingan dalam satu baris.
- `align-items: center;`
  Menyelaraskan elemen secara vertikal di tengah.
- `justify-content: space-between;`
  Memberi ruang di antara teks dan visual kanan (nanti bisa ditambah gambar atau ilustrasi).
- `gap: 2rem;`
  Menambahkan jarak antar dua kolom.
- `padding: 4rem 1.5rem;`
  Memberi ruang agar elemen tidak menempel ke tepi layar.
- `background: linear-gradient(...)`
  Memberi latar belakang yang bergradasi agar hero terlihat lebih hidup dan profesional.

2. Kicker
- `letter-spacing: 0.08em;`
  Menambahkan spasi antar huruf agar teks terasa lebih formal.
- `text-transform: uppercase;`
  Mengubah huruf menjadi kapital agar tampil seperti label atau kategori.
- `color: #4f7a4e;`
  Memberi warna hijau yang konsisten dengan brand.

3. Badge
- `display: inline-block;`
  Membuat badge tidak mengambil lebar penuh.
- `padding` memberi ruang agar badge terlihat jelas.
- `border-radius: 999px;`
  Membuat sudut badge bulat seperti tombol kecil.

4. Judul utama
- `font-size: clamp(2.2rem, 4vw, 4rem);`
  Ukuran font mengikuti lebar layar, supaya judul tetap enak dibaca di desktop maupun mobile.
- `line-height: 1.1;`
  Jarak antar baris dibuat rapat agar judul tidak terlalu berjarak.
- `font-weight: 800;`
  Membuat judul terlihat tebal dan berani.
- `.na-title span { display: block; }`
  Membuat tiap baris judul berada di baris berbeda.

5. Deskripsi
- `line-height: 1.7;`
  Jarak antar baris dibuat lebih lega agar teks mudah dibaca.
- `color: #2d4f2f;`
  Memberi warna teks yang lebih lembut tapi tetap kontras.

6. Tombol CTA
- `display: inline-block;`
  Membuat tombol punya ukuran dan ruang padding.
- `border-radius: 999px;`
  Membuat tombol membulat seperti bentuk modern.
- `text-decoration: none;`
  Menghilangkan garis bawah default link.
- `transition: all 0.2s ease;`
  Memberi efek halus saat hover.

7. State hover dan focus
- `:hover` dan `:focus-visible` dipakai untuk memberi feedback ketika user mengarahkan mouse atau keyboard.
- `outline: none` dipakai agar desain tetap rapi tanpa garis fokus default browser.

8. Responsif
- `@media (max-width: 991px)` diterapkan saat layar mengecil.
- `flex-direction: column;` mengubah layout menjadi vertikal.
- `align-items: flex-start;` membuat teks rata kiri agar lebih sederhana di layar kecil.
- `.na-actions { flex-direction: column; }` membuat tombol CTA turun ke bawah satu per satu.

---

#### Mengapa hero kiri penting?
Hero kiri adalah elemen pertama yang dilihat pengunjung ketika masuk ke landing page. Jika hero kiri bagus, maka orang akan tertarik untuk terus membaca.

Hero yang baik biasanya memiliki 4 tugas utama:
1. Menarik perhatian
2. Menjelaskan siapa programnya
3. Menjelaskan tujuan program
4. Mengajak user melakukan aksi

Dengan kata lain, hero kiri bukan hanya teks. Ia adalah alat komunikasi utama halaman landing.

---

#### Langkah belajar bertahap

1. Buat struktur HTML sederhana
   - buat `section`
   - buat `div`
   - isi dengan kicker, badge, judul, deskripsi, tombol

2. Tambahkan kelas CSS secara bertahap
   - mulai dari layout `display: flex`
   - lalu atur heading dan teks
   - lalu atur tombol CTA
   - lalu tambahkan media query

3. Uji tampilannya di browser
   - cek apakah teks rapi di desktop
   - cek apakah tombol berjarak benar
   - cek apakah judul tidak terlalu besar

4. Tingkatkan desain
   - tambahkan gambar di kanan hero
   - tambahkan shadow
   - sesuaikan warna agar lebih menarik

5. Integrasikan ke halaman landing
   - gabungkan navbar + hero
   - pastikan spacing konsisten
   - pastikan tombol dan teks berada pada satu fokus visual

---

#### Ringkasan singkat

Hero kiri adalah bagian yang berisi pesan utama landing page. Struktur dasarnya sederhana:
- kicker
- badge
- judul
- deskripsi
- CTA

Dengan HTML dan CSS yang benar, bagian ini bisa berubah dari sekadar teks biasa menjadi elemen yang kuat dan profesional.

Inilah inti dari layout landing page: struktur yang jelas + styling yang konsisten + akhiran yang mengajak user bertindak.

---

#### Latihan kecil
Coba buat versi sendiri dengan tema berikut:
- kicker: "Belajar dari rumah"
- badge: "Kelas Digital 2026"
- judul: "BANGUN KETERAMPILAN TEKNOLOGI"
- deskripsi: teks singkat tentang program belajar teknologi
- tombol: "Daftar" dan "Lihat Materi"

Tujuan latihan:
- ubah teks tanpa mengubah struktur HTML,
- ubah warna untuk sesuai tema,
- atur tata letak agar tetap rapi di layar kecil.

Ini adalah latihan penting agar siswa memahami bahwa HTML dan CSS bukan hanya untuk tampilan, tapi juga untuk komunikasi dan pengalaman pengguna.

