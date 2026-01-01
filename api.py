from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import datetime
import traceback

app = FastAPI(title="🤖 JARVIS API")

# Global variables for models (lazy load)
model = None
vectorizer = None

def load_models():
    global model, vectorizer
    try:
        model = joblib.load('models/intent/intent_classifier.pkl')
        vectorizer = joblib.load('models/intent/tfidf_vectorizer.pkl')
        print("✅ Models loaded!")
        return True
    except Exception as e:
        print(f"❌ Model load error: {e}")
        return False

class Query(BaseModel):
    text: str

def predict_intent(text):
    if model is None or vectorizer is None:
        return "error"
    try:
        return model.predict(vectorizer.transform([text]))[0]
    except:
        return "unknown"

def handle_intent(intent):
    responses = {
        'greeting': 'नमस्ते! JARVIS API ready! 😊',
        'time_query': f'समय: {datetime.datetime.now().strftime("%H:%M")} IST',
        'goodbye': 'अलविदा! API बंद। 😊',
        'error': 'Model loading error!',
        'unknown': 'समझा नहीं... Try "hello" or "नमस्ते"'
    }
    return responses.get(intent, f'Intent "{intent}" → Under development...')

@app.on_event("startup")
async def startup_event():
    load_models()

@app.post("/predict")
async def predict(query: Query):
    intent = predict_intent(query.text)
    response = handle_intent(intent)
    return {
        "input": query.text,
        "intent": intent, 
        "response": response,
        "timestamp": datetime.datetime.now().isoformat()
    }

@app.get("/")
async def root():
    return {"message": "🤖 JARVIS API v1.0 LIVE!", "endpoints": ["/predict", "/docs"]}

@app.get("/health")
async def health():
    models_ok = model is not None and vectorizer is not None
    return {"status": "healthy", "models_loaded": models_ok}
