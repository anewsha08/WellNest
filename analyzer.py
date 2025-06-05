import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Load 
df = pd.read_csv("symptom_dataset.csv")

# Features and labels
X = df["symptoms"]
y = df["disease"]

# Pipeline: vectorizer + classifier
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Train 
model.fit(X, y)

# Test 
while True:
    print("\n--- Symptom Analyzer ---")
    user_input = input("Enter your symptoms (comma separated): ")
    if user_input.lower() in ['exit', 'quit']:
        break
    prediction = model.predict([user_input])
    print("Possible disease:", prediction[0])
