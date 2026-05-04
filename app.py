import streamlit as st
from datetime import time

# -----------------------------------
# PAGE SETTINGS
# -----------------------------------
st.set_page_config(
    page_title="Smart Health Advisory System",
    page_icon="🏥",
    layout="wide"
)

# -----------------------------------
# TEMPORARY MEMORY
# -----------------------------------
if "reminders" not in st.session_state:
    st.session_state.reminders = []

# -----------------------------------
# STYLE
# -----------------------------------
st.markdown("""
<style>
.main {
    background-color:#f7fbff;
}
h1,h2,h3 {
    color:#0d47a1;
}
.stButton>button {
    background:#0d47a1;
    color:white;
    border-radius:10px;
    height:3em;
    width:100%;
}
.card {
    background:#e3f2fd;
    padding:20px;
    border-radius:12px;
    margin-bottom:15px;
}
.footer {
    text-align:center;
    color:gray;
    margin-top:40px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# LANGUAGE SELECTOR
# -----------------------------------
st.sidebar.title("🏥 Navigation")

language = st.sidebar.selectbox(
    "🌐 Select Language",
    ["English", "Hindi", "Kannada"]
)

page = st.sidebar.radio(
    "Go To",
    ["Home", "Symptom Checker", "Medicine Reminder", "About"]
)

# -----------------------------------
# HOME PAGE
# -----------------------------------
if page == "Home":

    if language == "English":
        st.title("🏥 Smart Health Advisory System")
        st.subheader("Advanced Health Support Website")
    elif language == "Hindi":
        st.title("🏥 स्मार्ट हेल्थ सलाह प्रणाली")
        st.subheader("उन्नत स्वास्थ्य सहायता वेबसाइट")
    else:
        st.title("🏥 ಸ್ಮಾರ್ಟ್ ಆರೋಗ್ಯ ಸಲಹಾ ವ್ಯವಸ್ಥೆ")
        st.subheader("ಮುನ್ನಡೆದ ಆರೋಗ್ಯ ಸಹಾಯ ವೆಬ್‌ಸೈಟ್")

    col1, col2, col3 = st.columns(3)

    col1.metric("Users", "100+")
    col2.metric("Languages", "3")
    col3.metric("Features", "5")

    st.markdown("""
    <div class="card">
    <h3>🤒 Symptom Checker</h3>
    Check symptoms and get health guidance.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>⏰ Medicine Reminder</h3>
    Save temporary reminders easily.
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------
# SYMPTOM CHECKER
# -----------------------------------
elif page == "Symptom Checker":

    st.title("🤒 Symptom Checker")

    symptom = st.text_area(
        "Enter symptoms (example: fever, cough, headache)"
    )

    if st.button("Analyze Symptoms"):

        s = symptom.lower()

        if "chest pain" in s:
            st.error("⚠ Serious Condition")
            st.progress(100)
            st.warning("Seek emergency medical help immediately.")

        elif "fever" in s and "cough" in s:
            st.success("Possible Condition: Flu / Viral Fever")
            st.progress(70)
            st.info("Severity: Medium")
            st.info("Rest, fluids, consult doctor if needed.")

        elif "fever" in s:
            st.success("Possible Condition: Fever")
            st.progress(50)
            st.info("Severity: Mild")
            st.info("Hydrate and monitor temperature.")

        elif "cough" in s:
            st.success("Possible Condition: Cold / Cough")
            st.progress(40)
            st.info("Severity: Mild")
            st.info("Warm water, steam, rest.")

        elif "headache" in s:
            st.success("Possible Condition: Headache / Stress")
            st.progress(30)
            st.info("Severity: Mild")
            st.info("Sleep and reduce stress.")

        elif "stomach" in s:
            st.success("Possible Condition: Digestion Issue")
            st.progress(45)
            st.info("Severity: Mild")
            st.info("Eat light food and hydrate.")

        else:
            st.warning("No clear match found.")
            st.info("Consult doctor for proper advice.")

# -----------------------------------
# MEDICINE REMINDER
# -----------------------------------
elif page == "Medicine Reminder":

    st.title("⏰ Medicine Reminder")

    med = st.text_input("Medicine Name")

    t = st.time_input(
        "Select Time",
        value=time(8,0)
    )

    if st.button("Add Reminder"):

        st.session_state.reminders.append(
            {"medicine": med, "time": str(t)}
        )

        st.success("Reminder Added")

    st.subheader("📋 Saved Temporary Reminders")

    if st.session_state.reminders:

        for item in st.session_state.reminders:
            st.write(
                f"💊 {item['medicine']} at {item['time']}"
            )

    else:
        st.write("No reminders added.")

# -----------------------------------
# ABOUT PAGE
# -----------------------------------
elif page == "About":

    st.title("ℹ️ About Project")

    st.write("""
This advanced project helps users:

- Check symptoms
- View severity level
- Get basic guidance
- Add medicine reminders
- Use 3 languages

Built using Python + Streamlit.
""")

# -----------------------------------
# FOOTER
# -----------------------------------
st.markdown("""
<div class="footer">
Smart Health Project
</div>
""", unsafe_allow_html=True)