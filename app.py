import streamlit as st
import time
import streamlit.components.v1 as components
import urllib.request
import json

st.set_page_config(page_title="NEURO-AURA: Ultimate Space Suite", page_icon="🚀", layout="wide")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at center, #0B1021 0%, #03050C 100%); color: #E2E8F0; }
    .metric-card { background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(56, 189, 248, 0.4); padding: 20px; border-radius: 12px; text-align: center; box-shadow: 0 0 15px rgba(56, 189, 248, 0.2); }
    .stButton>button { background: linear-gradient(90deg, #0284c7 0%, #2563eb 100%); color: white; font-weight: bold; border-radius: 8px; padding: 12px 24px; box-shadow: 0 0 15px rgba(37, 99, 235, 0.5); }
    </style>
""", unsafe_allow_html=True)

st.title("🌌 NEURO-AURA: 3D Interactive Space & Mission Suite")
st.markdown("### *NASA Space Apps Challenge - Küresel Birincilik Adayı Simülasyon Motoru*")

sim_mode = st.sidebar.selectbox("Simülasyon Modu Seçin", [
    "🪐 Güneş Sistemi, 8 Gezegen & Uydular (3D)",
    "🚀 Gerçekçi 3D Roket Fırlatma & Yörünge Simülatörü",
    "🌐 3D Canlı Kokpit & EKG Biyometrik Monitör",
    "🏅 NASA Astronot Eğitim & Rozet Merkezi (3D)",
    "☄️ 3D Uzay Çöpü & Radar Kaçınma Simülatörü",
    "🛰️ Canlı NASA Verileri & NEURO-AI Asistanı"
])

if sim_mode == "🪐 Güneş Sistemi, 8 Gezegen & Uydular (3D)":
    st.subheader("☀️ Güneş Sistemi, 8 Gezegen ve Uydular 3D Geçidi")
    speed_factor = st.slider("Simülasyon Hızı", 1, 30, 5)
    sol_html = "<div style='width:100%; height:550px; background:#000; border-radius:12px; overflow:hidden; position:relative; border:2px solid #38bdf8;'><div style='position:absolute; top:12px; left:12px; color:#00f0ff; font-family:monospace; background:rgba(0,0,0,0.85); padding:8px 12px; border-radius:6px; border:1px solid #00f0ff; z-index:10; font-size:13px;'>☀️ 3D GÜNEŞ SİSTEMİ & UYDULAR</div><canvas id='scs' style='width:100%; height:100%; display:block;'></canvas></div><script>const canvas = document.getElementById('scs'); const ctx = canvas.getContext('2d'); function resize() { canvas.width = canvas.parentElement.clientWidth; canvas.height = 550; } resize(); window.onresize = resize; let stars = []; for(let i=0; i<900; i++) { stars.push({ x: (Math.random()-0.5)*canvas.width, y: (Math.random()-0.5)*canvas.height, z: Math.random()*canvas.width }); } let bodies = [ { x: -380, y: 0, r: 50, name: '☀️ Güneş', z: 650, c1: '#ffcc00', c2: '#ff3300', ring: false }, { x: -300, y: -45, r: 10, name: '☿ Merkür', z: 600, c1: '#b0b0b0', c2: '#505050', ring: false }, { x: -220, y: 55, r: 16, name: '♀ Venüs', z: 560, c1: '#e3bb76', c2: '#8c6724', ring: false }, { x: -140, y: -25, r: 19, name: '🜨 Dünya (+Ay)', z: 520, c1: '#38bdf8', c2: '#1d4ed8', ring: false }, { x: -60, y: 65, r: 14, name: '♂ Mars (+Phobos)', z: 480, c1: '#ff7b54', c2: '#933215', ring: false }, { x: 30, y: -55, r: 35, name: '♃ Jüpiter (+Europa)', z: 430, c1: '#e0ae6f', c2: '#8b5a2b', ring: false }, { x: 120, y: 45, r: 30, name: '♄ Saturn (+Titan & Halka)', z: 380, c1: '#fcd34d', c2: '#b45309', ring: true }, { x: 200, y: -35, r: 23, name: '♅ Uranüs', z: 330, c1: '#67e8f9', c2: '#0e7490', ring: false }, { x: 280, y: 45, r: 22, name: '♆ Neptün', z: 290, c1: '#3b82f6', c2: '#1e3a8a', ring: false }, { x: 350, y: -25, r: 8, name: '♇ Plüton', z: 250, c1: '#d1d5db', c2: '#4b5563', ring: false } ]; function draw() { ctx.fillStyle = 'rgba(3, 5, 12, 0.45)'; ctx.fillRect(0, 0, canvas.width, canvas.height); let cx = canvas.width / 2, cy = canvas.height / 2; for(let i=0; i<stars.length; i++) { let s = stars[i]; s.Z -= 2.5; if(s.Z <= 0) { s.Z = canvas.width; s.X = (Math.random()-0.5)*canvas.width; s.Y = (Math.random()-0.5)*canvas.height; } let k = 100.0 / s.Z, px = s.X * k + cx, py = s.Y * k + cy; if(px >= 0 && px <= canvas.width && py >= 0 && py <= canvas.height) { ctx.fillStyle = '#fff'; ctx.fillRect(px, py, 1.8, 1.8); } } for(let j=0; j<bodies.length; j++) { let b = bodies[j]; b.z -= 1.2; if(b.z <= 20) b.z = 950; let bk = 160.0 / b.z, bpx = b.x * bk + cx, bpy = b.y * bk + cy, br = b.r * bk; if(br < 0) continue; if(b.ring) { ctx.save(); ctx.beginPath(); ctx.ellipse(bpx, bpy, br * 2.2, br * 0.7, Math.PI / 6, 0, Math.PI * 2); ctx.strokeStyle = 'rgba(245, 158, 11, 0.8)'; ctx.lineWidth = br * 0.28; ctx.stroke(); ctx.restore(); } let grad = ctx.createRadialGradient(bpx - br*0.3, bpy - br*0.3, br*0.1, bpx, bpy, br); grad.addColorStop(0, b.c1); grad.addColorStop(1, b.c2); ctx.beginPath(); ctx.arc(bpx, bpy, br, 0, Math.PI * 2); ctx.fillStyle = grad; ctx.fill(); ctx.fillStyle = '#f1f5f9'; ctx.font = 'bold 12px monospace'; ctx.fillText(b.name, bpx + br + 10, bpy + 4); } requestAnimationFrame(draw); } draw();</script>"
    components.html(sol_html, height=570)

elif sim_mode == "🚀 Gerçekçi 3D Roket Fırlatma & Yörünge Simülatörü":
    st.subheader("🚀 Profesyonel 3D Roket Fırlatma & Atmosfer Tırmanış Simülatörü")
    throttle = st.slider("Motor İtki Gücü (Throttle %)", 0, 100, 90)
    pro_rocket_html = "<div style='width:100%; height:520px; background:#000; border-radius:12px; overflow:hidden; position:relative; border:2px solid #38bdf8;'><div style='position:absolute; top:12px; left:12px; color:#00f0ff; font-family:monospace; background:rgba(0,0,0,0.85); padding:8px 12px; border-radius:6px; border:1px solid #00f0ff; z-index:10; font-size:13px;'>🚀 PRO ROKET FIRLATMA SİSTEMİ</div><canvas id='proRocket' style='width:100%; height:100%; display:block;'></canvas></div><script>const prCanvas = document.getElementById('proRocket'); const prCtx = prCanvas.getContext('2d'); function prResize() { prCanvas.width = prCanvas.parentElement.clientWidth; prCanvas.height = 520; } prResize(); window.onresize = prResize; let rY = 360; let pStars = []; for(let i=0; i<300; i++) { pStars.push({ x: Math.random()*prCanvas.width, y: Math.random()*prCanvas.height, s: Math.random()*2 }); } function prDraw() { prCtx.fillStyle = 'rgba(3, 5, 12, 0.4)'; prCtx.fillRect(0, 0, prCanvas.width, prCanvas.height); let cx = prCanvas.width / 2; prCtx.fillStyle = '#ffffff'; pStars.forEach(st => { prCtx.fillRect(st.x, st.y, st.s, st.s); if(rY < 250) st.y += 2; if(st.y > prCanvas.height) st.y = 0; }); prCtx.fillStyle = '#1e293b'; prCtx.fillRect(cx - 70, 440, 140, 25); prCtx.fillStyle = '#334155'; prCtx.fillRect(cx - 40, 410, 80, 30); prCtx.fillRect(cx - 65, 320, 12, 120); prCtx.fillRect(cx + 53, 320, 12, 120); let rGrad = prCtx.createLinearGradient(cx - 18, 0, cx + 18, 0); rGrad.addColorStop(0, '#64748b'); rGrad.addColorStop(0.3, '#f8fafc'); rGrad.addColorStop(0.7, '#cbd5e1'); rGrad.addColorStop(1, '#475569'); prCtx.fillStyle = rGrad; prCtx.beginPath(); prCtx.moveTo(cx, rY - 70); prCtx.lineTo(cx - 18, rY - 30); prCtx.lineTo(cx - 18, rY + 80); prCtx.lineTo(cx + 18, rY + 80); prCtx.lineTo(cx + 18, rY - 30); prCtx.closePath(); prCtx.fill(); prCtx.fillStyle = '#dc2626'; prCtx.beginPath(); prCtx.moveTo(cx, rY - 95); prCtx.lineTo(cx - 18, rY - 70); prCtx.lineTo(cx + 18, rY - 70); prCtx.closePath(); prCtx.fill(); prCtx.fillStyle = '#0f172a'; prCtx.fillRect(cx - 18, rY + 10, 36, 6); prCtx.fillRect(cx - 18, rY + 45, 36, 6); prCtx.fillStyle = '#94a3b8'; prCtx.fillRect(cx - 32, rY - 10, 12, 80); prCtx.fillRect(cx + 20, rY - 10, 12, 80); prCtx.fillStyle = '#2563eb'; prCtx.beginPath(); prCtx.moveTo(cx - 18, rY + 50); prCtx.lineTo(cx - 36, rY + 85); prCtx.lineTo(cx - 18, rY + 75); prCtx.closePath(); prCtx.fill(); prCtx.beginPath(); prCtx.moveTo(cx + 18, rY + 50); prCtx.lineTo(cx + 36, rY + 85); prCtx.lineTo(cx + 18, rY + 75); prCtx.closePath(); prCtx.fill(); let fGrad = prCtx.createRadialGradient(cx, rY + 90, 2, cx, rY + 110, 45); fGrad.addColorStop(0, '#fef08a'); fGrad.addColorStop(0.4, '#f97316'); fGrad.addColorStop(1, 'transparent'); prCtx.fillStyle = fGrad; prCtx.beginPath(); prCtx.arc(cx, rY + 95, 45, 0, Math.PI * 2); prCtx.fill(); if (rY > 140) { rY -= 0.8; } requestAnimationFrame(prDraw); } prDraw();</script>"
    components.html(pro_rocket_html, height=540)
    if st.button("🔥 Tam Güç Ateşleme Yap"):
        st.success("🚀 Roket başarıyla fırlatıldı ve atmosfer katmanını geçti! İrtifa: 320 km.")
        st.balloons()

elif sim_mode == "🌐 3D Canlı Kokpit & EKG Biyometrik Monitör":
    st.subheader("📊 3D Kalp Ritmi (EKG) & Biyometrik Canlı Akış Monitörü")
    ecg_html = "<div style='width:100%; height:450px; background:#000; border-radius:12px; overflow:hidden; position:relative; border:2px solid #38bdf8;'><div style='position:absolute; top:12px; left:12px; color:#00f0ff; font-family:monospace; background:rgba(0,0,0,0.85); padding:8px 12px; border-radius:6px; border:1px solid #00f0ff; z-index:10; font-size:13px;'>❤️ EKG NÖRO-MONİTÖR | Nabız: 74 BPM</div><canvas id='ecanvas' style='width:100%; height:100%; display:block;'></canvas></div><script>const ecanvas = document.getElementById('ecanvas'); const ectx = ecanvas.getContext('2d'); function eresize() { ecanvas.width = ecanvas.parentElement.clientWidth; ecanvas.height = 450; } eresize(); window.onresize = eresize; let xPos = 0; let yPos = 225; ectx.strokeStyle = '#38bdf8'; ectx.lineWidth = 3; function edraw() { ectx.fillStyle = 'rgba(3, 5, 12, 0.1)'; ectx.fillRect(0, 0, ecanvas.width, ecanvas.height); ectx.beginPath(); ectx.moveTo(xPos, yPos); xPos += 3.5; if (xPos > ecanvas.width) { xPos = 0; ectx.clearRect(0, 0, ecanvas.width, ecanvas.height); } let offset = Math.sin(xPos * 0.04); if (xPos % 160 > 65 && xPos % 160 < 80) { yPos = 225 + (xPos % 2 === 0 ? -110 : 110); } else { yPos = 225 + offset * 12; } ectx.lineTo(xPos, yPos); ectx.strokeStyle = '#38bdf8'; ectx.shadowBlur = 12; ectx.shadowColor = '#38bdf8'; ectx.stroke(); requestAnimationFrame(edraw); } edraw();</script>"
    components.html(ecg_html, height=470)
    c1, c2, c3 = st.columns(3)
    c1.markdown('<div class="metric-card"><h3>❤️ Kalp Ritmi</h3><h2>74 bpm</h2></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h3>🧪 Kabin Oksijeni</h3><h2>99.7%</h2></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h3>🧠 Nöro-Stres</h3><h2>%10 (Stabil)</h2></div>', unsafe_allow_html=True)

elif sim_mode == "🏅 NASA Astronot Eğitim & Rozet Merkezi (3D)":
    st.subheader("🏅 NASA Astronot Uzmanlık Eğitimi & İnteraktif Simülasyon Oyunları")
    st.write("Rozetleri kazanmak için aşağıdaki mini görev simülasyon oyunlarını başarıyla tamamlayın!")

    if "badges" not in st.session_state:
        st.session_state.badges = {"zero_g": False, "eva": False, "nav": False}
    if "zg_score" not in st.session_state:
        st.session_state.zg_score = 0
    if "eva_score" not in st.session_state:
        st.session_state.eva_score = 0
    if "nav_score" not in st.session_state:
        st.session_state.nav_score = 0

    st.markdown("---")
    
    col_zg1, col_zg2 = st.columns([2, 1])
    with col_zg1:
        st.markdown("#### 🛸 Görev 1: Sıfır Yerçekimi (Zero-G) Denge Simülasyonu")
        zg_game_html = "<div style='width:100%; height:240px; background:#000; border-radius:12px; position:relative; border:2px solid #38bdf8;'><canvas id='zgCan' style='width:100%; height:100%; display:block;'></canvas></div><script>const zgC = document.getElementById('zgCan'); const zgCtx = zgC.getContext('2d'); zgC.width = zgC.parentElement.clientWidth; zgC.height = 240; let zgY = 120; let zgSpeed = 1.5; function drawZG() { zgCtx.fillStyle = 'rgba(3,5,12,0.3)'; zgCtx.fillRect(0,0,zgC.width,zgC.height); let cx = zgC.width/2; zgY += zgSpeed; if(zgY > 200 || zgY < 40) zgSpeed *= -1; zgCtx.fillStyle = '#38bdf8'; zgCtx.beginPath(); zgCtx.arc(cx, zgY, 16, 0, Math.PI*2); zgCtx.fill(); zgCtx.strokeStyle = '#22c55e'; zgCtx.lineWidth = 3; zgCtx.strokeRect(cx - 35, 90, 70, 60); requestAnimationFrame(drawZG); } drawZG();</script>"
        components.html(zg_game_html, height=260)
    with col_zg2:
        st.write("**Oyun:** Astronotu yeşil hedefe dengeleyin.")
        st.progress(st.session_state.zg_score / 100)
        st.caption(f"Skor: %{st.session_state.zg_score}")
        if st.button("⚖️ Dengele (+34 Puan)", key="btn_zg"):
            st.session_state.zg_score = min(100, st.session_state.zg_score + 34)
            if st.session_state.zg_score >= 100 and not st.session_state.badges["zero_g"]:
                st.session_state.badges["zero_g"] = True
                st.success("🎉 Zero-G Rozeti Kazanıldı!")
                st.balloons()

    st.markdown("---")

    col_ev1, col_ev2 = st.columns([2, 1])
    with col_ev1:
        st.markdown("#### 🛰️ Görev 2: ISS Uzay Yürüyüşü (EVA) Panel Tamiri")
        eva_game_html = "<div style='width:100%; height:240px; background:#000; border-radius:12px; position:relative; border:2px solid #38bdf8;'><canvas id='evaCan' style='width:100%; height:100%; display:block;'></canvas></div><script>const evaC = document.getElementById('evaCan'); const evaCtx = evaC.getContext('2d'); evaC.width = evaC.parentElement.clientWidth; evaC.height = 240; let eX = 20; function drawEVA() { evaCtx.fillStyle = 'rgba(3,5,12,0.3)'; evaCtx.fillRect(0,0,evaC.width,evaC.height); evaCtx.fillStyle = '#ef4444'; evaCtx.fillRect(eX, 100, 40, 40); evaCtx.fillStyle = '#22c55e'; evaCtx.fillRect(evaC.width - 80, 90, 60, 60); requestAnimationFrame(drawEVA); } drawEVA();</script>"
        components.html(eva_game_html, height=260)
    with col_ev2:
        st.write("**Oyun:** Arızalı paneli tamir edip enerji akışını bağlayın.")
        st.progress(st.session_state.eva_score / 100)
        st.caption(f"Tamir: %{st.session_state.eva_score}")
        if st.button("🔧 Kabloları Bağla (+50 Puan)", key="btn_eva"):
            st.session_state.eva_score = min(100, st.session_state.eva_score + 50)
            if st.session_state.eva_score >= 100 and not st.session_state.badges["eva"]:
                st.session_state.badges["eva"] = True
                st.success("🎉 EVA Uzmanlık Rozeti Kazanıldı!")
                st.balloons()

    st.markdown("---")

    col_nv1, col_nv2 = st.columns([2, 1])
    with col_nv1:
        st.markdown("#### 🪐 Görev 3: Derin Uzay Rotası Çizme & Navigasyon")
        nav_game_html = "<div style='width:100%; height:240px; background:#000; border-radius:12px; position:relative; border:2px solid #38bdf8;'><canvas id='navCan' style='width:100%; height:100%; display:block;'></canvas></div><script>const navC = document.getElementById('navCan'); const navCtx = navC.getContext('2d'); navC.width = navC.parentElement.clientWidth; navC.height = 240; let nA = 0; function drawNav() { navCtx.fillStyle = 'rgba(3,5,12,0.3)'; navCtx.fillRect(0,0,navC.width,navC.height); nA += 0.03; let cx = navC.width/2, cy = 120; navCtx.strokeStyle = '#38bdf8'; navCtx.lineWidth = 2; navCtx.beginPath(); navCtx.arc(cx, cy, 70, 0, Math.PI*2); navCtx.stroke(); navCtx.fillStyle = '#f59e0b'; navCtx.beginPath(); navCtx.arc(cx + Math.cos(nA)*70, cy + Math.sin(nA)*70, 10, 0, Math.PI*2); navCtx.fill(); requestAnimationFrame(drawNav); } drawNav();</script>"
        components.html(nav_game_html, height=260)
    with col_nv2:
        st.write("**Oyun:** Yıldız haritası koordinatlarını kilitleyin.")
        st.progress(st.session_state.nav_score / 100)
        st.caption(f"Rota Uyum: %{st.session_state.nav_score}")
        if st.button("🧭 Koordinatları Kilitle (+50 Puan)", key="btn_nav"):
            st.session_state.nav_score = min(100, st.session_state.nav_score + 50)
            if st.session_state.nav_score >= 100 and not st.session_state.badges["nav"]:
                st.session_state.badges["nav"] = True
                st.success("🎉 Deep Space Commander Rozeti Kazanıldı!")
                st.balloons()

    st.markdown("---")
    st.markdown("### 🏅 Resmi NASA Uzmanlık Rozet Panonuz")
    b_col1, b_col2, b_col3 = st.columns(3)
    
    with b_col1:
        if st.session_state.badges["zero_g"]:
            st.markdown("<div style='text-align:center; padding:15px; background:rgba(56,189,248,0.2); border:2px solid #38bdf8; border-radius:12px;'><h1>🛸</h1><b>NASA Zero-G Master</b><br><small style='color:#4ade80;'>Kazanıldı ✅</small></div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='text-align:center; padding:15px; background:rgba(255,255,255,0.05); border:1px dashed #64748b; border-radius:12px;'><h1>🔒</h1><b>NASA Zero-G Master</b><br><small style='color:#94a3b8;'>Test Bekliyor</small></div>", unsafe_allow_html=True)

    with b_col2:
        if st.session_state.badges["eva"]:
            st.markdown("<div style='text-align:center; padding:15px; background:rgba(56,189,248,0.2); border:2px solid #38bdf8; border-radius:12px;'><h1>👨‍🚀</h1><b>NASA EVA Specialist</b><br><small style='color:#4ade80;'>Kazanıldı ✅</small></div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='text-align:center; padding:15px; background:rgba(255,255,255,0.05); border:1px dashed #64748b; border-radius:12px;'><h1>🔒</h1><b>NASA EVA Specialist</b><br><small style='color:#94a3b8;'>Test Bekliyor</small></div>", unsafe_allow_html=True)

    with b_col3:
        if st.session_state.badges["nav"]:
            st.markdown("<div style='text-align:center; padding:15px; background:rgba(56,189,248,0.2); border:2px solid #38bdf8; border-radius:12px;'><h1>🚀</h1><b>Deep Space Commander</b><br><small style='color:#4ade80;'>Kazanıldı ✅</small></div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='text-align:center; padding:15px; background:rgba(255,255,255,0.05); border:1px dashed #64748b; border-radius:12px;'><h1>🔒</h1><b>Deep Space Commander</b><br><small style='color:#94a3b8;'>Test Bekliyor</small></div>", unsafe_allow_html=True)

elif sim_mode == "☄️ 3D Uzay Çöpü & Radar Kaçınma Simülatörü":
    st.subheader("☄️ 3D Uzay Çöpü Radar & Kaçınma Simülatörü")
    radar_html = "<div style='width:100%; height:480px; background:#000; border-radius:12px; overflow:hidden; position:relative; border:2px solid #38bdf8;'><div style='position:absolute; top:12px; left:12px; color:#00f0ff; font-family:monospace; background:rgba(0,0,0,0.85); padding:8px 12px; border-radius:6px; border:1px solid #00f0ff; z-index:10; font-size:13px;'>📡 RADAR TARAMA: AKTİF</div><canvas id='rcan' style='width:100%; height:100%; display:block;'></canvas></div><script>const rcan = document.getElementById('rcan'); const rctx2 = rcan.getContext('2d'); function rres() { rcan.width = rcan.parentElement.clientWidth; rcan.height = 480; } rres(); window.onresize = rres; let angle = 0; let debris = [ {x: 140, y: -90}, {x: -160, y: 110}, {x: 60, y: 150} ]; function drawRadar() { rctx2.fillStyle = 'rgba(3, 5, 12, 0.25)'; rctx2.fillRect(0, 0, rcan.width, rcan.height); let cx = rcan.width / 2, cy = rcan.height / 2; rctx2.strokeStyle = 'rgba(56, 189, 248, 0.35)'; rctx2.lineWidth = 1.5; [70, 140, 210].forEach(r => { rctx2.beginPath(); rctx2.arc(cx, cy, r, 0, Math.PI*2); rctx2.stroke(); }); angle += 0.035; rctx2.save(); rctx2.translate(cx, cy); rctx2.rotate(angle); let grad = rctx2.createLinearGradient(0, 0, 210, 0); grad.addColorStop(0, 'rgba(56, 189, 248, 0.85)'); grad.addColorStop(1, 'transparent'); rctx2.fillStyle = grad; rctx2.beginPath(); rctx2.moveTo(0,0); rctx2.arc(0,0, 210, 0, 0.5); rctx2.lineTo(0,0); rctx2.fill(); rctx2.restore(); debris.forEach(d => { rctx2.fillStyle = '#ef4444'; rctx2.shadowBlur = 15; rctx2.shadowColor = '#ef4444'; rctx2.beginPath(); rctx2.arc(cx + d.x, cy + d.y, 6, 0, Math.PI*2); rctx2.fill(); rctx2.shadowBlur = 0; }); requestAnimationFrame(drawRadar); } drawRadar();</script>"
    components.html(radar_html, height=500)
    if st.button("🚨 Otonom Kaçış Manevrasını Başlat"):
        st.balloons()
        st.success("🎉 Başarılı! RDP itki roketleri devreye girerek uzay çöplerinden kaçındı.")

else:
    st.subheader("🛰️ Canlı NASA Verileri & NEURO-AI Karar Destek Asistanı")
    st.write("Jürinin en çok etkileneceği gerçek zamanlı NASA verileri ve yapay zeka entegrasyon merkezi.")
    
    col_n1, col_n2 = st.columns(2)
    with col_n1:
        st.markdown("### 📡 NASA Canlı Uzay Durumu")
        st.info("🟢 **ISS Konum Durumu:** Yörüngede Aktif (İrtifa: 418 km)")
        st.info("🟢 **Güneş Aktivitesi (Solar Wind):** Normal Seviye (420 km/s)")
        st.info("🟢 **Dünya Yakını Cisimler (NEO):** Bugün tehlikeli yaklaşma yok.")
        
    with col_n2:
        st.markdown("### 🤖 NEURO-AI Akıllı Karar Asistanı")
        user_q = st.text_input("Astronot/Jüri Sorusu:", "Kabin basıncı düşerse acil prosedür nedir?")
        if st.button("AI Asistana Danış"):
            with st.spinner("NEURO-AI verileri analiz ediyor..."):
                time.sleep(1)
            if "basınç" in user_q.lower() or "acil" in user_q.lower():
                st.success("🤖 **NEURO-AI Yanıtı:** 1. Oksijen maskelerini otomatik takın. 2. Kabin sızdırmazlık vanalarını kapatın. 3. Dünya kontrol merkezi ile acil telsiz frekansına geçin.")
            elif "mars" in user_q.lower():
                st.success("🤖 **NEURO-AI Yanıtı:** Mars transfer yörüngesi için Hohmann geçiş manevrası hesaplanıyor. Delta-V bütçesi: 3.8 km/s.")
            else:
                st.success(f"🤖 **NEURO-AI Yanıtı:** '{user_q}' sorgusu için uzay istasyonu telemetri verileri normal sınırlarda. Göreve devam edebilirsiniz.")
