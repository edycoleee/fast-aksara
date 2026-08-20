# Branch Pembelajaran JavaScript

Branch ini dibuat untuk belajar JavaScript secara bertahap agar siswa bisa membangun aplikasi web interaktif, mulai dari konsep dasar sampai integrasi dengan backend seperti FastAPI dan Jinja2.

Referensi utama: `02-js.md`

---

## Tujuan branch ini

Tujuan pembelajaran JavaScript di branch ini adalah agar siswa mampu:
- memahami logika pemrograman dasar,
- menulis program JavaScript dengan benar,
- mengubah elemen HTML melalui DOM,
- menangkap event dari user,
- memvalidasi form,
- menggunakan data array dan object,
- mengolah data dari backend melalui `fetch` dan API,
- membangun interaksi web yang hidup dan dinamis.

---

## Urutan belajar yang paling tepat

Untuk aplikasi web seperti ini, belajar JavaScript sebaiknya mengikuti urutan berikut:

1. Dasar JavaScript
2. Fungsi dan scope
3. Array dan object
4. DOM (Document Object Model)
5. Event listener
6. Form validation
7. ES6 modern
8. Async JS dan fetch
9. Manipulasi data frontend
10. State dan pola aplikasi sederhana
11. Debugging dan latihan proyek nyata

Jangan langsung belajar framework. Kita harus kuat di konsep dasar dulu agar nanti framework terasa mudah.

---

## 1. Tahap 1: Dasar JavaScript

Ini adalah fondasi utama.

### Yang dipelajari:
- variabel: `let`, `const`
- tipe data: string, number, boolean, null, undefined
- operator: aritmatika, perbandingan, logika
- kondisi: `if`, `else if`, `else`
- perulangan: `for`, `while`
- fungsi dasar

### Contoh:
```js
let nama = "Aksara";
const usia = 16;

if (usia >= 17) {
  console.log("Dewasa");
} else {
  console.log("Masih siswa");
}

for (let i = 1; i <= 3; i++) {
  console.log("Iterasi ke-" + i);
}
```

### Target pemahaman:
- memahami alur program dari atas ke bawah,
- bisa menulis logika sederhana,
- bisa membaca error di console.

---

## 2. Tahap 2: Fungsi dan scope

Fungsi merupakan blok kode yang bisa dipakai berulang.

### Yang dipelajari:
- function declaration
- function expression
- parameter dan return value
- arrow function
- scope lokal dan global

### Contoh:
```js
function hitungLuas(panjang, lebar) {
  return panjang * lebar;
}

const hasil = hitungLuas(5, 4);
console.log(hasil);

const tambah = (a, b) => a + b;
console.log(tambah(3, 7));
```

### Kapan dipakai?
- validasi form,
- hitung total,
- filter data,
- buka atau tutup modal,
- kirim request ke server.

---

## 3. Tahap 3: Array dan object

Data aplikasi web biasanya berbentuk array dan object.

### Yang dipelajari:
- array: `push`, `pop`, `shift`, `unshift`
- array lanjutan: `map`, `filter`, `find`
- object: properti dan method
- nested object
- destructuring

### Contoh:
```js
const artikel = [
  { judul: "Aksara Jawa", kategori: "Budaya" },
  { judul: "Sejarah Desa", kategori: "Sejarah" },
  { judul: "Kebudayaan", kategori: "Budaya" }
];

const hasil = artikel.filter(item => item.kategori === "Budaya");
console.log(hasil);

const { judul } = artikel[0];
console.log(judul);
```

### Kenapa penting?
Aplikasi web selalu berhubungan dengan:
- daftar artikel,
- daftar dokumentasi,
- daftar pengguna,
- data form,
- hasil API.

---

## 4. Tahap 4: DOM (Document Object Model)

DOM adalah cara JavaScript berinteraksi dengan HTML.

### Yang dipelajari:
- `document.getElementById()`
- `document.querySelector()`
- `document.querySelectorAll()`
- `textContent`
- `innerHTML`
- `createElement()`
- `remove()`

### Contoh:
```js
const judul = document.querySelector("h1");
judul.textContent = "Selamat Datang";

const tombol = document.getElementById("tombol");
tombol.addEventListener("click", () => {
  alert("Tombol diklik");
});
```

### Kenapa penting?
Tanpa DOM, JavaScript tidak bisa:
- mengubah teks,
- menambah atau menghapus elemen,
- membuka modal,
- update list data,
- membuat halaman terasa interaktif.

---

## 5. Tahap 5: Event dan interaksi user

Event adalah aksi dari user yang ditangkap oleh JavaScript.

### Event utama:
- `click`
- `submit`
- `input`
- `change`
- `keyup`
- `mouseover`
- `focus`
- `blur`

### Contoh:
```js
const button = document.querySelector("button");
button.addEventListener("click", function () {
  console.log("User menekan tombol");
});

const input = document.querySelector("input");
input.addEventListener("input", function () {
  console.log(input.value);
});
```

### Penerapan di aplikasi:
- tombol login,
- tombol tambah artikel,
- tombol edit/hapus,
- form pencarian,
- menu mobile,
- modal konfirmasi.

---

## 6. Tahap 6: Validasi form dan data user

Validasi input sangat penting untuk aplikasi web.

### Yang dipelajari:
- `required`
- cek string kosong
- cek panjang teks
- cek email
- cek angka
- menampilkan pesan error

### Contoh:
```js
const form = document.querySelector("form");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const nama = document.getElementById("nama").value.trim();

  if (!nama) {
    alert("Nama tidak boleh kosong");
    return;
  }

  console.log("Data valid:", nama);
});
```

### Kegunaan:
- form login admin,
- form tambah artikel,
- form edit dokumentasi,
- form upload,
- form pencarian,
- validasi data user.

---

## 7. Tahap 7: ES6 modern

Setelah dasar kuat, siswa belajar JavaScript yang lebih modern dan rapi.

### Yang dipelajari:
- template literals: `` `teks ${variabel}` ``
- spread operator: `...`
- destructuring
- default parameter
- rest parameter
- optional chaining: `?.`
- modules: `import` dan `export`

### Contoh:
```js
const nama = "Aksara";
console.log(`Halo ${nama}`);

const data = [1, 2, 3];
const baru = [...data, 4];
console.log(baru);

const user = { nama: "Admin", role: "admin" };
const { nama: namaUser } = user;
console.log(namaUser);
```

### Mengapa penting?
Kode modern lebih singkat, lebih mudah dibaca, dan lebih sering dipakai pada proyek nyata.

---

## 8. Tahap 8: Async JavaScript dan fetch

JavaScript modern juga harus bisa berkomunikasi dengan server.

### Yang dipelajari:
- `fetch()`
- Promise
- `async` dan `await`
- menangani error
- mengambil data dari API

### Contoh:
```js
async function ambilData() {
  const response = await fetch("/api/artikel");
  const data = await response.json();
  console.log(data);
}
```

### Kegunaan:
- mengambil artikel dari backend,
- menampilkan data ke halaman,
- menambah dan menghapus data tanpa reload,
- membuat aplikasi lebih dinamis.

---

## 9. Tahap 9: Manipulasi data di frontend

Setelah memahami array, object, DOM, dan API, siswa mulai memanipulasi data dengan cara yang lebih nyata.

### Fokus:
- menampilkan list data ke HTML,
- filter data berdasarkan kategori,
- mencari item,
- menambah item baru,
- mengubah item yang sudah ada,
- menampilkan status kosong jika data tidak ada.

### Contoh pola:
```js
const artikel = [
  { judul: "Aksara Jawa" },
  { judul: "Sejarah Desa" }
];

artikel.forEach(item => {
  console.log(item.judul);
});
```

---

## 10. Tahap 10: State dan pola aplikasi sederhana

Pada level lanjut, JavaScript tidak hanya digunakan untuk satu button, tapi untuk mengelola state aplikasi.

### Yang dipelajari:
- data aplikasi dalam variabel,
- saat data berubah, tampilan berubah,
- function reusable,
- pemisahan logika dan tampilan,
- pola dasar aplikasi interaktif.

### Contoh:
- daftar artikel yang bisa ditambah,
- menu aktif berdasarkan klik,
- filter kategori,
- modal konfirmasi,
- tombol edit dan delete.

---

## 11. Tahap 11: Debugging dan latihan proyek nyata

Siswa harus belajar cara membaca error dan mengecek hasil kode.

### Praktik penting:
- membuka console browser,
- mengecek `console.log()`,
- membaca error message,
- memeriksa elemen HTML di inspect,
- mencoba satu perubahan kecil lalu cek hasilnya.

### Latihan proyek:
- halaman profil sederhana,
- daftar artikel dengan tombol hapus,
- form tambah data,
- sidebar menu interaktif,
- landing page sekolah/desa,
- aplikasi CRUD sederhana.

---

## Target akhir pembelajaran

Setelah mempelajari materi ini, siswa diharapkan mampu:
- menulis JavaScript dasar dengan benar,
- memanipulasi DOM,
- menangani berbagai event,
- validasi form,
- mengolah array/object,
- berinteraksi dengan backend API,
- membuat halaman web yang lebih hidup dan interaktif.

Ini adalah fondasi sebelum masuk ke:
- Jinja2,
- FastAPI,
- integrasi frontend-backend,
- CRUD aplikasi web.

---

## Kesimpulan

JavaScript adalah bahasa yang membuat web menjadi interaktif.

- HTML = struktur halaman,
- CSS = tampilan halaman,
- JavaScript = logika dan interaksi.

Tanpa JavaScript, website hanya terlihat statis. Dengan JavaScript, halaman bisa:
- bereaksi saat user klik,
- menampilkan data dinamis,
- mengubah isi halaman,
- memvalidasi input,
- mengirim dan menerima data dari server.

Itulah alasan JavaScript sangat penting dalam membangun aplikasi web modern.

---

## Rangkuman singkat

JavaScript untuk aplikasi web ini belajar dari:
- dasar program,
- fungsi,
- array/object,
- DOM,
- event,
- validasi,
- ES6,
- async/fetch,
- interaksi data,
- proyek nyata.

Semua itu akan menjadi bekal utama sebelum masuk ke bagian Jinja2 dan FastAPI.
