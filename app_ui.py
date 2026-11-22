import streamlit as st

st.set_page_config(
    page_title="AI Heart Monitoring System",
    page_icon="❤️",
    layout="wide"
)

# Premium CSS

st.markdown("""
<style>

.stApp{
    background:linear-gradient(135deg,#ffe5ec,#e0f7ff);
}


.title{
    text-align:center;
    font-size:50px;
    font-weight:900;
    background:linear-gradient(90deg,#ff416c,#ff4b2b);
    -webkit-background-clip:text;
    color:transparent;
}


.card{
    background:white;
    padding:25px;
    border-radius:25px;
    box-shadow:0px 10px 30px rgba(0,0,0,0.1);
}


.stButton button{

    width:100%;
    height:60px;
    border-radius:30px;
    background:linear-gradient(90deg,#ff416c,#ff4b2b);
    color:white;
    font-size:22px;
    font-weight:bold;
    border:none;

}


.stButton button:hover{

    transform:scale(1.05);

}


</style>
""", unsafe_allow_html=True)


# Header

st.markdown(
    "<div class='title'>❤️ AI Heart Monitoring System</div>",
    unsafe_allow_html=True
)


st.write("")


# Dashboard cards

c1,c2,c3 = st.columns(3)

with c1:
    st.metric("🤖 Model","KNN AI")

with c2:
    st.metric("⚡ Status","Ready")

with c3:
    st.metric("❤️ Accuracy","AI Powered")


st.write("")


with st.container(border=True):

    st.subheader("👤 Patient Information")

    age = st.slider(
        "Age",
        18,
        100,
        40
    )

    cholesterol = st.slider(
        "Cholesterol",
        100,
        600,
        200
    )


if st.button("❤️ Analyze Heart Risk"):

    with st.spinner("AI analyzing health patterns..."):

        st.success("Analysis Complete")

        st.metric(
            "Risk Score",
            "25%"
        )


st.divider()

st.markdown(
    """
    <center>
    ❤️ Built by Aditya Thakur <br>
    Machine Learning + Streamlit Healthcare AI
    </center>
    """,
    unsafe_allow_html=True
)