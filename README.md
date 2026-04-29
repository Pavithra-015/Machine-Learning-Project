 # Machine Learning Project

#FAKE NEWS DETECTION SYSTEM
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Name:Pavithra kamath USN:25MSDSR026
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Dataset used from Kaggle:
https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset
-------------------------------------------------------------------------------------------------------------------------------------------------------------------


Files used:

Fake.csv

True.csv
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

ABSTRACT

This project presents a Fake News Detection System developed using Machine Learning and Natural Language Processing techniques. The system analyzes textual data from news articles and classifies them as Real or Fake.

The dataset consists of labeled news articles, which are preprocessed using NLP techniques such as tokenization, stopword removal, and stemming. Features are extracted using TF-IDF (Term Frequency–Inverse Document Frequency).

Two machine learning models are used: Naive Bayes (baseline) and Logistic Regression (final model). The model is evaluated using Accuracy, Precision, Recall, and F1-score, along with cross-validation.

A Streamlit web application is developed to allow users to input news content and receive predictions with confidence scores, keywords, and explanations.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

INTRODUCTION

With the rapid growth of digital media and social platforms, information spreads quickly across the world. While this improves communication, it also increases the spread of fake news and misinformation.

Fake news can influence public opinion, create panic, and negatively impact society. Manual verification is difficult due to the large volume of data generated daily.

Therefore, an automated system is required to detect fake news efficiently using machine learning techniques.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
PROBLEM STATEMENT

The organization receives a large volume of news articles and lacks an efficient way to verify their authenticity.

The goal is to develop an AI-powered Fake News Detection System that can analyze textual data and classify news as Real or Fake, while providing explanations and confidence scores.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
OBJECTIVES

1. To classify news articles as Real or Fake,
   
2. To provide a confidence score for predictions,

3. To identify important keywords influencing the result,

4. To handle noisy and unstructured text data,

5. To detect patterns associated with misinformation,

6. To provide insights and explanation for predictions.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
DATASET

Dataset used from Kaggle:
https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset


-------------------------------------------------------------------------------------------------------------------------------------------------------------------
   


Technologies Used:

1. Python, 

2. Pandas, NumPy,

3. Scikit-learn,

4. NLTK (Natural Language Processing),

5. TF-IDF Vectorizer,

6. Logistic Regression,

7. Naive Bayes,

8. Streamlit (Web App)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

   
METHODOLOGY

The system follows these steps:

1. Data Collection: 

      Load Fake and Real news datasets

2. Data Preprocessing (NLP):

      Tokenization
      
      Stopword removal
      
      Stemming
      
      Removing special characters

3. Feature Extraction

      TF-IDF is used to convert text into numerical form
   
4. Model Training

      Naive Bayes (baseline model)
      
      Logistic Regression (final model)

5. Evaluation
      
      Accuracy
      Precision
      Recall
      F1-score
      Cross-validation
-------------------------------------------------------------------------------------------------------------------------------------------------------------------


IMPLEMENTATION

The project is implemented using Python with libraries such as:

1. Pandas and NumPy (data handling),
   
2. NLTK (text preprocessing),
   
3. Scikit-learn (machine learning models),
   
4. Streamlit (web application)

The system combines TF-IDF vectorization with Logistic Regression to classify news articles. A rule-based component is also added to detect unrealistic patterns in text.
------------------------------------------------------------------------------------------------------------------------------------------------------------------


Results

The model achieved high performance:

Accuracy: ~98%

Precision: ~98%

Recall: ~98%

F1-score: ~98%

Output includes:

Real/Fake classification

Confidence score

Keywords

Explanation

Insights
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

HOW TO RUN:

Train Model:
python train_model.py

Run Application:
streamlit run app.py

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
CONCLUSION

This project successfully demonstrates the development of a Fake News Detection System using Machine Learning and Natural Language Processing techniques. The system effectively classifies news articles as Real or Fake by analyzing textual content, writing patterns, and keyword usage.

The implementation uses TF-IDF feature extraction along with Naive Bayes (baseline) and Logistic Regression (final model) to achieve high accuracy and reliable predictions. The model is evaluated using key performance metrics such as Accuracy, Precision, Recall, and F1-score, along with cross-validation to ensure robustness.

Additionally, the system provides a confidence score, highlights important keywords, and offers basic explanations and insights to improve interpretability. A simple Streamlit web interface allows users to interact with the system and obtain real-time predictions.

Although the model performs well on structured news data, it is important to note that it is pattern-based rather than fact-based, and may not accurately verify real-world events or very short/unstructured inputs.

Overall, this project provides an efficient and scalable solution for detecting misinformation, with potential applications in content moderation, media verification, and social platform monitoring.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
<img width="1774" height="887" alt="Work flow diagram" src="https://github.com/user-attachments/assets/9c0e47c5-b4c1-4c9b-8862-8e7c62424dad" />











