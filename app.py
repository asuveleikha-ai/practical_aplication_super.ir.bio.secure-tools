# app.py - V4 - PANDUAN DI TOMBOL, NGGAK NGALANGIN GAME!
# Main file path Streamlit: app.py
import streamlit as st
import os

st.set_page_config(page_title="Practical Application Game - Director's Cut", layout="wide")

st.markdown("""
<div style="background:linear-gradient(90deg,#ff7a00,#ffeb3b,#00e676);color:#000;padding:14px;border-radius:12px;text-align:center">
<b style="font-size:22px">🎮 PRACTICAL APPLICATION GAME - SIMULASI NYATA</b><br>
<b>🎬 DIRECTOR'S CUT - SUTRADARA: SIS + META AI</b><br>
<small>20% Classic + 50% Neuro Tron + 20% Main + 10% Panduan (di tombol, nggak ngalangin game!)</small>
</div>
""", unsafe_allow_html=True)

# TOMBOL PANDUAN - DI ATAS, KECIL, NGGAK NGALANGIN GAME!
col1, col2, col3 = st.columns([1,1,1])
with col1:
    show_panduan = st.button("📋 KLIK - LIHAT PANDUAN", help="Klik kalau mau baca panduan. Kalau nggak mau, biarin aja, game-nya lega!")
with col2:
    show_flow = st.button("🔀 KLIK - LIHAT FLOWCHART", help="Klik kalau mau liat flowchart YES / NO")
with col3:
    show_ekonomi = st.button("💰 KLIK - LIHAT EKONOMI", help="Klik kalau mau liat pembagian PTS ke Sales, Teknisi, Bos, Buyer")

# PANDUAN - CUMA TAMPIL KALAU TOMBOL DIPENCET! KALAU NGGAK DIPENCET, NGGAK MUNCUL, GAME LEGA!
if show_panduan:
    with st.expander("📋 PANDUAN - KLIK TOMBOL DI ATAS BUAT BUKA / TUTUP - NGGAK NGALANGIN GAME!", expanded=True):
        st.markdown("""
        ### 📋 PANDUAN - Game Balik Ngasih Contoh Dunia Nyata!
        **Bukan cuma liat dan ngasih pernyataan jadi game! Game-nya yang balik ngasih contoh dunia nyata!**

        **Sensor IR Obstacle / Proximity - Mata-nya Alat:**
        - IR Transmitter LED (bening) = Nembak cahaya IR
        - IR Receiver Photodiode (hitam) = Nangkep pantulan
        - Potensio Biru = Atur jarak 2-20cm, puter pake obeng kecil
        - LM393 = Otak kecil, mutusin ada benda / nggak ada benda
        - Wiring: VCC -> 3.3V / 5V | GND -> GND | OUT -> GPIO 15
        - OUT = LOW (0) = ADA BOTOL | OUT = HIGH (1) = KOSONG
        - Tips: Jangan kena matahari langsung, atur potensio 5-10cm, botol bening tempelin stiker putih!

        **Cara Pasang di Dunia Nyata (Sama Kayak di Game):**
        1. Pasang sensor IR di Rak Loker / Ruko / Sekolah, sama kayak di game
        2. Kabel VCC, GND, OUT sama kayak di game
        3. Atur potensio sama kayak di game
        4. Botol ditaro, sensor nyala, SCM berkurang, sama kayak di game!
        """)
else:
    st.caption("📋 Panduan ngumpet dulu ya, biar game-nya lega! Kalau mau baca, klik tombol 📋 KLIK - LIHAT PANDUAN di atas!")

if show_flow:
    with st.expander("🔀 FLOWCHART - Tersistematis - Ada Pilihan YES / NO!", expanded=True):
        st.markdown("""
        ```
        [START: Sales (Demand Planner + Marketing + Sales + Store Experience) Bangun]
        → [Cek Gudang Supplier lewat WA ke Bos]
        → [Ke Toko Supplier Alat Mikrokontroler - Ketemu Bos di Toko Supplier]
        → [Sales ngomong 1 bentuk pembicaraan ke Bos]
        → [DIAMOND 1: GUDANG LENGKAP?]
           YES → Bos: "Lengkap!" → Lanjut
           NO → Bos: "Nggak lengkap!" → Sales kanvas dulu, cari minat dulu
        → [DIAMOND 2: BOS SETUJU KONTRAK?]
           YES → Bos perintahkan Teknisi! → Teknisi Briefing!
           NO → Sales: "Nggak apa-apa Bos, kalau ada minat, hubungi saya ya, ini nomor saya!" → Kanvas ke Market
        → [TEKNISI CEK ALAT - DIAMOND 3: ALAT LENGKAP?]
           YES → Teknisi Rakit!
           NO → Indent Order! Tunggu barang datang!
        → [KANVAS KE MARKET: Rumah / Ruko / Outlet / Sekolah / Pasar / Mall / Departemen]
        → [Ketemu Buyer - Ngomong 1 bentuk pembicaraan]
        → [DIAMOND 4: BUYER MINAT?]
           YES → Buyer kasih nomor, minta kontrak! → Sales telpon Bos → Second Contract! → Indent Order → Instalasi → Jualan +100 PTS!
           NO → Buyer: "Belum minat!" → Sales: "Nggak apa-apa, hubungi saya ya!" → MAGER - Rebahan, 0 PTS!
        → [INSTALASI + TEST LAMPU ON!]
        → [MAINTENANCE: Sales + Teknisi + Bos + Buyer rawat bareng!]
        → [BESOK KANVAS LAGI - BERKONTINU!]
        ```

        **Bahasa ke Bos Supplier (1 bentuk):** "Bos, saya mau kanvas hari ini ke [Ruko/Sekolah/Pasar/Mall/Departemen/Rumah]. Kalau ada minat, saya mau kontrak. Stok di gudang Bos lengkap nggak? Kalau lengkap, saya berani janji ke Buyer."

        **Bahasa ke Buyer (1 bentuk):** "Pak/Bu, saya dari [Nama Toko Supplier Bos]. Ini produk kita, [Bio Health Room/CCTV AI/dll]. Kalau ada minat, saya bisa kontrak. Nanti Bos Supplier saya yang siapin barangnya, Teknisi yang rakit + instalasi. Boleh saya minta nomor teleponnya?"

        **Bahasa ke Teknisi (1 bentuk):** "Teknisi, alat-alatnya sudah siap belum? ESP32-S3 ada nggak? Sensor IR ada nggak? Kapasitor + Dioda ada nggak? Kalau kosong, kita indent dulu ya."
        """)
else:
    st.caption("🔀 Flowchart ngumpet dulu ya! Klik tombol 🔀 KLIK - LIHAT FLOWCHART kalau mau liat!")

if show_ekonomi:
    with st.expander("💰 EKONOMI MENYELURUH - PTS Dibagi ke Semua!", expanded=True):
        st.markdown("""
        | Pelaku | Peran | PTS | Maintenance |
        | :--- | :--- | :--- | :--- |
        | **Sales (Sis) - Founder / Pemilik Toko** | Demand Planner + Marketing + Sales + Store Experience + Maintenance! | Mager 0, Kanvas +5 (upah minum), Kontrak +30, Jualan +100, Maintenance +20 | Cek alat Buyer tiap bulan, ganti sensor |
        | **Bos Toko / Supplier** | Punya barang + mikrokontroler, kasih kontrak, kasih modal, kasih teknisi | Bagi hasil, untung dari penjualan | Sediain stok ESP32-S3, sensor, kapasitor, dioda |
        | **Teknisi / Staff / Manager Teknik** | Jasa aja, rakit, instalasi, briefing, test lampu ON | Briefing +10, Rakit +20, Instalasi +30, Maintenance +20 | Cek alat tiap minggu, ganti kapasitor kalau brownout |
        | **Buyer / Pengguna** | Beli, pakai, lapor kalau error, bayar maintenance | Buyer dapet alat sehat + maintenance gratis 1 bulan, Buyer Teladan +10 | Bersihin sensor, jangan kena matahari, tempelin stiker putih di botol bening |

        **Alur Duit:** Buyer bayar → Bos terima → Bagi ke Sales + Teknisi → Bos untung → Buyer dapet alat sehat → Buyer puas → Cerita ke tetangga → Tetangga jadi Buyer baru → Kanvas lagi → BERKONTINU!
        """)
else:
    st.caption("💰 Ekonomi ngumpet dulu ya! Klik tombol 💰 KLIK - LIHAT EKONOMI kalau mau liat!")

st.write("---")
st.write("**Aturan PTS Bener:** Mager doang = 0 PTS | Kanvas = +5 PTS | Kontrak = +30 PTS | Jualan = +100 PTS | **Target:** Perumahan, Mall, Ruko, Outlet, Sekolah, Departemen, Pasar, Rumah-rumah, Toko Permata, Toko Elektronik, Pabrik, Rumah Sakit, Hotel")

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

tab_classic, tab_neuro, tab_main = st.tabs(["🟦 20% CLASSIC - Game PTS Sales", "🟧 50% NEURO TRON - Observasi Mikrokontroler", "🟩 20% MAIN - Jalur Harian Sales"])

with tab_classic:
    st.markdown("**🎬 CLASSIC (20%): Pemain Utama = Sales.** Kanvas, ketemu Bos Supplier, ditolak, mager, ditelepon, second contract, jualan. Gerak-gerik Sales di Classic, dibaca Neuro jadi data mikrokontroler!")
    html = load_html(["index_Classic.html","index_classic.html"], "CLASSIC")
    st.components.v1.html(html, height=900, scrolling=True)

with tab_neuro:
    st.markdown("**🎬 NEURO TRON (50% - PALING GEDE!): Mata Film! MEMANTAU (bukan merekam!) tapi MEMFUNGSIKAN mikrokontroler seluruhnya!** Tangan gerak → IR detek! Gas → MQ-135 cium! Panas → MLX90640 liat! Api → IMX219 liat! Udara → SHT41 ukur! Debu → TCS34725 ukur! Botol → IR Proximity! Listrik → Kapasitor + Dioda cegah brownout! Semua jadi partikel elektron di Neural Grid!")
    html = load_html(["index_Neural.html","index_neural.html"], "NEURAL")
    st.components.v1.html(html, height=900, scrolling=True)

with tab_main:
    st.markdown("**🎬 MAIN (20%): Hasil Observasi Jadi PTS di Jalur Harian Sales!** Neuro bilang 'Instalasi berhasil!' → Main bilang '+100 PTS! Jualan! Deal!' Neuro bilang 'Teknisi berhasil rakit!' → Main bilang '+30 PTS buat Teknisi!'")
    html = load_html(["index.html","Index.html"], "MAIN")
    st.components.v1.html(html, height=900, scrolling=True)

st.markdown("---")
st.caption("PRACTICAL APPLICATION GAME - Director's Cut - Panduan di tombol, nggak ngalangin game! Sales = Demand Planner + Marketing + Sales + Store Experience | Bos = Supplier Mikrokontroler | Teknisi = Staff / Manager Teknik Bos | Buyer = Di Ruko / Sekolah / Pasar / Mall / Departemen / Rumah")
