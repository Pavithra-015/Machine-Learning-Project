# Machine Learning Project


Name:Pavithra kamath USN:25MSDSR026

#FAKE NEWS DETECTION SYSTEM

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

   
Machine Learning Workflow:

1. Data Collection (Fake & Real News Dataset from Kaggle),
 
2. Data Preprocessing (Tokenization, Stopword Removal, Stemming),

3. Feature Extraction using TF-IDF,

4. Model Training (Naive Bayes + Logistic Regression),

5. Model Evaluation (Accuracy, Precision, Recall, F1-score),

6. Deployment using Streamlit.



How to Run:

Train Model:
python train_model.py

Run Application:
streamlit run app.py







Objective:
To detect fake news using Machine Learning techniques and help reduce misinformation spread across digital platforms.



