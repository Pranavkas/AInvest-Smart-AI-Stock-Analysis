import yfinance as yf


def get_stock_data(stock):
    stock_obj = yf.Ticker(stock)
    data = stock_obj.history(period="1mo")
    return data