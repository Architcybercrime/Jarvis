# 🤖 Jarvis — Multilingual Low-Latency Voice Assistant

**Jarvis** is an AI-powered voice assistant built in Python that understands spoken commands, classifies user intent using a trained Machine Learning model, and responds in real time. Designed for low latency and multilingual support, Jarvis bridges speech recognition with intelligent NLP-based intent detection.

---

## 🌟 Features

- 🎤 **Voice Input** — Captures and processes real-time speech from the microphone
- 🧠 **Intent Classification** — ML model (TF-IDF + classifier) identifies what the user wants
- 🌍 **Multilingual Support** — Understands commands across multiple languages
- ⚡ **Low Latency** — Optimized for fast response time between speech and action
- 🔌 **REST API** — Expose assistant capabilities via `api.py` for integration with other apps
- ⚙️ **Configurable** — Easily tweak behaviour through `config.yaml`

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python |
| NLP / ML | TF-IDF Vectorizer + Intent Classifier (scikit-learn) |
| Speech Recognition | SpeechRecognition / pyttsx3 |
| API Layer | Flask (api.py) |
| Config | YAML |
| Model Storage | Pickle (.pkl) |

---

## 📁 Project Structure

```
Jarvis/
├── src/                        # Core assistant logic
│   ├── assistant.py            # Main voice assistant pipeline
│   ├── speech.py               # Speech recognition & TTS
│   ├── intent.py               # Intent detection logic
│   └── response.py             # Response generation
├── models/
│   └── intent/                 # Trained ML model files
├── data/
│   └── raw/                    # Raw training data for intent classification
├── tests/                      # Unit tests
├── api.py                      # Flask REST API to expose assistant
├── config.yaml                 # Configuration (language, thresholds, etc.)
├── intent_classifier.pkl       # Pre-trained intent classification model
├── tfidf_vectorizer.pkl        # Fitted TF-IDF vectorizer
├── .env.example                # Environment variable template
└── README.md
```

---

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Architcybercrime/Jarvis.git
cd Jarvis
```

### 2. Create & Activate Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
cp .env.example .env
# Edit .env with your API keys if required
```

### 5. Run the Voice Assistant
```bash
python src/assistant.py
```

### 6. Run the REST API (Optional)
```bash
python api.py
```
API will be available at: **http://127.0.0.1:5000**

---

## 🧠 How It Works

```
User speaks → Speech Recognition → Text
     ↓
TF-IDF Vectorizer → converts text to feature vector
     ↓
Intent Classifier (ML Model) → predicts intent
     ↓
Response Engine → generates and speaks response
```

1. **Speech Input** — Microphone captures the user's voice
2. **Speech-to-Text** — Converts audio to text in real time
3. **Vectorization** — TF-IDF vectorizer transforms text into numerical features
4. **Intent Detection** — Pre-trained ML classifier predicts the user's intent
5. **Response** — Jarvis responds verbally and/or executes the appropriate action

---

## 🌍 Multilingual Support

Jarvis is designed to handle commands in multiple languages. Language settings can be configured in `config.yaml`:

```yaml
language: en       # Change to 'hi', 'fr', 'es', etc.
latency_mode: low
confidence_threshold: 0.6
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/predict` | Send text, get predicted intent back |
| GET | `/health` | Check if the API is running |

**Example Request:**
```json
POST /predict
{
  "text": "What is the weather today?"
}
```

**Example Response:**
```json
{
  "intent": "get_weather",
  "confidence": 0.94
}
```

---

## 🧪 Running Tests

```bash
python -m pytest tests/
```

---

## 🔧 Requirements

- Python 3.8+
- Microphone (for voice input)
- Internet connection (for speech recognition API)

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Archit Agrawal**
- GitHub: [@Architcybercrime](https://github.com/Architcybercrime)
- Email: architagrawalking@gmail.com
- LeetCode: [leetcode.com/u/yO3MAhboDD](https://leetcode.com/u/yO3MAhboDD/)

---

*"Just like the real Jarvis — always listening, always learning."* 🚀
