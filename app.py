import streamlit as st
import time
import streamlit.components.v1 as components

st.set_page_config(page_title="NEURO-AURA: Space Suite", page_icon="🚀", layout="wide")

# ÇOK DİLLİ SÖZLÜK (TÜRKÇE, İNGİLİZCE, ARAPÇA, ALMANCA, FRANSIZCA, İSPANYOLCA)
LANGS = {
    "Türkçe": {
        "title": "🌌 NEURO-AURA: 3D İnteraktif Uzay & Görev Paketi",
        "subtitle": "NASA Space Apps Challenge - Astronot Eğitim & Simülasyon Sistemi",
        "select_sim": "Simülasyon Modu Seçin",
        "modes": [
            "🪐 Güneş Sistemi, 8 Gezegen & Uydular (3D)",
            "🚀 Gerçekçi 3D Roket Fırlatma & Yörünge Simülatörü",
            "🌐 3D Canlı Kokpit & EKG Biyometrik Monitör",
            "🏅 NASA Astronot Eğitim & Rozet Merkezi (3D)",
            "☄️ 3D Uzay Çöpü & Radar Kaçınma Simülatörü",
            "🛰️ Canlı Uzay Verileri & Sesli Lidya AI Asistanı"
        ],
        "speed": "Simülasyon Hızı",
        "throttle": "Motor İtki Gücü (Throttle %)",
        "fire_rocket": "🔥 Tam Güç Ateşleme Yap",
        "rocket_success": "🚀 Roket başarıyla fırlatıldı ve atmosfer katmanını geçti! İrtifa: 320 km.",
        "hr": "Kalp Ritmi", "oxy": "Kabin Oksijeni", "stress": "Nöro-Stres",
        "badge_title": "🏅 NASA Astronot Uzmanlık Eğitimi & İnteraktif Simülasyon Oyunları",
        "badge_desc": "Rozetleri kazanmak için aşağıdaki mini görev simülasyon oyunlarını başarıyla tamamlayın!",
        "zg_title": "🛸 Görev 1: Sıfır Yerçekimi (Zero-G) Denge Simülasyonu",
        "zg_btn": "⚖️ Dengele (+34 Puan)",
        "eva_title": "🛰️ Görev 2: ISS Uzay Yürüyüşü (EVA) Panel Tamiri",
        "eva_btn": "🔧 Kabloları Bağla (+50 Puan)",
        "nav_title": "🪐 Görev 3: Derin Uzay Rotası Çizme & Navigasyon",
        "nav_btn": "🧭 Koordinatları Kilitle (+50 Puan)",
        "badge_board": "🏅 Resmi NASA Uzmanlık Rozet Panonuz",
        "earned": "Kazanıldı ✅", "waiting": "Test Bekliyor",
        "radar_title": "☄️ 3D Uzay Çöpü Radar & Kaçınma Simülatörü",
        "radar_btn": "🚨 Otonom Kaçış Manevrasını Başlat",
        "radar_success": "🎉 Başarılı! RDP itki roketleri devreye girerek uzay çöplerinden kaçındı.",
        "ai_title": "🛰️ Canlı Uzay Verileri & Sesli Lidya AI Asistanı",
        "ai_desc": "Jürinin karşısında yapay zeka ile sesli diyalog kurabileceğiniz akıllı kokpit terminali.",
        "sys_status": "📡 Sistem Durumu",
        "iss_stat": "🟢 **ISS Konum Durumu:** Yörüngede Aktif (İrtifa: 418 km)",
        "solar_stat": "🟢 **Güneş Aktivitesi (Solar Wind):** Normal Seviye (420 km/s)",
        "neo_stat": "🟢 **Dünya Yakını Cisimler (NEO):** Güvenli sınırda.",
        "ai_terminal": "🤖 Sesli Lidya AI Asistanı",
        "ask_ph": "Sorunuz:",
        "default_q": "Kabin basıncı düşerse acil prosedür nedir?",
        "ai_ans_label": "🤖 **Lidya AI Yanıtı:** ",
        "play_voice": "🔊 Lidya AI Sesli Yanıtını Oynat",
        "lang_code": "tr-TR"
    },
    "English": {
        "title": "🌌 NEURO-AURA: 3D Interactive Space & Mission Suite",
        "subtitle": "NASA Space Apps Challenge - Astronaut Training & Simulation System",
        "select_sim": "Select Simulation Mode",
        "modes": [
            "🪐 Solar System, 8 Planets & Moons (3D)",
            "🚀 Realistic 3D Rocket Launch & Orbit Simulator",
            "🌐 3D Live Cockpit & ECG Biometric Monitor",
            "🏅 NASA Astronaut Training & Badge Center (3D)",
            "☄️ 3D Space Debris & Radar Avoidance Simulator",
            "🛰️ Live Space Data & Voice-Enabled Lidya AI Assistant"
        ],
        "speed": "Simulation Speed",
        "throttle": "Engine Throttle (%)",
        "fire_rocket": "🔥 Full Power Ignition",
        "rocket_success": "🚀 Rocket successfully launched and cleared the atmosphere! Altitude: 320 km.",
        "hr": "Heart Rate", "oxy": "Cabin Oxygen", "stress": "Neuro-Stress",
        "badge_title": "🏅 NASA Astronaut Expert Training & Interactive Simulation Games",
        "badge_desc": "Successfully complete the mini mission simulation games below to earn badges!",
        "zg_title": "🛸 Mission 1: Zero-Gravity (Zero-G) Balance Simulation",
        "zg_btn": "⚖️ Balance (+34 Pts)",
        "eva_title": "🛰️ Mission 2: ISS Spacewalk (EVA) Panel Repair",
        "eva_btn": "🔧 Connect Cables (+50 Pts)",
        "nav_title": "🪐 Mission 3: Deep Space Route Plotting & Navigation",
        "nav_btn": "🧭 Lock Coordinates (+50 Pts)",
        "badge_board": "🏅 Official NASA Expert Badge Board",
        "earned": "Earned ✅", "waiting": "Pending Test",
        "radar_title": "☄️ 3D Space Debris Radar & Avoidance Simulator",
        "radar_btn": "🚨 Initiate Autonomous Evasion Maneuver",
        "radar_success": "🎉 Success! RCS thrusters engaged and avoided space debris.",
        "ai_title": "🛰️ Live Space Data & Voice Lidya AI Assistant",
        "ai_desc": "Smart cockpit terminal where you can engage in voice dialogue with AI.",
        "sys_status": "📡 System Status",
        "iss_stat": "🟢 **ISS Position:** Active in Orbit (Altitude: 418 km)",
        "solar_stat": "🟢 **Solar Activity (Solar Wind):** Normal (420 km/s)",
        "neo_stat": "🟢 **Near-Earth Objects (NEO):** Within safe limits.",
        "ai_terminal": "🤖 Voice Lidya AI Assistant",
        "ask_ph": "Your Question:",
        "default_q": "What is the emergency procedure if cabin pressure drops?",
        "ai_ans_label": "🤖 **Lidya AI Response:** ",
        "play_voice": "🔊 Play Lidya AI Voice Response",
        "lang_code": "en-US"
    },
    "العربية": {
        "title": "🌌 NEURO-AURA: مجموعة الفضاء والمهمات التفاعلية ثلاثية الأبعاد",
        "subtitle": "تحدي تطبيقات الفضاء ناسا - نظام تدريب رواد الفضاء والمحاكاة",
        "select_sim": "اختر وضع المحاكاة",
        "modes": [
            "🪐 النظام الشمسي، 8 كواكب والأقمار (3D)",
            "🚀 محاكي إطلاق الصواريخ والمدار الواقعي (3D)",
            "🌐 قمرة القيادة الحية ومراقب المؤشرات الحيوية (3D)",
            "🏅 مركز تدريب وشارات رواد الفضاء ناسا (3D)",
            "☄️ محاكي رادار الحطام الفضائي وتجنب الاصطدام (3D)",
            "🛰️ بيانات الفضاء الحية ومساعد Lidya AI الصوتي"
        ],
        "speed": "سرعة المحاكاة",
        "throttle": "دفع المحرك (%)",
        "fire_rocket": "🔥 إشعال كامل الطاقة",
        "rocket_success": "🚀 تم إطلاق الصاروخ بنجاح وتجاوز الغلاف الجوي! الارتفاع: 320 كم.",
        "hr": "معدل ضربات القلب", "oxy": "أكسجين المقصورة", "stress": "الإجهاد العصبي",
        "badge_title": "🏅 تدريب خبراء رواد الفضاء ناسا وألعاب المحاكاة التفاعلية",
        "badge_desc": "أكمل ألعاب محاكاة المهام أدناه بنجاح لكسب الشارات!",
        "zg_title": "🛸 المهمة 1: محاكاة التوازن في انعدام الجاذبية (Zero-G)",
        "zg_btn": "⚖️ توازن (+34 نقطة)",
        "eva_title": "🛰️ المهمة 2: إصلاح لوحة السير في الفضاء لمحطة الفضاء الدولية (EVA)",
        "eva_btn": "🔧 توصيل الكابلات (+50 نقطة)",
        "nav_title": "🪐 المهمة 3: رسم مسار الفضاء العميق والملاحة",
        "nav_btn": "🧭 قفل الإحداثيات (+50 نقطة)",
        "badge_board": "🏅 لوحة شارات خبراء ناسا الرسمية",
        "earned": "تم الكسب ✅", "waiting": "في انتظار الاختبار",
        "radar_title": "☄️ محاكي رادار الحطام الفضائي وتجنب الاصطدام",
        "radar_btn": "🚨 بدء مناورة الهروب المستقلة",
        "radar_success": "🎉 نجاح! تم تشغيل دافعات RCS وتجنب الحطام الفضائي.",
        "ai_title": "🛰️ بيانات الفضاء الحية ومساعد Lidya AI الصوتي",
        "ai_desc": "محطة قمرة القيادة الذكية حيث يمكنك التفاعل الصوتي مع الذكاء الاصطناعي.",
        "sys_status": "📡 حالة النظام",
        "iss_stat": "🟢 **موقع محطة الفضاء الدولية:** نشط في المدار (الارتفاع: 418 كم)",
        "solar_stat": "🟢 **النشاط الشمسي (الرياح الشمسية):** مستوى طبيعي (420 كم/ث)",
        "neo_stat": "🟢 **الأجسام القريبة من الأرض (NEO):** ضمن الحدود الآمنة.",
        "ai_terminal": "🤖 مساعد Lidya AI الصوتي",
        "ask_ph": "سؤالك:",
        "default_q": "ما هي الإجراءات الطارئة في حال انخفاض ضغط المقصورة؟",
        "ai_ans_label": "🤖 **إجابة Lidya AI:** ",
        "play_voice": "🔊 تشغيل الرد الصوتي لـ Lidya AI",
        "lang_code": "ar-SA"
    },
    "Deutsch": {
        "title": "🌌 NEURO-AURA: 3D Interaktive Weltraum- & Missionssuite",
        "subtitle": "NASA Space Apps Challenge - Astronauten-Trainings- & Simulationssystem",
        "select_sim": "Simulationsmodus wählen",
        "modes": [
            "🪐 Sonnensystem, 8 Planeten & Monde (3D)",
            "🚀 Realistischer 3D-Raketenstart- & Orbit-Simulator",
            "🌐 3D Live-Cockpit & EKG Biometrischer Monitor",
            "🏅 NASA Astronauten-Training & Abzeichen-Center (3D)",
            "☄️ 3D Weltraummüll- & Radar-Vermeidungssimulator",
            "🛰️ Live-Weltraumdaten & Sprachgesteuerter Lidya AI Assistent"
        ],
        "speed": "Simulationsgeschwindigkeit",
        "throttle": "Triebwerksschub (Throttle %)",
        "fire_rocket": "🔥 Vollkraft-Zündung",
        "rocket_success": "🚀 Rakete erfolgreich gestartet und die Atmosphäre verlassen! Höhe: 320 km.",
        "hr": "Herzfrequenz", "oxy": "Kabinen-Sauerstoff", "stress": "Neuro-Stress",
        "badge_title": "🏅 NASA Astronauten-Experten-Training & Interaktive Simulationsspiele",
        "badge_desc": "Schließe die folgenden Mini-Missionsspiele erfolgreich ab, um Abzeichen zu verdienen!",
        "zg_title": "🛸 Mission 1: Schwerelosigkeits-Gleichgewichtssimulation (Zero-G)",
        "zg_btn": "⚖️ Ausgleichen (+34 Pkt)",
        "eva_title": "🛰️ Mission 2: ISS-Außenbordeinsatz (EVA) Panel-Reparatur",
        "eva_btn": "🔧 Kabel verbinden (+50 Pkt)",
        "nav_title": "🪐 Mission 3: Deep-Space-Routenplanung & Navigation",
        "nav_btn": "🧭 Koordinaten sperren (+50 Pkt)",
        "badge_board": "🏅 Offizielle NASA-Experten-Abzeichentafel",
        "earned": "Erworben ✅", "waiting": "Test ausstehend",
        "radar_title": "☄️ 3D Weltraummüll-Radar & Vermeidungssimulator",
        "radar_btn": "🚨 Autonomes Ausweichmanöver einleiten",
        "radar_success": "🎉 Erfolg! RCS-Triebwerke aktiviert und Weltraummüll ausgewichen.",
        "ai_title": "🛰️ Live-Weltraumdaten & Sprachgesteuerter Lidya AI Assistent",
        "ai_desc": "Intelligentes Cockpit-Terminal für den sprachbasierten Dialog mit KI.",
        "sys_status": "📡 Systemstatus",
        "iss_stat": "🟢 **ISS-Position:** Aktiv im Orbit (Höhe: 418 km)",
        "solar_stat": "🟢 **Sonnenaktivität (Sonnenwind):** Normal (420 km/s)",
        "neo_stat": "🟢 **Erdnahe Objekte (NEO):** Im sicheren Bereich.",
        "ai_terminal": "🤖 Sprach-Lidya AI Assistent",
        "ask_ph": "Ihre Frage:",
        "default_q": "Was ist das Notfallverfahren bei einem Abfall des Kabinendrucks?",
        "ai_ans_label": "🤖 **Lidya AI Antwort:** ",
        "play_voice": "🔊 Lidya AI Sprachantwort abspielen",
        "lang_code": "de-DE"
    },
    "Français": {
        "title": "🌌 NEURO-AURA: Suite Spatiale & de Mission Interactive 3D",
        "subtitle": "NASA Space Apps Challenge - Système d'Entraînement & de Simulation pour Astronautes",
        "select_sim": "Sélectionner le mode de simulation",
        "modes": [
            "🪐 Système Solaire, 8 Planètes & Satellites (3D)",
            "🚀 Simulateur Réaliste de Lancement de Fusée & d'Orbite (3D)",
            "🌐 Cockpit 3D en Direct & Moniteur Biométrique ECG",
            "🏅 Centre d'Entraînement & de Badges d'Astronaute de la NASA (3D)",
            "☄️ Simulateur 3D de Débris Spatiaux & d'Évitement Radar",
            "🛰️ Données Spatiales en Direct & Assistant Vocal Lidya AI"
        ],
        "speed": "Vitesse de Simulation",
        "throttle": "Poussée du Moteur (Throttle %)",
        "fire_rocket": "🔥 Allumage Pleine Puissance",
        "rocket_success": "🚀 Fusée lancée avec succès et sortie de l'atmosphère ! Altitude : 320 km.",
        "hr": "Fréquence Cardiaque", "oxy": "Oxygène de Cabine", "stress": "Neuro-Stress",
        "badge_title": "🏅 Entraînement d'Expert de la NASA & Jeux de Simulation Interactifs",
        "badge_desc": "Terminez avec succès les mini-jeux de mission ci-dessous pour gagner des badges !",
        "zg_title": "🛸 Mission 1 : Simulation d'Équilibre en Zéro-G",
        "zg_btn": "⚖️ Équilibrer (+34 pts)",
        "eva_title": "🛰️ Mission 2 : Réparation de Panneau ISS (EVA)",
        "eva_btn": "🔧 Connecter les câbles (+50 pts)",
        "nav_title": "🪐 Mission 3 : Traçage de Route en Espace Profond & Navigation",
        "nav_btn": "🧭 Verrouiller les coordonnées (+50 pts)",
        "badge_board": "🏅 Tableau Officiel des Badges d'Experts de la NASA",
        "earned": "Obtenu ✅", "waiting": "En attente",
        "radar_title": "☄️ Simulateur Radar de Débris Spatiaux & d'Évitement",
        "radar_btn": "🚨 Initier la Manœuvre d'Évitement Autonome",
        "radar_success": "🎉 Succès ! Propulseurs RCS activés, débris évités.",
        "ai_title": "🛰️ Données Spatiales en Direct & Assistant Vocal Lidya AI",
        "ai_desc": "Terminal de cockpit intelligent pour dialoguer vocalement avec l'IA.",
        "sys_status": "📡 Statut du Système",
        "iss_stat": "🟢 **Position de l'ISS :** Active en orbite (Altitude : 418 km)",
        "solar_stat": "🟢 **Activité Solaire (Vent Solaire) :** Niveau Normal (420 km/s)",
        "neo_stat": "🟢 **Objets Proches de la Terre (NEO) :** Dans les limites de sécurité.",
        "ai_terminal": "🤖 Assistant Vocal Lidya AI",
        "ask_ph": "Votre Question :",
        "default_q": "Quelle est la procédure d'urgence en cas de baisse de pression ?",
        "ai_ans_label": "🤖 **Réponse de Lidya AI :** ",
        "play_voice": "🔊 Lire la Réponse Vocale de Lidya AI",
        "lang_code": "fr-FR"
    },
    "Español": {
        "title": "🌌 NEURO-AURA: Suite Espacial y de Misión Interactiva 3D",
        "subtitle": "NASA Space Apps Challenge - Sistema de Entrenamiento y Simulación para Astronautas",
        "select_sim": "Seleccionar Modo de Simulación",
        "modes": [
            "🪐 Sistema Solar, 8 Planetas y Lunas (3D)",
            "🚀 Simulador Realista de Lanzamiento de Cohetes y Órbita (3D)",
            "🌐 Cabina 3D en Vivo y Monitor Biomédico ECG",
            "🏅 Centro de Entrenamiento y Medallas de Astronautas de la NASA (3D)",
            "☄️ Simulador 3D de Desechos Espaciales y Evasión por Radar",
            "🛰️ Datos Espaciales en Vivo y Asistente de Voz Lidya AI"
        ],
        "speed": "Velocidad de Simulación",
        "throttle": "Aceleración del Motor (Throttle %)",
        "fire_rocket": "🔥 Encendido a Plena Potencia",
        "rocket_success": "🚀 ¡Cohete lanzado con éxito y fuera de la atmósfera! Altitud: 320 km.",
        "hr": "Ritmo Cardíaco", "oxy": "Oxígeno en Cabina", "stress": "Neuro-Estrés",
        "badge_title": "🏅 Entrenamiento de Expertos de la NASA y Juegos de Simulación Interactivos",
        "badge_desc": "¡Completa con éxito los mini juegos de misión a continuación para ganar medallas!",
        "zg_title": "🛸 Misión 1: Simulación de Equilibrio en Gravedad Cero (Zero-G)",
        "zg_btn": "⚖️ Equilibrar (+34 Pts)",
        "eva_title": "🛰️ Misión 2: Reparación de Panel ISS (EVA)",
        "eva_btn": "🔧 Conectar cables (+50 Pts)",
        "nav_title": "🪐 Misión 3: Ruta del Espacio Profundo y Navegación",
        "nav_btn": "🧭 Bloquear coordenadas (+50 Pts)",
        "badge_board": "🏅 Panel Oficial de Medallas de Expertos de la NASA",
        "earned": "Obtenido ✅", "waiting": "Pendiente",
        "radar_title": "☄️ Simulador de Radar de Desechos Espaciales y Evasión",
        "radar_btn": "🚨 Iniciar Maniobra de Evasión Autónoma",
        "radar_success": "🎉 ¡Éxito! Propulsores RCS activados, desechos evitados.",
        "ai_title": "🛰️ Datos Espaciales en Vivo y Asistente de Voz Lidya AI",
        "ai_desc": "Terminal de cabina inteligente para interactuar por voz con la IA.",
        "sys_status": "📡 Estado del Sistema",
        "iss_stat": "🟢 **Posición de la ISS:** Activa en órbita (Altitud: 418 km)",
        "solar_stat": "🟢 **Actividad Solar (Viento Solar):** Nivel Normal (420 km/s)",
        "neo_stat": "🟢 **Objetos Cercanos a la Tierra (NEO):** Dentro de límites seguros.",
        "ai_terminal": "🤖 Asistente de Voz Lidya AI",
        "ask_ph": "Su Pregunta:",
        "default_q": "¿Cuál es el procedimiento de emergencia si baja la presión en cabina?",
        "ai_ans_label": "🤖 **Respuesta de Lidya AI:** ",
        "play_voice": "🔊 Reproducir Respuesta de Voz de Lidya AI",
        "lang_code": "es-ES"
    }
}

# DİL SEÇİMİ (SİDEBAR)
selected_lang_name = st.sidebar.selectbox("🌐 Dil / Language / اللغة / Sprache", list(LANGS.keys()))
t = LANGS[selected_lang_name]

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at center, #0B1021 0%, #03050C 100%); color: #E2E8F0; }
    .metric-card { background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(56, 189, 248, 0.4); padding: 20px; border-radius: 12px; text-align: center; box-shadow: 0 0 15px rgba(56, 189, 248, 0.2); }
    .stButton>button { background: linear-gradient(90deg, #0284c7 0%, #2563eb 100%); color: white; font-weight: bold; border-radius: 8px; padding: 12px 24px; box-shadow: 0 0 15px rgba(37, 99, 235, 0.5); }
    </style>
""", unsafe_allow_html=True)

st.title(t["title"])
st.markdown(f"### *{t['subtitle']}*")

sim_mode = st.sidebar.selectbox(t["select_sim"], t["modes"])

if sim_mode == t["modes"][0]:
    st.subheader(t["modes"][0])
    speed_factor = st.slider(t["speed"], 1, 30, 5)
    
    sol_html = """
    <div style='width:100%; height:550px; background:#000; border-radius:12px; overflow:hidden; position:relative; border:2px solid #38bdf8;'>
        <div style='position:absolute; top:12px; left:12px; color:#00f0ff; font-family:monospace; background:rgba(0,0,0,0.85); padding:8px 12px; border-radius:6px; border:1px solid #00f0ff; z-index:10; font-size:13px;'>☀️ 3D GÜNEŞ SİSTEMİ & UYDULAR</div>
        <canvas id='scs' style='width:100%; height:100%; display:block;'></canvas>
    </div>
    <script>
        const canvas = document.getElementById('scs');
        const ctx = canvas.getContext('2d');
        function resize() { canvas.width = canvas.parentElement.clientWidth; canvas.height = 550; }
        resize(); window.onresize = resize;
        let stars = [];
        for(let i=0; i<900; i++) { stars.push({ x: (Math.random()-0.5)*canvas.width, y: (Math.random()-0.5)*canvas.height, z: Math.random()*canvas.width }); }
        let bodies = [
            { x: -380, y: 0, r: 50, name: '☀️ Güneş', z: 650, c1: '#ffcc00', c2: '#ff3300', ring: false },
            { x: -300, y: -45, r: 10, name: '☿ Merkür', z: 600, c1: '#b0b0b0', c2: '#505050', ring: false },
            { x: -220, y: 55, r: 16, name: '♀ Venüs', z: 560, c1: '#e3bb76', c2: '#8c6724', ring: false },
            { x: -140, y: -25, r: 19, name: '🜨 Dünya (+Ay)', z: 520, c1: '#38bdf8', c2: '#1d4ed8', ring: false },
            { x: -60, y: 65, r: 14, name: '♂ Mars (+Phobos)', z: 480, c1: '#ff7b54', c2: '#933215', ring: false },
            { x: 30, y: -55, r: 35, name: '♃ Jüpiter (+Europa)', z: 430, c1: '#e0ae6f', c2: '#8b5a2b', ring: false },
            { x: 120, y: 45, r: 30, name: '♄ Saturn (+Titan & Halka)', z: 380, c1: '#fcd34d', c2: '#b45309', ring: true },
            { x: 200, y: -35, r: 23, name: '♅ Uranüs', z: 330, c1: '#67e8f9', c2: '#0e7490', ring: false },
            { x: 280, y: 45, r: 22, name: '♆ Neptün', z: 290, c1: '#3b82f6', c2: '#1e3a8a', ring: false },
            { x: 350, y: -25, r: 8, name: '♇ Plüton', z: 250, c1: '#d1d5db', c2: '#4b5563', ring: false }
        ];
        function draw() {
            ctx.fillStyle = 'rgba(3, 5, 12, 0.45)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            let cx = canvas.width / 2, cy = canvas.height / 2;
            for(let i=0; i<stars.length; i++) {
                let s = stars[i]; s.Z -= 2.5;
                if(s.Z <= 0) { s.Z = canvas.width; s.X = (Math.random()-0.5)*canvas.width; s.Y = (Math.random()-0.5)*canvas.height; }
                let k = 100.0 / s.Z, px = s.X * k + cx, py = s.Y * k + cy;
                if(px >= 0 && px <= canvas.width && py >= 0 && py <= canvas.height) {
                    ctx.fillStyle = '#fff'; ctx.fillRect(px, py, 1.8, 1.8);
                }
            }
            for(let j=0; j<bodies.length; j++) {
                let b = bodies[j]; b.z -= 1.2;
                if(b.z <= 20) b.z = 950;
                let bk = 160.0 / b.z, bpx = b.x * bk + cx, bpy = b.y * bk + cy, br = b.r * bk;
                if(br < 0) continue;
                if(b.ring) {
                    ctx.save(); ctx.beginPath();
                    ctx.ellipse(bpx, bpy, br * 2.2, br * 0.7, Math.PI / 6, 0, Math.PI * 2);
                    ctx.strokeStyle = 'rgba(245, 158, 11, 0.8)'; ctx.lineWidth = br * 0.28; ctx.stroke();
                    ctx.restore();
                }
                let grad = ctx.createRadialGradient(bpx - br*0.3, bpy - br*0.3, br*0.1, bpx, bpy, br);
                grad.addColorStop(0, b.c1); grad.addColorStop(1, b.c2);
                ctx.beginPath(); ctx.arc(bpx, bpy, br, 0, Math.PI * 2); ctx.fillStyle = grad; ctx.fill();
                ctx.fillStyle = '#f1f5f9'; ctx.font = 'bold 12px monospace';
                ctx.fillText(b.name, bpx + br + 10, bpy + 4);
            }
            requestAnimationFrame(draw);
        }
        draw();
    </script>
    """
    components.html(sol_html, height=570)

elif sim_mode == t["modes"][1]:
    st.subheader(t["modes"][1])
    throttle = st.slider(t["throttle"], 0, 100, 90)
    
    pro_rocket_html = """
    <div style='width:100%; height:520px; background:#000; border-radius:12px; overflow:hidden; position:relative; border:2px solid #38bdf8;'>
        <div style='position:absolute; top:12px; left:12px; color:#00f0ff; font-family:monospace; background:rgba(0,0,0,0.85); padding:8px 12px; border-radius:6px; border:1px solid #00f0ff; z-index:10; font-size:13px;'>🚀 PRO ROKET FIRLATMA SİSTEMİ</div>
        <canvas id='proRocket' style='width:100%; height:100%; display:block;'></canvas>
    </div>
    <script>
        const prCanvas = document.getElementById('proRocket');
        const prCtx = prCanvas.getContext('2d');
        function prResize() { prCanvas.width = prCanvas.parentElement.clientWidth; prCanvas.height = 520; }
        prResize(); window.onresize = prResize;
        let rY = 360; let pStars = [];
        for(let i=0; i<300; i++) { pStars.push({ x: Math.random()*prCanvas.width, y: Math.random()*prCanvas.height, s: Math.random()*2 }); }
        function prDraw() {
            prCtx.fillStyle = 'rgba(3, 5, 12, 0.4)'; prCtx.fillRect(0, 0, prCanvas.width, prCanvas.height);
            let cx = prCanvas.width / 2; prCtx.fillStyle = '#ffffff';
            pStars.forEach(st => {
                prCtx.fillRect(st.x, st.y, st.s, st.s);
                if(rY < 250) st.y += 2;
                if(st.y > prCanvas.height) st.y = 0;
            });
            prCtx.fillStyle = '#1e293b'; prCtx.fillRect(cx - 70, 440, 140, 25);
            prCtx.fillStyle = '#334155'; prCtx.fillRect(cx - 40, 410, 80, 30);
            prCtx.fillRect(cx - 65, 320, 12, 120); prCtx.fillRect(cx + 53, 320, 12, 120);
            let rGrad = prCtx.createLinearGradient(cx - 18, 0, cx + 18, 0);
            rGrad.addColorStop(0, '#64748b'); rGrad.addColorStop(0.3, '#f8fafc'); rGrad.addColorStop(0.7, '#cbd5e1'); rGrad.addColorStop(1, '#475569');
            prCtx.fillStyle = rGrad; prCtx.beginPath();
            prCtx.moveTo(cx, rY - 70); prCtx.lineTo(cx - 18, rY - 30);
            prCtx.lineTo(cx - 18, rY + 80); prCtx.lineTo(cx + 18, rY + 80);
            prCtx.lineTo(cx + 18, rY - 30); prCtx.closePath(); prCtx.fill();
            prCtx.fillStyle = '#dc2626'; prCtx.beginPath();
            prCtx.moveTo(cx, rY - 95); prCtx.lineTo(cx - 18, rY - 70); prCtx.lineTo(cx + 18, rY - 70); prCtx.closePath(); prCtx.fill();
            prCtx.fillStyle = '#0f172a'; prCtx.fillRect(cx - 18, rY + 10, 36, 6);
            prCtx.fillRect(cx - 18, rY + 45, 36, 6);
            prCtx.fillStyle = '#94a3b8'; prCtx.fillRect(cx - 32, rY - 10, 12, 80);
            prCtx.fillRect(cx + 20, rY - 10, 12, 80);
            prCtx.fillStyle = '#2563eb';
            prCtx.beginPath(); prCtx.moveTo(cx - 18, rY + 50); prCtx.lineTo(cx - 36, rY + 85); prCtx.lineTo(cx - 18, rY + 75); prCtx.closePath(); prCtx.fill();
            prCtx.beginPath(); prCtx.moveTo(cx + 18, rY + 50); prCtx.lineTo(cx + 36, rY + 85); prCtx.lineTo(cx + 18, rY + 75); prCtx.closePath(); prCtx.fill();
            let fGrad = prCtx.createRadialGradient(cx, rY + 90, 2, cx, rY + 110, 45);
            fGrad.addColorStop(0, '#fef08a'); fGrad.addColorStop(0.4, '#f97316'); fGrad.addColorStop(1, 'transparent');
            prCtx.fillStyle = fGrad; prCtx.beginPath(); prCtx.arc(cx, rY + 95, 45, 0, Math.PI * 2); prCtx.fill();
            if (rY > 140) { rY -= 0.8; }
            requestAnimationFrame(prDraw);
        }
        prDraw();
    </script>
    """
    components.html(pro_rocket_html, height=540)
    if st.button(t["fire_rocket"]):
        st.success(t["rocket_success"])
        st.balloons()

elif sim_mode == t["modes"][2]:
    st.subheader(t["modes"][2])
    
    ecg_html = """
    <div style='width:100%; height:450px; background:#000; border-radius:12px; overflow:hidden; position:relative; border:2px solid #38bdf8;'>
        <div style='position:absolute; top:12px; left:12px; color:#00f0ff; font-family:monospace; background:rgba(0,0,0,0.85); padding:8px 12px; border-radius:6px; border:1px solid #00f0ff; z-index:10; font-size:13px;'>❤️ EKG NÖRO-MONİTÖR | Nabız: 74 BPM</div>
        <canvas id='ecanvas' style='width:100%; height:100%; display:block;'></canvas>
    </div>
    <script>
        const ecanvas = document.getElementById('ecanvas');
        const ectx = ecanvas.getContext('2d');
        function eresize() { ecanvas.width = ecanvas.parentElement.clientWidth; ecanvas.height = 450; }
        eresize(); window.onresize = eresize;
        let xPos = 0; let yPos = 225;
        ectx.strokeStyle = '#38bdf8'; ectx.lineWidth = 3;
        function edraw() {
            ectx.fillStyle = 'rgba(3, 5, 12, 0.1)'; ectx.fillRect(0, 0, ecanvas.width, ecanvas.height);
            ectx.beginPath(); ectx.moveTo(xPos, yPos);
            xPos += 3.5;
            if (xPos > ecanvas.width) { xPos = 0; ectx.clearRect(0, 0, ecanvas.width, ecanvas.height); }
            let offset = Math.sin(xPos * 0.04);
            if (xPos % 160 > 65 && xPos % 160 < 80) {
                yPos = 225 + (xPos % 2 === 0 ? -110 : 110);
            } else {
                yPos = 225 + offset * 12;
            }
            ectx.lineTo(xPos, yPos);
            ectx.strokeStyle = '#38bdf8'; ectx.shadowBlur = 12; ectx.shadowColor = '#38bdf8';
            ectx.stroke();
            requestAnimationFrame(edraw);
        }
        edraw();
    </script>
    """
    components.html(ecg_html, height=470)
    c1, c2, c3 = st.columns(3)
    c1.markdown(f'<div class="metric-card"><h3>❤️ {t["hr"]}</h3><h2>74 bpm</h2></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="metric-card"><h3>🧪 {t["oxy"]}</h3><h2>99.7%</h2></div>', unsafe_allow_html=True)
    c3.markdown(f'<div class="metric-card"><h3>🧠 {t["stress"]}</h3><h2>%10</h2></div>', unsafe_allow_html=True)

elif sim_mode == t["modes"][3]:
    st.subheader(t["badge_title"])
    st.write(t["badge_desc"])

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
        st.markdown(f"#### {t['zg_title']}")
        zg_game_html = """
        <div style='width:100%; height:240px; background:#000; border-radius:12px; position:relative; border:2px solid #38bdf8;'>
            <canvas id='zgCan' style='width:100%; height:100%; display:block;'></canvas>
        </div>
        <script>
            const zgC = document.getElementById('zgCan');
            const zgCtx = zgC.getContext('2d');
            zgC.width = zgC.parentElement.clientWidth; zgC.height = 240;
            let zgY = 120; let zgSpeed = 1.5;
            function drawZG() {
                zgCtx.fillStyle = 'rgba(3,5,12,0.3)'; zgCtx.fillRect(0,0,zgC.width,zgC.height);
                let cx = zgC.width/2; zgY += zgSpeed;
                if(zgY > 200 || zgY < 40) zgSpeed *= -1;
                zgCtx.fillStyle = '#38bdf8'; zgCtx.beginPath(); zgCtx.arc(cx, zgY, 16, 0, Math.PI*2); zgCtx.fill();
                zgCtx.strokeStyle = '#22c55e'; zgCtx.lineWidth = 3; zgCtx.strokeRect(cx - 35, 90, 70, 60);
                requestAnimationFrame(drawZG);
            }
            drawZG();
        </script>
        """
        components.html(zg_game_html, height=260)
    with col_zg2:
        st.progress(st.session_state.zg_score / 100)
        if st.button(t["zg_btn"], key="btn_zg"):
            st.session_state.zg_score = min(100, st.session_state.zg_score + 34)
            if st.session_state.zg_score >= 100 and not st.session_state.badges["zero_g"]:
                st.session_state.badges["zero_g"] = True
                st.balloons()

    st.markdown("---")

    col_ev1, col_ev2 = st.columns([2, 1])
    with col_ev1:
        st.markdown(f"#### {t['eva_title']}")
        eva_game_html = """
        <div style='width:100%; height:240px; background:#000; border-radius:12px; position:relative; border:2px solid #38bdf8;'>
            <canvas id='evaCan' style='width:100%; height:100%; display:block;'></canvas>
        </div>
        <script>
            const evaC = document.getElementById('evaCan');
            const evaCtx = evaC.getContext('2d');
            evaC.width = evaC.parentElement.clientWidth; evaC.height = 240;
            let eX = 20;
            function drawEVA() {
                evaCtx.fillStyle = 'rgba(3,5,12,0.3)'; evaCtx.fillRect(0,0,evaC.width,evaC.height);
                evaCtx.fillStyle = '#ef4444'; evaCtx.fillRect(eX, 100, 40, 40);
                evaCtx.fillStyle = '#22c55e'; evaCtx.fillRect(evaC.width - 80, 90, 60, 60);
                requestAnimationFrame(drawEVA);
            }
            drawEVA();
        </script>
        """
        components.html(eva_game_html, height=260)
    with col_ev2:
        st.progress(st.session_state.eva_score / 100)
        if st.button(t["eva_btn"], key="btn_eva"):
            st.session_state.eva_score = min(100, st.session_state.eva_score + 50)
            if st.session_state.eva_score >= 100 and not st.session_state.badges["eva"]:
                st.session_state.badges["eva"] = True
                st.balloons()

    st.markdown("---")

    col_nv1, col_nv2 = st.columns([2, 1])
    with col_nv1:
        st.markdown(f"#### {t['nav_title']}")
        nav_game_html = """
        <div style='width:100%; height:240px; background:#000; border-radius:12px; position:relative; border:2px solid #38bdf8;'>
            <canvas id='navCan' style='width:100%; height:100%; display:block;'></canvas>
        </div>
        <script>
            const navC = document.getElementById('navCan');
            const navCtx = navC.getContext('2d');
            navC.width = navC.parentElement.clientWidth; navC.height = 240;
            let nA = 0;
            function drawNav() {
                navCtx.fillStyle = 'rgba(3,5,12,0.3)'; navCtx.fillRect(0,0,navC.width,navC.height);
                nA += 0.03; let cx = navC.width/2, cy = 120;
                navCtx.strokeStyle = '#38bdf8'; navCtx.lineWidth = 2;
                navCtx.beginPath(); navCtx.arc(cx, cy, 70, 0, Math.PI*2); navCtx.stroke();
                navCtx.fillStyle = '#f59e0b'; navCtx.beginPath();
                navCtx.arc(cx + Math.cos(nA)*70, cy + Math.sin(nA)*70, 10, 0, Math.PI*2);
                navCtx.fill();
                requestAnimationFrame(drawNav);
            }
            drawNav();
        </script>
        """
        components.html(nav_game_html, height=260)
    with col_nv2:
        st.progress(st.session_state.nav_score / 100)
        if st.button(t["nav_btn"], key="btn_nav"):
            st.session_state.nav_score = min(100, st.session_state.nav_score + 50)
            if st.session_state.nav_score >= 100 and not st.session_state.badges["nav"]:
                st.session_state.badges["nav"] = True
                st.balloons()

    st.markdown("---")
    st.markdown(f"### {t['badge_board']}")
    b_col1, b_col2, b_col3 = st.columns(3)
    
    with b_col1:
        st.markdown(f"<div style='text-align:center; padding:15px; background:rgba(56,189,248,0.2); border:2px solid #38bdf8; border-radius:12px;'><h1>🛸</h1><b>Zero-G Master</b><br><small style='color:#4ade80;'>{t['earned'] if st.session_state.badges['zero_g'] else t['waiting']}</small></div>", unsafe_allow_html=True)
    with b_col2:
        st.markdown(f"<div style='text-align:center; padding:15px; background:rgba(56,189,248,0.2); border:2px solid #38bdf8; border-radius:12px;'><h1>👨‍🚀</h1><b>EVA Specialist</b><br><small style='color:#4ade80;'>{t['earned'] if st.session_state.badges['eva'] else t['waiting']}</small></div>", unsafe_allow_html=True)
    with b_col3:
        st.markdown(f"<div style='text-align:center; padding:15px; background:rgba(56,189,248,0.2); border:2px solid #38bdf8; border-radius:12px;'><h1>🚀</h1><b>Deep Space Cmd</b><br><small style='color:#4ade80;'>{t['earned'] if st.session_state.badges['nav'] else t['waiting']}</small></div>", unsafe_allow_html=True)

elif sim_mode == t["modes"][4]:
    st.subheader(t["radar_title"])
    radar_html = """
    <div style='width:100%; height:480px; background:#000; border-radius:12px; overflow:hidden; position:relative; border:2px solid #38bdf8;'>
        <div style='position:absolute; top:12px; left:12px; color:#00f0ff; font-family:monospace; background:rgba(0,0,0,0.85); padding:8px 12px; border-radius:6px; border:1px solid #00f0ff; z-index:10; font-size:13px;'>📡 RADAR TARAMA: AKTİF</div>
        <canvas id='rcan' style='width:100%; height:100%; display:block;'></canvas>
    </div>
    <script>
        const rcan = document.getElementById('rcan');
        const rctx2 = rcan.getContext('2d');
        function rres() { rcan.width = rcan.parentElement.clientWidth; rcan.height = 480; }
        rres(); window.onresize = rres;
        let angle = 0;
        let debris = [ {x: 140, y: -90}, {x: -160, y: 110}, {x: 60, y: 150} ];
        function drawRadar() {
            rctx2.fillStyle = 'rgba(3, 5, 12, 0.25)'; rctx2.fillRect(0, 0, rcan.width, rcan.height);
            let cx = rcan.width / 2, cy = rcan.height / 2;
            rctx2.strokeStyle = 'rgba(56, 189, 248, 0.35)'; rctx2.lineWidth = 1.5;
            [70, 140, 210].forEach(r => {
                rctx2.beginPath(); rctx2.arc(cx, cy, r, 0, Math.PI*2); rctx2.stroke();
            });
            angle += 0.035;
            rctx2.save(); rctx2.translate(cx, cy); rctx2.rotate(angle);
            let grad = rctx2.createLinearGradient(0, 0, 210, 0);
            grad.addColorStop(0, 'rgba(56, 189, 248, 0.85)'); grad.addColorStop(1, 'transparent');
            rctx2.fillStyle = grad; rctx2.beginPath(); rctx2.moveTo(0,0); rctx2.arc(0,0, 210, 0, 0.5); rctx2.lineTo(0,0); rctx2.fill();
            rctx2.restore();
            debris.forEach(d => {
                rctx2.fillStyle = '#ef4444'; rctx2.shadowBlur = 15; rctx2.shadowColor = '#ef4444';
                rctx2.beginPath(); rctx2.arc(cx + d.x, cy + d.y, 6, 0, Math.PI*2); rctx2.fill();
                rctx2.shadowBlur = 0;
            });
            requestAnimationFrame(drawRadar);
        }
        drawRadar();
    </script>
    """
    components.html(radar_html, height=500)
    if st.button(t["radar_btn"]):
        st.balloons()
        st.success(t["radar_success"])

else:
    st.subheader(t["ai_title"])
    st.write(t["ai_desc"])
    
    col_n1, col_n2 = st.columns(2)
    with col_n1:
        st.markdown(f"### {t['sys_status']}")
        st.info(t["iss_stat"])
        st.info(t["solar_stat"])
        st.info(t["neo_stat"])
        
    with col_n2:
        st.markdown(f"### {t['ai_terminal']}")
        user_q = st.text_input(t["ask_ph"], t["default_q"])
        
        ai_response = f"{t['ai_ans_label']} {user_q} - Telemetry optimal."
        if selected_lang_name == "Türkçe":
            if "basınç" in user_q.lower() or "acil" in user_q.lower():
                ai_response = "Kabin basıncı düşerse: 1. Oksijen maskelerini takın. 2. Sızdırmazlık vanalarını kapatın. 3. Dünya kontrol merkezi ile iletişime geçin."
            else:
                ai_response = f"Lidya AI: Sorguladığınız '{user_q}' verileri normal sınırlarda. Göreve devam edebilirsiniz."
        elif selected_lang_name == "English":
            if "pressure" in user_q.lower() or "emergency" in user_q.lower():
                ai_response = "Lidya AI: If cabin pressure drops: 1. Don oxygen masks. 2. Close sealing valves. 3. Contact ground control."
            else:
                ai_response = f"Lidya AI: Telemetry for '{user_q}' is within normal limits. Proceed with mission."
        elif selected_lang_name == "Deutsch":
            if "druck" in user_q.lower() or "notfall" in user_q.lower():
                ai_response = "Lidya AI: Bei Druckabfall: 1. Sauerstoffmasken anlegen. 2. Ventile schließen. 3. Bodenkontrolle kontaktieren."
            else:
                ai_response = f"Lidya AI: Telemetrie für '{user_q}' ist im Normbereich. Fortfahren."
        elif selected_lang_name == "Français":
            if "pression" in user_q.lower() or "urgence" in user_q.lower():
                ai_response = "Lidya AI: Si la pression chute : 1. Mettre les masques. 2. Fermer les vannes. 3. Contacter le sol."
            else:
                ai_response = f"Lidya AI: La télémétrie pour '{user_q}' est normale."
        elif selected_lang_name == "Español":
            if "presión" in user_q.lower() or "emergencia" in user_q.lower():
                ai_response = "Lidya AI: Si baja la presión: 1. Poner mascarillas. 2. Cerrar válvulas. 3. Contactar control."
            else:
                ai_response = f"Lidya AI: La telemetría para '{user_q}' es normal."
        else:
            if "ضغط" in user_q:
                ai_response = "Lidya AI: في حالة انخفاض الضغط: 1. ارتداء أقنعة الأكسجين. 2. إغلاق صمامات الإحكام."
            else:
                ai_response = f"Lidya AI: البيانات الخاصة بـ '{user_q}' طبيعية."
            
        st.success(ai_response)
        
        safe_resp = ai_response.replace('"', '\\"')
        tts_html = f"""
        <div style="margin-top:10px;">
            <button onclick="speakText()" style="background:linear-gradient(90deg, #0284c7, #2563eb); color:white; border:none; padding:10px 20px; border-radius:8px; font-weight:bold; cursor:pointer; box-shadow:0 0 10px rgba(56,189,248,0.5);">{t["play_voice"]}</button>
        </div>
        <script>
            function speakText() {{
                if ('speechSynthesis' in window) {{
                    window.speechSynthesis.cancel();
                    let utterance = new SpeechSynthesisUtterance("{safe_resp}");
                    utterance.lang = '{t["lang_code"]}';
                    utterance.rate = 1.0;
                    window.speechSynthesis.speak(utterance);
                }} else {{
                    alert('Tarayıcınız ses sentezlemeyi desteklemiyor.');
                }}
            }}
        </script>
        """
        components.html(tts_html, height=60)
