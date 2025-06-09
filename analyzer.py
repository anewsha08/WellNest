import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Simulated dataset (replaces CSV for self-containment)
from io import StringIO

data = StringIO("""symptoms,disease
fever,cough,headache,Flu
sneezing,runny nose,itchy eyes,Allergy
chest pain,shortness of breath,weakness,Heart Attack
weight loss,frequent urination,thirst,Diabetes
fever,rash,joint pain,Dengue
""")

# Load data directly
df = pd.read_csv(data)

# Features and labels
X = df["symptoms"]
y = df["disease"]

# Build pipeline: vectorizer + classifier
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Train the model
model.fit(X, y)

# User interaction loop
while True:
    print("\n--- Symptom Analyzer ---")
    user_input = input("Enter your symptoms (comma separated): ")
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting Symptom Analyzer.")
        break
    prediction = model.predict([user_input])
    print("Possible disease:", prediction[0])
