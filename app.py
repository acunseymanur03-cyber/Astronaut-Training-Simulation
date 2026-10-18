import streamlit as st
import time

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Astronaut Training Simulation",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Astronaut Training & Cognitive Stress Simulator")
st.markdown("### NASA Space Apps Challenge - Adaptive Mission Control Suite")

# Kenar Çubuğu (Sidebar) - Eğitim Modları
st.sidebar.header("🎛️ Simülasyon Kontrol Paneli")
sim_mode = st.sidebar.selectbox(
    "Eğitim Modunu Seçin",
    [
        "Genel Durum & Biyometrik Takip",
        "Kritik Oksijen & Yaşam Destek",
        "Bilişsel Reaksiyon & Stres Testi"
    ]
)

if sim_mode == "Genel Durum & Biyometrik Takip":
    st.subheader("📊 Anlık Astronot Biyometrik Paneli")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Kalp Atış Hızı (HR)", value="78 bpm", delta="-2 bpm")
    with col2:
        st.metric(label="Kabin İçi Oksijen", value="98.2%", delta="+0.4%")
    with col3:
        st.metric(label="Bilişsel Stres Seviyesi", value="Düşük (Optimum)", delta="-5%")
        
    st.info("💡 Sistemler stabil çalışıyor. Astronot adayı göreve tamamen hazır.")

elif sim_mode == "Kritik Oksijen & Yaşam Destek":
    st.subheader("🧪 Yaşam Destek Ünitesi Simülasyonu")
    oxygen_slider = st.slider("Oksijen Basınç Simülasyonu (%)", 0, 100, 90)
    
    if oxygen_slider < 40:
        st.error("🚨 KRİTİK ALARM: Oksijen seviyesi tehlikeli sınırın altında! Acil maske protokolü devreye giriyor.")
    elif oxygen_slider < 70:
        st.warning("⚠️ UYARI: Oksijen oranında düşüş gözleniyor. Filtreleri kontrol edin.")
    else:
        st.success("✅ Yaşam destek sistemleri nominal düzeyde.")

else:
    st.subheader("🧠 Bilişsel Reaksiyon & Acil Durum Kriz Testi")
    st.write("Senaryo: Görev sırasında ani basınç kaybı ve ana bilgisayar arızası algılandı.")
    
    decision = st.radio(
        "İlk hamle olarak ne yapmalısın?",
        [
            "Yedek jeneratörü devreye sokup ana vanayı kapat",
            "Merkezi yapay zeka asistanına bağlanarak otomatik yama iste",
            "Kilitli tahliye bölmesine geçiş yap"
        ]
    )
    
    if st.button("Kararı Test Et"):
        with st.spinner("Simülasyon sonuçları analiz ediliyor..."):
            time.sleep(2)
        st.balloons()
        st.success(f"Seçilen strateji başarıyla uygulandı: **{decision}**. Görev güvenle sürdürülüyor!")
