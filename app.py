# app.py V6.2 - GAME AKTIF LAGI - TOMBOL STREAMLIT ASLI, BUKAN CUMA IFRAME
# BATIK 8in1 TETAP DIHAPUS DARI GAME - PISAH TOTAL!
import streamlit as st
import os, json
st.set_page_config(page_title="Practical Application Game V6.2 - AKTIF", layout="wide")

# --- SESSION STATE - BIAR PTS NGGAK HILANG KALAU KLIK ---
if "pts" not in st.session_state: st.session_state.pts = 0
if "hari" not in st.session_state: st.session_state.hari = 1
if "langkah" not in st.session_state: st.session_state.langkah = "Belum mulai. Klik 1. KANVAS!"
if "chars" not in st.session_state: st.session_state.chars = "🧑‍💼"
if "dialog" not in st.session_state: st.session_state.dialog = "Pagi Hari 1: Sales 4 Peran bangun. Klik 1. KANVAS! Ke Toko Supplier, ketemu Bos Supplier!"
if "voice_log" not in st.session_state: st.session_state.voice_log = []

levels = ["1 - Perumahan","2 - Outlet","3 - Ruko","4 - Sekolah","5 - Pasar","6 - Mall","7 - Departemen - MAX"]
def get_level(pts):
    if pts>=300: return 7
    if pts>=250: return 6
    if pts>=200: return 5
    if pts>=180: return 4
    if pts>=150: return 3
    if pts>=120: return 2
    return 1
def add_pts(n, txt):
    st.session_state.pts += n
    st.session_state.langkah = txt
def speak_js(text):
    # Voice pakai Web Speech API di browser - harus klik tombol dulu, browser baru izinkan suara
    safe = text.replace("'","").replace('"',"")
    return f"<script>try{{speechSynthesis.cancel();let u=new SpeechSynthesisUtterance('{safe}');u.lang='id-ID';speechSynthesis.speak(u);}}catch(e){{}}</script>"

st.markdown("""
<div style="background:linear-gradient(90deg,#ff7a00,#ffeb3b,#00e676);color:#000;padding:14px;border-radius:12px;text-align:center">
<b style="font-size:22px">🎮 PRACTICAL APPLICATION GAME V6.2 - AKTIF LAGI - TANPA BATIK</b><br>
<b>GAME AKTIF! TOMBOL DI BAWAH INI BENERAN BISA DIPENCET! BUKAN VIDEO DEMO!</b><br>
<small>Game = Promosi Gratis, 4 Item Ringkas | Super Secure + Super Infrared = Berbayar | Batik 8in1 DIHAPUS dari Game, Pisah Total!</small>
</div>
""", unsafe_allow_html=True)

# HUB 2 TOMBOL
c1,c2 = st.columns(2)
with c1: st.link_button("🟦 SUPER SECURE SYST V23 - Berbayar", "https://super-secure-syst-v23.streamlit.app/")
with c2: st.link_button("🟧 SUPER INFRARED - Berbayar", "https://super-infrared-giago2j38xeb3pdqmaxcqb.streamlit.app/")
st.caption("Batik DIHAPUS dari game. Cek Batik di app-nya sendiri, bukan di sini.")

# INFO KONEKSI REAL - JAWAB PERTANYAAN USER
with st.expander("🔌 KONEKSI REAL - APAKAH STREAMLIT DEMO INI TERHUBUNG KE ALAT BENERAN? - BACA INI!", expanded=True):
    st.markdown("""
    **JAWABAN JUJUR, SIS:**
    - **Streamlit demo yang lu liat sekarang = SIMULASI / VIDEO DEMO, BUKAN ALAT BENERAN!** Tombolnya jalanin simulasi di browser, bukan baca sensor ESP32 beneran!
    - **GitHub = LEMARI KODE SAJA!** GitHub cuma nyimpen file `app.py`, `index.html`, `mapping.json`, `peralatan.json`. GitHub **TIDAK** nerima data sensor, **TIDAK** bisa baca ESP32!
    - **Yang LEBIH NYATA harusnya: GAME SIMULASI REAL <-> API / DATABASE <-> ESP32-S3 BENERAN!**
    ```
    [ESP32-S3 + SHT41 + MQ-135 + MLX90640 di Rumah Buyer] --WiFi--> [API / Firebase / Supabase / MQTT] --Internet--> [STREAMLIT / GAME baca API] --> Tampil HIJAU / KUNING / MERAH BENERAN!
    ```
    - **Jadi:** Game <-> GitHub = **SALAH**, cuma nyimpen kode. Game <-> Streamlit Demo = **MASIH SIMULASI**, belum real. Game <-> API <-> ESP32 = **BARU REAL!**
    - **Untuk sekarang, kita masih mereka-reka (simulasi) biar flowchart + PTS + mapping-nya bener dulu.** Kalau flowchart udah bener, baru kita pasang API + ESP32 beneran. Jangan langsung pasang alat beneran kalau flowchart-nya belum bener, nanti alatnya bingung!
    """)

# PANGGUNG - TAMPILAN BERUBAH SETIAP KLIK!
lvl = get_level(st.session_state.pts)
st.markdown(f"""
<div style="background:#031a2a;border:2px solid #00e5ff;border-radius:12px;padding:14px;text-align:center">
<b>📅 HARI: {st.session_state.hari} | ⭐ PTS: {st.session_state.pts} | 🏆 LEVEL: {levels[lvl-1]}</b><br>
<b>Game Ringan - 4 Item Saja:</b> IR 7 Detik di HP | Bio Health Ringkas | CCTV AI Ringkas | SaaS SCM Demo<br>
<div style="font-size:60px">{st.session_state.chars}</div>
<div style="background:#fff;color:#000;padding:10px;border-radius:12px;font-weight:700">{st.session_state.dialog}</div>
<div style="background:#00e676;color:#000;padding:8px;border-radius:10px;font-weight:900;margin-top:8px">LANGKAH TERAKHIR: {st.session_state.langkah}</div>
</div>
""", unsafe_allow_html=True)

# === KONTROL AKTIF - TOMBOL STREAMLIT ASLI ===
st.markdown("### 🎮 KONTROL AKTIF - KLIK, LANGSUNG BERUBAH! BUKAN VIDEO!")
k1,k2,k3,k4,k5 = st.columns(5)
with k1:
    if st.button("🚶 1. KANVAS +5", use_container_width=True):
        st.session_state.chars="🧑‍💼🚶‍➡️🧑‍💼🪑"; st.session_state.dialog="Sales: Jalan ke Toko Supplier! Ketemu Bos Supplier!"; add_pts(5,"KANVAS +5!"); st.session_state.voice_log.append("Kanvas!")
with k2:
    if st.button("🧑‍💼 2. BOS SUPPLIER", use_container_width=True):
        st.session_state.chars="🧑‍💼💬🧑‍💼🪑"; st.session_state.dialog='Sales: "Bos, saya mau kanvas ke Ruko / Sekolah / Pasar / Mall! Stok gudang lengkap nggak?"'; st.session_state.langkah="BOS SUPPLIER - 1 bentuk pembicaraan!"; st.session_state.voice_log.append("Ketemu Bos!")
with k3:
    if st.button("📦 3. GUDANG?", use_container_width=True):
        st.session_state.chars="📦"; st.session_state.dialog="DIAMOND: GUDANG LENGKAP? YES = Lanjut! NO = Kanvas dulu!"; st.session_state.langkah="GUDANG - Cek QC!"; st.session_state.voice_log.append("Cek gudang!")
with k4:
    if st.button("📝 4. BOS SETUJU?", use_container_width=True):
        st.session_state.chars="🤝"; st.session_state.dialog="DIAMOND: BOS SETUJU? YES = Teknisi! NO = Kanvas ke Market!"; st.session_state.langkah="BOS SETUJU?"; st.session_state.voice_log.append("Bos setuju?")
with k5:
    if st.button("👨‍🔧 5. TEKNISI SOP", use_container_width=True):
        st.session_state.chars="👨‍🔧"; st.session_state.dialog='Teknisi: "Siap! SOP + OEE + KPI! Alat siap!"'; st.session_state.langkah="TEKNISI - SOP!"; st.session_state.voice_log.append("Teknisi!")
k6,k7,k8,k9,k10 = st.columns(5)
with k6:
    if st.button("🧑 6. BUYER MINAT?", use_container_width=True):
        st.session_state.chars="🧑‍💼💬🧑"; st.session_state.dialog='Sales ketemu Buyer: "Pak/Bu, saya dari Toko Supplier Bos. Ini produk kita. Kalau minat, saya bisa kontrak. Bos siapin barangnya, Teknisi rakit + instalasi. Boleh minta nomor teleponnya?"'; st.session_state.langkah="BUYER MINAT?"; st.session_state.voice_log.append("Buyer minat?")
with k7:
    if st.button("📝 7. SECOND CONTRACT +30", use_container_width=True):
        st.session_state.chars="🤝"; st.session_state.dialog="Second Contract! +30 PTS!"; add_pts(30,"SECOND CONTRACT +30!"); st.session_state.voice_log.append("Second Contract!")
with k8:
    if st.button("📦 8. INDENT ORDER", use_container_width=True):
        st.session_state.chars="📦⏳"; st.session_state.dialog="Indent Order: Pesan dulu, tunggu 2-3 hari!"; st.session_state.langkah="INDENT - Tunggu!"; st.session_state.voice_log.append("Indent order!")
with k9:
    if st.button("🔧 9. INSTALASI", use_container_width=True):
        st.session_state.chars="🔧💡"; st.session_state.dialog="Instalasi! Lampu ON, Cahaya Memancar, Aktif!"; st.session_state.langkah="INSTALASI - Lampu ON!"; st.session_state.voice_log.append("Instalasi!")
with k10:
    if st.button("💰 10. JUALAN +100", use_container_width=True):
        st.session_state.chars="💰😃🤝"; st.session_state.dialog="Jualan! Deal! +100 PTS! Naik Level! Mapping update! Buyer baru masuk peta!"; add_pts(100,"JUALAN +100! MAPPING UPDATE!"); st.session_state.voice_log.append("Jualan!")
k11,k12,k13 = st.columns(3)
with k11:
    if st.button("😴 MAGER 0 PTS", use_container_width=True):
        st.session_state.chars="😴"; st.session_state.dialog="Mager: Tidak menjalankan = 0 PTS!"; st.session_state.langkah="MAGER 0 PTS!"; st.session_state.voice_log.append("Mager!")
with k12:
    if st.button("📞 TELEPON BUNYI!", use_container_width=True):
        st.session_state.chars="📱📞😃"; st.session_state.dialog="Telepon Bunyi! Ada minat! Seneng!"; st.session_state.langkah="TELEPON - Ada minat!"; st.session_state.voice_log.append("Telepon bunyi!")
with k13:
    if st.button("🌅 HARI BERIKUTNYA!", use_container_width=True):
        st.session_state.hari+=1; st.session_state.chars="🌅🧑‍💼"; st.session_state.dialog=f"Hari {st.session_state.hari}: Berangkat lagi!"; st.session_state.langkah=f"HARI BERIKUTNYA - {st.session_state.hari}"; st.session_state.voice_log.append("Hari berikutnya!")

# VOICE - HARUS KLIK, BROWSER BARU IZINKAN SUARA!
st.markdown("### 🔊 SUARA / VOICE - KLIK TOMBOL INI, BARU BUNYI! (Browser nggak izinkan auto-play!)")
if st.button("🔊 TEST SUARA - BACA DIALOG TERAKHIR"):
    st.components.v1.html(speak_js(st.session_state.dialog), height=0)
    st.success(f"Voice: {st.session_state.dialog}")
    st.caption("Kalau nggak bunyi, cek: 1. Volume laptop / HP nyala? 2. Izin suara di browser diizinkan? 3. Coba klik lagi, browser kadang block suara pertama!")
if st.session_state.voice_log:
    st.caption(f"Voice Log (Auto-Record Simulasi): {' | '.join(st.session_state.voice_log[-10:])} - Ini log simulasi, bukan rekaman beneran. Rekaman beneran butuh mic + izin browser + API!")
if st.button("🔄 RESET GAME - PTS 0"):
    st.session_state.pts=0; st.session_state.hari=1; st.session_state.langkah="Reset!"; st.session_state.chars="🧑‍💼"; st.session_state.dialog="Game di-reset. Pagi Hari 1 lagi!"; st.session_state.voice_log=[]; st.rerun()

# MAPPING - TOMBOL, NGGAK NGALANGIN GAME
st.markdown("### 🗺️ MAPPING PER BUYER - PURNA JUAL")
if st.button("🗺️ KLIK - LIHAT MAPPING PER BUYER"):
    try:
        with open("mapping.json","r",encoding="utf-8") as f: m=json.load(f)
        st.write("**Rute Maintenance Hari Ini:**", m["rute_maintenance_hari_ini"])
        filt = st.selectbox("Filter App:", ["Semua","Super Secure","Super Infrared"])
        for b in m["buyers"]:
            if filt!="Semua" and b["app"]!=filt: continue
            color = "🟢" if "HIJAU" in b["status"] else "🟡" if "KUNING" in b["status"] else "🔴"
            st.markdown(f"**{color} {b['id']} - {b['nama']} - {b['app']}** | 📍 {b['alamat']} | 🔧 {b['peralatan']} | Status: {b['status']} | Kerusakan: {b['kerusakan']} | Maintenance Berikutnya: {b['maintenance_berikutnya']} | Teknisi: {b['teknisi']} | PTS: {b['pts']}")
        try:
            import pandas as pd
            df=pd.DataFrame([{"lat":b["lat"],"lon":b["lon"],"nama":b["nama"]} for b in m["buyers"]])
            st.map(df)
        except Exception as e: st.write("Map gagal:", e)
    except Exception as e: st.write("mapping.json belum ke-upload. Error:", e)
else:
    st.caption("Mapping ngumpet, klik tombol di atas kalau mau liat peta + maintenance!")

# PANDUAN / FLOWCHART / ITEM DIKURANGI - TOMBOL
c1,c2,c3 = st.columns(3)
with c1:
    if st.button("📋 PANDUAN"): st.info("Game HUB ringan! Cuma 4 item: IR 7 Detik, Bio Health Ringkas, CCTV AI Ringkas, SaaS SCM Demo. Batik DIHAPUS dari game! Cara main: Kanvas -> Bos -> Gudang -> Buyer -> Second Contract -> Indent -> Instalasi -> Jualan + Maintenance! Panduan di tombol, nggak ngalangin game!")
with c2:
    if st.button("✂️ ITEM DIKURANGI"): st.info("SEBELUM: 14 peralatan, berat! SESUDAH: Cuma 4! Yang berat DIHAPUS dari game! Batik 8in1 DIHAPUS, hidup di app sendiri!")
with c3:
    if st.button("🔀 FLOWCHART"): st.code("[START] -> [Cek Gudang] -> [Bos Supplier] -> [GUDANG LENGKAP? YES/NO] -> [BOS SETUJU? YES/NO] -> [TEKNISI SOP] -> [KANVAS] -> [BUYER MINAT? YES/NO] -> YES: Second Contract -> Indent -> Instalasi -> Jualan + Mapping! NO: Mager 0 PTS!")

st.write("---")
st.markdown("**V6.2 AKTIF:** Tombol Streamlit asli, PTS kesimpen di session, suara pakai Web Speech API (klik dulu baru bunyi), mapping per Buyer, Batik tetap pisah!")

# TAB VISUAL - IFRAME HANYA UNTUK LIHAT, KONTROL UTAMA DI ATAS!
st.markdown("### 🎬 VISUAL STAGE - LIHAT SAJA, KONTROLNYA DI ATAS (YANG AKTIF)!")
tab_classic, tab_neuro, tab_main = st.tabs(["🟦 20% CLASSIC - Game Ringan", "🟧 50% NEURO TRON - Observasi", "🟩 20% MAIN - Jalur Harian + MAPPING"])
def load_html(cands,label):
    try: files=os.listdir(".")
    except: files=[]
    lm={f.lower():f for f in files}
    for c in cands:
        if c in files:
            with open(c,"r",encoding="utf-8") as fh: return fh.read()
        if c.lower() in lm:
            with open(lm[c.lower()],"r",encoding="utf-8") as fh: return fh.read()
    return f"<h3>{label} belum ketemu</h3>"
with tab_classic:
    st.markdown("**CLASSIC (20%):** Visual saja. Kontrol aktif ada di atas!")
    st.components.v1.html(load_html(["index_classic.html"],"CLASSIC"), height=900, scrolling=True)
with tab_neuro:
    st.markdown("**NEURO TRON (50%):** Visual observasi saja. Kontrol aktif ada di atas!")
    st.components.v1.html(load_html(["index_neural.html","index_Neural.html"],"NEURAL"), height=900, scrolling=True)
with tab_main:
    st.markdown("**MAIN (20%):** Visual saja. Kontrol aktif ada di atas!")
    st.components.v1.html(load_html(["index.html"],"MAIN"), height=900, scrolling=True)
st.caption("V6.2 - AKTIF | Game = Simulasi (belum baca ESP32 beneran) | Real = ESP32 -> API -> Streamlit | GitHub = Lemari Kode Saja | Batik DIHAPUS dari Game")
