from tools.news_api import get_news
from tools.sentiment import analyze_sentiment


def market_research(stock):
    news = get_news(stock)
    sentiment = analyze_sentiment(news)
    
    return {
        "news": news,
        "sentiment": sentiment
    }