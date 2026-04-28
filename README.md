# Machine Learning Project


Name:Pavithra kamath USN:25MSDSR026

#Fake News Detection system

Dataset used from Kaggle:
https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

Files used:
Fake.csv
True.csv

The Fake News Detection System is a Machine Learning-based web application designed to identify whether a news article is real or fake using Natural Language Processing (NLP) techniques. In today’s digital world, misinformation spreads rapidly through social media and news platforms, making automated detection systems essential for maintaining information credibility.

This project uses TF-IDF feature extraction and classification algorithms (Naive Bayes and Logistic Regression) to analyze news content, headlines, writing style, and linguistic patterns. The system is deployed using Streamlit, allowing users to input news text and receive real-time predictions along with confidence scores and insights.

Key Features
1.Classifies news articles as Real or Fake,

2.Provides confidence/probability scores,

3.Displays important keywords influencing prediction,

Handles noisy and unstructured text data
Detects patterns commonly found in misinformation
Provides simple explanations for predictions
Interactive Streamlit web interface

Technologies Used
Python
Pandas, NumPy
Scikit-learn
NLTK (Natural Language Processing)
TF-IDF Vectorizer
Logistic Regression
Naive Bayes
Streamlit (Web App)

How It Works
Data is collected and combined from Fake and True news datasets
Text is cleaned (removal of stopwords, symbols, and noise)
TF-IDF converts text into numerical features
Logistic Regression model is trained on processed data
Model predicts whether news is Real or Fake with confidence score

How to Run
Train Model
python train_model.py

Run Application
streamlit run app.py

Output Example

Input:
“Government announces new policy”

Output:
Real News
Confidence: 91.2%

Objective
To detect fake news using Machine Learning techniques and help reduce misinformation spread across digital platforms.



