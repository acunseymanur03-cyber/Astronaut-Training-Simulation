import streamlit as st
import time
import random

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Astronaut Training Simulation - 3D Neural Suite",
    page_icon="🚀",
    layout="wide"
)

# Özel CSS ile Gece/Uzay Teması ve Neon Efektleri
st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at center, #0B1021 0%, #03050C 100%);
        color: #E2E8F0;
    }
    .metric-card {
        background: rgba(15, 23, 42, 0.75);
        border: 1px solid rgba(56, 189, 248, 0.3);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.15);
        text-align: center;
    }
    .stButton>button {
        background: linear-gradient(90deg, #0284c7 0%, #2563eb 100%);
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        box-shadow: 0 0 15px rgba(37, 99, 235, 0.4);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #0ea5e9 0%, #3b82f6 100%);
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.8);
    }
    </style>
""", unsafe_allow_html=True)

# Başlık ve 3D Hissiyatı Veren Görsel Banner
st.title("🌌 NEURO-AURA: 3D Astronaut Cognitive Training Suite")
st.markdown("### *NASA Space Apps Challenge - Advanced Zero-G & Stress Simulation Engine*")

# Yan Menü
st.sidebar.header("🕹️ Simülasyon Kontrol Paneli")
sim_mode = st.sidebar.selectbox(
    "Mod Seçimi",
    [
        "🚀 3D Kokpit & Biyometrik Takip",
        "⚖️ Yerçekimsiz Ortam (Zero-G) Denge Simülasyonu",
        "🚨 Acil Durum & Kriz Yönetim Simülatörü"
    ]
)

if sim_mode == "🚀 3D Kokpit & Biyometrik Takip":
    st.subheader("🌐 Canlı Uzay İstasyonu & Biyometrik Veri Akışı")
    
    # 3D Uzay Görseli Efekti
    st.image(
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop",
        caption="NASA Uzay İstasyonu Canlı Yörünge Görünümü",
        use_container_width=True
    )
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-card"><h3>❤️ Kalp Atış Hızı</h3><h2>74 bpm</h2><p style="color:#38bdf8;">Optimum Seviye</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>🧪 Kabin Oksijeni</h3><h2>99.4%</h2><p style="color:#4ade80;">Stabil Basınç</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h3>🧠 Bilişsel Yük</h3><h2>Düşük</h2><p style="color:#38bdf8;">Odak %98</p></div>', unsafe_allow_html=True)

elif sim_mode == "⚖️ Yerçekimsiz Ortam (Zero-G) Denge Simülasyonu":
    st.subheader("⚖️ Yerçekimsiz Ortamda Denge ve Oryantasyon Testi")
    st.write("Uzay boşluğunda yön bulma yeteneğini test eden 3D simülasyon motorunu çalıştırın.")
    
    gravity_level = st.slider("Simüle Edilen Yerçekimi Katsayısı (G)", 0.0, 1.0, 0.05)
    
    if st.button("🔄 3D Denge Kalibrasyonunu Başlat"):
        with st.spinner("Nöral ağlar ve jiroskopik sensörler kalibre ediliyor..."):
            time.sleep(2.5)
        st.success(f"✅ Kalibrasyon Başarılı! {gravity_level}G seviyesinde uzay yürüyüşü dengesi sağlandı.")
        st.balloons()

else:
    st.subheader("🚨 Acil Durum & Kriz Yönetim Simülatörü")
    st.write("Senaryo: Güneş fırtınası kaynaklı radyoaktif dalgalanma ve ana panel arızası!")
    
    crisis_action = st.radio(
        "Acil Durum Stratejisini Seçin:",
        [
            "Kalkanları aktifleştir ve acil sığınma bölmesine geç",
            "Yapay zeka (Lidya) destekli otomatik onarım protokolünü çalıştır",
            "Manuel oksijen regülasyonunu devreye sok"
        ]
    )
    
    if st.button("⚡ Krizi Yönet"):
        with st.spinner("Kriz senaryosu simüle ediliyor..."):
            time.sleep(2)
        st.error("⚠️ Simülasyon Sonucu: Sinyal bozulması önlendi, rota güvenli bölgeye sabitlendi!")
