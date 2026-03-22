# import os
# import sys

# # Fix import path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import streamlit as st
# import yfinance as yf

# from orchestration.workflow import run_analysis

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(
#     page_title="Financial Analysis Agent",
#     page_icon="📊",
#     layout="wide"
# )

# # ---------------- HEADER ----------------
# st.markdown("""
#     <h1 style='text-align: center;'>📊 Financial Analysis Agent</h1>
#     <p style='text-align: center; color: gray;'>
#     AI-powered stock analysis with insights & recommendations
#     </p>
# """, unsafe_allow_html=True)

# # ---------------- SIDEBAR ----------------
# with st.sidebar:
#     st.header("🔍 Input")
#     stock = st.text_input("Enter Stock (e.g., TCS.NS)")
#     analyze_btn = st.button("Analyze")

# # ---------------- MAIN LOGIC ----------------
# if analyze_btn:

#     if not stock:
#         st.warning("Please enter a stock name")

#     else:
#         try:
#             with st.spinner("Analyzing stock..."):

#                 result = run_analysis(stock)

#                 # Validate result keys (avoid crash)
#                 news = result.get("news", [])
#                 data = result.get("data", {})
#                 sentiment = result.get("sentiment", "No sentiment available")
#                 report = result.get("report", "No report generated")

#                 # Layout columns
#                 col1, col2 = st.columns(2)

#                 # ---------------- NEWS ----------------
#                 with col1:
#                     st.subheader("📰 News")
#                     if news:
#                         for n in news:
#                             st.markdown(f"- {n}")
#                     else:
#                         st.write("No news available")

#                 # ---------------- STOCK DATA + CHART ----------------
#                 with col2:
#                     st.subheader("📊 Stock Data")

#                     try:
#                         df = yf.Ticker(stock).history(period="1mo")

#                         if not df.empty:
#                             st.line_chart(df["Close"])
#                         else:
#                             st.warning("No stock data available")
#                     except:
#                         st.warning("Error fetching stock data")

#                     st.write({
#                         "Latest Price": data.get("latest_price", "N/A"),
#                         "Average Price": data.get("average_price", "N/A")
#                     })

#                 # ---------------- SENTIMENT ----------------
#                 st.subheader("🧠 Sentiment")
#                 st.info(sentiment)

#                 # ---------------- FINAL REPORT ----------------
#                 st.subheader("📝 Final Report")
#                 st.markdown(
#                     f"""
#                     <div style='background-color:#1E1E1E;padding:15px;border-radius:10px'>
#                     {report}
#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )


import os
import sys
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import yfinance as yf

from orchestration.workflow import run_analysis

# ---------------- PATH ----------------
BASE_DIR = os.path.dirname(__file__)
icon_path = os.path.join(BASE_DIR, "assets/icon.png")
logo_path = os.path.join(BASE_DIR, "assets/logo.png")
# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AInvest",
    page_icon=icon_path,
    layout="wide"
)

# ---------------- CSS (UI IMPROVEMENT) ----------------
st.markdown("""
<style>
body {
    background-color: #F8FAFC;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Cards */
.card {
    background: white;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0px 4px 12px rgba(10,0,0,0.05);
}

/* Buttons */
.stButton>button {
    border-radius: 10px;
    height: 45px;
    font-weight: 600;
}

/* Input */
input {
    border-radius: 10px !important;
}

/* Headings */
h1, h2, h3 {
    color: #1E293B;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "recent" not in st.session_state:
    st.session_state.recent = []

if "watchlist" not in st.session_state:
    st.session_state.watchlist = []

# ---------------- NAVBAR ----------------
# col1, col2, = st.columns([1,2])

# with col1:
#     st.image(icon_path, width=240)  # fixed proper size

# with col2:
#     st.markdown("""
#         <h2 style='margin-bottom:0;'>AInvest</h2>
#         <p style='color:#000000;margin-top:0;'>Smart AI Stock Analysis</p>
#     """, unsafe_allow_html=True)

# ---------------- NAVBAR ----------------
# st.markdown("""
# <style>
# .header {
#     display: flex;
#     align-items: center;
#     gap: 12px;
# }

# .logo {
#     width: 48px;
# }

# .brand {
#     font-size: 32px;
#     font-weight: 700;
#     color: #1E293B;
#     margin: 0;
# }

# .subtitle {
#     font-size: 14px;
#     color: #64748B;
#     margin-top: -5px;
# }
# </style>
# """, unsafe_allow_html=True)

# col1, col2 = st.columns([6,2])

# with col1:
#     st.markdown(f"""
#     <div class="header">
#         <img src="data:logo/png;base64,{open(icon_path, "rb").read().hex()}" class="logo">
#         <div>
#             <p class="brand">AInvest</p>
#             <p class="subtitle">Smart AI Stock Analysis</p>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

# with col2:
#     st.markdown("Home | Tools | Watchlist")

# st.markdown("---")
# ---------------- NAVBAR ----------------

col1, col2 = st.columns([6,2])

# with col1:
#     logo_col, text_col = st.columns([2,6])

#     with logo_col:
#         st.image(icon_path, width=290)   # ✅ proper logo size

#     with text_col:
#         st.markdown("""
#             <h1 style='margin-bottom:0; font-size:50px; font-weight:1000;'>
#                 AInvest
#             </h1>
#             <p style='margin-top:0px; color:#64748B; font-size:18px;'>
#                 Smart AI Stock Analysis
#             </p>
#         """, unsafe_allow_html=True)
with col1:
    import base64

    # convert logo to base64 (so HTML can render it properly)
    with open(logo_path, "rb") as f:
        data = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>
    .header-container {{
        display: flex;
        align-items: center;
        gap: 0px;  /* 🔥 no gap */
    }}

    .logo-img {{
        width: 220px;
        margin: 0;
        padding: 0;
    }}

    .text-container {{
        margin: 0;
        padding: 0;
    }}

    .brand {{
        font-size: 80px;
        font-weight: 1000;
        margin-top: 20;
        color: #1E293B;
    }}

    .subtitle {{
        font-size: 90px;
        font weight: 1000;        
        color: #1E293B;
                
        margin-top: 0px;
    }}
    </style>

    <div class="header-container">
        <img src="data:image/png;base64,{data}" class="logo-img"/>
        <div class="text-container">
            <p class="brand">Smart AI Stock Analysis</p>
            <p class="subtitle"></p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    nav = st.radio(
    "Navigation",
    ["Home", "Tools", "Watchlist"],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("---")
# ---------------- SEARCH ----------------
st.markdown("<h3 style='text-align:center;'>Search for a company</h3>", unsafe_allow_html=True)

col_center = st.columns([1,2,1])

with col_center[1]:
    stock_input = st.text_input(
    "Stock Input",
    placeholder="Enter stock (e.g., TCS)",
    label_visibility="collapsed"
)
    
    stock = stock_input.upper()
    if stock and "." not in stock:
        stock = stock + ".NS"

    analyze_btn = st.button("Analyze", use_container_width=True)

# ---------------- POPULAR STOCKS ----------------
st.markdown("### 🔥 Popular Stocks")

popular = ["TCS", "RELIANCE", "INFY", "HDFCBANK", "ICICIBANK"]
cols = st.columns(len(popular))

for i, s in enumerate(popular):
    if cols[i].button(s, use_container_width=True):
        stock = s + ".NS"
        analyze_btn = True

# ---------------- RECENT SEARCH ----------------
if st.session_state.recent:
    st.markdown("### 🕘 Recent Searches")
    cols = st.columns(len(st.session_state.recent))

    for i, s in enumerate(st.session_state.recent):
        if cols[i].button(s, use_container_width=True):
            stock = s
            analyze_btn = True

# ---------------- WATCHLIST ----------------
if st.session_state.watchlist:
    st.markdown("### ⭐ Watchlist")
    cols = st.columns(len(st.session_state.watchlist))

    for i, s in enumerate(st.session_state.watchlist):
        if cols[i].button(s, use_container_width=True):
            stock = s
            analyze_btn = True

st.markdown("---")

# 🔁 Auto refresh every 10 seconds
# st_autorefresh = st.empty()

# if "refresh" not in st.session_state:
#     st.session_state.refresh = 0

# time.sleep(10)
# st.session_state.refresh += 1
# st.rerun()

# ---------------- ANALYSIS ----------------
if analyze_btn and stock:

    with st.spinner("Analyzing..."):

        result = run_analysis(stock)

        # Save recent
        if stock not in st.session_state.recent:
            st.session_state.recent.insert(0, stock)

        st.session_state.recent = st.session_state.recent[:5]

        news = result.get("news", [])
        data = result.get("data", {})
        sentiment = result.get("sentiment", "No sentiment available")
        report = result.get("report", "No report generated")

        df = yf.Ticker(stock).history(period="5y")

        col1, col2 = st.columns([1,2])

        # ---------------- PRICE CARD ----------------
        with col1:
            st.markdown("<div class='card'>", unsafe_allow_html=True)

            st.markdown("### 💰 Current Price")
            st.markdown(
                f"<h1 style='color:#2563EB;'>₹ {data.get('latest_price', 'N/A')}</h1>",
                unsafe_allow_html=True
            )

            st.markdown("### 📊 Average Price")
            st.write(f"₹ {data.get('average_price', 'N/A')}")

            if st.button("⭐ Add to Watchlist"):
                if stock not in st.session_state.watchlist:
                    st.session_state.watchlist.append(stock)

            st.markdown("</div>", unsafe_allow_html=True)
        
        # ---------------- CHART ----------------
        with col2:
            st.markdown("<div class='card'>", unsafe_allow_html=True)

            st.markdown("### 📈 5-Year Price Trend")

            if not df.empty:
                st.line_chart(df["Close"])
            else:
                st.warning("No data available")

            st.markdown("</div>", unsafe_allow_html=True)

        # ---------------- NEWS ----------------
        st.markdown("### 📰 News")
        if news:
            for n in news:
                st.markdown(f"- {n}")
        else:
            st.write("No news available")

        # ---------------- SENTIMENT ----------------
        st.markdown("### 🧠 Sentiment")
        st.info(sentiment)

        # ---------------- REPORT ----------------
        st.markdown("### 📄 Final Report")
        st.markdown(
            f"""
            <div style='background-color:#111827;color:white;padding:20px;border-radius:12px'>
            {report}
            </div>
            """,
            unsafe_allow_html=True
        )

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:gray;'>
    <p>© 2026 AInvest • AI Financial Platform</p>
</div>
""", unsafe_allow_html=True)

