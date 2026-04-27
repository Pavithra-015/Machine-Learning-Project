import pandas as pd
import numpy as np
import re
import nltk
import pickle

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

import seaborn as sns
import matplotlib.pyplot as plt

nltk.download('stopwords')

# ---------------- DATASET ----------------
fake = pd.read_csv("Fake.csv")
real = pd.read_csv("True.csv")

fake["label"] = 0
real["label"] = 1

df = pd.concat([fake, real])
df = df.sample(frac=1).reset_index(drop=True)

# ---------------- PREPROCESSING ----------------
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)   # noisy text handling
    words = text.split()                     # TOKENIZATION
    words = [w for w in words if w not in stop_words]  # STOPWORDS
    words = [stemmer.stem(w) for w in words]            # STEMMING
    return " ".join(words)

df["content"] = df["title"] + " " + df["text"]
df["content"] = df["content"].apply(clean_text)

# ---------------- FEATURES ----------------
X = df["content"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

vectorizer = TfidfVectorizer(max_df=0.7, ngram_range=(1,2))  # TF-IDF
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# ---------------- MODELS ----------------
nb_model = MultinomialNB()                 # Naive Bayes (baseline)
nb_model.fit(X_train_vec, y_train)

lr_model = LogisticRegression(max_iter=500)  # Logistic Regression (final)
lr_model.fit(X_train_vec, y_train)

# ---------------- PREDICTION ----------------
y_pred = lr_model.predict(X_test_vec)

# ---------------- METRICS ----------------
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))

print("\nClassification Report:\n", classification_report(y_test, y_pred))

# ---------------- CONFUSION MATRIX ----------------
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d")
plt.title("Confusion Matrix")
plt.show()

# ---------------- CROSS VALIDATION ----------------
cv = cross_val_score(lr_model, X_train_vec, y_train, cv=5)
print("Cross Validation Accuracy:", cv.mean())

# ---------------- TOP WORDS ----------------
features = vectorizer.get_feature_names_out()
coef = lr_model.coef_[0]

top_fake = coef.argsort()[:10]
top_real = coef.argsort()[-10:]

print("\nTop Fake Words:")
print([features[i] for i in top_fake])

print("\nTop Real Words:")
print([features[i] for i in top_real])

# ---------------- SAMPLE PREDICTIONS ----------------
print("\nSample Predictions:")
for i in range(3):
    sample = X_test.iloc[i]
    vec = vectorizer.transform([sample])
    pred = lr_model.predict(vec)[0]

    print("\nNews:", sample[:200])
    print("Prediction:", "Real" if pred == 1 else "Fake")

# ---------------- INSIGHTS ----------------
print("\nINSIGHTS:")
print("- Fake news contains emotional/sensational words")
print("- Real news contains factual structured language")
print("- Headlines strongly influence classification")

# ---------------- SAVE MODEL ----------------
pickle.dump(lr_model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model saved successfully!")