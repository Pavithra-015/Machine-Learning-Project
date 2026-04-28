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

1. Classifies news articles as Real or Fake,

2. Provides confidence/probability scores,

3. Displays important keywords influencing prediction,

4. Handles noisy and unstructured text data,
5. Detects patterns commonly found in misinformation,
6. Provides simple explanations for predictions,
7. Interactive Streamlit web interface.
   

Technologies Used:

1. Python, 

2. Pandas, NumPy,

3. Scikit-learn,

4. NLTK (Natural Language Processing),

5. TF-IDF Vectorizer,

6. Logistic Regression,

7. Naive Bayes,

8. Streamlit (Web App)
   

How It Works:

1. Data is collected and combined from Fake and True news datasets,
   
2. Text is cleaned (removal of stopwords, symbols, and noise),
   
3. TF-IDF converts text into numerical features,

4. Logistic Regression model is trained on processed data,
   
5.Model predicts whether news is Real or Fake with confidence score


How to Run:

Train Model:
python train_model.py

Run Application:
streamlit run app.py


Output Example:

Input:
“Government announces new policy”

Output:

Real News

Confidence: 91.2%


Objective:
To detect fake news using Machine Learning techniques and help reduce misinformation spread across digital platforms.



