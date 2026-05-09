import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
from streamlit_option_menu import option_menu

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(layout="wide")

# ----------------------------
# LOAD CSS
# ----------------------------
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ----------------------------
# SIDEBAR
# ----------------------------
with st.sidebar:

    st.markdown("## 📊 Stock Analyzer")

    selected = option_menu(
        menu_title=None,
        options=["Dashboard", "Reports"],
        icons=["house", "bar-chart"],
        default_index=0,
    )

    st.markdown("---")

    ticker = st.text_input("Ticker", "AAPL")

    # 🔥 DATE RANGE SLIDER
    date_range = st.slider(
        "Select Date Range",
        min_value=datetime(2018,1,1),
        max_value=datetime.now(),
        value=(datetime(2020,1,1), datetime.now())
    )

    start_date, end_date = date_range

    # 🔥 REFRESH BUTTON
    refresh = st.button("🔄 Refresh Data")

# ----------------------------
# FETCH DATA
# ----------------------------
@st.cache_data
def load_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    df.reset_index(inplace=True)
    return df

if refresh:
    st.cache_data.clear()

df = load_data(ticker, start_date, end_date)

# ----------------------------
# FIX MULTI INDEX
# ----------------------------
if isinstance(df.columns, pd.MultiIndex):
    df.columns = [col[0] for col in df.columns]

# ----------------------------
# FEATURES
# ----------------------------
df['MA20'] = df['Close'].rolling(20).mean()
df['MA50'] = df['Close'].rolling(50).mean()
df['Daily Return'] = df['Close'].pct_change()
df['Volatility'] = df['Daily Return'].rolling(20).std()

# ----------------------------
# BUY / SELL SIGNAL
# ----------------------------
df['Signal'] = "HOLD"

df.loc[df['MA20'] > df['MA50'], 'Signal'] = "BUY"
df.loc[df['MA20'] < df['MA50'], 'Signal'] = "SELL"

latest_signal = df.iloc[-1]['Signal']

# ----------------------------
# HEADER
# ----------------------------
st.title("📈 Stock Market Dashboard")

# ----------------------------
# METRICS
# ----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"<div class='card blue'>Max Price<br><h2>{df['Close'].max():.2f}</h2></div>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<div class='card green'>Avg Return<br><h2>{df['Daily Return'].mean()*100:.2f}%</h2></div>", unsafe_allow_html=True)

with col3:
    st.markdown(f"<div class='card red'>Volatility<br><h2>{df['Volatility'].mean()*100:.2f}%</h2></div>", unsafe_allow_html=True)

with col4:
    st.markdown(f"<div class='card orange'>Min Price<br><h2>{df['Close'].min():.2f}</h2></div>", unsafe_allow_html=True)

# ----------------------------
# SIGNAL DISPLAY
# ----------------------------
if latest_signal == "BUY":
    st.markdown(f"<h2 class='buy'>📈 BUY SIGNAL</h2>", unsafe_allow_html=True)
elif latest_signal == "SELL":
    st.markdown(f"<h2 class='sell'>📉 SELL SIGNAL</h2>", unsafe_allow_html=True)
else:
    st.markdown("<h2>HOLD</h2>", unsafe_allow_html=True)

# ----------------------------
# MAIN CHART
# ----------------------------
left, right = st.columns([2,1])

with left:
    st.markdown("<div class='section-title'>Stock Trend</div>", unsafe_allow_html=True)

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], name='Close', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['MA20'], name='MA20', line=dict(color='green')))
    fig.add_trace(go.Scatter(x=df['Date'], y=df['MA50'], name='MA50', line=dict(color='orange')))

    fig.update_layout(template="plotly_dark")

    st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# DONUT CHART
# ----------------------------
with right:
    st.markdown("<div class='section-title'>Signals</div>", unsafe_allow_html=True)

    counts = df['Signal'].value_counts()

    fig2 = go.Figure(data=[go.Pie(
        labels=counts.index,
        values=counts.values,
        hole=.6
    )])

    fig2.update_layout(template="plotly_dark")

    st.plotly_chart(fig2, use_container_width=True)

# ----------------------------
# RETURNS HISTOGRAM
# ----------------------------
st.markdown("<div class='section-title'>Returns Distribution</div>", unsafe_allow_html=True)

fig3 = px.histogram(df.dropna(), x='Daily Return', nbins=50)
fig3.update_layout(template="plotly_dark")

st.plotly_chart(fig3, use_container_width=True)

# ----------------------------
# VOLATILITY
# ----------------------------
st.markdown("<div class='section-title'>Volatility</div>", unsafe_allow_html=True)

fig4 = go.Figure()
fig4.add_trace(go.Scatter(x=df['Date'], y=df['Volatility'], fill='tozeroy', line=dict(color='red')))
fig4.update_layout(template="plotly_dark")

st.plotly_chart(fig4, use_container_width=True)

# ----------------------------
# TABLE
# ----------------------------
st.markdown("<div class='section-title'>Recent Data</div>", unsafe_allow_html=True)

st.dataframe(df.tail(10), use_container_width=True)

# ----------------------------
# DOWNLOAD
# ----------------------------
csv = df.to_csv(index=False)

st.download_button(
    "📥 Download Report",
    csv,
    file_name=f"{ticker}_report.csv"
)