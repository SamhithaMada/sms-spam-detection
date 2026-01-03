import os
import streamlit as st
import joblib
import re

st.set_page_config(
    page_title="SMS Spam Detection",
    page_icon="📱",
    layout="centered"
)

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

@st.cache_resource
def load_model():
    # Get absolute path to this file (app.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, "..", "models", "sms_spam_lr_pipeline.pkl")
    return joblib.load(model_path)

model = load_model()


THRESHOLD = 0.4   # tuned threshold
MIN_WORDS = 3     # SMS can be short

st.title("📱 SMS Spam Detection")
st.write("Enter an SMS message to check whether it is spam.")

sms_text = st.text_area(
    "SMS Message",
    height=150,
    placeholder="Type or paste the SMS text here..."
)

if st.button("Check Message"):
    if sms_text.strip() == "":
        st.warning("Please enter a message.")
    else:
        cleaned = clean_text(sms_text)
        if len(cleaned.split()) < MIN_WORDS:
            st.warning("Message too short to classify reliably.")
        else:
            prob_spam = model.predict_proba([cleaned])[0][1]

            if prob_spam >= THRESHOLD:
                st.error("🚨 This message is SPAM")
            else:
                st.success("✅ This message is NOT spam")
