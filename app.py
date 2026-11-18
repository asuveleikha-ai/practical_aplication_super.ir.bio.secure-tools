# app.py - PRACTICAL APPLICATION GAME - Streamlit - Nampilin ke-3 Index Sekaligus!
# Cara pakai di Streamlit Cloud (share.streamlit.io):
# Repo: asuveleikha-ai/practicalapplication-gamesupersecure-tools
# Branch: main
# Main file path: app.py
# Jangan isi index.html, isi app.py!
import streamlit as st
import os

st.set_page_config(page_title="Practical Application Game - Simulasi Nyata", layout="wide")

st.markdown("""
<div style="background:linear-gradient(90deg,#ff7a00,#ffeb3b,#00e676);color:#000;padding:14px;border-radius:12px;text-align:center">
<b style="font-size:22px">🎮 PRACTICAL APPLICATION GAME - SIMULASI NYATA - SIMULASI REAL</b><br>
<b>PRACTICAL • APPLICATION • GAME • SIMULASI REAL • SIMULASI NYATA</b><br>
<small>Game ini merekam dunia nyata - pabrik, rumah, sekolah, pasar - jadi permainan + simulasi yang benar, diterima umum, sesuai standar kehidupan nyata yang terus membaik dan lestari.</small>
</div>
""", unsafe_allow_html=True)

st.write("**Jalur Harian Sales:** Kanvas → Ketemu Bos di Meja → Persetujuan Kontrak (Diterima / Tidak Diterima) → Briefing Teknisi → Prosedur Kontrak → Penjualan! Kalau ditolak, jangan marah, kasih nomor telepon, nanti ada telepon, Second Contract Deal! Terus berkontinu, berlanjut, berlanjut!")
st.write("**Aturan PTS Bener:** Mager doang = 0 PTS | Udah Kanvas = +5 PTS (upah minum) | Udah Kontrak = +30 PTS | Udah Penjualan = +100 PTS")
st.write("**Target Market:** Perumahan, Mall, Ruko, Outlet, Sekolah, Departemen, Pasar, Rumah-rumah, Toko Permata, Toko Elektronik, Pabrik, Rumah Sakit, Hotel")

def load_html(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    return f"<h3>File {filename} belum ada di repo. Upload dulu file {filename} ke GitHub.</h3><p>File yang ada: index.html (utama), index_Classic.html, index_Neural.html</p>"

tab1, tab2, tab3, tab4 = st.tabs(["🏠 MAIN - Jalur Harian Sales", "📄 CLASSIC - Versi Biasa", "⚡ NEURAL - Versi Tron", "📋 PANDUAN - Cara Main & Pasang di Dunia Nyata"])

with tab1:
    st.header("🏠 MAIN - Jalur Harian Sales - Yang Utama!")
    st.info("Ini index.html yang utama! Yang dibuka GitHub Pages kalau buka link tanpa nama file. Isinya: Jalur Harian Sales, Kanvas, Bos, Kontrak, Teknisi, Jualan, Aturan PTS Bener, Animasi Kartun.")
    html_main = load_html("index.html")
    st.components.v1.html(html_main, height=900, scrolling=True)

with tab2:
    st.header("📄 CLASSIC - Versi Biasa")
    st.info("Ini index_Classic.html - Versi klasik, tampilan biasa, buat perbandingan sama Neural.")
    html_classic = load_html("index_Classic.html")
    st.components.v1.html(html_classic, height=900, scrolling=True)

with tab3:
    st.header("⚡ NEURAL - Versi Tron / Neural Grid")
    st.info("Ini index_Neural.html - Versi Tron, Neural Grid, biru-oranye, partikel elektron gerak-gerak, CENTER nyala.")
    html_neural = load_html("index_Neural.html")
    st.components.v1.html(html_neural, height=900, scrolling=True)

with tab4:
    st.header("📋 PANDUAN - Game Balik Ngasih Contoh Dunia Nyata!")
    st.markdown("""
    ### Bukan cuma liat dan ngasih pernyataan jadi game!
    ### Game-nya yang balik ngasih contoh dunia nyata!

    **Contoh Sensor IR Obstacle / Proximity - Mata-nya Alat:**
    - IR Transmitter LED (bening) = Nembak cahaya IR
    - IR Receiver Photodiode (hitam) = Nangkep pantulan
    - Potensio Biru = Atur jarak 2-20cm, puter pake obeng kecil
    - LM393 = Otak kecil, mutusin ada benda / nggak ada benda
    - Wiring: VCC -> 3.3V / 5V | GND -> GND | OUT -> GPIO 15
    - OUT = LOW (0) = ADA BOTOL | OUT = HIGH (1) = KOSONG
    - Tips: Jangan kena matahari langsung, atur potensio 5-10cm, botol bening tempelin stiker putih!

    **Flowchart Ketemu Bos:**
    - Kanvas -> Ketemu Bos di Meja -> Sales ngomong: "Bos, ini produk kita, kalau ada minat, mohon dihubungi ya Bos, ini nomor telepon saya!"
    - Kalau DITERIMA -> Persetujuan Kontrak -> Briefing Teknisi -> Prosedur Kontrak -> Penjualan! +100 PTS
    - Kalau TIDAK DITERIMA -> Jangan marah, cari orderan lain, mager dulu (0 PTS), nanti ada telepon, Second Contract Deal! +30 PTS, balik ke Briefing Teknisi!

    **Cara Pasang di Dunia Nyata (Sama Kayak di Game):**
    1. Pasang sensor IR di Rak Loker / Ruko / Sekolah, sama kayak di game
    2. Kabel VCC, GND, OUT sama kayak di game
    3. Atur potensio sama kayak di game
    4. Botol ditaro, sensor nyala, SCM berkurang, sama kayak di game!
    5. Jadi game-nya jadi panduan praktis, bukan cuma hiburan!

    **File di Repo:**
    - index.html = Utama (GitHub Pages)
    - index_Classic.html = Cadangan Classic
    - index_Neural.html = Cadangan Neural
    - app.py = Ini, buat Streamlit, nampilin ke-3 index sekaligus, nggak timpang tindih, nggak ada yang dibuang!
    - kontrak.json, peralatan.json, panduan_installasi.md, super_secure_syst_v23.py = Data pendukung
    """)
    st.success("Di Streamlit, ke-3 index tampil semua lewat tab-tab di atas! Di GitHub Pages, cuma index.html yang tampil sebagai halaman utama, yang lain dibuka lewat link lengkapnya. Nggak ada yang timpang tindih, nggak ada yang dibuang!")

st.markdown("---")
st.caption("PRACTICAL APPLICATION GAME - Sales / Demand Planner - Canvassing - Ruko, Sekolah, Pasar, Mall, Perumahan, Departemen - Dibuat dari observasi nyata, game balik jadi contoh dunia nyata.")
