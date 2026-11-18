# app.py V6.4 - GAME DI DEPAN, PENJELASAN DI KOTAK KECIL, SUARA SEMUA, NEURAL ADA PANEL
import streamlit as st, os
st.set_page_config(page_title="Practical Application Game V6.4 - GAME DI DEPAN", layout="wide")
st.markdown("""
<div style="background:linear-gradient(90deg,#ff7a00,#ffeb3b,#00e676);color:#000;padding:12px;border-radius:12px;text-align:center">
<b>🎮 PRACTICAL APPLICATION GAME V6.4 - GAME DI DEPAN!</b><br>
<small>Link: asuveleikha-ai.github.io/practicalaplication_gamesupersecure_tools - Link ini terkoneksi ke peralatan mikrokontroler, dan link ini juga yang terkoneksi ke game simulasi real ini.</small>
</div>
""", unsafe_allow_html=True)
def load(fn):
    if os.path.exists(fn):
        with open(fn, "r", encoding="utf-8") as f: return f.read()
    return "<h3>File belum ketemu</h3>"
# Game di depan langsung, tanpa tab panjang - tapi tetap ada 3 tab di bawah untuk Classic / Neural / Main
tab_main, tab_classic, tab_neuro = st.tabs(["🟩 MAIN - GAME DI DEPAN (UTAMA)", "🟦 CLASSIC 20%", "🟧 NEURAL 50% - PANEL OBSERVASI"])
with tab_main:
    st.components.v1.html(load("index.html"), height=3400, scrolling=True)
with tab_classic:
    st.components.v1.html(load("index_classic.html"), height=3400, scrolling=True)
with tab_neuro:
    st.markdown("**NEURAL - Panel Kontrol Observasi Otomasi ada di atas game! Link GitHub Ai Chaliveret terkoneksi di sini!**")
    # Cari file neural lowercase dulu, baru capital
    html = load("index_neural.html") if os.path.exists("index_neural.html") else load("index_Neural.html")
    st.components.v1.html(html, height=3800, scrolling=True)
st.caption("V6.4 - GAME DI DEPAN | Penjelasan di Kotak Kecil | Link GitHub Ai Chaliveret terkoneksi ke peralatan mikrokontroler + ke game simulasi real ini | Batik Dihapus dari Game | Suara: Klik SUARAKAN SEMUA, besok koreksi lagi!")
