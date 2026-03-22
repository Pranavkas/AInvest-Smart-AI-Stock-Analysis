import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

def analyze_sentiment(news_list):

    if not news_list:
        return "No news available"

    text = "\n".join(news_list)

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": f"Analyze sentiment (Positive/Negative/Neutral):\n{text}"}
                ]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    result = response.json()

    # DEBUG PRINT (IMPORTANT)
    print("Gemini Response:", result)

    if "candidates" in result:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"API ERROR: {result}"