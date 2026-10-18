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
    "🚀 3D Gerçekçi Gezegen & Uzay Uçuşu",
    "🌐 Canlı Kokpit Paneli",
    "👨‍🚀 EVA Uzay Yürüyüşü",
    "☄️ Uzay Çöpü Kaçınma"
])

if sim_mode == "🚀 3D Gerçekçi Gezegen & Uzay Uçuşu":
    st.subheader("🪐 Fotogerçekçi Gezegen Geçişi & Derin Uzay Simülatörü")
    
    # Gerçekçi gradyanlı, gölgeli ve halkalı gezegenler simülasyonu
    realistic_space_html = """
    <div style="width:100%; height:500px; background:#000; border-radius:12px; overflow:hidden; position:relative; border:1px solid #38bdf8;">
        <div style="position:absolute; top:12px; left:12px; color:#00f0ff; font-family:monospace; background:rgba(0,0,0,0.85); padding:8px 12px; border-radius:6px; border:1px solid #00f0ff; z-index:10; font-size:13px;">
            🪐 FOTOGERÇEKÇİ GEZEGEN SİSTEMİ: AKTİF
        </div>
        <canvas id="rc"></canvas>
    </div>
    <script>
        const canvas = document.getElementById('rc');
        const ctx = canvas.getContext('2d');
        function resize() {
            canvas.width = canvas.parentElement.clientWidth;
            canvas.height = 500;
        }
        resize();
        window.onresize = resize;
        
        let stars = [];
        for(let i=0; i<600; i++) {
            stars.push({
                x: (Math.random() - 0.5) * canvas.width,
                y: (Math.random() - 0.5) * canvas.height,
                z: Math.random() * canvas.width
            });
        }
        
        // Detaylı ve Gerçekçi Gezegenler
        let planets = [
            { x: -160, y: -90, r: 50, name: 'Mars II (Terraforming)', z: 450, c1: '#ff7b54', c2: '#933215', ring: false },
            { x: 180, y: 110, r: 85, name: 'Saturnian Gas Giant', z: 700, c1: '#ffd369', c2: '#b38b24', ring: true },
            { x: -200, y: 140, r: 40, name: 'Kepler-452b (Oceanic)', z: 950, c1: '#00adb5', c2: '#003840', ring: false }
        ];

        function draw() {
            ctx.fillStyle = "rgba(2, 4, 10, 0.4)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            let cx = canvas.width / 2;
            let cy = canvas.height / 2;
            
            // Yıldızlar
            for(let i=0; i<stars.length; i++) {
                let s = stars[i];
                s.Z -= 2;
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

            // Gezegenler
            for(let j=0; j<planets.length; j++) {
                let p = planets[j];
                p.z -= 1.0;
                if(p.z <= 40) { p.z = 1000; }
                
                let pk = 160.0 / p.z;
                let ppx = p.x * pk + cx;
                let ppy = p.y * pk + cy;
                let pr = p.r * pk;
                
                if (pr < 0) continue;

                // Gezegen Halkası (Satürn Gibi)
                if(p.ring) {
                    ctx.save();
                    ctx.beginPath();
                    ctx.ellipse(ppx, ppy, pr * 1.8, pr * 0.5, Math.PI / 6, 0, Math.PI * 2);
                    ctx.strokeStyle = "rgba(218, 165, 32, 0.6)";
                    ctx.lineWidth = pr * 0.2;
                    ctx.stroke();
                    ctx.restore();
                }

                // 3D Küre Gradyanı (Işık ve Gölge Efekti)
                let grad = ctx.createRadialGradient(ppx - pr*0.3, ppy - pr*0.3, pr*0.1, ppx, ppy, pr);
                grad.addColorStop(0, p.c1);
                grad.addColorStop(1, p.c2);
                
                ctx.beginPath();
                ctx.arc(ppx, ppy, pr, 0, Math.PI * 2);
                ctx.fillStyle = grad;
                ctx.shadowBlur = 25;
                ctx.shadowColor = p.c1;
                ctx.fill();
                ctx.shadowBlur = 0;

                // Atmosfer Parlaması
                let atmos = ctx.createRadialGradient(ppx, ppy, pr * 0.9, ppx, ppy, pr * 1.2);
                atmos.addColorStop(0, 'rgba(56, 189, 248, 0.3)');
                atmos.addColorStop(1, 'rgba(56, 189, 248, 0)');
                ctx.beginPath();
                ctx.arc(ppx, ppy, pr * 1.2, 0, Math.PI * 2);
                ctx.fillStyle = atmos;
                ctx.fill();

                // Gezegen Etiketi
                ctx.fillStyle = "#f1f5f9";
                ctx.font = "bold 12px monospace";
                ctx.fillText(p.name, ppx + pr + 8, ppy);
            }

            requestAnimationFrame(draw);
        }
        draw();
    </script>
    """
    components.html(realistic_space_html, height=520)
    
    speed = st
