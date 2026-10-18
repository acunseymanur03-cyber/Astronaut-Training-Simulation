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
    "🚀 3D Uzay, Yıldızlar ve Gezegenler",
    "🌐 Canlı Kokpit Paneli",
    "👨‍🚀 EVA Uzay Yürüyüşü",
    "☄️ Uzay Çöpü Kaçınma"
])

if sim_mode == "🚀 3D Uzay, Yıldızlar ve Gezegenler":
    st.subheader("🪐 Derin Uzay, Yıldız Tarlası ve Gezegen Geçiş Simülatörü")
    
    # Yıldızlar ve Gezegenleri birlikte gösteren gelişmiş HTML/JS simülasyonu
    planet_space_html = """
    <div style="width:100%; height:500px; background:#000; border-radius:12px; overflow:hidden; position:relative; border:1px solid #38bdf8;">
        <div style="position:absolute; top:12px; left:12px; color:#00f0ff; font-family:monospace; background:rgba(0,0,0,0.8); padding:8px 12px; border-radius:6px; border:1px solid #00f0ff; z-index:10; font-size:13px;">
            🪐 GEZEGEN GEÇİŞİ: AKTİF | Yıldızlar ve Gezegenler
        </div>
        <canvas id="pc"></canvas>
    </div>
    <script>
        const canvas = document.getElementById('pc');
        const ctx = canvas.getContext('2d');
        function resize() {
            canvas.width = canvas.parentElement.clientWidth;
            canvas.height = 500;
        }
        resize();
        window.onresize = resize;
        
        let stars = [];
        for(let i=0; i<500; i++) {
            stars.push({
                x: (Math.random() - 0.5) * canvas.width,
                y: (Math.random() - 0.5) * canvas.height,
                z: Math.random() * canvas.width
            });
        }
        
        // Gezegenler
        let planets = [
            { x: -150, y: -80, radius: 45, color: '#ff4500', name: 'Mars II', z: 400 },
            { x: 200, y: 100, radius: 70, color: '#38bdf8', name: 'Gas Giant Alpha', z: 600 },
            { x: -220, y: 150, radius: 35, color: '#eab308', name: 'Exoplanet Kepler', z: 800 }
        ];

        function draw() {
            ctx.fillStyle = "rgba(3, 5, 12, 0.35)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            let cx = canvas.width / 2;
            let cy = canvas.height / 2;
            
            // Yıldızları çiz
            for(let i=0; i<stars.length; i++) {
                let s = stars[i];
                s.Z -= 2.5;
                if(s.Z <= 0) { s.Z = canvas.width; s.X = (Math.random() - 0.5) * canvas.width; s.Y = (Math.random() - 0.5) * canvas.height; }
                let k = 100.0 / s.Z;
                let px = s.X * k + cx;
                let py = s.Y * k + cy;
                if(px >= 0 && px <= canvas.width && py >= 0 && py <= canvas.height) {
                    let sz = (1 - s.Z / canvas.width) * 2;
                    ctx.fillStyle = "#ffffff";
                    ctx.beginPath();
                    ctx.arc(px, py, sz < 0 ? 0 : sz, 0, Math.PI * 2);
                    ctx.fill();
                }
            }

            // Gezegenleri çiz ve hareket ettir
            for(let j=0; j<planets.length; j++) {
                let p = planets[j];
                p.z -= 1.2;
                if(p.z <= 50) { p.z = 900; }
                
                let pk = 150.0 / p.z;
                let ppx = p.x * pk + cx;
                let ppy = p.y * pk + cy;
                let pradius = p.radius * pk;
                
                ctx.beginPath();
                ctx.arc(ppx, ppy, pradius < 0 ? 0 : pradius, 0, Math.PI * 2);
                ctx.fillStyle = p.color;
                ctx.shadowBlur = 20;
                ctx.shadowColor = p.color;
                ctx.fill();
                ctx.shadowBlur = 0; // reset shadow
                
                // Gezegen İsmi
                ctx.fillStyle = "#e2e8f0";
                ctx.font = "12px monospace";
                ctx.fillText(p.name, ppx + pradius + 5, ppy);
            }

            requestAnimationFrame(draw);
        }
        draw();
    </script>
    """
    components.html(planet_space_html, height=520)
    
    speed = st.slider("Warp Motor Hızı", 1, 10, 5)
    target = st.selectbox("Yörünge Hedefi", ["Mars II Kolonisi", "Gas Giant Alpha", "Exoplanet Kepler Sistemi"])
    st.info(f"📍 Rota: **{target}** | Hız: **{speed} Mach**")

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
