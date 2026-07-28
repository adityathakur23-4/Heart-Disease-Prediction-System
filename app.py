
import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)
# 🌙 Theme Toggle

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False


theme = st.sidebar.toggle(
    "🌙 Dark Mode",
    value=st.session_state.dark_mode
)


st.session_state.dark_mode = theme



if st.session_state.dark_mode:

    background = """
    <style>

    .stApp {
        background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
        color:white;
    }

    h1,h2,h3,h4,h5,h6,p,label {
        color:white !important;
    }

    div[data-testid="stMetric"] {
        background:#1e293b;
        padding:15px;
        border-radius:15px;
    }

    </style>
    """

else:

    background = """
    <style>

    .stApp {
        background: linear-gradient(135deg,#eef7ff,#dcefff);
    }

    h1,h2,h3,h4,h5,h6,p,label {
        color:#333;
    }

    div[data-testid="stMetric"] {
        background:white;
        padding:15px;
        border-radius:15px;
    }

    </style>
    """


st.markdown(background, unsafe_allow_html=True)
# ❤️ Animated Heart Pulse

st.markdown("""
<style>

.heart-container{
    text-align:center;
    margin-top:10px;
}


.heart{
    font-size:70px;
    animation: heartbeat 1.2s infinite;
}


@keyframes heartbeat{

    0%{
        transform:scale(1);
    }

    25%{
        transform:scale(1.15);
    }

    40%{
        transform:scale(1);
    }

    60%{
        transform:scale(1.15);
    }

    100%{
        transform:scale(1);
    }

}


.pulse-text{

    font-size:22px;
    font-weight:bold;
    color:#d90429;

}

</style>


<div class="heart-container">

<div class="heart">
❤️
</div>

<div class="pulse-text">
AI Heart Monitoring System
</div>

</div>

""", unsafe_allow_html=True)







st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#eef7ff,#dcefff);
}

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#d90429;
}

.subtitle{
    text-align:center;
    font-size:18px;
    color:#555;
    margin-bottom:30px;
}

div.stButton > button{
    width:100%;
    height:55px;
    font-size:22px;
    font-weight:bold;
    border-radius:15px;
    background:#e63946;
    color:white;
    border:none;
}

div.stButton > button:hover{
    background:#c1121f;
    color:white;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

div[data-testid="stMetric"]{
    box-shadow:0 8px 20px rgba(0,0,0,0.15);
    transition:0.3s;
}

div[data-testid="stMetric"]:hover{
    transform:scale(1.05);
}

</style>
""", unsafe_allow_html=True)

# Load model
model = joblib.load("KNN_heart (1).pkl")
scaler = joblib.load("scaler (1).pkl")
expected_columns = joblib.load("columns.pkl")
with st.sidebar:
    st.title("🫀 Heart Predictor")
    st.markdown("---")
    st.success("Model Loaded")
    st.write("### About")
    st.write("AI-based Heart Disease Prediction using KNN.")
st.markdown("<div class='main-title'>❤️ Heart Disease Prediction System</div>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Algorithm", "KNN")

with c2:
    st.metric("Status", "🟢 Ready")

with c3:
    st.metric("Version", "1.0")

st.markdown("<div class='subtitle'>AI Powered Cardiovascular Risk Assessment</div>", unsafe_allow_html=True)





with st.container(border=True):

    st.subheader("👤 Patient Information")

    left, right = st.columns(2)

    with left:
        age = st.slider("Age", 18, 100, 40)
        sex = st.selectbox("Sex", ["M", "F"])
        chest_pain = st.selectbox("Chest Pain", ["ATA", "NAP", "TA", "ASY"])
        resting_bp = st.number_input("Resting Blood Pressure", 80, 200, 120)
        cholesterol = st.number_input("Cholesterol", 100, 600, 200)

    with right:
        fasting_bs = st.selectbox("Fasting Blood Sugar", [0, 1])
        resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
        max_hr = st.slider("Maximum Heart Rate", 60, 220, 150)
        exercise_angina = st.selectbox("Exercise Angina", ["Y", "N"])
        oldpeak = st.slider("Oldpeak", 0.0, 6.0, 1.0)
        st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

st.write("")

if st.button("❤️ Predict Heart Disease"):

    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    scaled_input = scaler.transform(input_df)

    prediction = model.predict(scaled_input)[0]
        # 🧠 AI Risk Probability

    probability = model.predict_proba(scaled_input)[0][1]

    risk_score = round(probability * 100, 2)

    st.subheader("🧠 AI Risk Score")

    

    st.metric(
        "Heart Disease Probability",
        f"{risk_score}%"
    )

    st.progress(int(risk_score))

    

    

    st.divider()    
    st.subheader("Risk Meter")

    if prediction == 1:

        result = "⚠️ High Risk of Heart Disease"

        st.error("## ⚠️ High Risk of Heart Disease")
        
        st.progress(90)

        recommendation = """
- ❤️ Consult a cardiologist.
- 🥗 Eat a heart-healthy diet.
- 🚶 Exercise regularly.
- 🚭 Avoid smoking.
- 🩺 Monitor blood pressure.
"""

        st.markdown("""
### Recommendations
- ❤️ Consult a cardiologist.
- 🥗 Eat a heart-healthy diet.
- 🚶 Exercise regularly.
- 🚭 Avoid smoking.
- 🩺 Monitor blood pressure.
""")


    else:

        result = "✅ Low Risk of Heart Disease"

        st.success("## ✅ Low Risk of Heart Disease")
        st.balloons()
        st.progress(20)

        recommendation = """
- 🥗 Balanced diet
- 🏃 Exercise regularly
- 😴 Sleep 7–8 hours
- 💧 Stay hydrated
- ❤️ Annual health check-up
"""

        st.markdown("""
### Healthy Lifestyle
- 🥗 Balanced diet
- 🏃 Exercise regularly
- 😴 Sleep 7–8 hours
- 💧 Stay hydrated
- ❤️ Annual health check-up
""")

    
    # 📄 DOWNLOAD REPORT

    report = f"""
❤️ Heart Disease Prediction Report

Date:
{datetime.now()}

Patient Details:

Age: {age}
Sex: {sex}
Chest Pain: {chest_pain}
Resting BP: {resting_bp}
Cholesterol: {cholesterol}
Maximum Heart Rate: {max_hr}

Prediction:
{result}

Recommendations:
{recommendation}
"""

    # 🔍 AI Explanation

    st.subheader("🔍 Why did AI predict this?")


    reasons = []


    if age > 50:
        reasons.append("⚠️ Age increases cardiovascular risk")

    if cholesterol > 240:
        reasons.append("⚠️ High cholesterol detected")

    if resting_bp > 140:
        reasons.append("⚠️ High blood pressure detected")

    if exercise_angina == "Y":
        reasons.append("⚠️ Exercise-related chest pain detected")

    if max_hr < 120:
        reasons.append("⚠️ Low maximum heart rate detected")


    if len(reasons) == 0:
        st.success("✅ No major risk factors detected")

    else:
        for reason in reasons:
            st.warning(reason)
            

            
            
    st.download_button(
        label="📄 Download Health Report",
        data=report,
        file_name="Heart_Disease_Report.txt",
        mime="text/plain"
    )

st.markdown("---")
        

st.markdown(
    "<center>❤️ Developed by Aditya Thakur</center>",
    unsafe_allow_html=True
)
with st.expander("❤️ Heart Health Tips"):

    st.write("""
✅ Exercise daily

✅ Eat healthy food

✅ Avoid smoking

✅ Reduce stress

✅ Sleep 7–8 hours

✅ Stay hydrated
""")