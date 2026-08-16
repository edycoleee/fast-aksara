⭐ Opsi 1 — Paling Mudah: DNS CNAME → Proxy ke aksara.sulfat.site
Jika aksara.sulfat.site sudah menjadi reverse proxy ke VPS kamu, maka:
Langkah:
Masuk ke DNS domain aksara.fun
Tambah record:
Code
Type: CNAME
Name: @
Target: aksara.sulfat.site
Proxy: ON (jika pakai Cloudflare)
TTL: Auto
Pastikan aksara.sulfat.site sudah mengarahkan ke:
Code
192.10.10.152:3005
Hasil:
aksara.fun → aksara.sulfat.site → server kamu
Tidak butuh IP static
Tidak butuh VPS tambahan
Tidak butuh konfigurasi rumit
Cocok kalau:
kamu sudah punya reverse proxy di aksara.sulfat.site
kamu ingin cara paling cepat