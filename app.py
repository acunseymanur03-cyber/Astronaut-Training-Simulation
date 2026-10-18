import streamlit as st
import time
import streamlit.components.v1 as components

st.set_page_config(page_title="NEURO-AURA Space Simulator", page_icon="🚀", layout="wide")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at center, #0B1021 0%, #03050C 100%); color: #E2E8F0; }
    .metric-card { background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(56, 189, 248, 0.4); padding: 20px; border-radius: 12px; text-align: center; box-shadow: 0 0 15px rgba(56, 189, 248, 0.2); }
    .stButton>button { background: linear-gradient(90deg, #0284c7 0%, #2563eb 100%); color: white; font-weight: bold; border-radius: 8px; padding: 12px 24px; box-shadow: 0 0 15px rgba(37, 99, 235, 0.5); }
    </style>
""", unsafe_allow_html=True)

st.title("🌌 NEURO-AURA: Interstellar 3D Flight & Training Engine")
st.markdown("### *NASA Space Apps Challenge - Advanced Simulation Suite*")

# Sol Menüden Hız Kontrolünü de içeren gelişmiş panel
sim_mode = st.sidebar.selectbox("Eğitim Modu Seçin", [
    "🚀 3D Gerçekçi Gezegen & Hız Kontrollü Uçuş",
    "🌐 Canlı Kokpit & Biyometrik Monitör",
    "👨‍🚀 EVA Uzay Yürüyüşü Simülatörü",
    "☄️ Uzay Çöpü Kaçınma Manevrası"
])

if sim_mode == "🚀 3D Gerçekçi Gezegen & Hız Kontrollü Uçuş":
    st.subheader("🪐 İnteraktif Warp Hızı & Gezegen Geçiş Simülatörü")
    st.write("Aşağıdaki hız slider'ını değiştirerek uzay gemisinin warp hızını anlık olarak artırıp azaltabilirsin!")
    
    # Python slider değerini doğrudan HTML/JS içine aktarıyoruz
    speed_val = st.slider("Warp Motor Hızı (Mach)", min_value=1, max_value=20, value=5)
    
    # Slider değerine göre hızlanan gelişmiş JavaScript simülasyonu
    sim_html = f"""
    <div style="width:100%; height:520px; background:#000; border-radius:12px; overflow:hidden; position:relative; border:1px solid #38bdf8;">
        <div style="position:absolute; top:12px; left:12px; color:#00f0ff; font-family:monospace; background:rgba(0,0,0,0.85); padding:8px 12px; border-radius:6px; border:1px solid #00f0ff; z-index:10; font-size:13px;">
            🚀 WARP HIZI: {speed_val}x | SİSTEM AKTİF
        </div>
        <canvas id="vc"></canvas>
    </div>
    <script>
        const canvas = document.getElementById('vc');
        const ctx = canvas.getContext('2d');
        let currentSpeed = {speed_val};

        function resize() {{
            canvas.width = canvas.parentElement.clientWidth;
            canvas.height = 520;
        }}
        resize();
        window.onresize = resize;
        
        let stars = [];
        for(let i=0; i<700; i++) {{
            stars.push({{
                x: (Math.random() - 0.5) * canvas.width,
                y: (Math.random() - 0.5) * canvas.height,
                z: Math.random() * canvas.width
            }});
        }}
        
        let planets = [
            {{ x: -180, y: -100, r: 55, name: 'Mars II (Terraforming)', z: 500, c1: '#ff7b54', c2: '#933215', ring: false }},
            {{ x: 200, y: 120, r: 90, name: 'Saturnian Gas Giant', z: 800, c1: '#ffd369', c2: '#b38b24', ring: true }},
            {{ x: -220, y: 160, r: 45, name: 'Kepler-452b (Oceanic)', z: 1100, c1: '#00adb5', c2: '#003840', ring: false }}
        ];

        function draw() {{
            ctx.fillStyle = "rgba(2, 4, 10, 0.35)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            let cx = canvas.width / 2;
            let cy = canvas.height / 2;
            
            // Yıldızlar (Hıza göre hareket eder)
            for(let i=0; i<stars.length; i++) {{
                let s = stars[i];
                s.Z -= (currentSpeed * 0.6);
                if(s.Z <= 0) {{ s.Z = canvas.width; s.X = (Math.random() - 0.5) * canvas.width; s.Y = (Math.random() - 0.5) * canvas.height; }}
                let k = 120.0 / s.Z;
                let px = s.X * k + cx;
                let py = s.Y * k + cy;
                if(px >= 0 && px <= canvas.width && py >= 0 && py <= canvas.height) {{
                    let sz = (1 - s.Z / canvas.width) * (currentSpeed > 10 ? 3 : 2);
                    ctx.fillStyle = "#ffffff";
                    ctx.beginPath();
                    ctx.arc(px, py, sz < 0 ? 0 : sz, 0, Math.PI * 2);
                    ctx.fill();
                }}
            }}

            // Gezegenler (Hıza duyarlı akış)
            for(let j=0; j<planets.length; j++) {{
                let p = planets[j];
                p.z -= (currentSpeed * 0.35);
                if(p.z <= 40) {{ p.z = 1200; }}
                
                let pk = 180.0 / p.z;
                let ppx = p.x * pk + cx;
                let ppy = p.y * pk + cy;
                let pr = p.r * pk;
                
                if (pr < 0) continue;

                if(p.ring) {{
                    ctx.save();
                    ctx.beginPath();
                    ctx.ellipse(ppx, ppy, pr * 1.8, pr * 0.5, Math.PI / 6, 0, Math.PI * 2);
                    ctx.strokeStyle = "rgba(218, 165, 32, 0.7)";
                    ctx.lineWidth = pr * 0.22;
                    ctx.stroke();
                    ctx.restore();
                }}

                let grad = ctx.createRadialGradient(ppx - pr*0.3, ppy - pr*0.3, pr*0.1, ppx, ppy, pr);
                grad.addColorStop(0, p.c1);
                grad.addColorStop(1, p.c2);
                
                ctx.beginPath();
                ctx.arc(ppx, ppy, pr, 0, Math.PI * 2);
                ctx.fillStyle = grad;
                ctx.shadowBlur = 30;
                ctx.shadowColor = p.c1;
                ctx.fill();
                ctx.shadowBlur = 0;

                ctx.fillStyle = "#f1f5f9";
                ctx.font = "bold 13px monospace";
                ctx.fillText(p.name, ppx + pr + 10, ppy);
            }}

            requestAnimationFrame(draw);
        }}
        draw();
    </script>
    """
    components.html(sim_html, height=540)
    st.success(f"⚡ Motor Durumu: Aktif warp hızı **{speed_val}x** ile uzay tünelinde seyahat ediliyor.")

elif sim_mode == "🌐 Canlı Kokpit & Biyometrik Monitör":
    st.subheader("📊 Astronot Canlı Sağlık & Yaşam Destek Paneli")
    c1, c2, c3 = st.columns(3)
    c1.markdown('<div class="metric-card"><h3>❤️ Kalp Atış Hızı</h3><h2>74 bpm</h2><p style="color:#38bdf8;">Stabil</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="metric-card"><h3>🧪 Kabin Oksijeni</h3><h2>99.7%</h2><p style="color:#4ade80;">Normal Basınç</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="metric-card"><h3>🧠 Nöro-Stres</h3><h2>%10</h2><p style="color:#38bdf8;">Yüksek Odak</p></div>', unsafe_allow_html=True)
    
    st.write("---")
    st.info("💡 Bu panel astronotun uzay yürüyüşü ve yüksek G kuvveti altındaki anlık biyometrik verilerini simüle eder.")

elif sim_mode == "👨‍🚀 EVA Uzay Yürüyüşü Simülatörü":
    st.subheader("👨‍🚀 Extravehicular Activity (EVA) - Sırt Roketi İtki Testi")
    st.write("Uzay aracından ayrılarak boşlukta serbest manevra yapma simülasyonu.")
    
    eva_power = st.slider("Jetpack İtki Gücü (%)", 0, 100, 50)
    tether = st.checkbox("Güvenlik Halatı Bağlı (Tether Active)", value=True)
    
    if st.button("🚀 İtki Patlat ve Manevra Yap"):
        with st.spinner("Kütle çekim ve jiroskopik denge hesaplanıyor..."):
            time.sleep(1.5)
        if tether:
            st.success(f"✅ Başarılı! %{eva_power} itki gücüyle güvenli yaklaşma sağlandı.")
        else:
            st.warning("⚠️ Dikkat! Halatsız serbest uçuşta yön sabitleme zorlaştı, stabilizatörler devreye girdi.")

else:
    st.subheader("☄️ Uzay Çöpü Kaçınma Manevrası")
    st.write("Radar Sistemi: 30 km mesafede yüksek hızlı uzay kalıntısı yaklaşıyor!")
    
    action = st.radio("Acil Kaçış Stratejisi:", [
        "RDP İtki roketleriyle yörüngeyi 3 km yukarı taşı",
        "Kabin zırh kalkanlarını yoğunlaştırıp açıyı koru",
        "Lidya AI Otonom Kaçış Protokolünü Çalıştır"
    ])
    
    if st.button("🚨 Kaçış Manevrasını Başlat"):
        with st.spinner("Otonom rota hesaplanıyor..."):
            time.sleep(2)
        st.balloons()
        st.success(f"🎉 Harika Karar! **{action}** başarıyla uygulandı, araç tehlikeden kurtuldu.")
