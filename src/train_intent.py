import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os
import numpy as np

print("🧠 TRAINING JARVIS INTENT CLASSIFIER...")

df = pd.read_csv("data/raw/jarvis_training_data.csv")
X = df["text"]
y = df["intent"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

vectorizer = TfidfVectorizer(max_features=3000, ngram_range=(1,2))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train_vec, y_train)

train_acc = model.score(X_train_vec, y_train)
test_acc = model.score(X_test_vec, y_test)
print(f"✅ TRAIN ACCURACY: {train_acc:.2%}")
print(f"✅ TEST ACCURACY:  {test_acc:.2%}")

os.makedirs("models/intent", exist_ok=True)
joblib.dump(model, "models/intent/intent_classifier.pkl")
joblib.dump(vectorizer, "models/intent/tfidf_vectorizer.pkl")

print("✅ MODELS SAVED:")
print("   models/intent/intent_classifier.pkl")
print("   models/intent/tfidf_vectorizer.pkl")

test_phrases = ["hello jarvis", "नमस्ते", "what time is it", "bye"]
print("\n🔮 LIVE PREDICTIONS:")
for phrase in test_phrases:
    pred = model.predict(vectorizer.transform([phrase]))[0]
    confidence = np.max(model.predict_proba(vectorizer.transform([phrase]))[0])
    print(f"  \"{phrase}\" → {pred} ({confidence:.2%})")
