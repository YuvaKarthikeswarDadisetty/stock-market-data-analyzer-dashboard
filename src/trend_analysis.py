import matplotlib.pyplot as plt
import os

# Ensure images folder exists
os.makedirs("images", exist_ok=True)

# ----------------------------
# ADD MOVING AVERAGES
# ----------------------------
def add_moving_averages(df):
    df['MA20'] = df['Close'].rolling(window=20).mean()
    df['MA50'] = df['Close'].rolling(window=50).mean()
    return df

# ----------------------------
# DETECT TREND
# ----------------------------
def detect_trend(df):
    latest = df.iloc[-1]

    if latest['MA20'] > latest['MA50']:
        trend = "Bullish 📈"
    elif latest['MA20'] < latest['MA50']:
        trend = "Bearish 📉"
    else:
        trend = "Sideways ➖"

    print("\nCurrent Market Trend:", trend)
    return trend

# ----------------------------
# PLOT MOVING AVERAGE
# ----------------------------
def plot_moving_averages(df, ticker):
    plt.figure(figsize=(12,6))

    plt.plot(df['Close'], label='Close Price')
    plt.plot(df['MA20'], label='MA20')
    plt.plot(df['MA50'], label='MA50')

    plt.title(f"{ticker} Moving Average Analysis")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid()

    file_path = f"images/{ticker}_moving_average.png"
    plt.savefig(file_path)
    plt.close()

    print(f"Saved: {file_path}")

# ----------------------------
# RUN TREND ANALYSIS
# ----------------------------
def run_trend_analysis(df, ticker):
    print("\nRunning Trend Analysis...\n")

    df = add_moving_averages(df)
    trend = detect_trend(df)
    plot_moving_averages(df, ticker)

    print("\nTrend Analysis Completed!")

    return df, trend