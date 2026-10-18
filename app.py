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
st.markdown("### *NASA Space Apps Challenge - Advanced 3D Simulation Engine*")

sim_mode = st.sidebar.selectbox("Simülasyon Modu Seçin", [
    "🪐 Güneş Sistemi, 8 Gezegen & Uydular (3D)",
    "🚀 Gerçekçi 3D Roket Fırlatma & Yörünge Simülatörü",
    "🌐 3D Canlı Kokpit & EKG Biyometrik Monitör",
    "🏅 NASA Astronot Eğitim & Rozet Merkezi (3D)",
    "☄️ 3D Uzay Çöpü & Radar Kaçınma Simülatörü"
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
    st.subheader("🏅 NASA Astronot Uzmanlık Eğitimi & Rozet Kazanma Simülatörü")
    st.write("Görev simülasyonlarını başarıyla tamamlayarak resmi NASA astronot uzmanlık rozetlerini kazanın!")
    if "badges" not in st.session_state:
        st.session_state.badges = {"zero_g": False, "eva": False, "nav": False}
    train_html = "<div style='width:100%; height:380px; background:#000; border-radius:12px; overflow:hidden; position:relative; border:2px solid #38bdf8;'><div style='position:absolute; top:12px; left:12px; color:#00f0ff; font-family:monospace; background:rgba(0,0,0,0.85); padding:8px 12px; border-radius:6px; border:1px solid #00f0ff; z-index:10; font-size:13px;'>🧑‍🚀 NASA EĞİTİM Kapsülü | Yerçekimsizlik Testi</div><canvas id='tcan' style='width:100%; height:100%; display:block;'></canvas></div><script>const tcan = document.getElementById('tcan'); const tctx = tcan.getContext('2d'); function tres() { tcan.width = tcan.parentElement.clientWidth; tcan.height = 380; } tres(); window.onresize = tres; let aY = 190; let dir = 1; function drawTrain() { tctx.fillStyle = 'rgba(3, 5, 12, 0.3)'; tctx.fillRect(0, 0, tcan.width, tcan.height); let cx = tcan.width / 2; aY += 0.8 * dir; if (aY > 230 || aY < 150) dir *= -1; tctx.fillStyle = '#38bdf8'; tctx.shadowBlur = 15; tctx.shadowColor = '#38bdf8'; tctx.beginPath(); tctx.arc(cx, aY - 30, 18, 0, Math.PI * 2); tctx.fill(); tctx.fillStyle = '#f8fafc'; tctx.beginPath(); tctx.roundRect(cx - 15, aY - 8, 30, 45, 8); tctx.fill(); tctx.fillStyle = '#ef4444'; tctx.fillRect(cx - 22, aY, 7, 25); tctx.fillRect(cx + 15, aY, 7, 25); tctx.strokeStyle = '#00f0ff'; tctx.lineWidth = 2; [40, 80, 120].forEach(r => { tctx.beginPath(); tctx.arc(cx, aY, r + Math.sin(Date.now() * 0.003) * 5, 0, Math.PI * 2); tctx.stroke(); }); requestAnimationFrame(drawTrain); } drawTrain();</script>"
    components.html(train_html, height=400)
    st.markdown("### 🎯 NASA Eğitim Görevleri")
    col_e1, col_e2, col_e3 = st.columns(3)
    with col_e1:
        st.markdown("<div class='metric-card'><h4>🌍 Sıfır Yerçekimi (Zero-G) Uyum</h4><p>Uzayda yön ve denge kontrolü testi.</p></div>", unsafe_allow_html=True)
        if st.button("🎓 Zero-G Testini Başlat"):
            with st.spinner("Sıfır yerçekimi odası simüle ediliyor..."):
                time.sleep(1.5)
            st.session_state.badges["zero_g"] = True
            st.success("🎉 Tebrikler! Zero-G sertifikasını kazandınız!")
            st.balloons()
    with col_e2:
        st.markdown("<div class='metric-card'><h4>🛰️ ISS Uzay Yürüyüşü (EVA)</h4><p>Uluslararası Uzay İstasyonu dış tamiri.</p></div>", unsafe_allow_html=True)
        if st.button("🔧 EVA Görevini Yap"):
            with st.spinner("Uzay elbisesi basınçlandırılıyor..."):
                time.sleep(1.5)
            st.session_state.badges["eva"] = True
            st.success("🎉 Tebrikler! EVA Uzmanlık sertifikasını kazandınız!")
            st.balloons()
    with col_e3:
        st.markdown("<div class='metric-card'><h4>🪐 Derin Uzay Navigasyonu</h4><p>Yıldız sistemleri üzerinden rotalama.</p></div>", unsafe_allow_html=True)
        if st.button("🧭 Navigasyonu Tamamla"):
            with st.spinner("Yıldız haritaları işleniyor..."):
                time.sleep(1.5)
            st.session_state.badges["nav"] = True
            st.success("🎉 Tebrikler! Kaptan Navigatör sertifikasını kazandınız!")
            st.balloons()
    st.markdown("---")
    st.markdown("### 🏅 Kazanılan Resmi NASA Uzmanlık Rozetleriniz")
    b_col1, b_col2, b_col3 = st.columns(3)
    with b_col1:
        if st.session_state.badges["zero_g"]:
            st.markdown("<div style='text-align:center; padding:15px; background:rgba(56,189,248,0.2); border:2px solid #38bdf8; border-radius:12px;'><h1>🛸</h1><b>NASA Zero-G Master</b><br><small style='color:#4ade80;'>Kazanıldı ✅</small></div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='text-align:center; padding:15px; background:rgba(255,255,255,0.05); border:1px dashed #64748b; border-radius:12px;'><h1>🔒</h1><b>NASA Zero-G Master</b><br><small style='color:#94a3b8;'>Kilitli</small></div>", unsafe_allow_html=True)
    with b_col2:
        if st.session_state.badges["eva"]:
            st.markdown("<div style='text-align:center; padding:15px; background:rgba(56,189,248,0.2); border:2px solid #38bdf8; border-radius:12px;'><h1>👨‍🚀</h1><b>NASA EVA Specialist</b><br><small style='color:#4ade80;'>Kazanıldı ✅</small></div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='text-align:center; padding:15px; background:rgba(255,255,255,0.05); border:1px dashed #64748b; border-radius:12px;'><h1>🔒</h1><b>NASA EVA Specialist</b><br><small style='color:#94a3b8;'>Kilitli</small></div>", unsafe_allow_html=True)
    with b_col3:
        if st.session_state.badges["nav"]:
            st.markdown("<div style='text-align:center; padding:15px; background:rgba(56,189,248,0.2); border:2px solid #38bdf8; border-radius:12px;'><h1>🚀</h1><b>Deep Space Commander</b><br><small style='color:#4ade80;'>Kazanıldı ✅</small></div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='text-align:center; padding:15px; background:rgba(255,255,255,0.05); border:1px dashed #64748b; border-radius:12px;'><h1>🔒</h1><b>Deep Space Commander</b><br><small style='color:#94a3b8;'>Kilitli</small></div>", unsafe_allow_html=True)

else:
    st.subheader("☄️ 3D Uzay Çöpü Radar & Kaçınma Simülatörü")
    radar_html = "<div style='width:100%; height:480px; background:#000; border-radius:12px; overflow:hidden; position:relative; border:2px solid #38bdf8;'><div style='position:absolute; top:12px; left:12px; color:#00f0ff; font-family:monospace; background:rgba(0,0,0,0.85); padding:8px 12px; border-radius:6px; border:1px solid #00f0ff; z-index:10; font-size:13px;'>📡 RADAR TARAMA: AKTİF</div><canvas id='rcan' style='width:100%; height:100%; display:block;'></canvas></div><script>const rcan = document.getElementById('rcan'); const rctx2 = rcan.getContext('2d'); function rres() { rcan.width = rcan.parentElement.clientWidth; rcan.height = 480; } rres(); window.onresize = rres; let angle = 0; let debris = [ {x: 140, y: -90}, {x: -160, y: 110}, {x: 60, y: 150} ]; function drawRadar() { rctx2.fillStyle = 'rgba(3, 5, 12, 0.25)'; rctx2.fillRect(0, 0, rcan.width, rcan.height); let cx = rcan.width / 2, cy = rcan.height / 2; rctx2.strokeStyle = 'rgba(56, 189, 248, 0.35)'; rctx2.lineWidth = 1.5; [70, 140, 210].forEach(r => { rctx2.beginPath(); rctx2.arc(cx, cy, r, 0, Math.PI*2); rctx2.stroke(); }); angle += 0.035; rctx2.save(); rctx2.translate(cx, cy); rctx2.rotate(angle); let grad = rctx2.createLinearGradient(0, 0, 210, 0); grad.addColorStop(0, 'rgba(56, 189, 248, 0.85)'); grad.addColorStop(1, 'transparent'); rctx2.fillStyle = grad; rctx2.beginPath(); rctx2.moveTo(0,0); rctx2.arc(0,0, 210, 0, 0.5); rctx2.lineTo(0,0); rctx2.fill(); rctx2.restore(); debris.forEach(d => { rctx2.fillStyle = '#ef4444'; rctx2.shadowBlur = 15; rctx2.shadowColor = '#ef4444'; rctx2.beginPath(); rctx2.arc(cx + d.x, cy + d.y, 6, 0, Math.PI*2); rctx2.fill(); rctx2.shadowBlur = 0; }); requestAnimationFrame(drawRadar); } drawRadar();</script>"
    components.html(radar_html, height=500)
    if st.button("🚨 Otonom Kaçış Manevrasını Başlat"):
        st.balloons()
        st.success("🎉 Başarılı! RDP itki roketleri devreye girerek uzay çöplerinden kaçındı.")
