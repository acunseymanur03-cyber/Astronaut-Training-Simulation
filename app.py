import streamlit as st
import time
import streamlit.components.v1 as components

st.set_page_config(page_title="NEURO-AURA Space Simulator", page_icon="🚀", layout="wide")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at center, #0B1021 0%, #03050C 100%); color: #E2E8F0; }
    .metric-card { background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(56, 189, 248, 0.4); padding: 18px; border-radius: 12px; text-align: center; }
    .stButton>button { background: linear-gradient(90deg, #0284c7 0%, #2563eb 100%); color: white; font-weight: bold; border-radius: 8px; padding: 10px 24px; }
    </style>
""", unsafe_allow_html=True)

st.title("🌌 NEURO-AURA: Interstellar 3D Flight & Training Engine")
st.markdown("### *NASA Space Apps Challenge - Advanced Simulation Suite*")

sim_mode = st.sidebar.selectbox("Eğitim Modu Seçin", [
    "🚀 3D Uzayda Seyahat",
    "🌐 Canlı Kokpit Paneli",
    "👨‍🚀 EVA Uzay Yürüyüşü",
    "☄️ Uzay Çöpü Kaçınma"
])

if sim_mode == "🚀 3D Uzayda Seyahat":
    st.subheader("🪐 Derin Uzay Navigasyon Simülatörü")
    
    # Tırnak hatasını önleyen güvenli HTML bileşeni
    space_html = "<div style='width:100%; height:450px; background:#000; border-radius:12px; display:flex; align-items:center; justify-content:center; border:1px solid #38bdf8;'><h2 style='color:#38bdf8; font-family:monospace;'>🚀 WARP SPEED ACTIVE: YILDIZLAR ARASI SEYAHAT EDİLİYOR...</h2></div>"
    components.html(space_html, height=470)
    
    speed = st.slider("Warp Hızı", 1, 10, 5)
    st.info(f"Mevcut İtki Seviyesi: {speed} Mach")

elif sim_mode == "🌐 Canlı Kokpit Paneli":
    st.subheader("📊 Astronot Sağlık & Yaşam Destek Paneli")
    c1, c2, c3 = st.columns(3)
    c1.markdown('<div class="metric-card"><h3>Kalp Atış</h3><h2>72 bpm</h2></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h3>Oksijen</h3><h2>99.8%</h2></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h3>Stres</h3><h2>%12</h2></div>', unsafe_allow_html=True)

elif sim_mode == "👨‍🚀 EVA Uzay Yürüyüşü":
    st.subheader("👨‍🚀 Uzay Yürüyüşü İtki Testi")
    power = st.slider("İtki Gücü (%)", 0, 100, 40)
    if st.button("İtki Uygula"):
        st.success(f"Başarılı! %{power} güçle manevra tamamlandı.")

else:
    st.subheader("☄️ Kriz Yönetimi")
    st.write("Radar uyarısı: Yüksek hızlı nesne yaklaşıyor!")
    if st.button("Otonom Kaçış Rotasını Başlat"):
        st.balloons()
        st.success("Manevra başarılı, araç güvenli bölgede!")
