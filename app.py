import streamlit as st
import time
import streamlit.components.v1 as components

st.set_page_config(page_title="NEURO-AURA: Ultimate Space Suite", page_icon="🚀", layout="wide")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at center, #0B1021 0%, #03050C 100%); color: #E2E8F0; }
    .metric-card { background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(56, 189, 248, 0.4); padding: 20px; border-radius: 12px; text-align: center; box-shadow: 0 0 15px rgba(56, 189, 248, 0.2); }
    .stButton>button { background: linear-gradient(90deg, #0284c7 0%, #2563eb 100%); color: white; font-weight: bold; border-radius: 8px; padding: 12px 24px; box-shadow: 0 0 15px rgba(37, 99, 235, 0.5); }
    </style>
""", unsafe_allow_html=True)

st.title("🌌 NEURO-AURA: Solar System & Advanced Rocket Simulation")
st.markdown("### *NASA Space Apps Challenge - Comprehensive Flight & Orbital Suite*")

sim_mode = st.sidebar.selectbox("Simülasyon Modu Seçin", [
    "🪐 Güneş Sistemi, 8 Gezegen, Uydular & Yıldızlar",
    "🚀 Gerçek Fiziksel Roket Fırlatma Simülatörü",
    "🌐 Canlı Kokpit & Biyometrik Monitör",
    "☄️ Uzay Çöpü & Kriz Yönetim Merkezi"
])

if sim_mode == "🪐 Güneş Sistemi, 8 Gezegen, Uydular & Yıldızlar":
    st.subheader("☀️ Güneş, 8 Gezegen, Cüce Gezegenler ve Uydular Geçidi")
    st.write("Güneş'ten Plüton'a kadar tüm sistem hız kontrolüyle akıyor.")
    
    speed_factor = st.slider("Simülasyon / Warp Hızı", min_value=1, max_value=30, value=5)
    
    sol_html = """
    <div style="width:100%; height:540px; background:#000; border-radius:12px; overflow:hidden; position:relative; border:1px solid #38bdf8;">
        <div style="position:absolute; top:10px; left:10px; color:#00f0ff; font-family:monospace; background:rgba(0,0,0,0.85); padding:6px 10px; border-radius:6px; border:1px solid #00f0ff; z-index:10; font-size:12px;">
            ☀️ GÜNEŞ SİSTEMİ & UYDULAR
        </div>
        <canvas id="scs"></canvas>
    </div>
    <script>
        const canvas = document.getElementById('scs');
        const ctx = canvas.getContext('2d');

        function resize() {
            canvas.width = canvas.parentElement.clientWidth;
            canvas.height = 540;
        }
        resize();
        window.onresize = resize;
        
        let stars = [];
        for(let i=0; i<800; i++) {
            stars.push({
                x: (Math.random() - 0.5) * canvas.width,
                y: (Math.random() - 0.5) * canvas.height,
                z: Math.random() * canvas.width
            });
        }
        
        let bodies = [
            { x: -350, y: 0, r: 45, name: '☀️ Güneş', z: 600, color1: '#ffcc00', color2: '#ff3300', ring: false },
            { x: -280, y: -40, r: 10, name: '☿ Merkür', z: 580, color1: '#b0b0b0', color2: '#505050', ring: false },
            { x: -210, y: 50, r: 16, name: '♀ Venüs', z: 550, color1: '#e3bb76', color2: '#8c6724', ring: false },
            { x: -140, y: -20, r: 18, name: '🜨 Dünya (+Ay)', z: 520, color1: '#38bdf8', color2: '#1d4ed8', ring: false },
            { x: -70, y: 60, r: 14, name: '♂ Mars (+Phobos)', z: 490, color1: '#ff7b54', color2: '#933215', ring: false },
            { x: 10, y: -50, r: 32, name: '♃ Jüpiter (+Europa)', z: 450, color1: '#e0ae6f', color2: '#8b5a2b', ring: false },
            { x: 90, y: 40, r: 28, name: '♄ Saturn (+Titan & Halka)', z: 410, color1: '#fcd34d', color2: '#b45309', ring: true },
            { x: 170, y: -30, r: 22, name: '♅ Uranüs', z: 370, color1: '#67e8f9', color2: '#0e7490', ring: false },
            { x: 240, y: 40, r: 21, name: '♆ Neptün', z: 330, color1: '#3b82f6', color2: '#1e3a8a', ring: false },
            { x: 310, y: -20, r: 8, name: '♇ Plüton', z: 300, color1: '#d1d5db', color2: '#4b5563', ring: false }
        ];

        function draw() {
            ctx.fillStyle = "rgba(3, 5, 12, 0.4)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            let cx = canvas.width / 2;
            let cy = canvas.height / 2;
            
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

            for(let j=0; j<bodies.length; j++) {
                let b = bodies[j];
                b.z -= 1.2;
                if(b.z <= 30) { b.z = 900; }
                
                let bk = 150.0 / b.z;
                let bpx = b.x * bk + cx;
                let bpy = b.y * bk + cy;
                let br = b.r * bk;
                
                if (br < 0) continue;

                if(b.ring) {
                    ctx.save();
                    ctx.beginPath();
                    ctx.ellipse(bpx, bpy, br * 2.0, br * 0.6, Math.PI / 6, 0, Math.PI * 2);
                    ctx.strokeStyle = "rgba(245, 158, 11, 0.7)";
                    ctx.lineWidth = br * 0.25;
                    ctx.stroke();
                    ctx.restore();
                }

                let grad = ctx.createRadialGradient(bpx - br*0.3, bpy - br*0.3, br*0.1, bpx, bpy, br);
                grad.addColorStop(0, b.color1);
                grad.addColorStop(1, b.color2);
                
                ctx.beginPath();
                ctx.arc(bpx, bpy, br, 0, Math.PI * 2);
                ctx.fillStyle = grad;
                ctx.shadowBlur = 20;
                ctx.shadowColor = b.color1;
                ctx.fill();
                ctx.shadowBlur = 0;

                ctx.fillStyle = "#f1f5f9";
                ctx.font = "bold 11px monospace";
                ctx.fillText(b.name, bpx + br + 8, bpy + 4);
            }

            requestAnimationFrame(draw);
        }
        draw();
    </script>
    """
    components.html(sol_html, height=560)
    st.success(f"🌌 Güneş Sistemi, Gezegenler ve Uydular aktif!")

elif sim_mode == "🚀 Gerçek Fiziksel Roket Fırlatma Simülatörü":
    st.subheader("🚀 Fizik Tabanlı Canlı Roket Fırlatma & Yörünge Motoru")
    throttle = st.slider("Motor İtki Gücü (Throttle %)", 0, 100, 85)
    payload_weight = st.selectbox("Yük (Payload)", ["Standart Uydu (500 kg)", "Derin Uzay Sondayı (1200 kg)", "Astronot Kapsülü (2500 kg)"])
    
    if st.button("🔥 Ateşle ve Fırlat!"):
        with st.spinner("Geri sayım başlatıldı... Liftoff! 🚀"):
            time.sleep(2)
        max_altitude = throttle * 12.5
        max_speed = throttle * 340
        burn_time = 100 - (throttle // 3)
        st.success("🎯 **Fırlatma Başarılı!**")
        c_a, c_b, c_c = st.columns(3)
        c_a.metric("Ulaşılan İrtifa", f"{max_altitude:.1f} km")
        c_b.metric("Maksimum Hız", f"{max_speed} m/s")
        c_c.metric("Yakıt Verimliliği", f"%{burn_time}")
        st.balloons()
    else:
        st.warning("⚠️ Roket fırlatma rampasında bekliyor.")

elif sim_mode == "🌐 Canlı Kokpit & Biyometrik Monitör":
    st.subheader("📊 Astronot Canlı Sağlık & Yaşam Destek Paneli")
    c1, c2, c3 = st.columns(3)
    c1.markdown('<div class="metric-card"><h3>Kalp Atış</h3><h2>74 bpm</h2></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h3>Oksijen</h3><h2>99.7%</h2></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h3>Nöro-Stres</h3><h2>%10</h2></div>', unsafe_allow_html=True)

else:
    st.subheader("☄️ Uzay Çöpü Kaçınma Manevrası")
    action = st.radio("Strateji Seç:", ["RDP İtki roketleriyle kaç", "Zırh kalkanı aç", "Lidya AI Otonom Mod"])
    if st.button("🚨 Manevrayı Başlat"):
        st.balloons()
        st.success("Manevra başarılı!")
