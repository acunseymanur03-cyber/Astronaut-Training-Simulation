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
    st.subheader("🪐 Derin Uzay Navigasyon ve Yıldız Tarlası Simülatörü")
    
    # Hareketli yıldız simülasyonu HTML kodu
    star_html = """
    <div style="width:100%; height:480px; background:#000; border-radius:12px; overflow:hidden; position:relative; border:1px solid #38bdf8;">
        <div style="position:absolute; top:12px; left:12px; color:#00f0ff; font-family:monospace; background:rgba(0,0,0,0.75); padding:8px 12px; border-radius:6px; border:1px solid #00f0ff; z-index:10; font-size:13px;">
            🚀 WARP HIZI: AKTİF | Yıldızlar Arası Seyahat
        </div>
        <canvas id="sc"></canvas>
    </div>
    <script>
        const c = document.getElementById('sc');
        const x = c.getContext('2d');
        function resize() {
            c.width = c.parentElement.clientWidth;
            c.height = 480;
        }
        resize();
        window.onresize = resize;
        
        let num = 600;
        let arr = [];
        for(let i=0; i<num; i++) {
            arr.push({
                X: (Math.random() - 0.5) * c.width,
                Y: (Math.random() - 0.5) * c.height,
                Z: Math.random() * c.width
            });
        }
        function loop() {
            x.fillStyle = "rgba(3, 5, 12, 0.3)";
            x.fillRect(0, 0, c.width, c.height);
            let cx = c.width / 2;
            let cy = c.height / 2;
            for(let i=0; i<num; i++) {
                let s = arr[i];
                s.Z -= 3;
                if(s.Z <= 0) { s.Z = c.width; s.X = (Math.random() - 0.5) * c.width; s.Y = (Math.random() - 0.5) * c.height; }
                let k = 100.0 / s.Z;
                let px = s.X * k + cx;
                let py = s.Y * k + cy;
                if(px >= 0 && px <= c.width && py >= 0 && py <= c.height) {
                    let sz = (1 - s.Z / c.width) * 2.5;
                    x.fillStyle = "#38bdf8";
                    x.beginPath();
                    x.arc(px, py, sz < 0 ? 0 : sz, 0, Math.PI * 2);
                    x.fill();
                }
            }
            requestAnimationFrame(loop);
        }
        loop();
    </script>
    """
    components.html(star_html, height=500)
    
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
