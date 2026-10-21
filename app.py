import math
import streamlit as st

st.set_page_config(
    page_title="NEURO-AURA | Junior Astronaut Trainer",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------
# LANGUAGE
# ---------------------------

LANG = {
    "Türkçe": {
        "title": "NEURO-AURA",
        "subtitle": "Genç Astronot Görev Eğitim Laboratuvarı",
        "mission": "Görev Merkezi",
        "rocket": "Roket Fiziği Laboratuvarı",
        "debris": "Uzay Enkazı Simülatörü",
        "training": "Astronot Eğitimi",
        "health": "Biyometrik Simülasyon",
        "quiz": "Bilim Testi",
        "about": "Proje Hakkında",
        "mass": "Roketin başlangıç kütlesi (kg)",
        "thrust": "Motor itkisi (N)",
        "fuel": "Yakıt kütlesi (kg)",
        "burn": "Motor çalışma süresi (s)",
        "calculate": "Hesapla",
        "scenario": "Görev senaryosu",
        "answer": "Kararını seç",
        "submit": "Kararımı değerlendir",
        "correct": "Doğru karar!",
        "incorrect": "Bu karar en güvenli seçenek değil.",
        "score": "Görev puanı",
        "distance": "En yakın yaklaşma mesafesi (km)",
        "relative_speed": "Göreli hız (km/s)",
        "simulate": "Yaklaşmayı değerlendir",
        "heart": "Örnek kalp atış hızı (atım/dakika)",
        "oxygen": "Örnek oksijen doygunluğu (%)",
        "save": "Eğitim sonuçları",
        "reset": "Puanları sıfırla",
        "disclaimer": "Eğitim prototipidir. Hesaplamalar basitleştirilmiştir; gerçek uzay uçuşlarında kullanılmamalıdır."
    },
    "English": {
        "title": "NEURO-AURA",
        "subtitle": "Junior Astronaut Mission Training Laboratory",
        "mission": "Mission Control",
        "rocket": "Rocket Physics Lab",
        "debris": "Space Debris Simulator",
        "training": "Astronaut Training",
        "health": "Biometric Simulation",
        "quiz": "Science Quiz",
        "about": "About",
        "mass": "Initial rocket mass (kg)",
        "thrust": "Engine thrust (N)",
        "fuel": "Fuel mass (kg)",
        "burn": "Engine burn time (s)",
        "calculate": "Calculate",
        "scenario": "Mission scenario",
        "answer": "Choose your decision",
        "submit": "Evaluate my decision",
        "correct": "Good decision!",
        "incorrect": "This is not the safest option.",
        "score": "Mission score",
        "distance": "Closest approach distance (km)",
        "relative_speed": "Relative speed (km/s)",
        "simulate": "Evaluate approach",
        "heart": "Sample heart rate (beats/minute)",
        "oxygen": "Sample oxygen saturation (%)",
        "save": "Training results",
        "reset": "Reset score",
        "disclaimer": "Educational prototype. Calculations are simplified and must not be used for real spaceflight."
    }
}

language = st.sidebar.selectbox("🌐 Language / Dil", ["Türkçe", "English"])
t = LANG[language]

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = {}

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 15% 15%, #182653 0%, transparent 35%),
        radial-gradient(circle at 85% 80%, #251544 0%, transparent 35%),
        #070b18;
    color: #f5f7ff;
}
section[data-testid="stSidebar"] {
    background: #10162b;
}
h1, h2, h3 {
    color: #b9c8ff;
}
div.stButton > button {
    border-radius: 12px;
    border: 1px solid #7189ff;
    min-height: 42px;
}
.metric-card {
    background: #141d37;
    padding: 18px;
    border-radius: 15px;
    border: 1px solid #35436d;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 " + t["title"])
st.subheader(t["subtitle"])
st.caption("SOLOCODER • Independent educational prototype")

st.info("ℹ️ " + t["disclaimer"])

pages = [
    t["mission"],
    t["rocket"],
    t["debris"],
    t["training"],
    t["health"],
    t["quiz"],
    t["about"]
]

page = st.sidebar.radio("🛰️ Navigation", pages)

st.sidebar.metric(t["score"], st.session_state.score)
if st.sidebar.button(t["reset"]):
    st.session_state.score = 0
    st.session_state.answered = {}
    st.rerun()

# ---------------------------
# MISSION CONTROL
# ---------------------------

if page == t["mission"]:
    st.header("🌌 " + t["mission"])

    col1, col2, col3 = st.columns(3)
    col1.metric("Mission status", "READY")
    col2.metric("Training modules", "5")
    col3.metric("Astronaut rank", "Candidate")

    st.markdown("""
    ### Your mission begins here

    Complete training activities, explore simplified physics,
    and make decisions in astronaut mission scenarios.

    **Mission objectives**
    - Understand basic rocket motion.
    - Learn how relative motion affects collision risk.
    - Practice safe, evidence-based decisions.
    - Check your knowledge with a science quiz.
    """ if language == "English" else """
    ### Görevin burada başlıyor

    Eğitim etkinliklerini tamamla, basitleştirilmiş fizik modellerini
    keşfet ve astronot görevlerinde kararlar ver.

    **Görev hedefleri**
    - Roket hareketinin temel prensiplerini anlamak.
    - Göreli hareketin çarpışma riskini nasıl etkilediğini öğrenmek.
    - Bilimsel verilere dayalı güvenli kararlar vermek.
    - Bilim testiyle bilgini değerlendirmek.
    """)

    st.progress(min(st.session_state.score / 100, 1.0))
    st.write(f'{t["score"]}: {st.session_state.score}')

# ---------------------------
# ROCKET PHYSICS
# ---------------------------

elif page == t["rocket"]:
    st.header("🚀 " + t["rocket"])

    st.write(
        "Bu model, motor itkisinin ve kütlenin idealize edilmiş etkisini gösterir."
        if language == "Türkçe"
        else "This model illustrates the idealized effect of thrust and mass."
    )

    mass = st.number_input(
        t["mass"], min_value=100.0, max_value=1000000.0,
        value=10000.0, step=500.0
    )
    fuel = st.number_input(
        t["fuel"], min_value=0.0, max_value=500000.0,
        value=3000.0, step=100.0
    )
    thrust = st.number_input(
        t["thrust"], min_value=0.0, max_value=50000000.0,
        value=200000.0, step=10000.0
    )
    burn = st.slider(t["burn"], 1, 300, 30)

    if st.button(t["calculate"]):
        if fuel >= mass:
            st.error(
                "Yakıt kütlesi roketin başlangıç kütlesinden küçük olmalı."
                if language == "Türkçe"
                else "Fuel mass must be smaller than initial rocket mass."
            )
        else:
            # Simplified constant-mass approximation.
            # Does not represent a complete launch or orbital model.
            acceleration = thrust / mass
            ideal_delta_v = acceleration * burn
            weight = mass * 9.81
            thrust_to_weight = thrust / weight if weight else 0

            c1, c2 = st.columns(2)
            c1.metric("Initial acceleration", f"{acceleration:.2f} m/s²")
            c2.metric("Idealized Δv", f"{ideal_delta_v:.1f} m/s")

            st.metric("Thrust-to-weight ratio", f"{thrust_to_weight:.2f}")

            if thrust_to_weight <= 1:
                st.warning(
                    "İlk kütle için itki, Dünya'daki ağırlığı aşmıyor."
                    if language == "Türkçe"
                    else "At initial mass, thrust does not exceed Earth's weight."
                )
            else:
                st.success(
                    "İdeal modelde itki/ağırlık oranı 1'den büyük."
                    if language == "Türkçe"
                    else "In this idealized model, thrust-to-weight exceeds 1."
                )

            st.warning(
                "Bu hesap sabit kütleli ve sabit itişli bir yaklaşımdır. "
                "Yakıt tüketimini, atmosferik sürüklemeyi, kademeleri veya "
                "gerçek yörünge dinamiğini modellemez."
                if language == "Türkçe"
                else
                "This assumes constant mass and thrust. It does not model "
                "fuel consumption, atmospheric drag, staging, or real orbital dynamics."
            )

# ---------------------------
# SPACE DEBRIS
# ---------------------------

elif page == t["debris"]:
    st.header("🛰️ " + t["debris"])

    st.write(
        "İki cismin göreli hareketine dayalı basitleştirilmiş yaklaşma modeli."
        if language == "Türkçe"
        else "A simplified approach model based on relative motion."
    )

    distance = st.slider(t["distance"], 0.1, 100.0, 10.0, 0.1)
    speed = st.slider(t["relative_speed"], 0.01, 10.0, 1.0, 0.01)

    if st.button(t["simulate"]):
        time_hours = distance / speed / 3600

        st.metric(
            "Time at current range and speed",
            f"{distance / speed:.2f} seconds"
        )

        st.write(
            "Bu süre, mesafe ve hızın aynı doğrultuda sabit kaldığı varsayımıyla "
            "hesaplanır. Gerçek çarpışma olasılığı değildir."
            if language == "Türkçe"
            else
            "This assumes constant speed along the same line. It is not a real collision probability."
        )

        if distance < 2:
            st.warning(
                "Senaryo: Yakın mesafeyi dikkatle değerlendir. Tek bir mesafe değeri "
                "çarpışma riskini belirlemeye yetmez."
                if language == "Türkçe"
                else
                "Scenario: assess the close range carefully. Distance alone cannot determine collision risk."
            )
        else:
            st.info(
                "Daha doğru bir değerlendirme için göreli yön, hız vektörü ve zaman içindeki konum gerekir."
                if language == "Türkçe"
                else
                "A better assessment needs relative direction, velocity vectors, and position over time."
            )

# ---------------------------
# ASTRONAUT TRAINING
# ---------------------------

elif page == t["training"]:
    st.header("🧑‍🚀 " + t["training"])

    scenarios = {
        "Türkçe": [
            {
                "id": "oxygen",
                "title": "Görev 1: Oksijen uyarısı",
                "question": "Kontrol panelinde oksijen sistemi uyarısı gördün. İlk adımın ne?",
                "options": [
                    "Uyarıyı görmezden gelmek",
                    "Kontrol listesini izlemek ve görev prosedürünü uygulamak",
                    "Rastgele düğmelere basmak"
                ],
                "correct": 1,
                "explanation": "Güvenli yaklaşım, doğrulanmış kontrol listesini ve eğitimde öğrenilen acil durum prosedürünü izlemektir."
            },
            {
                "id": "navigation",
                "title": "Görev 2: Navigasyon sorunu",
                "question": "Navigasyon ekranındaki veriler birbiriyle uyuşmuyor. Ne yaparsın?",
                "options": [
                    "Verileri doğrular ve görev prosedürüne göre ekiple iletişim kurarım",
                    "Rastgele bir yön seçerim",
                    "Hiçbir şeyi kontrol etmeden devam ederim"
                ],
                "correct": 0,
                "explanation": "Tutarsız veriler doğrulanmalı; kararlar görev prosedürlerine ve ekip iletişimine dayanmalıdır."
            },
            {
                "id": "debris",
                "title": "Görev 3: Uzay enkazı uyarısı",
                "question": "Bir enkaz uyarısı aldın ancak yörünge verileri henüz doğrulanmadı. Ne yaparsın?",
                "options": [
                    "Uyarıyı hemen kapatırım",
                    "Verileri doğrular ve görev kontrolünün prosedürünü izlerim",
                    "Kendi tahminimle ani bir manevra yaparım"
                ],
                "correct": 1,
                "explanation": "Gerçek görevlerde çarpışma değerlendirmesi yörünge verileri ve görev prosedürleriyle yapılır. Rastgele manevra güvenli değildir."
            }
        ],
        "English": [
            {
                "id": "oxygen",
                "title": "Mission 1: Oxygen alert",
                "question": "You see an oxygen-system warning. What is your first step?",
                "options": [
                    "Ignore the warning",
                    "Follow the checklist and mission procedure",
                    "Press random buttons"
                ],
                "correct": 1,
                "explanation": "The safe approach is to follow the verified checklist and trained emergency procedures."
            },
            {
                "id": "navigation",
                "title": "Mission 2: Navigation problem",
                "question": "Navigation readings do not agree. What do you do?",
                "options": [
                    "Verify the readings and follow mission communication procedures",
                    "Choose a random direction",
                    "Continue without checking anything"
                ],
                "correct": 0,
                "explanation": "Inconsistent data should be verified, and decisions should follow mission procedures and team communication."
            },
            {
                "id": "debris",
                "title": "Mission 3: Debris alert",
                "question": "You receive a debris alert, but orbital data are not yet verified. What do you do?",
                "options": [
                    "Dismiss the alert immediately",
                    "Verify the data and follow mission-control procedures",
                    "Make a sudden maneuver based on a guess"
                ],
                "correct": 1,
                "explanation": "Real collision assessments rely on orbital data and mission procedures. Random maneuvers are not safe."
            }
        ]
    }

    for item in scenarios[language]:
        st.subheader(item["title"])
        st.write(item["question"])

        choice = st.radio(
            item["question"],
            item["options"],
            key=f'choice_{item["id"]}',
            label_visibility="collapsed"
        )

        if st.button(t["submit"], key=f'submit_{item["id"]}'):
            if item["id"] not in st.session_state.answered:
                selected = item["options"].index(choice)
                if selected == item["correct"]:
                    st.session_state.score += 10
                    st.success(t["correct"])
                else:
                    st.warning(t["incorrect"])

                st.session_state.answered[item["id"]] = True
                st.info(item["explanation"])
            else:
                st.info(item["explanation"])

        st.divider()

# ---------------------------
# SIMULATED BIOMETRICS
# ---------------------------

elif page == t["health"]:
    st.header("❤️ " + t["health"])

    st.warning(
        "Aşağıdaki değerler yalnızca örnek eğitim verileridir; gerçek kişiyi ölçmez."
        if language == "Türkçe"
        else
        "The following values are illustrative training data and do not measure a real person."
    )

    heart = st.slider(t["heart"], 40, 160, 74)
    oxygen = st.slider(t["oxygen"], 80, 100, 98)

    c1, c2 = st.columns(2)
    c1.metric("Heart rate", f"{heart} bpm")
    c2.metric("Oxygen saturation", f"{oxygen}%")

    st.write(
        "Bu ekran tıbbi değerlendirme sağlamaz. Değerler yalnızca simülasyon için seçilir."
        if language == "Türkçe"
        else
        "This screen does not provide medical assessment. Values are selected for simulation only."
    )

# ---------------------------
# SCIENCE QUIZ
# ---------------------------

elif page == t["quiz"]:
    st.header("🧠 " + t["quiz"])

    if language == "Türkçe":
        questions = [
            (
                "Roketin itki kuvveti başlangıçtaki ağırlığından küçükse, Dünya yüzeyinde ideal koşullarda ne olur?",
                [
                    "Roket mutlaka yörüngeye çıkar",
                    "Roket ağırlığını yenerek dikey kalkış yapamaz",
                    "Yakıt kütlesi önemsiz olur"
                ],
                1,
                "İlk anda yukarı yönlü itkinin ağırlığı aşması gerekir; gerçek uçuşta ek kuvvetler de etkilidir."
            ),
            (
                "Uzay enkazının çarpışma riskini değerlendirmek için hangisi daha önemlidir?",
                [
                    "Yalnızca cismin rengi",
                    "Göreli konum ve hız bilgileri",
                    "Cismin adı"
                ],
                1,
                "Yaklaşma geometrisi ve göreli hareket risk değerlendirmesinde önemlidir."
            ),
            (
                "Simülasyondaki biyometrik değerler neyi temsil eder?",
                [
                    "Gerçek zamanlı tıbbi ölçümü",
                    "Örnek eğitim verisini",
                    "Kesin sağlık teşhisini"
                ],
                1,
                "Bu prototipte biyometrik değerler kullanıcı tarafından seçilen örnek verilerdir."
            )
        ]
    else:
        questions = [
            (
                "If rocket thrust is smaller than its initial weight, what happens under ideal conditions at Earth's surface?",
                [
                    "It must reach orbit",
                    "It cannot lift vertically against its weight",
                    "Fuel mass becomes irrelevant"
                ],
                1,
                "Initial upward thrust must exceed weight for vertical liftoff; real flight involves additional forces."
            ),
            (
                "Which is more important for assessing space-debris collision risk?",
                [
                    "Object color alone",
                    "Relative position and velocity",
                    "Object name"
                ],
                1,
                "Encounter geometry and relative motion are important to risk assessment."
            ),
            (
                "What do the biometric values in this simulation represent?",
                [
                    "Real-time medical measurements",
                    "Illustrative training data",
                    "A definitive medical diagnosis"
                ],
                1,
                "In this prototype, biometric values are illustrative data selected by the user."
            )
        ]

    for i, (question, options, correct, explanation) in enumerate(questions):
        st.subheader(f"Question {i + 1}")
        selected = st.radio(
            question,
            options,
            key=f"quiz_{language}_{i}"
        )

        if st.button("Check answer" if language == "English" else "Cevabı kontrol et",
                     key=f"quiz_submit_{language}_{i}"):
            if st.session_state.answered.get(f"quiz_{language}_{i}", False):
                st.info(explanation)
            else:
                if options.index(selected) == correct:
                    st.success("Correct!" if language == "English" else "Doğru!")
                    st.session_state.score += 5
                else:
                    st.error("Try again." if language == "English" else "Tekrar dene.")

                st.session_state.answered[f"quiz_{language}_{i}"] = True
                st.info(explanation)

# ---------------------------
# ABOUT
# ---------------------------

elif page == t["about"]:
    st.header("🌌 " + t["about"])

    if language == "Türkçe":
        st.markdown("""
        **NEURO-AURA**, gençlerin uzay görevlerini ve temel bilimsel prensipleri
        etkileşimli senaryolarla keşfetmesine yönelik bağımsız bir eğitim prototipidir.

        ### Tasarım ilkeleri
        - Bilimsel açıklamalarla desteklenen etkileşim
        - Karar verme ve görev senaryoları
        - Basitleştirilmiş modellerin açıkça belirtilmesi
        - Simüle edilmiş veriler ile gerçek ölçümlerin ayrılması

        ### Sınırlamalar
        Bu prototip NASA tarafından geliştirilmiş veya onaylanmış bir ürün değildir.
        Gerçek astronot eğitimi, tıbbi değerlendirme ya da uçuş planlaması için kullanılamaz.
        """)
    else:
        st.markdown("""
        **NEURO-AURA** is an independent educational prototype designed to help
        young learners explore space missions and basic scientific principles.

        ### Design principles
        - Interactive learning supported by scientific explanations
        - Decision-making and mission scenarios
        - Clear communication of model limitations
        - Separation of simulated data from real measurements

        ### Limitations
        This prototype is not developed or endorsed by NASA.
        It is not suitable for real astronaut training, medical assessment, or flight planning.
        """)

st.divider()
st.caption("NEURO-AURA • SoloCoder • Educational prototype")
