from tools.yahoo_finance import get_stock_data


def analyze_stock(stock):
    data = get_stock_data(stock)
    
    latest_price = data["Close"].iloc[-1]
    avg_price = data["Close"].mean()
    
    return {
        "latest_price": latest_price,
        "average_price": avg_price
    }