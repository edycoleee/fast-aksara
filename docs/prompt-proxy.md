# Panduan Konfigurasi Reverse Proxy — aksara.fun
> Dijalankan di server **192.10.10.15** (SSL termination, Nginx sudah existing).
> App live aksara saat ini ada di **192.10.10.154:3004**.
> Domain utama yang akan dipakai untuk produksi adalah **aksara.fun**. Untuk setup yang sederhana dan aman, gunakan satu domain utama saja.
>
> Catatan penting: jika aplikasi memiliki validasi host / allowed hosts / redirect domain, maka host utama harus ditambahkan di app agar domain produksi `aksara.fun` diterima dengan benar.

---

## Daftar Isi

1. [Prasyarat](#prasyarat)
2. [Buat File Konfigurasi Nginx](#buat-file-konfigurasi-nginx)
3. [Aktifkan Site](#aktifkan-site)
4. [Dapatkan Sertifikat SSL (Let's Encrypt)](#dapatkan-sertifikat-ssl-lets-encrypt)
5. [Konfigurasi Final Setelah Certbot](#konfigurasi-final-setelah-certbot)
6. [Verifikasi](#verifikasi)
7. [Checklist Hardening Reverse Proxy](#checklist-hardening-reverse-proxy)

---

## Prasyarat

Pastikan kondisi ini terpenuhi sebelum mulai:

```bash
# Di server 192.10.10.15 ─────────────────────────────────────

# 1. Nginx sudah running (existing, melayani domain lain)
nginx -v
systemctl status nginx

# 2. Certbot sudah terinstall
certbot --version

# 3. Port 80 dan 443 terbuka di firewall (sudah ada dari domain lain)
sudo ufw status  # port 80 dan 443 harus ALLOW

# 4. DNS domain utama sudah mengarah ke IP publik 192.10.10.15
# Domain yang dipakai: aksara.fun
dig +short aksara.fun
# Harus mengembalikan IP publik server ini

# 5. App backend sudah berjalan di app server
curl -I http://192.10.10.154:3004
# Harus mengembalikan HTTP 200 atau 30x

# 6. Pastikan tidak ada konflik site name
ls /etc/nginx/sites-enabled/
# Tidak boleh ada file bernama aksara.fun

# 7. Jika app sudah punya validasi host, tambahkan host utama di allowed_hosts / CORS / redirect config
# misalnya: aksara.fun, www.aksara.fun
```

---

## Buat File Konfigurasi Nginx

```bash
sudo nano /etc/nginx/sites-available/aksara.fun
```

Isi dengan konfigurasi berikut (blok HTTP dulu — certbot akan menambah blok HTTPS):

```nginx
# ============================================================
# aksara.fun — Reverse Proxy
# Server: 192.10.10.15 (SSL termination, existing nginx)
# Upstream: 192.10.10.154:3004 (app live aksara)
# ============================================================

# ── HTTP: redirect ke HTTPS ───────────────────────────────────
server {
    listen 80;
    listen [::]:80;
    server_name aksara.fun www.aksara.fun;

    # Certbot akan mengisi bagian ini secara otomatis.
    # Jangan tambahkan isi lain di sini sebelum certbot dijalankan.
}
```

> Karena domain utama yang dipakai adalah `aksara.fun`, kita cukup fokus pada satu host utama dan satu upstream backend.

Simpan, lalu lanjut ke langkah aktifkan site.

---

## Aktifkan Site

```bash
# Buat symlink ke sites-enabled
sudo ln -s /etc/nginx/sites-available/aksara.fun \
           /etc/nginx/sites-enabled/aksara.fun

# Uji konfigurasi — pastikan tidak konflik dengan site existing
sudo nginx -t

# Reload Nginx (tidak restart, domain lain tidak terganggu)
sudo systemctl reload nginx
```

---

## Dapatkan Sertifikat SSL (Let's Encrypt)

```bash
# Certbot akan otomatis memodifikasi file konfigurasi aksara.fun
# dan menambahkan blok HTTPS + redirect.
sudo certbot --nginx -d aksara.fun -d www.aksara.fun

# Ikuti prompt certbot:
# - Email sudah terdaftar dari domain lain → pilih opsi reuse
# - Setujui ToS
# - Pilih opsi redirect (pilih 2: Redirect — recommended)
```

Setelah certbot selesai, verifikasi auto-renew (juga mencakup domain lain yang sudah ada):

```bash
sudo certbot renew --dry-run
# Harus sukses tanpa error untuk semua domain
```

---

## Konfigurasi Final Setelah Certbot

Setelah certbot berjalan, buka kembali file konfigurasi dan **ganti seluruh isinya** dengan
konfigurasi lengkap berikut (certbot terkadang menghasilkan konfigurasi minimal):

```bash
sudo nano /etc/nginx/sites-available/aksara.fun
```

```nginx
# ============================================================
# aksara.fun — Reverse Proxy (192.10.10.15)
# ============================================================
# Upstream : 192.10.10.154:3004  (app live aksara)
# SSL      : Let's Encrypt via Certbot
# ============================================================

# ── HTTP → HTTPS redirect ─────────────────────────────────────
server {
    listen 80;
    listen [::]:80;
    server_name aksara.fun www.aksara.fun;

    # Certbot well-known challenge (jangan hapus)
    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}

# ── HTTPS (SSL termination) ───────────────────────────────────
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name aksara.fun www.aksara.fun;

    # ── SSL Certificate (Let's Encrypt) ──────────────────────
    ssl_certificate     /etc/letsencrypt/live/aksara.fun/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/aksara.fun/privkey.pem;

    # ── SSL Hardening ─────────────────────────────────────────
    ssl_protocols             TLSv1.2 TLSv1.3;
    ssl_ciphers               ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256;
    ssl_prefer_server_ciphers off;
    ssl_session_cache         shared:SSL_aksara:10m;
    ssl_session_timeout       1d;
    ssl_session_tickets       off;

    # HSTS — aktifkan hanya setelah yakin HTTPS berjalan sempurna
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;

    # ── Logging ───────────────────────────────────────────────
    access_log /var/log/nginx/aksara_access.log;
    error_log  /var/log/nginx/aksara_error.log warn;

    # ── Proxy ke App Stack (backend live aksara) ───────────────
    location / {
        proxy_pass         http://192.10.10.154:3004;
        proxy_http_version 1.1;

        # Forward IP asli klien ke aksara-app di app server
        proxy_set_header   Host              $host;
        proxy_set_header   X-Real-IP         $remote_addr;
        proxy_set_header   X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto $scheme;
        proxy_set_header   Connection        "";

        # Timeout upstream
        proxy_connect_timeout 10s;
        proxy_read_timeout    120s;
        proxy_send_timeout    120s;

        # Buffer — nonaktifkan agar streaming/SSE tidak tertunda
        proxy_buffering    off;
        proxy_buffer_size  4k;
    }
}
```

Terapkan:

```bash
sudo nginx -t && sudo systemctl reload nginx
```

---

## Verifikasi

```bash
# ── Di server 192.10.10.15 ─────────────────────────────────────

# 1. Cek konfigurasi Nginx (semua site, termasuk yang existing)
sudo nginx -t
# Ekspektasi: syntax is ok / test is successful

# 2. Pastikan site aksara aktif
ls -la /etc/nginx/sites-enabled/
# Harus ada: aksara.fun

# 3. Uji redirect HTTP → HTTPS
curl -I http://aksara.fun
# Ekspektasi: HTTP/1.1 301 Moved Permanently
#             Location: https://aksara.fun/

# 4. Uji HTTPS landing page
curl -I https://aksara.fun
# Ekspektasi: HTTP 200 atau 30x

# 5. Cek header keamanan dari response
curl -I https://aksara.fun
# Ekspektasi: response HTTPS valid (status bukan 5xx)

# 6. Cek sertifikat SSL
echo | openssl s_client -connect aksara.fun:443 -servername aksara.fun 2>/dev/null \
  | openssl x509 -noout -dates -subject
# Tampilkan: notAfter (tanggal kedaluwarsa) dan CN=aksara.fun

# 7. Uji halaman login admin melewati full stack
curl -I https://aksara.fun/admin/login
# Ekspektasi: HTTP 200

# 8. Cek log akses real-time saat ada request
sudo tail -f /var/log/nginx/aksara_access.log
# Buka https://aksara.fun di browser, pastikan log muncul

# 9. Pastikan log error bersih
sudo tail -20 /var/log/nginx/aksara_error.log

# 10. Pastikan domain lain (kos, absen) masih berjalan normal
curl -s https://kos.sulfat.site/health
curl -s https://absen.sulfat.site/health 2>/dev/null || true
```

---

## Checklist Hardening Reverse Proxy

### Firewall pada 192.10.10.15

```bash
# Port 80 dan 443 sudah ALLOW dari setup domain lain — verifikasi saja
sudo ufw status | grep -E '80|443'
# Harus sudah ALLOW. Jika belum:
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw reload
```

### Firewall pada 192.10.10.154 (App Server)

```bash
# Port 3004 (aksara stack): hanya izinkan dari reverse proxy 192.10.10.15
sudo ufw allow from 192.10.10.15 to any port 3004 proto tcp

# Pastikan port 3004 tidak bisa diakses publik langsung
sudo ufw deny 3004

sudo ufw reload
sudo ufw status numbered | grep 3004
```

### Auto-Renew Certbot

```bash
# Cek timer systemd certbot (biasanya sudah aktif otomatis)
systemctl status certbot.timer

# Jika belum aktif:
sudo systemctl enable certbot.timer
sudo systemctl start certbot.timer

# Uji dry-run
sudo certbot renew --dry-run
```

### Log Rotation (sudah default di Nginx, verifikasi)

```bash
cat /etc/logrotate.d/nginx
# Pastikan /var/log/nginx/*.log sudah masuk konfigurasi rotate
```

### Checklist Final

- [x] DNS `aksara.fun` → IP publik 192.10.10.15
- [x] HTTP 80 redirect ke HTTPS 443
- [x] SSL TLSv1.2 + TLSv1.3 only, cipher modern
- [x] `X-Real-IP` diteruskan ke app server (IP asli klien)
- [x] `X-Forwarded-Proto: https` diteruskan (FastAPI bisa deteksi HTTPS)
- [x] Log terpisah: `/var/log/nginx/aksara_access.log`
- [x] Port 3004 di app server hanya bisa diakses dari 192.10.10.15
- [x] Auto-renew certbot aktif (`certbot.timer`) — sudah ada dari domain lain
- [x] Domain lain (kos, absen) tidak terganggu setelah penambahan site baru
- [x] Host utama yang dipakai adalah `aksara.fun`
- [x] Jika app punya validasi host, host utama juga harus ditambahkan di allowed hosts / CORS / redirect config
- [ ] HSTS aktif (`Strict-Transport-Security`) — aktifkan setelah konfirmasi HTTPS stabil
- [ ] Rate limit di reverse proxy (opsional)
- [ ] Monitoring SSL expiry (mis. UptimeRobot SSL monitor → aksara.fun)

---

## Referensi Cepat — Perintah Berguna

```bash
# Reload konfigurasi tanpa downtime (domain lain tetap berjalan)
sudo systemctl reload nginx

# Test konfigurasi sebelum reload
sudo nginx -t

# Lihat semua site yang aktif
ls -la /etc/nginx/sites-enabled/

# Cek status Nginx
sudo systemctl status nginx

# Cek log error langsung
sudo journalctl -u nginx -f

# Cek log aksara secara spesifik
sudo tail -f /var/log/nginx/aksara_access.log
sudo tail -f /var/log/nginx/aksara_error.log

# Perpanjang sertifikat manual (jika timer tidak jalan)
sudo certbot renew

# Cek tanggal kedaluwarsa semua sertifikat (termasuk aksara)
sudo certbot certificates

# Hapus site aksara jika perlu rollback (tidak ganggu domain lain)
# sudo rm /etc/nginx/sites-enabled/aksara.fun
# sudo systemctl reload nginx
```

# Next Steps

1. Eksekusi setup reverse proxy di server 192.10.10.15

```bash
sudo nginx -t
sudo systemctl reload nginx
sudo certbot --nginx -d aksara.fun -d www.aksara.fun
sudo certbot renew --dry-run
```

2. Verifikasi jalur domain ke backend

```bash
curl -I http://aksara.fun
curl -I https://aksara.fun
curl -I https://aksara.fun/admin/login
curl -I http://192.10.10.154:3004
```

3. Jika ada error 502/504 dari domain

```bash
# Di reverse proxy server
sudo tail -50 /var/log/nginx/aksara_error.log

# Di app server
docker ps --format 'table {{.Names}}\t{{.Status}}' | grep aksara-app
docker logs --tail 120 aksara-app
```

4. Jika SSL gagal issue/renew

```bash
dig +short aksara.fun
dig +short www.aksara.fun
sudo certbot certificates
sudo certbot renew --dry-run
```

5. Hardening app yang direkomendasikan (setelah routing stabil)

- Aktifkan trusted host: aksara.fun dan www.aksara.fun.
- Jalankan uvicorn dengan proxy header trust: --proxy-headers dan --forwarded-allow-ips.
- Set cookie admin sebagai secure saat HTTPS.

6. Validasi akhir setelah semua perubahan

```bash
curl -I https://aksara.fun
curl -I https://aksara.fun/admin/login
sudo tail -20 /var/log/nginx/aksara_error.log
docker logs --tail 100 aksara-app
```

7. Jika rollback dibutuhkan

```bash
sudo rm /etc/nginx/sites-enabled/aksara.fun
sudo nginx -t
sudo systemctl reload nginx
```
