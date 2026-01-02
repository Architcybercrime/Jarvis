import joblib
import datetime
from gtts import gTTS
import pygame
import io

# Load JARVIS brain
model = joblib.load('models/intent/intent_classifier.pkl')
vectorizer = joblib
