# app.py V7.0 - PRACTICAL APPLICATION - PUBLISH INFORMATION + PODCAST + NEURAL
# aichaliveret inteligent market infokan ke masyarakat.
# Alur: Neural -> Classic -> Publish Information -> Network
# Market menyeluruh, tidak dibedakan. Network: YouTube, TikTok, Facebook, Instagram, WhatsApp.
import streamlit as st, os
st.set_page_config(page_title="Practical Application - Publish Information, Podcast, Neural - aichaliveret", layout="wide")
st.markdown("""
<div style="background:linear-gradient(90deg,#00e676,#00e5ff,#7c4dff);color:#000;padding:14px;border-radius:12px;text-align:center">
<b>aichaliveret company - aichaliveret by meta.ai</b><br>
<b>Practical Application - SaaS System for Market Intelligence & Decision Support</b><br>
<b>aichaliveret inteligent market infokan ke masyarakat.</b><br>
<small>Link: asuveleikha-ai.github.io/super.ir.bio.secure-tools - Link ini terkoneksi ke peralatan mikrokontroler, dan link ini juga yang terkoneksi ke Ruang Simulasi Observasi Pasar kita.</small><br>
<b>Kalau suara di Streamlit terblokir, buka link GitHub Pages langsung - di sana suara 100% jalan. Di Streamlit, klik tombol No.1 AKTIFKAN SUARA dulu!</b>
</div>
""", unsafe_allow_html=True)

def load(fn):
    if os.path.exists(fn):
        with open(fn, "r", encoding="utf-8") as f:
            return f.read()
    return "<h3>File belum ketemu: " + fn + "</h3>"

st.markdown("**Market menyeluruh, tidak dibedakan:** Perumahan, Ruko, Toko, Outlet, Mall, Pasar, Minimarket, Supermarket, Sekolah, Departemen Pemerintah, dan Kementerian. Pejabat adalah bagian dari masyarakat yang sama. | **Network:** YouTube, TikTok, Facebook, Instagram, dll, juga WhatsApp - satu kesimpulan, banyak tempat tampil.")

tab_publish, tab_classic, tab_neural = st.tabs(["PUBLISH INFORMATION - Ringkasan & Kesimpulan (UTAMA)", "CLASSIC - Podcast Intelligent Market", "NEURAL - Ruang Rakit, Observasi, Prediksi"])

with tab_publish:
    st.markdown("**Modul 3 - Publish Information:** Tempat kita meringkas dan memberikan kesimpulan observasi dari Neural, sebagai inteligent penelitian dan evaluasi terhadap pantauan observasi alat-alat mikrokontroler Super Secure dan Super Infrared.")
    st.components.v1.html(load("index.html"), height=5200, scrolling=True)

with tab_classic:
    st.markdown("**Modul 2 - Classic: Podcast Intelligent Market.** Tempat kita membawakan acara dan memberitakan hasil observasi atas alat-alat kita.")
    st.components.v1.html(load("index_classic.html"), height=4200, scrolling=True)

with tab_neural:
    st.markdown("**Modul 1 - Neural: Ruang Rakit, Observasi, dan Prediksi.** Tempat kita merakit, menyimak, memahami, memprediksi seluruh deteksi dan sensor. Mapping spesifik, terkoordinasi, jelas, detail alamat, terdeteksi aktif bila terhubung dan sensor, sehingga terpantau, terkendali, dan bisa maintenance sebagai layanan purna jual. Alat test: Multimeter Tester, Tester Sinyal WiFi, Tester Sensor, Tester Baterai / Daya.")
    html_n = load("index_neural.html") if os.path.exists("index_neural.html") else load("index_Neural.html")
    st.components.v1.html(html_n, height=5200, scrolling=True)

st.caption("V7.0 - Practical Application - Publish Information + Podcast + Neural. Template Kesimpulan 5 Bagian: Apa yang diobservasi, Apa yang terverifikasi, Apa yang belum diketahui, Apa risikonya, Apa skenario dan keputusan yang bisa diambil. Alur: Neural -> Classic -> Publish Information -> Network. Tidak ada kesimpulan yang dipublikasikan sebelum terverifikasi di Neural.")
