import streamlit as st
import time

st.set_page_config(page_title="NEURO-AURA: Space Suite", page_icon="🚀", layout="wide")

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
    with col1:
        st.metric("Merkür & Venüs", "İç Yörünge", "Stabil")
    with col2:
        st.metric("Dünya & Ay", "Yaşam Kuşağı", "1.0 AU")
    with col3:
        st.metric("Mars & Jüpiter", "Dış Yörünge", "Kuşak Aktif")
    with col4:
        st.metric("Satürn & Diğerleri", "Derin Uzay", "Uzak Mesafe")

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
    with c1:
        st.metric("Kalp Ritmi", "74 bpm", "-2 bpm")
    with c2:
        st.metric("Kabin Oksijeni", "99.7%", "Normal")
    with c3:
        st.metric("Nöro-Stres", "%10", "Stabil")
    st.success("Tüm yaşam desteği sensörleri normal değerlerde çalışıyor.")

elif sim_mode == "🏅 NASA Astronot Eğitim & Rozet Merkezi":
    st.subheader("🏅 NASA Astronot Uzmanlık Eğitimi & Rozet Merkezi")
    st.write("Görev simülasyonlarını tamamlayarak resmi uzmanlık rozetlerini kazanın!")

    if "badges" not in st.session_state:
        st.session_state.badges = {"zero_g": False, "eva": False, "nav": False}
    if "zg_score" not in st.session_state:
        st.session_state.zg_score = 0
    if "eva_score" not in st.session_state:
        st.session_state.eva_score = 0
    if "nav_score" not in st.session_state:
        st.session_state.nav_score = 0

    st.markdown("---")
    
    c_zg1, c_zg2 = st.columns([2, 1])
    with c_zg1:
        st.markdown("#### 🛸 Görev 1: Sıfır Yerçekimi (Zero-G) Denge Testi")
        st.progress(st.session_state.zg_score / 100)
    with c_zg2:
        if st.button("⚖️ Dengele (+34 Puan)", key="zg_btn"):
            st.session_state.zg_score = min(100, st.session_state.zg_score + 34)
            if st.session_state.zg_score >= 100:
                st.session_state.badges["zero_g"] = True
                st.success("Zero-G Rozeti Kazanıldı!")

    st.markdown("---")

    c_ev1, c_ev2 = st.columns([2, 1])
    with c_ev1:
        st.markdown("#### 🛰️ Görev 2: ISS Uzay Yürüyüşü (EVA) Panel Tamiri")
        st.progress(st.session_state.eva_score / 100)
    with c_ev2:
        if st.button("🔧 Kabloları Bağla (+50 Puan)", key="eva_btn"):
            st.session_state.eva_score = min(100, st.session_state.eva_score + 50)
            if st.session_state.eva_score >= 100:
                st.session_state.badges["eva"] = True
                st.success("EVA Rozeti Kazanıldı!")

    st.markdown("---")

    c_nv1, c_nv2 = st.columns([2, 1])
    with c_nv1:
        st.markdown("#### 🪐 Görev 3: Derin Uzay Navigasyon Rotası")
        st.progress(st.session_state.nav_score / 100)
    with c_nv2:
        if st.button("🧭 Koordinat Kilitle (+50 Puan)", key="nav_btn"):
            st.session_state.nav_score = min(100, st.session_state.nav_score + 50)
            if st.session_state.nav_score >= 100:
                st.session_state.badges["nav"] = True
                st.success("Deep Space Rozeti Kazanıldı!")

    st.markdown("---")
    st.markdown("### 🏅 Rozet Panonuz")
    b1, b2, b3 = st.columns(3)
    b1.metric("Zero-G Master", "Kazanıldı ✅" if st.session_state.badges["zero_g"] else "Kilitli 🔒")
    b2.metric("EVA Specialist", "Kazanıldı ✅" if st.session_state.badges["eva"] else "Kilitli 🔒")
    b3.metric("Deep Space Commander", "Kazanıldı ✅" if st.session_state.badges["nav"] else "Kilitli 🔒")

elif sim_mode == "☄️ Uzay Çöpü & Radar Takibi":
    st.subheader("☄️ Uzay Çöpü Radar & Çarpışma Önleme Modülü")
    st.info("📡 Radar taraması aktif. Çevredeki yörünge kalıntıları taranıyor.")
    if st.button("🚨 Otonom Kaçış Manevrasını Başlat"):
        st.balloons()
        st.success("Başarılı! RDP itki sistemleri devreye girerek uzay çöpünden kaçındı.")

else:
    st.subheader("🛰️ Sistem Durumu & AI Asistanı")
    st.info("🟢 **ISS Konum Durumu:** Yörüngede Aktif (İrtifa: 418 km)")
    user_q = st.text_input("Sorunuz:", "Kabin basıncı düşerse acil prosedür nedir?")
    if st.button("Asistana Sor"):
        st.success("🤖 **Yanıt:** Kabin basıncı düşerse: 1. Oksijen maskelerini otomatik takın. 2. Sızdırmazlık vanalarını kapatın.")
