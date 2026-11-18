# app.py V6.3 - GAME DULU, TANPA KONEKSI KE DEMO STREAMLIT - SATU LEMBAR
import streamlit as st, os
st.set_page_config(page_title="Practical Application Game V6.3 - GAME DULU + SATU LEMBAR", layout="wide")
st.markdown("""
<div style="background:linear-gradient(90deg,#ff7a00,#ffeb3b,#00e676);color:#000;padding:12px;border-radius:12px;text-align:center">
<b>🎮 PRACTICAL APPLICATION GAME V6.3 - GAME DULU! JANGAN KONEKSI DULU KE DEMO STREAMLIT!</b><br>
<small>Game dulu di lembar ini! Batik 8in1 Dihapus dari Game, Pisah Total! Sistem terpasang nanti di Server, baru game dikoneksikan ke sistem, di Server!</small>
</div>
""", unsafe_allow_html=True)
st.caption("Satu lembar penjelasan di bawah ini menjawab: Di mana sistem disimpan? Di mana prototipe disimpan? Di mana pabrik autonomous? Di mana game dikoneksikan nanti? - Semua dalam satu lembar!")
# Load satu_lembar.html kalau ada, kalau nggak ada load index.html
def load():
    for fn in ["satu_lembar.html", "index.html"]:
        if os.path.exists(fn):
            with open(fn, "r", encoding="utf-8") as f: return f.read()
    return "<h3>File game belum ketemu</h3>"
html = load()
st.components.v1.html(html, height=3200, scrolling=True)
st.caption("V6.3 - GAME DULU | GitHub = Lemari Kode | Server = Tempat Sistem Terpasang + Tempat Koneksi | Play Store = Toko Download | Prototipe = Di Lokasi Buyer + Firmware di ESP32 | Pabrik Autonomous = Pisah Total | Game dikoneksikan nanti, di Server, setelah sistem terpasang!")
