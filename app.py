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

st.title("🌌 NEURO-AURA: 3D Interactive Space & Mission Suite")
st.markdown("### *NASA Space Apps Challenge - Sesli AI Destekli Küresel Birincilik Adayı*")

sim_mode = st.sidebar.selectbox("Simülasyon Modu Seçin", [
    "🪐 Güneş Sistemi, 8 Gezegen & Uydular (3D)",
    "🚀 Gerçekçi 3D Roket Fırlatma & Yörünge Simülatörü",
    "🌐 3D Canlı Kokpit & EKG Biyometrik Monitör",
    "🏅 NASA Astronot Eğitim & Rozet Merkezi (3D)",
    "☄️ 3D Uzay Çöpü & Radar Kaçınma Simülatörü",
    "🛰️ Canlı NASA Verileri & Sesli NEURO-AI Asistanı"
])

if sim_mode == "🪐 Güneş Sistemi, 8 Gezegen & Uydular (3D)":
    st.subheader("☀️ Güneş Sistemi, 8 Gezegen ve Uydular 3D Geçidi")
    speed_factor = st.slider("Simülasyon Hızı", 1, 30, 5)
    sol_html = "<div style='width:100%; height:550px; background:#000; border-radius:12px; overflow:hidden; position:relative; border:2px solid #38bdf8;'><div style='position:absolute; top:12px; left:12px; color:#00f0ff; font-family:monospace; background:rgba(0,0,0,0.85); padding:8px 12px; border-radius:6px; border:1px solid #00f0ff; z-index:10; font-size:13px;'>☀️ 3D GÜNEŞ SİSTEMİ & UYDULAR</div><canvas id='scs' style='width:100%; height:100%; display:block;'></canvas></div><script>const canvas = document.getElementById('scs'); const ctx = canvas.getContext('2d'); function resize() { canvas.width = canvas.parentElement.clientWidth; canvas.height = 550; } resize(); window.onresize = resize; let stars = []; for(let i=0; i<900; i++) { stars.push({ x: (Math.random()-0.5)*canvas.width, y: (Math.random()-0.5)*canvas.height, z: Math.random()*canvas.width }); } let bodies = [ { x: -380, y: 0, r: 50, name: '☀️ Güneş', z: 650, c1: '#ffcc00', c2: '#ff3300', ring: false }, { x: -300, y: -45, r: 10, name: '☿ Merkür', z: 600, c1: '#b0b0b0', c2: '#505050', ring: false }, { x: -220, y: 55, r: 16, name: '♀ Venüs', z: 560, c1: '#e3bb76', c2: '#8c6724', ring: false }, { x: -140, y: -25, r: 19, name: '🜨 Dünya (+Ay)', z: 520, c1: '#38bdf8', c2: '#1d4ed8', ring: false }, { x: -60, y: 65, r: 14, name: '♂ Mars (+Phobos)', z: 480, c1: '#ff7b54', c2: '#933215', ring: false }, { x: 30, y: -55, r: 35, name: '♃ Jüpiter (+Europa)', z: 430, c1: '#e0ae6f', c2: '#8b5a2b', ring: false }, { x: 120, y: 45, r: 30, name: '♄ Saturn (+Titan & Halka)', z: 380, c1: '#fcd34d', c2: '#b45309', ring: true }, { x: 200, y: -35, r: 23, name: '♅ Uranüs', z: 330, c1: '#67e8f9', c2: '#0e7490', ring: false }, { x: 280, y: 45, r: 22, name: '♆ Neptün', z: 290, c1: '#3b82f6', c2: '#1e3a8a', ring: false }, { x: 350, y: -25, r: 8, name: '♇ Plüton', z: 250, c1: '#d1d5db', c2: '#4b5563', ring: false } ]; function draw() { ctx.fillStyle = 'rgba(3, 5, 12, 0.45)'; ctx.fillRect(0, 0, canvas.width, canvas.height); let cx = canvas.width / 2, cy = canvas.height / 2; for(let i=0; i<stars.length; i++) { let s = stars[i]; s.Z -= 2.5; if(s.Z <= 0) { s.Z = canvas.width; s.X = (Math.random()-0.5)*canvas.width; s.Y = (Math.random()-0.5)*canvas.height; } let k = 100.0 / s.Z, px = s.X * k + cx, py = s.Y * k + cy; if(px >= 0 && px <= canvas.width && py >= 0 && py <= canvas.height) { ctx.fillStyle = '#fff'; ctx.fillRect(px, py, 1.8, 1.8); } } for(let j=0; j<bodies.length; j++) { let b = bodies[j]; b.z -= 1.2; if(b.z <= 20) b.z = 950; let bk = 160.0 / b.z, bpx = b.x * bk + cx, bpy = b.y * bk + cy, br = b.r * bk; if(br < 0) continue; if(b.ring) { ctx.save(); ctx.beginPath(); ctx.ellipse(bpx, bpy, br * 2.2, br * 0.7, Math.PI / 6, 0, Math.PI * 2); ctx.strokeStyle = 'rgba(245, 158, 11, 0.8)'; ctx.lineWidth = br * 0.28; ctx.stroke(); ctx.restore(); } let grad = ctx.createRadialGradient(bpx - br*0.3, bpy - br*0.3, br*0.1, bpx, bpy, br); grad.addColorStop(0, b.c1); grad.addColorStop(1, b.c2); ctx.beginPath(); ctx.
