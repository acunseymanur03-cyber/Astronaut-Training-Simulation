import streamlit as st
import time
import streamlit.components.v1 as components

# Sayfa Yapılandırması
st.set_page_config(
    page_title="NEURO-AURA: 3D Space Flight & Training Simulator",
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
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(56, 189, 248, 0.4);
        padding: 18px;
        border-radius: 12px;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.2);
        text-align: center;
    }
    .stButton>button {
        background: linear-gradient(90deg, #0284c7 0%, #2563eb 100%);
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 12px 28px;
        box-shadow: 0 0 15px rgba(37, 99, 235, 0.5);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #0ea5e9 0%, #3b82f6 100%);
        box-shadow: 0 0 30px rgba(56, 189, 248, 0.9);
    }
    </style>
""", unsafe_allow_html=True)

# Başlık
st.title("🌌 NEURO-AURA: Interstellar 3D Flight & Training Engine")
st.markdown("### *NASA Space Apps Challenge - Deep Space Exploration & Biometric Training Suite*")

# Yan Menü
st.sidebar.header("🕹️ Simülasyon Kontrol Merkezi")
sim_mode = st.sidebar.selectbox(
    "Eğitim & Seyahat Modu Seçin",
    [
        "🚀 3D Uzayda Seyahat (Interstellar Warp)",
        "🌐 Canlı Kokpit & Biyometrik Paneller",
        "👨‍🚀 EVA Uzay Yürüyüşü & İtki Testi",
        "☄️ Uzay Çöpü Kaçınma & Kriz Yönetimi"
    ]
)

if sim_mode == "🚀 3D Uzayda Seyahat (Interstellar Warp)":
    st.subheader("🪐 3D Derin Uzay Navigasyon Simülatörü")
    st.write("Aşağıdaki 3D simülatörde uzay boşluğundaki yıldız tarlasında canlı seyahat edebilirsin!")
    
    # HTML & Three.js 3D Yıldız Tarlası
    html_3d = """
    <div id="canvas-container" style="width:100%; height:500px; background:#000; border-radius:12px; overflow:hidden; position:relative;">
        <div style="position:absolute; top:10px; left:10px; color:#00f0ff; font-family:monospace; background:rgba(0,0,0,0.7); padding:8px 12px; border-radius:6px; border:1px solid #00f0ff;">
            🚀 WARP HIZI: ACTIVE | 3D Space Flight Simulation
        </div>
        <canvas id="starCanvas"></canvas>
    </div>

    <script>
        const canvas = document.getElementById('starCanvas');
        const ctx = canvas.getContext('2d');

        function resize() {
            canvas.width = canvas.parentElement.clientWidth;
            canvas.height = 500;
        }
        resize();

        const numStars = 800;
        const stars = [];

        for (let i = 0; i < numStars; i++) {
            stars.push({
                x: (Math.random() - 0.5) * canvas.width,
                y: (Math.random() - 0.5) * canvas.height,
                z: Math.random() * canvas.width,
                o: '0.' + Math.floor(Math.random() * 99) + 1
            });
        }

        function draw() {
            ctx.fillStyle = "rgba(3, 5, 12, 0.2)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            const cx = canvas.width / 2;
            const cy = canvas.height / 2;

            for (let i = 0; i < numStars; i++) {
                let star = stars[i];
                star.z -= 4;

                if (star.z <= 0) {
                    star.z = canvas.width;
                    star.x = (Math.random() - 0.5) * canvas.width;
                    star.y = (Math.random() - 0.5) * canvas.height;
                }

                let k = 128.0 / star.z;
                let px = star.x * k + cx;
                let py = star.y * k + cy;

                if (px >= 0 && px <= canvas.width && py >= 0 && py <= canvas.height) {
                    let size = (1 - star.z / canvas.width) * 2.5;
                    ctx.beginPath();
                    ctx.fillStyle = "#38bdf8";
                    ctx.arc(px, py, size, 0, Math.PI * 2);
                    ctx.fill();
                }
            }
            requestAnimationFrame(draw);
