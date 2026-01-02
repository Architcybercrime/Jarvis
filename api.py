from fastapi import FastAPI
from pydantic import BaseModel
import datetime

app = FastAPI(title="🤖 JARVIS API")

class Query(BaseModel):
    text: str

def predict_intent(text):
    text_lower = text.lower()
    if any(word in text_lower for word in ['hello', 'hi', 'नमस्ते', 'hey']):
        return 'greeting'
    elif any(word in text_lower for word in ['time', 'समय', 'क्या समय']):
        return 'time_query'
    elif any(word in text_lower for word in ['bye', 'goodbye', 'अलविदा']):
        return 'goodbye'
    return 'unknown'

def handle_intent(intent):
    responses = {
        'greeting': 'नमस्ते! JARVIS API ready! 😊',
        'time_query': f'समय: {datetime.datetime.now().strftime("%H:%M")} IST',
        'goodbye': 'अलविदा! API बंद। 😊',
        'unknown': 'समझा नहीं... Try "hello" or "नमस्ते"'
    }
    return responses.get(intent, f'Intent "{intent}" → Under development...')

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
    return {"status": "healthy"}
