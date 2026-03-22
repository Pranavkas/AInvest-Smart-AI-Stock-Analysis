# 📊 AInvest — Smart AI Stock Analysis Platform

AInvest is an AI-powered financial analysis platform designed to provide real-time stock insights, sentiment analysis, and intelligent investment recommendations through an interactive web interface.

It combines financial data, news intelligence, and generative AI to help users make informed decisions in a simple and intuitive way.

---

## 🚀 Overview

AInvest allows users to:

* Search any stock (NSE-supported)
* View real-time price trends and historical charts
* Analyze market sentiment using news data
* Generate AI-powered financial reports
* Track recent searches and maintain a watchlist

---

## ✨ Key Features

### 📈 Market Data Analysis

* Fetches live stock data using Yahoo Finance
* Calculates latest price and average price
* Displays interactive charts (time-series trends)

### 🧠 AI-Powered Insights

* Uses LLM (Google Gemini API) for:

  * Sentiment analysis
  * Financial report generation
* Converts raw data into actionable insights

### 📰 News Intelligence

* Fetches latest stock-related news
* Performs sentiment classification (positive/neutral/negative)

### 📊 Interactive Dashboard

* Built with Streamlit
* Clean UI with:

  * Search functionality
  * Popular stocks quick access
  * Recent searches
  * Watchlist management

### ⚡ Smart Workflow System

* Modular agent-based architecture:

  * Market Researcher
  * Data Analyst
  * Report Generator

---

## 🏗️ Project Architecture

```
AInvest-Smart-AI-Stock-Analysis/
│
├── app/
│   └── main.py                # Streamlit UI
│
├── agents/
│   ├── market_researcher.py   # News + sentiment pipeline
│   ├── data_analyst.py        # Stock data processing
│   └── report_writer.py       # AI report generation
│
├── tools/
│   ├── news_api.py
│   ├── sentiment.py
│   └── yahoo_finance.py
│
├── orchestration/
│   └── workflow.py            # Main pipeline controller
│
├── config/
│   ├── settings.py
│   └── prompts.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup Guide

Follow these steps carefully to run the project locally.

---

### 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/AInvest-Smart-AI-Stock-Analysis.git
cd AInvest-Smart-AI-Stock-Analysis
```

---

### 🔹 Step 2: Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

---

### 🔹 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 Step 4: Configure Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key
NEWS_API_KEY=your_news_api_key
```

> ⚠️ Important: Never push your `.env` file to GitHub

---

### 🔹 Step 5: Run the Application

```bash
streamlit run app/main.py
```

---

### 🔹 Step 6: Open in Browser

```
http://localhost:8501
```

---

## 🧪 How to Use

1. Enter stock name (e.g., `TCS`, `INFY`)
2. Click **Analyze**
3. View:

   * 📊 Stock price data
   * 📈 Chart visualization
   * 📰 News updates
   * 🧠 Sentiment analysis
   * 📄 AI-generated report

---

## 📊 Sample Output

* Latest Price vs Average Price
* Sentiment: Positive / Neutral / Negative
* Recommendation: BUY / HOLD / WAIT
* Target Price & Risk Insights

---

## ⚠️ Known Limitations

* Only supports NSE stocks (`.NS` auto-appended)
* News availability depends on API
* Real-time refresh is limited by API constraints

---

## 🔮 Future Enhancements

* 📉 Candlestick charts (TradingView style)
* 📊 Portfolio tracking dashboard
* 🔔 Real-time alerts system
* 🌐 Cloud deployment (public access)
* 📱 Mobile responsive UI

---

## 👨‍💻 Author

**Pranav Kashyap**

* Aspiring AI Engineer / Data Scientist
* Focus: Machine Learning, Generative AI, Financial Systems

---

## ⚠️ Disclaimer

This project is for educational and demonstration purposes only.
It does not constitute financial advice.

---

## ⭐ Support

If you found this useful:

* ⭐ Star the repository
* 🍴 Fork the project
* 🤝 Contribute improvements

---

## 📜 License

This project is licensed under the MIT License.
