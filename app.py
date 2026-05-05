import streamlit as st
import sqlite3
import smtplib
from email.mime.text import MIMEText

# ==========================
# EMAIL SETTINGS
# ==========================

SENDER_EMAIL = "pavankumarhj17@gmail.com"
APP_PASSWORD = "hafj awjg liwy zitz"

# ==========================
# DATABASE
# ==========================

conn = sqlite3.connect("reminders.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS reminders(
id INTEGER PRIMARY KEY AUTOINCREMENT,
email TEXT,
medicine TEXT,
time TEXT
)
""")

conn.commit()

# ==========================
# EMAIL FUNCTION
# ==========================

def send_email(to_email, medicine):
    try:
        msg = MIMEText(f"Reminder to take {medicine}")
        msg["Subject"] = "Medicine Reminder"
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()

    except:
        pass

# ==========================
# LANGUAGE
# ==========================

lang = st.sidebar.selectbox(
    "Choose Language",
    ["English", "Kannada", "Hindi"]
)

if lang == "English":
    title = "Smart Health Advisory System"
    symptom_text = "Enter Symptom"
    button_text = "Analyze"
    reminder_text = "Medicine Reminder"

elif lang == "Kannada":
    title = "ಸ್ಮಾರ್ಟ್ ಆರೋಗ್ಯ ಸಲಹಾ ವ್ಯವಸ್ಥೆ"
    symptom_text = "ಲಕ್ಷಣ ನಮೂದಿಸಿ"
    button_text = "ಪರಿಶೀಲಿಸಿ"
    reminder_text = "ಔಷಧಿ ನೆನಪಿಸುವಿಕೆ"

else:
    title = "स्मार्ट हेल्थ सलाह प्रणाली"
    symptom_text = "लक्षण दर्ज करें"
    button_text = "जांच करें"
    reminder_text = "दवा रिमाइंडर"

# ==========================
# UI
# ==========================

st.title(title)

menu = st.sidebar.selectbox(
    "Menu",
    ["Home", "Symptom Checker", "Reminder", "Saved Reminders"]
)

# ==========================
# HOME
# ==========================

if menu == "Home":
    st.header("Welcome")
    st.write("Advanced Health Website")

# ==========================
# SYMPTOM CHECKER
# ==========================

elif menu == "Symptom Checker":

    st.header("Symptom Checker")

    symptom = st.text_input(symptom_text)

    if st.button(button_text):

        s = symptom.lower()

        if "fever" in s:
            st.success("Possible Fever")
            st.write("Medicine: Paracetamol")
            st.write("Drink water and rest")

        elif "cold" in s:
            st.success("Common Cold")
            st.write("Medicine: Cetirizine")

        elif "cough" in s:
            st.success("Cough")
            st.write("Medicine: Cough Syrup")

        elif "headache" in s:
            st.success("Headache")
            st.write("Medicine: Ibuprofen")

        elif "stomach pain" in s:
            st.success("Stomach Pain")
            st.write("Medicine: Antacid")

        elif "leg pain" in s:
            st.success("Leg Pain")
            st.write("Medicine: Pain Relief Gel")

        elif "hand pain" in s:
            st.success("Hand Pain")
            st.write("Medicine: Pain Relief Tablet")

        elif "chest pain" in s:
            st.error("Emergency! Visit hospital immediately.")

        else:
            st.warning("Consult doctor")

# ==========================
# REMINDER
# ==========================

elif menu == "Reminder":

    st.header(reminder_text)

    email = st.text_input("Email")
    medicine = st.text_input("Medicine Name")
    time = st.text_input("Time Example: 08:30 AM")

    if st.button("Save Reminder"):
        c.execute(
            "INSERT INTO reminders(email, medicine, time) VALUES (?, ?, ?)",
            (email, medicine, time)
        )
        conn.commit()

        send_email(email, medicine)

        st.success("Reminder Saved and Test Email Sent")

# ==========================
# SAVED REMINDERS
# ==========================

elif menu == "Saved Reminders":

    st.header("Saved Reminders")

    c.execute("SELECT email, medicine, time FROM reminders")
    rows = c.fetchall()

    for row in rows:
        st.write(f"{row[0]} | {row[1]} | {row[2]}")
