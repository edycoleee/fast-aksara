
# Hosting aksara.fun via Cloudflare Tunnel (Aman untuk Layanan Existing)

Dokumen ini menjelaskan langkah detail untuk menambahkan aplikasi baru `fast-aksara` pada server yang sudah memiliki beberapa aplikasi Docker aktif.

Topologi target:

- Domain publik: `aksara.fun`
- Cloudflare Tunnel: route hostname ke origin lokal
- Origin server: `192.10.10.152`
- Aplikasi baru: `fast-aksara` pada `192.10.10.152:3004`

Tujuan utama: menambah aplikasi baru tanpa mengganggu aplikasi existing.

## 1. Prinsip Aman (Wajib Dipahami)

Penambahan aplikasi baru tidak akan mengganggu layanan existing jika:

1. Port aplikasi baru tidak bentrok.
2. Hostname baru (`aksara.fun`) dipetakan spesifik ke service baru.
3. Rule ingress Cloudflare Tunnel tidak menimpa rule lama.
4. Resource server masih cukup (CPU, RAM, disk).

Gangguan biasanya terjadi karena salah konfigurasi, bukan karena jumlah aplikasi.

## 2. Pre-Check Sebelum Konfigurasi

Jalankan pemeriksaan berikut di server `192.10.10.152`.

### 2.1 Cek container yang sedang aktif

```bash
docker ps --format "table {{.Names}}\t{{.Ports}}\t{{.Status}}"
```

Pastikan port `3004` belum dipakai aplikasi lain.

### 2.2 Cek port yang listen di host

```bash
ss -tulpen | grep 3004 || true
```

Jika tidak ada konflik, lanjut.

### 2.3 Cek resource server

```bash
free -h
df -h
docker stats --no-stream
```

Jika resource mepet, lakukan optimasi dulu agar aplikasi lama tidak terdampak.

## 3. Jalankan Aplikasi fast-aksara

Pastikan aplikasi merespons sehat secara lokal sebelum dipublikasikan.

### 3.1 Menjalankan container (contoh)

Sesuaikan dengan compose/project yang dipakai:

```bash
docker compose up -d
```

### 3.2 Verifikasi aplikasi lokal

```bash
curl -I http://192.10.10.152:3004
curl -I http://127.0.0.1:3004
```

Minimal harus mendapat respons HTTP (200/301/302/404 masih menandakan service hidup, tergantung route).

## 4. Konfigurasi Cloudflare Tunnel

Ada dua pola umum: via dashboard atau file config `cloudflared`.
Gunakan salah satu, jangan campur tanpa kontrol versi.

### 4.1 Jika menggunakan config file cloudflared

Contoh `config.yml`:

```yaml
tunnel: <TUNNEL_ID>
credentials-file: /etc/cloudflared/<TUNNEL_ID>.json

ingress:
	- hostname: aksara.fun
		service: http://192.10.10.152:3004
	- service: http_status:404
```

Catatan penting:

1. Rule `aksara.fun` harus spesifik.
2. Rule catch-all `http_status:404` diletakkan paling bawah.
3. Jangan hapus rule hostname aplikasi lain.

### 4.2 Jika tunnel melayani banyak domain

Tambahkan hanya satu blok hostname baru untuk `aksara.fun`, biarkan mapping domain existing tetap sama.

### 4.3 Restart service cloudflared

```bash
sudo systemctl restart cloudflared
sudo systemctl status cloudflared --no-pager
```

Jika tidak pakai systemd, restart sesuai metode deploy cloudflared Anda.

## 5. Konfigurasi DNS di Cloudflare

Pada zone `aksara.fun`:

1. Buat record `CNAME` untuk host `@` atau `www` (sesuai kebutuhan).
2. Arahkan ke target tunnel (`<tunnel-id>.cfargotunnel.com`) jika metode Anda membutuhkan DNS record manual.
3. Pastikan proxy Cloudflare aktif (orange cloud), jika memang itu pola yang dipakai.

Jika hostname dikelola langsung dari menu Tunnel Public Hostname, ikuti pola existing Anda dan konsisten.

## 6. Uji Akses End-to-End

Setelah tunnel dan DNS siap:

```bash
curl -I https://aksara.fun
```

Lanjutkan uji dari browser:

1. Akses `https://aksara.fun`.
2. Pastikan halaman terbuka normal.
3. Cek log aplikasi saat ada request.

```bash
docker logs -f <nama_container_fast_aksara>
```

## 7. Validasi Aplikasi Existing (Anti-Regresi)

Wajib cek beberapa domain lama setelah deploy:

```bash
curl -I https://<domain-existing-1>
curl -I https://<domain-existing-2>
curl -I https://<domain-existing-3>
```

Jika semua tetap normal, berarti penambahan aplikasi baru aman.

## 8. Strategi Rollback Cepat

Jika terjadi gangguan:

1. Kembalikan config tunnel ke versi sebelumnya.
2. Restart `cloudflared`.
3. Hentikan sementara container `fast-aksara` jika perlu.

Contoh:

```bash
docker compose down
sudo systemctl restart cloudflared
```

Saran: simpan backup file config sebelum perubahan.

## 9. Checklist Singkat Deploy Aman

- [ ] Port `3004` tidak bentrok
- [ ] Container `fast-aksara` healthy
- [ ] Ingress `aksara.fun` mengarah ke `192.10.10.152:3004`
- [ ] Rule existing tidak berubah
- [ ] DNS Cloudflare benar
- [ ] Uji domain baru sukses
- [ ] Uji domain existing tetap sukses

## 10. Kesimpulan

Menambah `fast-aksara` dengan domain `aksara.fun` melalui Cloudflare Tunnel sangat memungkinkan dan umumnya aman. Risiko gangguan ke layanan existing rendah selama rule hostname, port, dan urutan ingress dikonfigurasi dengan benar dan divalidasi setelah deploy.

