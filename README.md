# Machine Learning Project


Name:Pavithra kamath USN:25MSDSR026

#Fake News Detection system

This project is a Fake News Detection System developed using Machine Learning and Natural Language Processing techniques. The system analyzes news text and classifies it as Real or Fake using a Logistic Regression model with TF-IDF feature extraction.

It also provides a confidence score for each prediction and is integrated with a simple Streamlit web interface, allowing users to input news content and get instant results.

The project aims to reduce the spread of misinformation by providing an automated and efficient solution for fake news detection.

Features: 1.Classifies news as Real or Fake, 2.Provides confidence score, 3.Handles noisy and unstructured text, 4.Simple and interactive web interface, 5.Fast and accurate predictions.

Dataset: Dataset used from Kaggle: https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

Files used: 1.Fake.csv 2.True.csv

Technologies Used: Python, Pandas, NumPy, Scikit-learn, NLTK, Streamlit.

How It Works: 1.Data is collected and combined, 2.Text is cleaned (remove stopwords, symbols), 3.TF-IDF converts text to numerical features, 4.Logistic Regression model is trained, 5.Model predicts Real/Fake with confidence score.

Train Model: python train_model.py

Run Application: streamlit run app.py

Usage: 1.Enter news text in the input box, 2.Click Predict, 3.View result (Real/Fake) with confidence score.

Output Example: Input: "Government announces new policy"

Output: Real News Confidence: 91.2%
