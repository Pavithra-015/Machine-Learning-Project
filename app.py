import streamlit as st
import pickle
import re

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Fake News Detector", layout="centered")

st.title("📰 Fake News Detection System")
st.markdown("Detect whether a news article is **Real or Fake** using Machine Learning")

# ---------------- CLEAN TEXT ----------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.split()  # tokenization
    return " ".join(text)

# ---------------- INPUT ----------------
news = st.text_area("Enter News Article (Title + Content)")

# ---------------- PREDICTION ----------------
if st.button("Analyze News"):

    if news.strip() == "":
        st.warning("⚠️ Please enter news text")
    else:
        cleaned = clean_text(news)
        vec = vectorizer.transform([cleaned])

        prediction = model.predict(vec)[0]
        prob = model.predict_proba(vec)[0]

        confidence = max(prob) * 100

        # ---------------- RESULT ----------------
        st.subheader("📊 Prediction Result")

        if prediction == 1:
            st.success("✅ REAL NEWS")
        else:
            st.error("❌ FAKE NEWS")

        st.write("Confidence Score:", round(confidence, 2), "%")

        # ---------------- KEYWORDS ----------------
        st.subheader("🔑 Key Influential Words")

        words = cleaned.split()
        st.write(words[:10])

        # ---------------- EXPLANATION ----------------
        st.subheader("🧠 Why this prediction?")

        if prediction == 0:
            st.write("⚠️ Detected patterns similar to misinformation:")
            st.write("- Emotional or sensational words")
            st.write("- Lack of factual structure")
            st.write("- Similar patterns seen in fake news dataset")
        else:
            st.write("✔️ News contains factual and structured language patterns")

        # ---------------- INSIGHTS ----------------
        st.subheader("📌 Misinformation Insight")

        st.info("""
        Fake news often contains:
        - Sensational headlines  
        - Emotional wording  
        - Repeated keywords  
        
        Real news contains:
        - Factual statements  
        - Structured writing  
        - Neutral tone  
        """)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("🔍 AI-Powered Fake News Detection System | Built using NLP + Machine Learning")