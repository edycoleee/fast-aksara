# Branch Pembelajaran JavaScript

Branch ini berisi materi belajar JavaScript yang runtut dan praktis untuk membangun aplikasi web dari dasar sampai siap dipakai di proyek nyata.

Referensi utama: `02-js.md`

---

## Tujuan belajar

Tujuan utama dari pembelajaran ini adalah supaya siswa mampu:
- memahami logika pemrograman JavaScript,
- menulis program sederhana dengan benar,
- mengubah tampilan HTML melalui DOM,
- menangkap interaksi user dengan event,
- memvalidasi form,
- menggunakan array dan object,
- belajar ES6 modern,
- berinteraksi dengan API dan backend,
- membuat halaman web yang lebih hidup dan dinamis.

---

## Urutan belajar yang disarankan

Materi yang ada di `02-js.md` mengikuti urutan yang logis:

1. Dasar JavaScript
2. Fungsi dan scope
3. Array dan object
4. DOM (Document Object Model)
5. Event listener
6. Form validation
7. ES6 modern
8. Async JS dan fetch
9. Manipulasi data di frontend
10. State dan pola aplikasi sederhana
11. Debugging dan latihan proyek nyata

Jangan langsung masuk ke framework. Kuatkan dulu konsep dasar JavaScript, baru nanti framework akan terasa lebih mudah.

---

## 1. Dasar JavaScript

Ini adalah tahap paling penting.

Yang harus dikuasai:
- variabel `let` dan `const`
- tipe data string, number, boolean, null, undefined
- operator aritmatika, perbandingan, dan logika
- kondisi `if`, `else if`, `else`
- perulangan `for` dan `while`
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

### Fokus latihan:
- menghitung jumlah bilangan,
- menentukan nilai siswa,
- menampilkan nama dengan urutan tertentu.

---

## 2. Fungsi dan scope

Fungsi adalah blok kode yang bisa dipakai berulang.

### Yang dipelajari:
- function declaration,
- function expression,
- parameter dan return value,
- arrow function,
- scope lokal dan global,
- hoisting dasar.

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

### Kegunaan:
- validasi form,
- kalkulasi data,
- filter daftar,
- buka/tutup modal,
- kirim data ke API.

---

## 3. Array dan object

Data di aplikasi web biasanya berbentuk array dan object.

### Yang dipelajari:
- array: `push`, `pop`, `shift`, `unshift`, `map`, `filter`, `find`
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

### Latihan yang cocok:
- menampilkan semua judul artikel,
- filter artikel berdasarkan kategori,
- ubah format object menjadi array baru.

---

## 4. DOM (Document Object Model)

DOM adalah cara JavaScript berinteraksi dengan HTML.

### Yang dipelajari:
- `getElementById()`
- `querySelector()`
- `querySelectorAll()`
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
- menutup modal,
- update data di halaman,
- membuat halaman menjadi interaktif.

---

## 5. Event dan interaksi user

Event adalah aksi yang dilakukan user, seperti klik, input, submit, dan hover.

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
- tombol edit dan hapus,
- form pencarian,
- menu mobile,
- modal konfirmasi.

---

## 6. Validasi form dan data user

Validasi sangat penting untuk menjaga data masuk dengan benar.

### Yang dipelajari:
- `required`
- cek string kosong
- cek panjang teks
- cek email
- cek angka
- tampilkan pesan error

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

## 7. ES6 modern

Setelah dasar kuat, siswa masuk ke JavaScript modern.

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

---

## 8. Async JavaScript dan fetch

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

### Kegunaannya:
- mengambil artikel dari backend,
- menampilkan data ke halaman,
- menambah dan menghapus data tanpa reload,
- membuat aplikasi lebih dinamis.

---

## 9. Manipulasi data di frontend

Setelah memahami array, object, DOM, dan API, siswa mulai memanipulasi data dengan lebih nyata.

### Fokus:
- menampilkan list data ke HTML,
- filter data berdasarkan kategori,
- mencari item,
- menambah item baru,
- mengubah item yang ada,
- menampilkan status kosong jika data tidak ada.

---

## 10. State dan pola aplikasi sederhana

Pada level lanjut, JavaScript tidak hanya dipakai untuk satu tombol, tapi untuk mengelola state aplikasi.

### Yang dipelajari:
- data aplikasi di variabel,
- saat data berubah, tampilan ikut berubah,
- fungsi reusable,
- pola dasar aplikasi interaktif.

### Contoh:
- daftar artikel yang bisa ditambah,
- menu aktif saat diklik,
- filter kategori,
- modal konfirmasi,
- tombol edit dan delete.

---

## 11. Debugging dan latihan proyek nyata

Pembelajaran JavaScript tidak lengkap tanpa latihan debugging.

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
- menangani event user,
- memvalidasi form,
- menggunakan array dan object,
- berinteraksi dengan backend API,
- membuat halaman yang hidup dan interaktif.

Ini adalah bekal utama sebelum masuk ke tahap berikutnya:
- Jinja2,
- FastAPI,
- integrasi frontend-backend,
- CRUD aplikasi web.

---

## Kesimpulan

JavaScript adalah bahasa yang membuat web menjadi interaktif.

- HTML = struktur halaman
- CSS = tampilan halaman
- JavaScript = logika dan interaksi

Tanpa JavaScript, website hanya statis. Dengan JavaScript, halaman bisa:
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
