from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob
import random

app = FastAPI()

class Message(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Crypto API e pornit!"}

@app.post("/sentiment")
def get_sentiment(msg: Message):
    score = TextBlob(msg.text).sentiment.polarity
    return {"score": score}

@app.get("/signal")
def get_signal():
    return {
        "coin": "ETH",
        "signal": random.choice(["Buy", "Sell", "Hold"]),
        "confidence": round(random.uniform(0.6, 0.95), 2)
    }
