# app.py - V2 - FIX Huruf Gede-Kecil - Streamlit - Nampilin ke-3 Index Sekaligus!
# Main file path di Streamlit: app.py
import streamlit as st
import os

st.set_page_config(page_title="Practical Application Game - Simulasi Nyata", layout="wide")

st.markdown("""
<div style="background:linear-gradient(90deg,#ff7a00,#ffeb3b,#00e676);color:#000;padding:14px;border-radius:12px;text-align:center">
<b style="font-size:22px">🎮 PRACTICAL APPLICATION GAME - SIMULASI NYATA - SIMULASI REAL</b><br>
<b>PRACTICAL • APPLICATION • GAME • SIMULASI REAL • SIMULASI NYATA</b><br>
<small>Game ini merekam dunia nyata - pabrik, rumah, sekolah, pasar - jadi permainan + simulasi yang benar, diterima umum, sesuai standar kehidupan nyata.</small>
</div>
""", unsafe_allow_html=True)

st.write("**Jalur Harian:** Kanvas → Ketemu Bos di Meja → Kontrak (Diterima / Tidak Diterima) → Briefing Teknisi → Prosedur Kontrak → Penjualan! Kalau ditolak, kasih nomor telepon, nanti ada telepon, Second Contract Deal!")
st.write("**Aturan PTS Bener:** Mager doang = 0 PTS | Udah Kanvas = +5 PTS (upah minum) | Udah Kontrak = +30 PTS | Udah Penjualan = +100 PTS")
st.write("**Target Market:** Perumahan, Mall, Ruko, Outlet, Sekolah, Departemen, Pasar, Rumah-rumah, Toko Permata, Toko Elektronik, Pabrik, Rumah Sakit, Hotel")

# FIX: Cari file tanpa peduli huruf gede-kecil
def find_file(candidates):
    # List semua file di folder ini, biar tau nama benernya
    try:
        files = os.listdir(".")
    except:
        files = []
    # Buat peta huruf kecil -> nama asli
    lower_map = {f.lower(): f for f in files}
    for cand in candidates:
        if cand in files:
            return cand
        if cand.lower() in lower_map:
            return lower_map[cand.lower()]
    return None

def load_html(candidates, label):
    found = find_file(candidates)
    if found:
        st.success(f"✅ Ketemu file: {found} → ditampilin sebagai {label}")
        with open(found, "r", encoding="utf-8") as f:
            return f.read()
    else:
        # Kasih tau file apa aja yang ada, biar nggak bingung
        try:
            files = os.listdir(".")
        except:
            files = ["(tidak bisa list)"]
        return f"<h3>File {label} belum ketemu. Dicari: {candidates}</h3><p>File yang ada di Streamlit sekarang: {files}</p><p>Solusi: Cek nama file di GitHub, pastikan ada file index.html / index_Classic.html / index_Neural.html di root repo (bukan di folder lain). Kalau namanya beda huruf, app.py V2 ini sudah otomatis nyari yang mirip.</p>"

tab1, tab2, tab3, tab4 = st.tabs(["🏠 MAIN - Jalur Harian Sales", "📄 CLASSIC - Versi Biasa", "⚡ NEURAL - Versi Tron", "📋 PANDUAN"])

with tab1:
    st.header("🏠 MAIN - Jalur Harian Sales - Yang Utama!")
    st.info("Ini index.html yang utama! Yang dibuka GitHub Pages kalau buka link tanpa nama file.")
    html_main = load_html(["index.html", "Index.html", "INDEX.HTML"], "MAIN")
    st.components.v1.html(html_main, height=900, scrolling=True)

with tab2:
    st.header("📄 CLASSIC - Versi Biasa")
    st.info("Ini index_Classic.html - Versi klasik, tampilan biasa, buat perbandingan sama Neural.")
    html_classic = load_html(["index_Classic.html", "index_classic.html", "index-classic.html", "Index_Classic.html", "index_Classic.HTML"], "CLASSIC")
    st.components.v1.html(html_classic, height=900, scrolling=True)

with tab3:
    st.header("⚡ NEURAL - Versi Tron / Neural Grid")
    st.info("Ini index_Neural.html - Versi Tron, Neural Grid, biru-oranye, partikel elektron gerak-gerak, CENTER nyala.")
    html_neural = load_html(["index_Neural.html", "index_neural.html", "index-neural.html", "Index_Neural.html", "index_Neural.HTML"], "NEURAL")
    st.components.v1.html(html_neural, height=900, scrolling=True)

with tab4:
    st.header("📋 PANDUAN - Game Balik Ngasih Contoh Dunia Nyata!")
    st.markdown("""
    ### Bukan cuma liat dan ngasih pernyataan jadi game!
    ### Game-nya yang balik ngasih contoh dunia nyata!

    **Sensor IR Obstacle / Proximity - Mata-nya Alat:**
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
    """)
    st.success("Di Streamlit, ke-3 index tampil semua lewat tab-tab di atas!")

st.markdown("---")
st.caption("PRACTICAL APPLICATION GAME - Sales / Demand Planner - Canvassing - Ruko, Sekolah, Pasar, Mall, Perumahan, Departemen")
