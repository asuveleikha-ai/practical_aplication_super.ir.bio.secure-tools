# app.py V6.1 - HUB RINGAN TANPA BATIK + MAPPING SUPER SECURE + SUPER INFRARED
import streamlit as st
import os, json
st.set_page_config(page_title="Practical Application Game V6 - HUB + MAPPING", layout="wide")
st.markdown("""
<div style="background:linear-gradient(90deg,#ff7a00,#ffeb3b,#00e676);color:#000;padding:14px;border-radius:12px;text-align:center">
<b style="font-size:22px">🎮 PRACTICAL APPLICATION GAME V6.1 - HUB RINGAN - TANPA BATIK</b><br>
<b>GAME DIKURANGI JADI 4 ITEM SAJA - RINGAN! BATIK 8in1 DIHAPUS DARI GAME!</b><br>
<small>Game = Promosi Gratis | Super Secure + Super Infrared = Berbayar (Max 10 Buyer) | Batik Guard DIHAPUS dari Game, hidup di app sendiri!</small>
</div>
""", unsafe_allow_html=True)

# 3 TOMBOL HUB KE 3 APP BERBAYAR
st.markdown("### 🔗 HUB - KLIK UNTUK PINDAH KE APP BERBAYAR (REPORT + KONTROL PISAH)")
c1,c2 = st.columns(2)
with c1: st.link_button("🟦 SUPER SECURE SYST V23 - Berbayar", "https://super-secure-syst-v23.streamlit.app/")
with c2: st.link_button("🟧 SUPER INFRARED - Berbayar", "https://super-infrared-giago2j38xeb3pdqmaxcqb.streamlit.app/")
# BATIK DIHAPUS DARI GAME - TIDAK ADA TOMBOL BATIK DI SINI
st.caption("Game ini HUB ringan TANPA BATIK! Batik 8in1 DIHAPUS dari game, cek di app Batik Guard sendiri. Report Super Secure + Super Infrared ada di app masing-masing!")

# TOMBOL PANDUAN / MAPPING - NGGAK NGALANGIN GAME
c1,c2,c3,c4 = st.columns(4)
with c1: show_panduan = st.button("📋 PANDUAN")
with c2: show_map = st.button("🗺️ MAPPING PER BUYER")
with c3: show_kurang = st.button("✂️ ITEM DIKURANGI")
with c4: show_flow = st.button("🔀 FLOWCHART")

if show_panduan:
    with st.expander("📋 PANDUAN - Ringan!", expanded=True):
        st.markdown("**Game ini HUB ringan!** Cuma 4 item: IR 7 Detik di HP, Bio Health Room Ringkas, CCTV AI Ringkas, SaaS SCM Demo. Yang berat-berat pindah ke Super Secure / Super Infrared! Batik DIHAPUS dari game! Cara main: Kanvas -> Bos Supplier -> Gudang -> Buyer -> Second Contract -> Indent -> Instalasi -> Jualan + Maintenance! Panduan di tombol, nggak ngalangin game!")
else: st.caption("📋 Panduan ngumpet, klik tombol 📋 PANDUAN kalau mau baca!")

if show_kurang:
    with st.expander("✂️ ITEM DIKURANGI - DARI 14 JADI 4!", expanded=True):
        st.markdown("""
        **SEBELUM (Berat):** 14 peralatan di game, campur aduk sama pabrik, game berat, report numpuk!
        **SESUDAH (Ringan - Cuma 4):**
        1. IR 7 Detik di HP - Demo paling ringan, di HP saja!
        2. Bio Health Room Ringkas - SHT41 + MQ-135 + ESP32-S3 saja!
        3. CCTV AI Ringkas - 1 kamera saja!
        4. SaaS SCM Demo - Demo catat stok, bukan kontrol pabrik!
        **YANG DIPINDAH:**
        - Yang berat-berat DIHAPUS dari game, tidak ada lagi di game!
        - Ke Super Secure / Super Infrared: Super Secure Syst + Super Infrared lengkap!
        **Hasil:** Game jadi ringan, loading cepet, pemain nggak bingung, report nggak numpuk!
        """)
else: st.caption("✂️ Item dikurangi ngumpet, klik tombol ✂️ ITEM DIKURANGI kalau mau liat!")

if show_flow:
    with st.expander("🔀 FLOWCHART - Sama, Bentuknya Sama!", expanded=True):
        st.code("""
[START: Sales 4 Peran Bangun] -> [Cek Gudang WA ke Bos] -> [Ke Toko Supplier, Ketemu Bos]
-> [DIAMOND 1: GUDANG LENGKAP? YES/NO] -> [DIAMOND 2: BOS SETUJU? YES/NO]
-> [TEKNISI SOP + OEE + KPI] -> [KANVAS KE MARKET] -> [DIAMOND 3: BUYER MINAT? YES/NO]
-> YES: Second Contract -> Indent Order -> Instalasi -> Jualan + Maintenance + Mapping!
-> NO: Mager 0 PTS!
-> Kalau Buyer minat yang berbayar, kasih link: Super Secure / Super Infrared saja!
        """)
else: st.caption("🔀 Flowchart ngumpet, klik tombol 🔀 FLOWCHART kalau mau liat!")

if show_map:
    with st.expander("🗺️ MAPPING PER BUYER - PURNA JUAL - SESUAI DAERAH PENEMPATAN!", expanded=True):
        try:
            with open("mapping.json","r",encoding="utf-8") as f: m=json.load(f)
            st.write("**Rute Maintenance Hari Ini:**", m["rute_maintenance_hari_ini"])
            buyers=m["buyers"]
            # Filter
            filt = st.selectbox("Filter App:", ["Semua","Super Secure","Super Infrared"]) # BATIK DIHAPUS DARI GAME
            for b in buyers:
                if filt!="Semua" and b["app"]!=filt: continue
                color = "🟢" if "HIJAU" in b["status"] else "🟡" if "KUNING" in b["status"] else "🔴"
                st.markdown(f"**{color} {b['id']} - {b['nama']} - {b['app']}** | 📍 {b['alamat']} | 🔧 {b['peralatan']} | Status: {b['status']} | Heartbeat: {b['last_heartbeat']} | Kerusakan: {b['kerusakan']} | Maintenance Berikutnya: {b['maintenance_berikutnya']} | Teknisi: {b['teknisi']} | PTS: {b['pts']}")
            st.markdown("**Peta:** Hijau = Sehat, Kuning = Perlu Maintenance, Merah = Rusak, Teknisi Harus Datang Hari Ini! Setiap Buyer punya ID, alamat, lat/lon, peralatan, status, teknisi, jadwal maintenance. Detail lengkap ada di app masing-masing (Super Secure / Super Infrared / Batik Guard), HUB ini cuma ringkasan!")
            # Map
            try:
                import pandas as pd
                df=pd.DataFrame([{"lat":b["lat"],"lon":b["lon"],"nama":b["nama"]} for b in buyers])
                st.map(df)
            except Exception as e: st.write("Map gagal load:", e)
        except Exception as e: st.write("mapping.json belum ke-upload. Upload mapping.json V6 dulu. Error:", e)
else: st.caption("🗺️ Mapping ngumpet, klik tombol 🗺️ MAPPING PER BUYER kalau mau liat peta + maintenance!")

st.write("---")
st.markdown("**Game Ringan - 4 Item Saja:** IR 7 Detik di HP + Bio Health Ringkas + CCTV AI Ringkas + SaaS SCM Demo | **PTS Game:** Kanvas +5, Kontrak +30, Jualan +100 | **PTS Berbayar:** Super Secure / Infrared +200 (Batik TIDAK di game) | **Mapping:** Sesuai daerah penempatan Buyer, gampang maintenance per Buyer!")

def find_file(cands):
    try: files=os.listdir(".")
    except: files=[]
    lm={f.lower():f for f in files}
    for c in cands:
        if c in files: return c
        if c.lower() in lm: return lm[c.lower()]
    return None
def load_html(cands,label):
    f=find_file(cands)
    if f:
        with open(f,"r",encoding="utf-8") as fh: return fh.read()
    return f"<h3>{label} belum ketemu</h3>"

tab_classic, tab_neuro, tab_main = st.tabs(["🟦 20% CLASSIC - Game Ringan", "🟧 50% NEURO TRON - Observasi", "🟩 20% MAIN - Jalur Harian + MAPPING"])
with tab_classic:
    st.markdown("**CLASSIC (20%): Game Ringan, 4 Item Saja!** Kanvas, Bos, Kontrak, Teknisi, Jualan!")
    html=load_html(["index_Classic.html","index_classic.html"],"CLASSIC")
    st.components.v1.html(html,height=900,scrolling=True)
with tab_neuro:
    st.markdown("**NEURO TRON (50%): Observasi Mikrokontroler!** Tangan gerak -> IR detek! Gas -> MQ-135! Panas -> MLX90640! Dll!")
    html=load_html(["index_Neural.html","index_neural.html"],"NEURAL")
    st.components.v1.html(html,height=900,scrolling=True)
with tab_main:
    st.markdown("**MAIN (20%): Jalur Harian + MAPPING!** Hasil Observasi Jadi PTS + Level! Mapping per Buyer di sini! Klik tombol 🗺️ MAPPING di atas untuk liat peta!")
    html=load_html(["index.html","Index.html"],"MAIN")
    st.components.v1.html(html,height=900,scrolling=True)
st.caption("V6.1 - HUB Ringan TANPA BATIK + Mapping Per Buyer | Game = Promosi | Super Secure + Super Infrared = Berbayar | Batik DIHAPUS dari Game")
