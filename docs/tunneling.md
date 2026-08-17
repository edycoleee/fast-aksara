# Tunneling `aksara.fun` ke Server `192.10.10.152:3004`

Dokumen ini menjelaskan alur lengkap dari awal sampai domain publik bisa mengakses aplikasi yang berjalan di server lokal `192.10.10.152` pada port `3004`.

Target akhir:

- Aplikasi berjalan di server: `http://192.10.10.152:3004`
- Akses publik melalui Cloudflare Tunnel: `https://aksara.fun`
- Traffic publik tetap aman tanpa membuka port aplikasi ke internet langsung

## 1. Gambaran Arsitektur

Alur request yang benar adalah:

```text
Browser → https://aksara.fun → Cloudflare Edge → Cloudflare Tunnel → 192.10.10.152:3004
```

Artinya:

1. User membuka `https://aksara.fun`
2. Cloudflare menerima request di edge
3. Cloudflare Tunnel meneruskan request ke server lokal
4. Aplikasi di `192.10.10.152:3004` merespons halaman

## 2. Prasyarat

Pastikan hal berikut sudah tersedia:

- Server Ubuntu aktif di `192.10.10.152`
- Aplikasi sudah listen di port `3004`
- Domain `aksara.fun` sudah menggunakan nameserver Cloudflare
- Anda memiliki akses ke Cloudflare Zero Trust

## 3. Verifikasi Aplikasi Lokal

Sebelum menghubungkan domain, pastikan aplikasi lokal sudah hidup.

Jalankan di server:

```bash
curl -i http://127.0.0.1:3004/
```

Jika aplikasi sehat, respons harus berupa `200 OK` atau respons HTTP valid dari aplikasi.

Anda juga bisa cek port yang sedang listen:

```bash
ss -lnt | grep 3004
```

Jika muncul `0.0.0.0:3004` atau `[::]:3004`, berarti service siap menerima koneksi.

## 4. Install Cloudflared di Server

Gunakan repositori resmi Cloudflare untuk Debian/Ubuntu.

```bash
sudo mkdir -p --mode=0755 /usr/share/keyrings
curl -fsSL https://pkg.cloudflare.com/cloudflare-public-v2.gpg | sudo tee /usr/share/keyrings/cloudflare-public-v2.gpg >/dev/null

echo 'deb [signed-by=/usr/share/keyrings/cloudflare-public-v2.gpg] https://pkg.cloudflare.com/cloudflared any main' | sudo tee /etc/apt/sources.list.d/cloudflared.list

sudo apt-get update
sudo apt-get install cloudflared
```

Setelah selesai, cek versi:

```bash
cloudflared --version
```

## 5. Buat Tunnel di Cloudflare

Masuk ke Cloudflare Dashboard:

- Zero Trust
- Networks
- Tunnels
- Create a tunnel

Beri nama tunnel, misalnya:

- `aksara-tunnel`

Cloudflare akan memberi Anda tunnel ID dan token/connector setup.

## 6. Install Connector di Server

Karena Anda ingin koneksi berjalan terus di server, jalankan connector dengan token dari Cloudflare.

Di halaman tunnel, pilih opsi install connector, lalu jalankan di server:

```bash
sudo cloudflared service install <TOKEN_DARI_CLOUDFLARE>
```

Atau jika ingin menjalankan manual:

```bash
cloudflared tunnel run --token <TOKEN_DARI_CLOUDFLARE>
```

Jika Anda memilih service install, tunnel akan otomatis hidup saat server restart.

## 7. Konfigurasi Public Hostname

Setelah tunnel aktif, buat hostname publik untuk domain Anda.

Di Cloudflare Zero Trust:

1. Buka tunnel `aksara-tunnel`
2. Masuk ke tab `Public Hostnames`
3. Tambahkan hostname baru:

	- Hostname: `aksara.fun`
	- Service type: `HTTP`
	- Service URL: `http://192.10.10.152:3004`

Jika Anda juga ingin `www.aksara.fun`, tambahkan satu lagi:

	- Hostname: `www.aksara.fun`
	- Service type: `HTTP`
	- Service URL: `http://192.10.10.152:3004`

Penting:

- Gunakan hostname yang sama persis dengan domain yang ingin dibuka
- Jika hanya ingin domain utama, cukup `aksara.fun`
- Jangan mengarahkannya ke port lain jika aplikasi memang berjalan di `3004`

## 8. Pastikan DNS Cloudflare Benar

DNS untuk `aksara.fun` harus resolve ke Cloudflare, bukan ke IP server secara langsung.

Hal yang perlu dipastikan:

1. Nameserver domain sudah memakai nameserver Cloudflare
2. Record untuk `aksara.fun` ada di Cloudflare
3. Jika memakai tunnel public hostname, Cloudflare akan menangani routing ke connector

Jika `aksara.fun` belum resolve, biasanya penyebabnya:

- record root domain belum dibuat
- nameserver registrar belum diarahkan ke Cloudflare
- hanya `www.aksara.fun` yang aktif, tetapi root domain `aksara.fun` belum ada

## 9. Jalankan dan Cek Status Tunnel

Jika service install sudah dilakukan, cek status service:

```bash
sudo systemctl status cloudflared --no-pager
```

Jika tunnel berjalan normal, Cloudflare Dashboard akan menampilkan:

- Status: `Healthy`
- Connector: `Connected`

## 10. Uji Akses dari Internet

Setelah hostname dan tunnel aktif, uji dari browser atau terminal:

```bash
curl -I https://aksara.fun
```

Jika ingin cek halaman penuh:

```bash
curl -i https://aksara.fun/
```

Hasil yang benar berarti request publik sudah sampai ke aplikasi di port `3004`.

## 11. Alur Troubleshooting

Jika domain belum bisa dibuka, cek dari bawah ke atas:

### A. Aplikasi lokal hidup atau tidak

```bash
curl -i http://127.0.0.1:3004/
ss -lnt | grep 3004
```

### B. Connector cloudflared aktif atau tidak

```bash
sudo systemctl status cloudflared --no-pager
```

### C. Tunnel di Cloudflare sehat atau tidak

Lihat dashboard Zero Trust → Tunnels.

### D. Public hostname sudah ada atau belum

Pastikan `aksara.fun` diarahkan ke service `http://192.10.10.152:3004`.

### E. DNS root domain sudah resolve atau belum

Jika muncul `DNS_PROBE_FINISHED_NXDOMAIN`, berarti masalah ada di DNS, bukan di aplikasi.

## 12. Kesalahan Yang Paling Sering Terjadi

1. Tunnel aktif, tapi public hostname belum dibuat
2. Public hostname ada, tapi diarahkan ke port yang salah
3. Aplikasi hidup di `3004`, tetapi tunnel diarahkan ke `8080`
4. Domain baru hanya punya `www`, tetapi root domain `aksara.fun` belum ada
5. Nameserver domain belum benar ke Cloudflare

## 13. Ringkasan Langkah Cepat

Kalau ingin urutan paling singkat:

1. Pastikan app hidup di `http://127.0.0.1:3004`
2. Install `cloudflared` di server
3. Buat tunnel di Cloudflare Zero Trust
4. Install connector dengan token
5. Tambahkan public hostname `aksara.fun`
6. Arahkan ke `http://192.10.10.152:3004`
7. Cek status tunnel jadi `Healthy` dan `Connected`
8. Buka `https://aksara.fun`

## 14. Catatan Penting

- Gunakan `https://` untuk akses publik
- Jangan expose port `3004` ke internet jika sudah lewat Cloudflare Tunnel
- Jika ingin menambah subdomain lain, cukup tambah hostname baru ke tunnel yang sama selama service tujuannya jelas

## 15. Hasil Akhir yang Diharapkan

Jika semua langkah benar, maka:

- aplikasi tetap jalan di `192.10.10.152:3004`
- Cloudflare Tunnel aktif dan sehat
- `aksara.fun` terbuka via HTTPS
- tidak ada port aplikasi yang terbuka langsung ke publik
