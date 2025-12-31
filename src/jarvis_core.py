import joblib
import datetime

model = joblib.load('models/intent/intent_classifier.pkl')
vectorizer = joblib.load('models/intent/tfidf_vectorizer.pkl')

def predict_intent(text):
    return model.predict(vectorizer.transform([text]))[0]

def handle_intent(intent):
    responses = {
        'greeting': 'नमस्ते Archit! JARVIS ready! क्या चाहिए?',
        'time_query': f'समय: {datetime.datetime.now().strftime("%H:%M")}',
        'goodbye': 'Bye! मिलते हैं 😊'
    }
    return responses.get(intent, 'समझ नहीं आया...')

if __name__ == "__main__":
    print("🤖 JARVIS ACTIVE!")
    tests = ['hello', 'नमस्ते', 'time', 'bye']
    for user_input in tests:
        intent = predict_intent(user_input)
        response = handle_intent(intent)
        print(f"User: {user_input}")
        print(f"JARVIS: {intent} → {response}\n")

