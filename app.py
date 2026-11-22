
import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# ----------------------------------
# PAGE CONFIGURATION
# ----------------------------------

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------
# THEME CONFIGURATION
# ----------------------------------

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

dark_mode = st.sidebar.toggle(
    "🌙 Dark Mode",
    value=st.session_state.dark_mode
)

st.session_state.dark_mode = dark_mode

if dark_mode:
    bg = "#0B1220"
    sidebar_bg = "#111C2E"
    card_bg = "#172438"
    text_color = "#F1F5F9"
    muted = "#A5B4C7"
    accent = "#38BDF8"
    border = "#293B52"
    input_bg = "#172438"
else:
    bg = "#F3F7FC"
    sidebar_bg = "#FFFFFF"
    card_bg = "#FFFFFF"
    text_color = "#172033"
    muted = "#64748B"
    accent = "#DC3545"
    border = "#DFE7F0"
    input_bg = "#FFFFFF"

# ----------------------------------
# GLOBAL CSS
# ----------------------------------

st.markdown(f"""
<style>

.stApp {{
    background: {bg};
    color: {text_color};
}}

[data-testid="stHeader"] {{
    background: transparent;
}}

[data-testid="stSidebar"] {{
    background: {sidebar_bg};
    border-right: 1px solid {border};
}}

[data-testid="stSidebar"] * {{
    color: {text_color} !important;
}}

.main .block-container {{
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}}

h1, h2, h3, h4, p, label {{
    color: {text_color};
}}

.stMarkdown, .stCaption {{
    color: {muted};
}}

div[data-testid="stMetric"] {{
    background: {card_bg};
    border: 1px solid {border};
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0 5px 18px rgba(0,0,0,0.06);
}}

div[data-testid="stMetric"] label {{
    color: {muted} !important;
}}

div[data-testid="stMetric"] [data-testid="stMetricValue"] {{
    color: {text_color} !important;
}}

div[data-testid="stVerticalBlockBorderWrapper"] {{
    background: {card_bg};
    border: 1px solid {border};
    border-radius: 18px;
}}

div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {{
    background: {input_bg};
    border-color: {border};
    border-radius: 10px;
}}

div[data-baseweb="select"] *,
div[data-baseweb="input"] input {{
    color: {text_color} !important;
}}

div[data-testid="stSlider"] {{
    color: {accent};
}}

div.stButton > button {{
    width: 100%;
    min-height: 55px;
    background: {accent};
    color: white;
    border: none;
    border-radius: 12px;
    font-size: 18px;
    font-weight: 700;
    transition: 0.2s;
}}

div.stButton > button:hover {{
    filter: brightness(0.88);
    color: white;
    border: none;
}}

div[data-testid="stAlert"] {{
    border-radius: 12px;
}}

hr {{
    border-color: {border};
}}

.stProgress > div > div > div > div {{
    background-color: {accent};
}}

</style>
""", unsafe_allow_html=True)

# ----------------------------------
# ANIMATED HEART
# ----------------------------------

st.markdown("""
<style>
.heart-container {
    text-align: center;
    padding: 5px;
}

.heart {
    font-size: 55px;
    animation: heartbeat 1.2s infinite;
}

@keyframes heartbeat {
    0%, 100% {transform: scale(1);}
    25%, 60% {transform: scale(1.15);}
    40%, 80% {transform: scale(1);}
}

.hero-title {
    text-align: center;
    font-size: 38px;
    font-weight: 800;
    letter-spacing: -1px;
    color: #DC3545 !important;
}

.hero-subtitle {
    text-align: center;
    font-size: 16px;
    margin-bottom: 25px;
    opacity: 0.8;
}

</style>

<div class="heart-container">
    <div class="heart">❤️</div>
</div>
""", unsafe_allow_html=True)

# ----------------------------------
# LOAD ML MODEL
# ----------------------------------

@st.cache_resource
def load_models():
    model = joblib.load("KNN_heart (1).pkl")
    scaler = joblib.load("scaler (1).pkl")
    columns = joblib.load("columns.pkl")
    return model, scaler, columns

try:
    model, scaler, expected_columns = load_models()
except Exception as e:
    st.error(f"Unable to load model files: {e}")
    st.stop()

# ----------------------------------
# SIDEBAR
# ----------------------------------

with st.sidebar:

    st.markdown("# 🫀 Heart Predictor")
    st.markdown("---")

    st.success("ML Model Loaded")

    st.markdown("### About")

    st.write(
        "An AI-based heart disease risk prediction "
        "application powered by Machine Learning."
    )

    st.markdown("---")

    st.markdown("### Technology")

    st.write("🐍 Python")
    st.write("🤖 K-Nearest Neighbors")
    st.write("📊 Scikit-learn")
    st.write("🌐 Streamlit")

    st.markdown("---")

    st.caption("Version 1.0 | Developed by Aditya Thakur")

# ----------------------------------
# MAIN HEADER
# ----------------------------------

st.markdown(
    '<div class="hero-title">Heart Disease Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">'
    'AI-Powered Cardiovascular Risk Assessment'
    '</div>',
    unsafe_allow_html=True
)

# ----------------------------------
# DASHBOARD METRICS
# ----------------------------------

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Algorithm", "KNN")

with c2:
    st.metric("Model Status", "🟢 Ready")

with c3:
    st.metric("Version", "1.0")

st.write("")

# ----------------------------------
# PATIENT INFORMATION
# ----------------------------------

with st.container(border=True):

    st.subheader("👤 Patient Information")

    st.caption(
        "Enter the patient's medical information "
        "to generate an ML-based risk estimate."
    )

    left, right = st.columns(2, gap="large")

    with left:

        age = st.slider(
            "Age",
            18, 100, 40
        )

        sex = st.selectbox(
            "Sex",
            ["M", "F"]
        )

        chest_pain = st.selectbox(
            "Chest Pain Type",
            ["ATA", "NAP", "TA", "ASY"]
        )

        resting_bp = st.number_input(
            "Resting Blood Pressure",
            80, 200, 120
        )

        cholesterol = st.number_input(
            "Cholesterol",
            100, 600, 200
        )

    with right:

        fasting_bs = st.selectbox(
            "Fasting Blood Sugar",
            [0, 1]
        )

        resting_ecg = st.selectbox(
            "Resting ECG",
            ["Normal", "ST", "LVH"]
        )

        max_hr = st.slider(
            "Maximum Heart Rate",
            60, 220, 150
        )

        exercise_angina = st.selectbox(
            "Exercise Angina",
            ["Y", "N"]
        )

        oldpeak = st.slider(
            "Oldpeak",
            0.0, 6.0, 1.0
        )

        st_slope = st.selectbox(
            "ST Slope",
            ["Up", "Flat", "Down"]
        )

st.write("")

# ----------------------------------
# PREDICTION
# ----------------------------------

if st.button("❤️ Predict Heart Disease", use_container_width=True):

    try:

        raw_input = {
            "Age": age,
            "RestingBP": resting_bp,
            "Cholesterol": cholesterol,
            "FastingBS": fasting_bs,
            "MaxHR": max_hr,
            "Oldpeak": oldpeak,
            "Sex_" + sex: 1,
            "ChestPainType_" + chest_pain: 1,
            "RestingECG_" + resting_ecg: 1,
            "ExerciseAngina_" + exercise_angina: 1,
            "ST_Slope_" + st_slope: 1
        }

        input_df = pd.DataFrame([raw_input])

        for col in expected_columns:
            if col not in input_df.columns:
                input_df[col] = 0

        input_df = input_df[expected_columns]

        scaled_input = scaler.transform(input_df)

        prediction = model.predict(scaled_input)[0]

        # Find probability of positive class (1)
        classes = list(model.classes_)
        positive_index = classes.index(1)

        probability = model.predict_proba(scaled_input)[0][positive_index]

        risk_score = round(probability * 100, 2)

        st.markdown("---")

        st.subheader("🧠 Prediction Results")

        st.metric(
            "Estimated Heart Disease Probability",
            f"{risk_score}%"
        )

        st.progress(int(risk_score))

        st.caption(
            "This percentage is the model's estimated probability, "
            "not a clinically validated diagnosis."
        )

        st.subheader("Risk Assessment")

        if prediction == 1:

            result = "Higher predicted risk"

            st.error(
                "⚠️ The model predicts a higher likelihood "
                "of heart disease."
            )

            recommendation = """
- Consult a qualified healthcare professional.
- Discuss cardiovascular risk factors.
- Follow professional dietary and exercise advice.
- Monitor blood pressure and cholesterol.
- Avoid smoking.
"""

            st.markdown("### ❤️ Recommendations")
            st.markdown(recommendation)

        else:

            result = "Lower predicted risk"

            st.success(
                "✅ The model predicts a lower likelihood "
                "of heart disease."
            )

            recommendation = """
- Maintain a balanced diet.
- Exercise regularly.
- Maintain healthy sleep habits.
- Stay hydrated.
- Continue routine health check-ups.
"""

            st.markdown("### 🌿 Healthy Lifestyle")
            st.markdown(recommendation)

        # ----------------------------------
        # INPUT-BASED OBSERVATIONS
        # ----------------------------------

        st.markdown("---")

        st.subheader("🔍 Input-Based Observations")

        st.caption(
            "These observations are based on simple input thresholds; "
            "they are not explanations of the KNN model."
        )

        reasons = []

        if age > 50:
            reasons.append("Age is above 50.")

        if cholesterol > 240:
            reasons.append("Cholesterol is above 240.")

        if resting_bp > 140:
            reasons.append("Resting blood pressure is above 140.")

        if exercise_angina == "Y":
            reasons.append("Exercise-related angina is reported.")

        if max_hr < 120:
            reasons.append("Maximum heart rate is below 120.")

        if reasons:

            for reason in reasons:
                st.warning(reason)

        else:
            st.info("No listed threshold-based observations were triggered.")

        # ----------------------------------
        # DOWNLOAD REPORT
        # ----------------------------------

        report = f"""
HEART DISEASE PREDICTION REPORT
================================

Date: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}

PATIENT DETAILS
---------------
Age: {age}
Sex: {sex}
Chest Pain: {chest_pain}
Resting Blood Pressure: {resting_bp}
Cholesterol: {cholesterol}
Fasting Blood Sugar: {fasting_bs}
Resting ECG: {resting_ecg}
Maximum Heart Rate: {max_hr}
Exercise Angina: {exercise_angina}
Oldpeak: {oldpeak}
ST Slope: {st_slope}

PREDICTION
----------
Result: {result}
Estimated Probability: {risk_score}%

RECOMMENDATIONS
---------------
{recommendation}

DISCLAIMER
----------
This report is generated by a machine learning model.
It is not a medical diagnosis or a substitute for
professional medical advice.
"""

        st.download_button(
            label="📄 Download Health Report",
            data=report,
            file_name="Heart_Disease_Report.txt",
            mime="text/plain",
            use_container_width=True
        )

    except Exception as e:

        st.error(f"Prediction error: {e}")

# ----------------------------------
# FOOTER
# ----------------------------------

st.markdown("---")

with st.expander("❤️ Heart Health Tips"):

    st.markdown("""
    - Exercise regularly.
    - Eat a balanced diet.
    - Avoid smoking.
    - Manage stress.
    - Maintain healthy sleep habits.
    - Schedule routine health check-ups.
    """)

st.markdown(
    "<center>❤️ Developed by Aditya pratap singh | "
    "Machine Learning Project</center>",
    unsafe_allow_html=True
)
