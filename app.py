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
    st.write("Aşağıdaki 3D simülatörde fareyi sürükleyerek kamerayı döndürebilir, uzay boşluğundaki yıldız tarlasında seyahat edebilirsin!")
    
    # Three.js Tabanlı Canlı 3D Yıldız Tarlası & Seyahat Simülasyonu (HTML/JS)
    threejs_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { margin: 0; overflow: hidden; background-color: #000; }
            canvas { display: block; width: 100vw; height: 500px; }
            #info {
                position: absolute;
                top: 10px;
                left: 10px;
                color: #00f0ff;
                font-family: monospace;
                font-size: 14px;
                background: rgba(0,0,0,0.6);
                padding: 8px 12px;
                border-radius: 5px;
                border: 1px solid #00f0ff;
            }
        </style>
    </head>
    <body>
        <div id="info">🚀 WARP HIZI: ACTIVE | Fare ile bakış açısını değiştirin</div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script>
            let scene, camera, renderer, stars, starGeo;
            let count = 4000;

            function init() {
                scene = new THREE.Scene();
                camera = new THREE.PerspectiveCamera(60, window.innerWidth / 500, 1, 1000);
                camera.position.z = 1;
                camera.rotation.x = Math.PI/2;

                renderer = new THREE.WebGLRenderer();
                renderer.setSize(window.innerWidth, 500);
                document.body.appendChild(renderer.domElement);

                starGeo = new THREE.BufferGeometry();
                let positions = new Float32Array(count * 3);

                for(let i=0; i<count*3; i+=3) {
                    positions[i] = Math.random() * 600 - 300;
                    positions[i+1] = Math.random() * 600 - 300;
                    positions[i+2] = Math.random() * 600 - 300;
                }

                starGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));

                let sprite = new THREE.TextureLoader().load('https://threejs.org/examples/textures/sprites/disc.png');
                let starMaterial = new THREE.PointsMaterial({
                    color: 0x38bdf8,
                    size: 0.8,
                    transparent: true
                });

                stars = new THREE.Points(starGeo, starMaterial);
                scene.add(stars);

                window.addEventListener("resize", onWindowResize, false);
                animate();
            }

            function onWindowResize() {
                camera.aspect = window.innerWidth / 500;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, 500);
            }

