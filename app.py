# app.py V6.7 - MAPPING + GPS TERPANTAU - TOMBOL + VOICE DI DALAM GAME
import streamlit as st, os
st.set_page_config(page_title="Practical Application Game V6.7 - MAPPING + GPS TERPANTAU - Tombol + Voice Aktif", layout="wide")
st.markdown("""
<div style="background:linear-gradient(90deg,#ff7a00,#ffeb3b,#00e676);color:#000;padding:12px;border-radius:12px;text-align:center">
<b>🎮 V6.7 - MAPPING + GPS TERPANTAU - TOMBOL + VOICE AKTIF!</b><br>
<small>Link: asuveleikha-ai.github.io/practicalaplication_gamesupersecure_tools - Link ini terkoneksi ke peralatan mikrokontroler, dan link ini juga yang terkoneksi ke game simulasi real ini.</small><br>
<b>⚠️ Kalau suara di Streamlit ke-blokir, buka link GitHub langsung (GitHub Pages) - di sana suara 100% jalan! Di Streamlit, klik tombol No.1 AKTIFKAN SUARA dulu!</b>
</div>
""", unsafe_allow_html=True)
def load(fn):
    if os.path.exists(fn):
        with open(fn, "r", encoding="utf-8") as f: return f.read()
    return "<h3>File belum ketemu</h3>"
tab_main, tab_classic, tab_neuro = st.tabs(["🟩 MAIN - GAME DI DEPAN (UTAMA)", "🟦 CLASSIC 20%", "🟧 NEURAL 50% - PANEL OBSERVASI"])
with tab_main:
    st.components.v1.html(load("index.html"), height=4200, scrolling=True)
with tab_classic:
    st.components.v1.html(load("index_classic.html"), height=4200, scrolling=True)
with tab_neuro:
    st.markdown("**NEURAL - Ruang Observasi Super Secure + Super Infrared - TANPA Tombol Game! Game cuma di MAIN!**")
    html_n = load("index_neural.html") if os.path.exists("index_neural.html") else load("index_Neural.html")
    st.components.v1.html(html_n, height=4600, scrolling=True)
st.caption("V6.7 - MAPPING + GPS TERPANTAU - Tombol game di dalam panel game + Voice Recorder di dalam panel game, semua tombol langsung bersuara! Kalau suara di Streamlit ke-blokir, buka link GitHub langsung!")
