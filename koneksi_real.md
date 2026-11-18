# KONEKSI REAL - GAME SIMULASI REAL <-> APA?

## JAWABAN SINGKAT
- **Streamlit Demo sekarang = SIMULASI / VIDEO DEMO, BUKAN ALAT BENERAN!**
- **GitHub = LEMARI KODE SAJA!** Cuma nyimpen file, TIDAK bisa baca sensor!
- **Yang LEBIH NYATA: GAME <-> API / DATABASE <-> ESP32-S3 BENERAN!**

## DIAGRAM YANG BENAR
```
[ESP32-S3 + SHT41 + MQ-135 + MLX90640 di Rumah Buyer]
   | WiFi
   v
[API / Firebase / Supabase / MQTT - Database di Internet]
   | Internet
   v
[STREAMLIT / GAME baca API] -> Tampil HIJAU / KUNING / MERAH BENERAN!
```

## DIAGRAM YANG SALAH (YANG SEKARANG)
```
[GAME di Streamlit] <-> [GitHub] = SALAH! GitHub cuma lemari kode, nggak bisa baca sensor!
[GAME di Streamlit] = SIMULASI SAJA, tombolnya jalanin simulasi di browser, bukan baca ESP32!
```

## KENAPA KITA MASIH SIMULASI DULU?
1. Flowchart + PTS + Mapping harus bener dulu!
2. Kalau flowchart belum bener, alat beneran jadi bingung!
3. Kita masih mereka-reka (simulasi) biar Sales + Teknisi + Bos + Buyer ngerti alurnya dulu!
4. Kalau udah bener, baru pasang API + ESP32 beneran!

## LANGKAH KE REAL (NANTI, BUKAN SEKARANG)
1. ESP32-S3 kirim data tiap 1 menit ke API (misal Firebase)
2. API simpan: suhu, gas, api, heartbeat, tegangan kapasitor
3. Streamlit baca API, tampilkan status HIJAU / KUNING / MERAH BENERAN
4. Kalau MERAH, Streamlit kirim notif ke Teknisi: "Pasar Jaya E kapasitor habis, datang hari ini!"
5. Teknisi datang, ganti kapasitor, ESP32 kirim lagi, status jadi HIJAU lagi!

## BATIK 8in1 TETAP PISAH!
- Batik Guard 8in1 DIHAPUS dari game simulasi real!
- Batik hidup di app-nya sendiri, dengan API-nya sendiri, database-nya sendiri!
- Game simulasi real hanya untuk Super Secure + Super Infrared, 4 item ringan!
