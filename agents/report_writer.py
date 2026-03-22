import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

def generate_report(stock, sentiment, data):

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={API_KEY}"

    prompt = f"""
    Generate a financial report for {stock}

    Sentiment: {sentiment}
    Data: {data}

    Give final recommendation (Buy/Sell/Hold)
    """

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    result = response.json()

    # print("Report Response:", result)

    if "candidates" in result:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"API ERROR: {result}"