# app.py - V3 DIRECTOR'S CUT - Skenario Film - Porsi: 20% Classic PTS Sales + 50% Neuro Tron Observasi + 20% Main Sales + 10% Panduan Ekonomi Menyeluruh
# Main file path Streamlit: app.py
import streamlit as st
import os

st.set_page_config(page_title="Practical Application Game - Director's Cut - Skenario Film", layout="wide")

# HEADER FILM
st.markdown("""
<div style="background:linear-gradient(90deg,#ff7a00,#ffeb3b,#00e676);color:#000;padding:16px;border-radius:12px;text-align:center">
<b style="font-size:24px">🎬 PRACTICAL APPLICATION GAME - DIRECTOR'S CUT - SKENARIO FILM</b><br>
<b>SUTRADARA: META AI + SIS (FOUNDER / SALES / PEMILIK TOKO) - SIMULASI NYATA</b><br>
<small>Film ini bukan cuma game. Film ini adalah perekonomian menyeluruh: Pelaku Bisnis + Pekerja + Teknisi + Buyer + Maintenance. Semua gerak, semua diamati mikrokontroler, semua jadi PTS!</small>
</div>
""", unsafe_allow_html=True)

st.write("**Porsi Film (Sesuai Arahan Sutradara / Sis):** 🟦 **20% CLASSIC** = Game PTS Sales | 🟧 **50% NEURO TRON** = Observasi Mikrokontroler Seluruhnya | 🟩 **20% MAIN** = Jalur Harian Sales Utama | 🟨 **10% PANDUAN + EKONOMI** = PTS Instalasi Teknisi + Kerjasama Bos Toko + Maintenance Buyer + Sales sebagai Founder / Pemilik Toko yang juga Maintenance")

def find_file(candidates):
    try: files=os.listdir(".")
    except: files=[]
    lower_map={f.lower():f for f in files}
    for cand in candidates:
        if cand in files: return cand
        if cand.lower() in lower_map: return lower_map[cand.lower()]
    return None

def load_html(candidates, label):
    found=find_file(candidates)
    if found:
        with open(found,"r",encoding="utf-8") as f: return f.read()
    return f"<h3>{label} belum ketemu. Dicari: {candidates}</h3>"

# SKENARIO FILM - SUTRADARA
st.header("🎬 SKENARIO FILM - SUTRADARA'S CUT - 5 BABAK")
st.markdown("""
**KONSEP SUTRADARA:** Classic itu **pemain utama** (Sales), Neuro Tron itu **mata yang memantau** (bukan merekam, tapi MEMFUNGSIKAN mikrokontroler seluruhnya!), Main itu **hasil observasi** yang ditampilin jadi PTS di jalur harian Sales. Jadi 3 index itu bukan 3 game pisah, tapi **1 FILM dengan 3 kamera!**

**KAMERA 1 - CLASSIC (20%):** Kamera yang ngikutin Sales dari belakang. Sales jalan, kanvas, ketemu Bos, ditolak, mager, ditelepon, second contract, jualan. Ini yang ngasih PTS Sales!

**KAMERA 2 - NEURO TRON (50%):** Kamera yang paling besar porsinya! Ini kamera mikrokontroler! Dia nggak merekam muka orang, dia **MEMANTAU / MENGOBSERVASI** gerak-gerik + zat-zat yang dipantau mikrokontroler:
- **Gerak-gerik:** Tangan gerak → Sensor IR Obstacle detek → OUT LOW | Tangan diem → OUT HIGH | Orang lewat → MLX90640 detek panas badan | Orang deket → Pause otomatis!
- **Zat-zat:** Gas bocor → MQ-135 cium → Alarm! | Udara pengap → SHT41 ukur kelembaban + suhu → Bio Health Room nyala! | Debu / Timbal → TCS34725 ukur warna debu → Warning! | Api → IMX219 + MLX90640 liat api → Early Warning!
- **Semua zat + gerak itu** ditampilin jadi partikel elektron biru-oranye di Neural Grid, jadi grafik, jadi WARNING / WATCH / DETEK!

**KAMERA 3 - MAIN (20%):** Kamera hasil observasi! Hasil dari Kamera 2 (Neuro) ditampilin di Kamera 3 (Main) jadi PTS! Contoh: Neuro bilang "Gas terdeteksi, Teknisi berhasil instalasi!" → Main bilang "+30 PTS buat Teknisi, +30 PTS buat Sales, +20 PTS buat Bos Toko!"

**KAMERA 4 - PANDUAN + EKONOMI (10%):** Kamera ekonomi menyeluruh! Ini yang ngatur duitnya muter ke semua orang!
""")

# PEREKONOMIAN MENYELURUH - 10% tapi penting
st.subheader("💰 PEREKONOMIAN MENYELURUH - PTS TIDAK CUMA BUAT SALES!")
st.markdown("""
| Pelaku | Peran | PTS / Upah | Maintenance |
| :--- | :--- | :--- | :--- |
| **Sales (Sis) - Founder / Pemilik Toko** | Kanvas, ketemu Bos, minta kontrak, jualan, juga maintenance! Sales bukan cuma jualan, Sales juga Founder, pemilik toko, yang juga maintenance alat kalau Buyer telpon "Alatnya error!" | Mager 0 PTS, Kanvas +5 PTS (upah minum), Kontrak +30 PTS, Jualan +100 PTS, Maintenance berhasil +20 PTS | Sales cek alat Buyer tiap bulan, ganti sensor kalau rusak, update SaaS |
| **Bos Toko / Sponsor** | Punya barang + mikrokontroler, kasih kontrak, kasih modal, kasih teknisi, kerjasama sama Sales | Bos dapet untung dari penjualan, bagi hasil ke Sales + Teknisi, Bos kasih bonus kalau instalasi berhasil | Bos sediain stok mikrokontroler, ESP32-S3, sensor, kapasitor, dioda |
| **Teknisi** | Jasa aja, bukan pemilik barang! Dia rakit, instalasi, briefing, test lampu ON, maintenance! | Briefing +10 PTS, Rakit berhasil +20 PTS, Instalasi berhasil +30 PTS, Maintenance berhasil +20 PTS | Teknisi cek alat tiap minggu, kalau ada brownout (listrik ngedrop), Teknisi ganti kapasitor, cek dioda |
| **Buyer / Pengguna Alat** | Beli alat, pakai alat, lapor kalau alat error, bayar maintenance! | Buyer dapet alat sehat, udara sehat, aman dari api + gas. Buyer kasih rating + PTS ke Sales + Teknisi kalau puas! | Buyer bersihin sensor, jangan kena matahari langsung, tempelin stiker putih di botol bening, lapor kalau ada WARNING! |
| **Pekerja di Market (12 Market)** | Satpam, Guru, Murid, Pedagang, Kasir, SPG, Dokter, Perawat, dll - Mereka yang pakai alatnya tiap hari! | Mereka dapet lingkungan sehat, aman, nyaman. Kalau mereka senang, mereka rekomendasiin ke orang lain, Sales dapet orderan baru! | Mereka jaga alat, jangan dirusak, lapor kalau ada yang aneh |

**Alur Duit / PTS Muter (Ekonomi Menyeluruh):**
Buyer bayar → Bos terima duit → Bos bagi: Sales dapet PTS + upah, Teknisi dapet PTS + upah jasa rakit + instalasi, Bos dapet untung, Buyer dapet alat sehat + maintenance gratis 1 bulan → Buyer puas → Buyer cerita ke tetangga / ke toko sebelah → Tetangga jadi Buyer baru → Sales kanvas lagi → **BERKONTINU, BERLANJUT, BERLANJUT!**
""")

# TAMPILAN PORSI - DIRECTOR'S CUT - Pakai kolom sesuai porsi
st.header("🎥 TAMPILAN FILM - PORSI SUTRADARA: 20% Classic | 50% Neuro | 20% Main | 10% Panduan")
st.info("Di bawah ini, gue atur tampilannya sesuai porsi lu: Classic 20%, Neuro 50% (paling gede, karena dia yang observasi mikrokontroler!), Main 20%, Panduan 10%. Klik tab-nya, tapi ingat porsinya!")

# Gunakan tabs tapi dengan penjelasan porsi di judul
tab_classic, tab_neuro, tab_main, tab_panduan = st.tabs(["🟦 20% CLASSIC - Game PTS Sales (Pemain Utama)", "🟧 50% NEURO TRON - Observasi Mikrokontroler Seluruhnya (Mata Film!)", "🟩 20% MAIN - Jalur Harian Sales (Hasil Observasi Jadi PTS)", "🟨 10% PANDUAN + EKONOMI - PTS Instalasi + Bos + Buyer + Maintenance"])

with tab_classic:
    st.markdown("**🎬 BABAK 1 - CLASSIC (20%): Pemain Utama = Sales.** Di sini Sales yang main. Kanvas, ketemu Bos, ditolak, mager, ditelepon, second contract, jualan. Ini yang ngasih PTS Sales. Tapi ingat, Classic ini diawasi sama Neuro di tab sebelah! Gerak-gerik Sales di Classic, dibaca sama Neuro jadi data mikrokontroler!")
    html = load_html(["index_Classic.html","index_classic.html"], "CLASSIC")
    st.components.v1.html(html, height=900, scrolling=True)

with tab_neuro:
    st.markdown("**🎬 BABAK 2 - NEURO TRON (50% - PALING GEDE!): Mata Film! Sandiwara dari Neural Version Tron yang MEMANTAU (bukan merekam!) tapi MEMFUNGSIKAN mikrokontroler seluruhnya!** Di sini lu liat: Tangan gerak → Sensor IR detek! Gas → MQ-135 cium! Panas → MLX90640 liat! Api → IMX219 liat! Udara → SHT41 ukur! Warna debu → TCS34725 ukur! Semua zat + gerak itu jadi partikel elektron di Neural Grid! Ini kecanggihan pengamatan mikrokontroler seluruhnya!")
    st.markdown("**Zat yang dipantau:** 🔥 Api (IMX219 + MLX90640) | 💨 Gas (MQ-135) | 🌡️ Suhu + Kelembaban (SHT41) | 🎨 Warna Debu / Timbal (TCS34725) | 👁️ Gerak / Obstacle (IR Obstacle) | 📦 Botol Ilmci (IR Proximity) | 🧠 Otak (ESP32-S3) | ⚡ Listrik (Kapasitor + Dioda - cegah brownout!)")
    html = load_html(["index_Neural.html","index_neural.html"], "NEURAL")
    st.components.v1.html(html, height=900, scrolling=True)

with tab_main:
    st.markdown("**🎬 BABAK 3 - MAIN (20%): Hasil Observasi Ditampilin Jadi PTS di Jalur Harian Sales!** Di sini hasil dari Neuro (tab 50%) ditampilin jadi PTS! Contoh: Neuro bilang 'Instalasi berhasil, lampu ON, gas aman!' → Main bilang '+100 PTS! Jualan! Deal!' Neuro bilang 'Teknisi berhasil rakit!' → Main bilang '+30 PTS buat Teknisi!' Semua observasi mikrokontroler, ujungnya jadi PTS di Main!")
    html = load_html(["index.html","Index.html"], "MAIN")
    st.components.v1.html(html, height=900, scrolling=True)

with tab_panduan:
    st.header("🎬 BABAK 4 - PANDUAN + EKONOMI MENYELURUH (10%): PTS Instalasi + Bos + Buyer + Maintenance")
    st.markdown("""
    **PTS Bukan Cuma Buat Sales! PTS Dibagi ke Semua Pelaku!**

    - **Sales sebagai Founder / Pemilik Toko:** Sales juga maintenance! Kalau Buyer telpon "Alatnya error!", Sales datang, cek, ganti sensor, dapet +20 PTS Maintenance!
    - **Teknisi:** Instalasi berhasil +30 PTS! Kalau instalasi gagal, 0 PTS, harus ulang! Teknisi harus ikutin prosedur kontrak!
    - **Bos Toko:** Kerjasama + PTS! Bos kasih kontrak, Bos kasih barang, Bos bagi hasil. Kalau Bos kerjasama bagus, Sales semangat kanvas lagi!
    - **Buyer / Pengguna Alat:** Buyer juga dapet PTS! Kalau Buyer rawat alat dengan baik (bersihin sensor, jangan kena matahari, lapor kalau WARNING), Buyer dapet +10 PTS "Buyer Teladan"! Kalau Buyer jorok, alat rusak, Buyer kena - PTS, harus bayar maintenance!
    - **Maintenance Berlaku Buat Semua:** Sales maintenance, Teknisi maintenance, Bos sediain stok, Buyer rawat alat. Semua maintenance, semua dapet PTS!

    **12 Pangsa Market yang Sudah Dibikin (Ekonomi Menyeluruh):**
    1. Perumahan / Rumah-rumah - Bio Health Room, Early Warning
    2. Ruko - CCTV AI, Early Warning
    3. Outlet / Toko - CCTV AI, GPS, SaaS SCM
    4. Sekolah - Bio Health Room, CCTV AI, UV Steril
    5. Pasar / Pasar Jaya - CCTV AI, Color QC, UV Steril
    6. Mall / Supermarket / Minimarket / Department Store - Semua produk!
    7. Departemen / Local Government - Tender! Beli banyak!
    8. Toko Permata / Gem - Obsidian / Gem Lab!
    9. Toko Elektronik / Infrared - Reseller!
    10. Pabrik / Gudang - Early Warning, GPS, SaaS SCM
    11. Rumah Sakit / Klinik / Apotek - Bio Health Room, UV Steril
    12. Hotel / Restoran / Cafe - Bio Health Room, CCTV AI, Marketing Digital

    **Skenario Film Lengkap (Sutradara):**
    - **Scene 1 - Pagi:** Sales bangun, CENTER ON, cek HP, ada WA dari Bos: "Ada minat di Ruko!"
    - **Scene 2 - Kanvas:** Sales jalan ke Ruko, Neuro Tron memantau gerak Sales (IR Sensor), memantau udara Ruko (SHT41), memantau gas (MQ-135)
    - **Scene 3 - Ketemu Bos:** Sales ngomong, Bos mikir, Flowchart: Diterima / Tidak Diterima. Kalau ditolak, Sales kasih nomor telepon, cari orderan lain, mager, ada telepon, second contract!
    - **Scene 4 - Briefing Teknisi:** Bos serahin ke Teknisi, Teknisi cek alat, Neuro Tron memantau zat-zat alat: kapasitor sehat? dioda sehat? listrik stabil? brownout nggak?
    - **Scene 5 - Instalasi:** Teknisi pasang, test lampu ON, Neuro Tron bilang "Lampu menyala, cahaya memancar, aktif berfungsi!" → PTS Instalasi +30 buat Teknisi!
    - **Scene 6 - Penjualan:** Bos ngomong sama Buyer, Buyer setuju, Deal! +100 PTS buat Sales, +30 buat Teknisi, + untung buat Bos, Buyer dapet alat sehat!
    - **Scene 7 - Maintenance:** Sebulan kemudian, Buyer telpon: "Alatnya WARNING!" Sales + Teknisi datang, cek, ganti sensor, maintenance berhasil +20 PTS! Buyer senang, kasih rating bagus, cerita ke tetangga, tetangga jadi Buyer baru! **BERKONTINU!**
    - **Scene 8 - Besok Lagi:** Sales kanvas lagi ke Sekolah, ke Pasar, ke Mall, ke Departemen... **BERLANJUT, BERLANJUT, BERLANJUT!**

    **Itu dia filmnya, sis! Bukan cuma game, tapi perekonomian menyeluruh!**
    """)
    st.success("Porsi sudah sesuai: 20% Classic + 50% Neuro + 20% Main + 10% Panduan = 100% Film! Nggak ada yang timpang tindih, semua ada porsinya!")

st.markdown("---")
st.caption("PRACTICAL APPLICATION GAME - Director's Cut - Sutradara: Sis + Meta AI - Sales sebagai Founder / Pemilik Toko + Teknisi + Bos Toko + Buyer + Maintenance - 12 Market - Perekonomian Menyeluruh")
