import streamlit as st
import time

st.set_page_config(page_title="NEURO-AURA: Space Suite", page_icon="🚀", layout="wide")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at center, #0B1021 0%, #03050C 100%); color: #E2E8F0; }
    .metric-card { background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(56, 189, 248, 0.4); padding: 20px; border-radius: 12px; text-align: center; box-shadow: 0 0 15px rgba(56, 189, 248, 0.2); }
    .stButton>button { background: linear-gradient(90deg, #0284c7 0%, #2563eb 100%); color: white; font-weight: bold; border-radius: 8px; padding: 12px 24px; box-shadow: 0 0 15px rgba(37, 99, 235, 0.5); width: 100%; }
    </style>
""", unsafe_allow_html=True)

st.title("🌌 NEURO-AURA: 3D Interactive Space & Mission Suite")
st.markdown("### *NASA Space Apps Challenge - Astronot Eğitim & Simülasyon Sistemi*")

sim_mode = st.sidebar.selectbox("Simülasyon Modu Seçin", [
    "🪐 Güneş Sistemi & Gezegenler",
    "🚀 Roket Fırlatma Simülatörü",
    "🌐 Canlı Kokpit & EKG Monitör",
    "🏅 NASA Astronot Eğitim & Rozet Merkezi",
    "☄️ Uzay Çöpü & Radar Takibi",
    "🛰️ Sistem Durumu & AI Asistanı"
])

if sim_mode == "🪐 Güneş Sistemi & Gezegenler":
    st.subheader("☀️ Güneş Sistemi ve 8 Gezegen Modülü")
    speed = st.slider("Simülasyon Hızı", 1, 30, 5)
    st.info("🪐 Güneş, 8 ana gezegen ve uydularının yörünge simülasyon motoru aktif.")
    col1, col2, col3, col4 = st.columns(4)
    col1.markdown('<div class="metric-card"><h4>Merkür & Venüs</h4><p>İç Yörünge</p></div>', unsafe_allow_html=True)
    col2.markdown('<div class="metric-card"><h4>Dünya & Ay</h4><p>Yaşam Kuşağı</p></div>', unsafe_allow_html=True)
    col3.markdown('<div class="metric-card"><h4>Mars & Jüpiter</h4><p>Dış Yörünge</p></div>', unsafe_allow_html=True)
    col4.markdown('<div class="metric-card"><h4>Satürn & Diğerleri</h4><p>Derin Uzay</p></div>', unsafe_allow_html=True)

elif sim_mode == "🚀 Roket Fırlatma Simülatörü":
    st.subheader("🚀 Profesyonel Roket Fırlatma & Atmosfer Tırmanışı")
    throttle = st.slider("Motor İtki Gücü (Throttle %)", 0, 100, 90)
    st.markdown(f"Mevcut İtki Gücü: **%{throttle}** - Ateşlemeye hazır.")
    if st.button("🔥 Tam Güç Ateşleme Yap"):
        with st.spinner("Roket ateşleniyor ve atmosfer katmanları geçiliyor..."):
            time.sleep(1.5)
        st.success("🚀 Roket başarıyla yörüngeye yerleşti! İrtifa: 320 km.")
        st.balloons()

elif sim_mode == "🌐 Canlı Kokpit & EKG Monitör":
    st.subheader("📊 Biyometrik Canlı Akış ve Kokpit Monitörü")
    c1, c2, c3 = st.columns(3)
    c1.markdown('<div class="metric-card"><h3>❤️ Kalp Ritmi</h3><h2>74 bpm</h2></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h3>🧪 Kabin Oksij
