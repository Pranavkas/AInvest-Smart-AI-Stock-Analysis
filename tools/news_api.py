import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

def get_news(stock):
    url = f"https://newsapi.org/v2/everything?q={stock}&apiKey={API_KEY}"
    response = requests.get(url)
    articles = response.json().get("articles", [])
    
    headlines = [article["title"] for article in articles[:5]]
    return headlines