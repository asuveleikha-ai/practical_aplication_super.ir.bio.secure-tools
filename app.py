# app.py - V5 - REVISI SPONSORSHIP + LEGAL + 4 PERAN + LEVEL 1-8 + MARKETING DIGITAL + PANDUAN DI TOMBOL
# Main file path Streamlit: app.py
import streamlit as st
import os, json

st.set_page_config(page_title="Practical Application Game - V5 Sponsorship + Legal", layout="wide")

st.markdown("""
<div style="background:linear-gradient(90deg,#ff7a00,#ffeb3b,#00e676);color:#000;padding:14px;border-radius:12px;text-align:center">
<b style="font-size:22px">🎮 PRACTICAL APPLICATION GAME - SIMULASI NYATA - V5 REVISI</b><br>
<b>🎬 DIRECTOR'S CUT - LEGAL + SPONSORSHIP + 4 PERAN + LEVEL 1-8</b><br>
<small>Sales = Demand Planner + Marketing Digital + Sales + Store Experience (1 orang sekarang, nanti sewa pekerja) | Bos = Supplier + Sponsor | Teknisi = Staff Bos | Buyer = Di Market | SaaS + Prototype MILIK FOUNDER</small>
</div>
""", unsafe_allow_html=True)

# TOMBOL - PANDUAN NGGAK NGALANGIN GAME!
c1,c2,c3,c4 = st.columns(4)
with c1: show_panduan = st.button("📋 PANDUAN")
with c2: show_flow = st.button("🔀 FLOWCHART YES/NO")
with c3: show_kontrak = st.button("📜 KONTRAK SPONSORSHIP")
with c4: show_level = st.button("🏆 LEVEL 1-8")

if show_panduan:
    with st.expander("📋 PANDUAN - Klik tombol buat buka/tutup, nggak ngalangin game!", expanded=True):
        st.markdown("""
        **Game Balik Ngasih Contoh Dunia Nyata!** Bukan cuma liat jadi game, game-nya yang balik ngasih contoh dunia nyata!
        **Sensor IR:** Transmitter bening nembak IR, Receiver hitam nangkep pantulan, Potensio Biru atur 2-20cm, LM393 otak kecil. Wiring: VCC->3.3V/5V, GND->GND, OUT->GPIO 15. OUT LOW=ADA BOTOL, HIGH=KOSONG. Tips: Jangan kena matahari, atur 5-10cm, botol bening tempelin stiker putih!
        **IR 7 Detik:** Bisa terpasang di HP saja! Deteksi 7 detik: Panas, gas, api, warna, dari HP saja!
        **Cara Pasang Dunia Nyata = Sama Kayak di Game:** Pasang sensor, kabel sama, atur potensio sama, botol ditaro sensor nyala, SCM berkurang!
        """)
else: st.caption("📋 Panduan ngumpet, klik tombol 📋 PANDUAN kalau mau baca!")

if show_flow:
    with st.expander("🔀 FLOWCHART TERSISTEMATIS - YES / NO - Diamond!", expanded=True):
        st.code("""
[START: PAGI - Sales (Demand Planner + Marketing + Sales + Store Experience) Bangun - Di game ditampilkan, masing-masing dapat point + peringkat level]
 -> [CEK HP + CEK GUDANG SUPPLIER LEWAT WA KE BOS: "Bos, stok ESP32-S3 ada nggak? Sensor IR ada nggak? Kapasitor ada nggak?"]
 -> [KE TOKO SUPPLIER - KETEMU BOS DI TOKO SUPPLIER - 1 BENTUK PEMBICARAAN]
    "Bos, saya mau kanvas hari ini ke [Ruko/Sekolah/Pasar/Mall/Departemen/Rumah]. Kalau ada minat, saya mau kontrak. Stok gudang lengkap nggak?"
 -> [DIAMOND 1: GUDANG LENGKAP?]
    YES -> Bos: "Lengkap!" -> Lanjut
    NO -> Sales: "Ya udah Bos, saya kanvas dulu, cari minat dulu, nanti saya kabarin Bos!"
 -> [DIAMOND 2: BOS SETUJU KONTRAK?]
    YES -> Bos perintahkan Teknisi! Teknisi Briefing! SOP + OEE + KPI!
    NO -> Sales: "Nggak apa-apa Bos, kalau ada minat, hubungi saya ya, ini nomor saya!" -> Kanvas ke Market
 -> [TEKNISI CEK ALAT - DIAMOND 3: ALAT LENGKAP?]
    YES -> Teknisi Rakit!
    NO -> Indent Order! Tunggu barang datang! Kepala Gudang + Teknisi lapor ke Bos!
 -> [KANVAS KE MARKET: Rumah / Ruko / Outlet / Sekolah / Pasar / Mall / Departemen]
 -> [KETEMU BUYER - 1 BENTUK PEMBICARAAN]
    "Pak/Bu, saya dari Toko Supplier Bos. Ini produk kita, Bio Health / CCTV AI / dll. Kalau minat, saya bisa kontrak. Bos siapin barangnya, Teknisi rakit + instalasi. Boleh minta nomor teleponnya?"
 -> [DIAMOND 4: BUYER MINAT?]
    YES -> Buyer kasih nomor, minta kontrak! Sales telpon Bos -> Second Contract! -> Indent Order -> Instalasi -> Jualan +100 PTS!
    NO -> Sales: "Nggak apa-apa, hubungi saya ya!" -> MAGER - Rebahan, 0 PTS! (Bila tidak menjalankan = Mager, Bila YES ada kontrak = Senang + dapat PTS!)
 -> [INSTALASI + TEST LAMPU ON, CAHAYA MEMANCAR, AKTIF BERFUNGSI!]
 -> [MAINTENANCE: Sales + Teknisi + Bos + Buyer rawat bareng - Purna Jual Jaminan Kualitas!]
 -> [BESOK KANVAS LAGI - BERKONTINU!]
 -> [KALAU BUYER SURVEY KE TOKO: Bos promosikan SaaS + Prototype Founder, Bos dapat KOMISI 10%!]
        """)
else: st.caption("🔀 Flowchart ngumpet, klik tombol 🔀 FLOWCHART kalau mau liat!")

if show_kontrak:
    with st.expander("📜 KONTRAK SPONSORSHIP - LEGAL - Baca Teliti!", expanded=True):
        try:
            with open("kontrak.json","r",encoding="utf-8") as f: k=json.load(f)
            st.json(k)
        except Exception as e: st.write("kontrak.json belum ke-upload / belum update. Upload kontrak.json V24 dulu. Error:", e)
        st.markdown("""
        **Inti Kontrak:**
        - **SaaS + Prototype MILIK FOUNDER**, bisa dijual sebagai Sales IT. Bos sebagai Sponsor, bukan pemilik SaaS.
        - **Barang mikrokontroler MILIK BOS**, Founder tidak klaim barang Bos.
        - **Bos sebagai Sponsor:** Bos sediakan barang, gudang, teknisi, tempat promosi. Kalau Buyer survey ke toko dan Bos promosikan SaaS + Prototype Founder dan Buyer jadi beli, **Bos dapat KOMISI 10%**.
        - **Insentif 4 Peran Founder (Bukan Teknisi):** Demand Planner +15 PTS per rencana akurat, Marketing Digital +15 PTS per lead dari konten, Sales: Mager 0, Kanvas +5, Kontrak +30, Jualan +100, Store Experience +20 per Buyer rating bagus / repeat order. Capek kerja di laptop + capek mikir + capek kanvas harus dihargai!
        - **Teknisi:** Briefing +10, Rakit +20, Instalasi +30, Maintenance +20. Ikut SOP, OEE >=85% = Bonus, KPI: Instalasi berhasil, komplain 0-1, respon max 24 jam.
        - **Gudang QC:** Kepala Gudang tanggung jawab QC, Teknisi lapor ke Bos tiap minggu.
        - **Purna Jual:** Maintenance Jaminan Kualitas. Founder maintenance SaaS + follow-up, Teknisi maintenance hardware, Bos sediain sparepart.
        - **Kerja 4 Peran Bukan 1 Orang Kalau Sudah Berkembang:** Sekarang sendiri, nanti sewa + cari pekerja.
        """)
else: st.caption("📜 Kontrak ngumpet, klik tombol 📜 KONTRAK kalau mau baca!")

if show_level:
    with st.expander("🏆 LEVEL 1-8 - Makin Tinggi Makin Kompleks!", expanded=True):
        st.markdown("""
        | Level | Nama | Peralatan | Kompleksitas | PTS Jualan |
        | :--- | :--- | :--- | :--- | :--- |
        | 1 | Perumahan Pribadi | Bio Health + IR 7 Detik di HP | Rendah - 1 ruangan | +100 |
        | 2 | Outlet | Bio Health + CCTV AI + SaaS SCM | Rendah-Sedang | +120 |
        | 3 | Ruko | Super IR Guard + CCTV AI + Early Warning + SaaS | Sedang | +150 |
        | 4 | Sekolah | Bio Health + UV Steril + CCTV AI + Early Warning + SaaS | Sedang-Tinggi | +180 |
        | 5 | Pasar / Pasar Jaya | Color QC + CCTV AI + GPS + SaaS + UV Steril | Tinggi | +200 |
        | 6 | Mall / Supermarket / Minimarket / Department Store | Semua + Marketing Digital | Tinggi | +250 |
        | 7 | Departemen / Local Government | Tender - Puluhan unit | Sangat Tinggi | +300 |
        | 8 | **Autonomous Prototype Pabrik Batik 8in1 - TERTINGGI** | **8in1: Bio Health + Super IR Guard + Color QC Batik + Obsidian + CCTV AI + GPS + SaaS SCM + UV Steril + Super Infrared + SuperSecure + IR 7 Detik - Semua Otomatis!** | **Paling Tinggi - Autonomous!** | **+500 - LEGEND!** |

        **Di Game Simulasi Perlu Dijelaskan + Ditampilkan:** Setiap level ditampilkan di game, masing-masing dapat point + peringkat level semakin bertingkat dan komplit. Level 1 paling gampang, Level 8 paling susah, tapi PTS-nya paling gede!
        **Variant Peralatan + System Aplikasi:** Nanti kita sesuaikan variant peralatannya + system aplikasinya, karena kita ada IR 7 Detik (di HP saja), Super Infrared, SuperSecure, SaaS SCM System, dll.
        """)
else: st.caption("🏆 Level ngumpet, klik tombol 🏆 LEVEL kalau mau liat!")

st.write("---")
st.markdown("**Marketing Digital - Paling Efektif:** 1. Sponsor Bos Toko Supplier (Bos promosikan di toko + sosmed Bos) + 2. Video Short (Kling / CapCut) - Demo alat nyala + 3. Live + Testimoni Buyer + 4. Konten Edukasi | **Kerja di Laptop:** Founder kerja di laptop juga nyari network, marketingin digital, bikin konten, jawab DM, update SaaS, cek dashboard - Capek mikir + capek laptop harus dihargai dengan insentif Demand Planner + Marketing Digital! | **Game Simulator:** Practical Application Simulator dapat + mampu berfungsi real nyata bila terhubung dengan SaaS + Prototype, berapapun pelanggan bisa terkoneksi otomatis aktif sebagaimana fungsinya!")
st.write("**Aturan PTS:** Mager 0 | Kanvas +5 | Kontrak +30 | Jualan +100 | Maintenance +20 | Demand Planner +15 | Marketing Digital +15 | Store Experience +20 | **Target:** Perumahan, Outlet, Ruko, Sekolah, Pasar, Mall, Departemen, Toko Permata, Toko Elektronik, Pabrik Batik 8in1, Rumah Sakit, Hotel")

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

tab_classic, tab_neuro, tab_main = st.tabs(["🟦 20% CLASSIC - Game PTS Sales", "🟧 50% NEURO TRON - Observasi Mikrokontroler", "🟩 20% MAIN - Jalur Harian Sales + Level"])
with tab_classic:
    st.markdown("**CLASSIC (20%): Pemain Utama = Sales (4 Peran).** Kanvas, ketemu Bos Supplier, ditolak, mager, ditelepon, second contract, jualan. Gerak-gerik Sales dibaca Neuro jadi data mikrokontroler!")
    html = load_html(["index_Classic.html","index_classic.html"], "CLASSIC")
    st.components.v1.html(html, height=900, scrolling=True)
with tab_neuro:
    st.markdown("**NEURO TRON (50%): Mata Film! MEMANTAU (bukan merekam!) tapi MEMFUNGSIKAN mikrokontroler seluruhnya!** Tangan gerak → IR detek! Gas → MQ-135! Panas → MLX90640! Api → IMX219! Udara → SHT41! Debu → TCS34725! Botol → IR Proximity! Listrik → Kapasitor + Dioda cegah brownout! Semua jadi partikel elektron!")
    html = load_html(["index_Neural.html","index_neural.html"], "NEURAL")
    st.components.v1.html(html, height=900, scrolling=True)
with tab_main:
    st.markdown("**MAIN (20%): Hasil Observasi Jadi PTS + Level!** Neuro bilang 'Instalasi berhasil!' → Main bilang '+100 PTS! Jualan! Deal!' + Naik Level! Level 1 Perumahan → Level 8 Pabrik Batik 8in1 Autonomous!")
    html = load_html(["index.html","Index.html"], "MAIN")
    st.components.v1.html(html, height=900, scrolling=True)

st.markdown("---")
st.caption("V5 - Sales = Demand Planner + Marketing Digital + Sales + Store Experience | Bos = Supplier + Sponsor (Komisi 10% kalau promosikan SaaS + Prototype Founder ke Buyer yang survey ke toko) | Teknisi = Staff Bos, SOP + OEE + KPI | SaaS + Prototype MILIK FOUNDER, bisa dijual sebagai Sales IT | Gudang QC: Kepala Gudang + Teknisi lapor ke Bos | Purna Jual Jaminan Kualitas")
