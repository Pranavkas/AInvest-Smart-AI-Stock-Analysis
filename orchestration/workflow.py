from agents.data_analyst import analyze_stock
from agents.market_researcher import market_research
from agents.report_writer import generate_report


def run_analysis(stock):
    research = market_research(stock)
    data = analyze_stock(stock)
    
    report = generate_report(
        stock,
        research["sentiment"],
        data
    )
    
    return {
        "news": research["news"],
        "sentiment": research["sentiment"],
        "data": data,
        "report": report
    }