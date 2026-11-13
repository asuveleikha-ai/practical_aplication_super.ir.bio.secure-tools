# Panduan Installasi - Practical Application Game
# File ini BISA DI-UPDATE tanpa ganggu index.html

## 1. Infrared Anti Kebakaran - SG-810
- ESP32-S3 sebagai OTAK, terima WiFi terkoneksi via internet ke HP dan Laptop.
- Gunakan KAPASITOR untuk mencadangkan daya agar TCS34725 dan IMX219 berfungsi dengan baik.
- TCS34725 + IMX219 mendeteksi kebakaran, gas berbahaya mudah terbakar.
- SHT41 + MQ-135 mendeteksi ruang sehat tanpa timbal dan debu.
- Tes: Tekan tombol ON, lampu senter menyala, cahaya memancar = installasi benar, aktif berfungsi.

## 2. Bio Health Room
- Pasang SHT41 + MQ-135 di tengah ruangan, ESP32-S3 di atas.
- Kipas nyala kalau lembab >65%, alarm kalau gas naik.
- Tes: Udara bersih, kipas muter.

## 3. Obsidian Gem Lab
- Pasang IMX219 menghadap batu, ESP32-S3 foto + bandingkan warna.
- Tes: Flash, stempel ASLI / PALSU muncul.

## 4. Cara Update Kontrak / Peralatan / Panduan
- Edit file kontrak.json / peralatan.json / panduan-installasi.md ini saja.
- Upload ulang ke GitHub repo practicalapplication-gameinfraredtolls.
- JANGAN edit index.html kalau game sudah jalan sempurna.
- Game baca file baru otomatis.
