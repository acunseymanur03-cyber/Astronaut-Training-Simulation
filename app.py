import streamlit as st
import time
import streamlit.components.v1 as components

st.set_page_config(page_title="NEURO-AURA: Ultimate 3D Space Suite", page_icon="🚀", layout="wide")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at center, #0B1021 0%, #03050C 100%); color: #E2E8F0; }
    .metric-card { background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(56, 189, 248, 0.4); padding: 20px; border-radius: 12px; text-align: center; box-shadow: 0 0 15px rgba(56, 189, 248, 0.2); }
    .stButton>button { background: linear-gradient(90deg, #0284c7 0%, #2563eb 100%); color: white; font-weight: bold; border-radius: 8px; padding: 12px 24px; box-shadow: 0 0 15px rgba(37, 99, 235, 0.5); }
    </style>
""", unsafe_allow_html=True)

st.title("🌌 NEURO-AURA: 3D Interactive Space & Mission Suite")
st.markdown("### *NASA Space Apps Challenge - 3D Immersive Simulation Engine*")

sim_mode = st.sidebar.selectbox("Simülasyon Modu Seçin", [
    "🪐 Güneş Sistemi, 8 Gezegen & Uydular (3D)",
    "🚀 3D Gerçek Zamanlı Roket Fırlatma Simülatörü",
    "🌐 3D Canlı Kokpit & EKG Biyometrik Monitör",
    "☄️ 3D Uzay Çöpü & Radar Kaçınma Simülatörü"
])

if sim_mode == "🪐 Güneş Sistemi, 8 Gezegen & Uydular (3D)":
    st.subheader("☀️ Güneş Sistemi, 8 Gezegen ve Uydular 3D Geçidi")
    speed_factor = st.slider("Simülasyon Hızı", 1, 30, 5)
    
    sol_html = f"""
    <div style="width:100%; height:520px; background:#000; border-radius:12px; overflow:hidden; position:relative; border:1px solid #38bdf8;">
        <div style="position:absolute; top:10px; left:10px; color:#00f0ff; font-family:monospace; background:rgba(0,0,0,0.85); padding:6px 10px; border-radius:6px; border:1px solid #00f0ff; z-index:10; font-size:12px;">
            ☀️ 3D GÜNEŞ SİSTEMİ | Hız: {speed_factor}x
        </div>
        <canvas id="scs"></canvas>
    </div>
    <script>
        const canvas = document.getElementById('scs');
        const ctx = canvas.getContext('2d');
        let speed = {speed_factor};
        function resize() {{ canvas.width = canvas.parentElement.clientWidth; canvas.height = 520; }}
        resize();
        window.onresize = resize;
        
        let stars = [];
        for(let i=0; i<800; i++) {{ stars.push({{ x: (Math.random()-0.5)*canvas.width, y: (Math.random()-0.5)*canvas.height, z: Math.random()*canvas.width }}); }}
        
        let bodies = [
            {{ x: -350, y: 0, r: 45, name: '☀️ Güneş', z: 600, c1: '#ffcc00', c2: '#ff3300', ring: false }},
            {{ x: -280, y: -40, r: 10, name: '☿ Merkür', z: 580, c1: '#b0b0b0', c2: '#505050', ring: false }},
            {{ x: -210, y: 50, r: 16, name: '♀ Venüs', z: 550, c1: '#e3bb76', c2: '#8c6724', ring: false }},
            {{ x: -140, y: -20, r: 18, name: '🜨 Dünya (+Ay)', z: 520, c1: '#38bdf8', c2: '#1d4ed8', ring: false }},
            {{ x: -70, y: 60, r: 14, name: '♂ Mars (+Phobos)', z: 490, color1: '#ff7b54', color2: '#933215', ring: false }},
            {{ x: 10, y: -50, r: 32, name: '♃ Jüpiter (+Europa)', z: 450, c1: '#e0ae6f', c2: '#8b5a2b', ring: false }},
            {{ x: 90, y: 40, r: 28, name: '♄ Saturn (+Titan & Halka)', z: 410, c1: '#fcd34d', c2: '#b45309', ring: true }},
            {{ x: 170, y: -30, r: 22, name: '♅ Uranüs', z: 370, c1: '#67e8f9', c2: '#0e7490', ring: false }},
            {{ x: 240, y: 40, r: 21, name: '♆ Neptün', z: 330, c1: '#3b82f6', c2: '#1e3a8a', ring: false }},
            {{ x: 310, y: -20, r: 8, name: '♇ Plüton', z: 300, c1: '#d1d5db', c2: '#4b5563', ring: false }}
        ];

        function draw() {{
            ctx.fillStyle = "rgba(3, 5, 12, 0.4)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            let cx = canvas.width / 2, cy = canvas.height / 2;
            
            for(let i=0; i<stars.length; i++) {{
                let s = stars[i];
                s.Z -= (speed * 0.5);
                if(s.Z <= 0) {{ s.Z = canvas.width; s.X = (Math.random()-0.5)*canvas.width; s.Y = (Math.random()-0.5)*canvas.height; }}
                let k = 100.0 / s.Z, px = s.X * k + cx, py = s.Y * k + cy;
                if(px >= 0 && px <= canvas.width && py >= 0 && py <= canvas.height) {{
                    ctx.fillStyle = "#fff"; ctx.fillRect(px, py, 1.5, 1.5);
                }}
            }}

            for(let j=0; j<bodies.length; j++) {{
                let b = bodies[j];
                b.z -= (speed * 0.25);
                if(b.z <= 30) b.z = 900;
                let bk = 150.0 / b.z, bpx = b.x * bk + cx, bpy = b.y * bk + cy, br = b.r * bk;
                if(br < 0) continue;

                if(b.ring) {{
                    ctx.save();
                    ctx.beginPath();
                    ctx.ellipse(bpx, bpy, br * 2.0, br * 0.6, Math.PI / 6, 0, Math.PI * 2);
                    ctx.strokeStyle = "rgba(245, 158, 11, 0.7)"; ctx.lineWidth = br * 0.25; ctx.stroke();
                    ctx.restore();
                }}

                let grad = ctx.createRadialGradient(bpx - br*0.3, bpy - br*0.3, br*0.1, bpx, bpy, br);
                grad.addColorStop(0, b.c1 || '#ffcc00'); grad.addColorStop(1, b.color2 || '#ff3300');
                ctx.beginPath(); ctx.arc(bpx, bpy, br, 0, Math.PI * 2); ctx.fillStyle = grad; ctx.fill();

                ctx.fillStyle = "#f1f5f9"; ctx.font = "bold 11px monospace";
                ctx.fillText(b.name, bpx + br + 8, bpy + 4);
            }}
            requestAnimationFrame(draw);
        }}
        draw();
    </script>
    """
    components.html(sol_html, height=540)

elif sim_mode == "🚀 3D Gerçek Zamanlı Roket Fırlatma Simülatörü":
    st.subheader("🚀 3D Canlı Roket Fırlatma & Atmosfer Tırmanış Simülasyonu")
    throttle = st.slider("Motor İtki Gücü (Throttle %)", 0, 100, 85)
    
    # 3D Roket Animasyon Kanvası
    rocket_html = f"""
    <div style="width:100%; height:450px; background:#000; border-radius:12px; overflow:hidden; position:relative; border:1px solid #38bdf8;">
        <div style="position:absolute; top:10px; left:10px; color:#00f0ff; font-family:monospace; background:rgba(0,0,0,0.85); padding:6px 10px; border-radius:6px; border:1px solid #00f0ff; z-index:10; font-size:12px;">
            🚀 ROKET FIRLATMA SİMÜLATÖRÜ | İtki: {throttle}%
        </div>
        <canvas id="rcanvas"></canvas>
    </div>
    <script>
        const rcanvas = document.getElementById('rcanvas');
        const rctx = rcanvas.getContext('2d');
        let throttleVal = {throttle};
        function rresize() {{ rcanvas.width = rcanvas.parentElement.clientWidth; rcanvas.height = 450; }}
        rresize();
        window.onresize = rresize;

        let rocketY = 320;
        let flameSize = throttleVal * 0.6;

        function rdraw() {{
            rctx.fillStyle = "rgba(3, 5, 12, 0.35)";
            rctx.fillRect(0, 0, rcanvas.width, rcanvas.height);
            let cx = rcanvas.width / 2;

            // Fırlatma Rampası
            rctx.fillStyle = "#334155";
            rctx.fillRect(cx - 50, 380, 100, 20);
            rctx.fillStyle = "#475569";
            rctx.fillRect(cx - 30, 360, 60, 20);

            // Roket Gövdesi (3D Efektli)
            let grad = rctx.createLinearGradient(cx - 15, 0, cx + 15, 0);
            grad.addColorStop(0, '#94a3b8'); grad.addColorStop(0.5, '#f8fafc'); grad.addColorStop(1, '#64748b');
            
            rctx.fillStyle = grad;
            rctx.beginPath();
            rctx.moveTo(cx, rocketY - 50);
            rctx.lineTo(cx - 15, rocketY);
            rctx.lineTo(cx - 15, rocketY + 60);
            rctx.lineTo(cx + 15, rocketY + 60);
            rctx.lineTo(cx + 15, rocketY);
            rctx.closePath();
            rctx.fill();

            // Roket Ucu (Koni)
            rctx.fillStyle = "#ef4444";
            rctx.beginPath();
            rctx.moveTo(cx, rocketY - 65);
            rctx.lineTo(cx - 15, rocketY - 50);
            rctx.lineTo(cx + 15, rocketY - 50);
            rctx.closePath();
            rctx.fill();

            // Roket Kanatları
            rctx.fillStyle = "#3b82f6";
            rctx.beginPath();
            rctx.moveTo(cx - 15, rocketY + 30);
            rctx.lineTo(cx - 28, rocketY + 65);
            rctx.lineTo(cx - 15, rocketY + 55);
            rctx.closePath();
            rctx.fill();

            rctx.beginPath();
            rctx.moveTo(cx + 15, rocketY + 30);
            rctx.lineTo(cx + 28, rocketY + 65);
            rctx.lineTo(cx + 15, rocketY + 55);
            rctx.closePath();
            rctx.fill();

            // Alevler ve Duman (İtki Gücüne Bağlı)
            if (throttleVal > 10) {{
                let fGrad = rctx.createRadialGradient(cx, rocketY + 70, 2, cx, rocketY + 85, flameSize);
                fGrad.addColorStop(0, '#fde047'); fGrad.addColorStop(0.5, '#f97316'); fGrad.addColorStop(1, 'transparent');
                rctx.fillStyle = fGrad;
                rctx.beginPath();
                rctx.arc(cx, rocketY + 75, flameSize, 0, Math.PI * 2);
                rctx.fill();
            }}

            // Yavaşça yukarı süzülme animasyonu
            if (rocketY > 120) {{
                rocketY -= (throttleVal * 0.015);
            }}

            requestAnimationFrame(rdraw);
        }}
        rdraw();
    </script>
    """
    components.html(rocket_html, height=470)
    
    if st.button("🔥 Tam Ateşleme Başlat"):
        st.success("🚀 Roket başarıyla yörüngeye fırlatıldı! İrtifa: 240 km.")
        st.balloons()

elif sim_mode == "🌐 3D Canlı Kokpit & EKG Biyometrik Monitör":
    st.subheader("📊 3D Kalp Ritmi (EKG) & Biyometrik Canlı Akış Monitörü")
    
    # 3D EKG ve Biyometrik Simülasyonu
