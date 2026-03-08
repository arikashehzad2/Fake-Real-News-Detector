import streamlit as st
import joblib
import pandas as pd
from textblob import TextBlob

# 1. Load the model
model = joblib.load('lr_model.pkl')

# 2. Page Setup
st.title("📰 AI Fake News Detector")
st.write("Paste an article below to see if it is Real or Fake.")

# 3. User Input
news_text = st.text_area("Enter News Content:", height=200)

if st.button("Analyze News"):
    if news_text:
        # --- Feature Extraction ---
        char_cnt = len(news_text)
        word_cnt = len(news_text.split())
        caps_cnt = sum(1 for c in news_text if c.isupper())
        blob = TextBlob(news_text)
        pol = blob.sentiment.polarity
        subj = blob.sentiment.subjectivity
        
        input_data = pd.DataFrame([{
            'char_count': char_cnt, 'word_count': word_cnt,
            'polarity': pol, 'subjectivity': subj, 'caps_count': caps_cnt
        }])
        
        # --- Prediction ---
        prediction = model.predict(input_data)[0]
        result = "REAL" if prediction == 0 else "FAKE"
        
        # 4. Show Result
        if result == "FAKE":
            st.error(f"Verdict: This news looks {result}")
        else:
            st.success(f"Verdict: This news looks {result}")
    else:
        st.warning("Please paste some text first!")