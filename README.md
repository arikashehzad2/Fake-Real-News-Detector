# 📰 AI Fake News Detector

An end-to-end Machine Learning project that classifies news articles as **Real** or **Fake** based on their linguistic patterns and sentiment analysis.

## 🚀 Deployment Link
**(https://fake-real-news-detector-bv9mfciyyxvmhrffcx5voz.streamlit.app/)**

## 📂 Project Structure
* `fake_real_news_predictor.ipynb`: Jupyter Notebook containing Data Cleaning, Feature Engineering, and Model Training.
* `main.py`: The Streamlit web application code.
* `lr_model.pkl`: The trained Logistic Regression model (the "brain").
* `fake_real_news.csv`: The dataset used for training (100 news samples).
* `requirements.txt`: List of Python libraries required to run the app.

## 🛠️ Features Used for Prediction
The model analyzes 5 key features from the text:
1. **Character Count**: Total length of the article.
2. **Word Count**: Number of words used.
3. **Polarity**: How emotional/opinionated the text is (Sentiment).
4. **Subjectivity**: Whether the text is factual or biased.
5. **Caps Count**: Number of capital letters (to detect "shouting" or clickbait).

## 💻 How to Run Locally
1. Install dependencies:
   ```bash

   pip install -r requirements.txt
