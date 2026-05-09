import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure images folder exists
os.makedirs("images", exist_ok=True)

# ----------------------------
# CALCULATE RETURNS
# ----------------------------
def calculate_returns(df):
    df['Daily Return'] = df['Close'].pct_change()
    return df

# ----------------------------
# CALCULATE VOLATILITY
# ----------------------------
def calculate_volatility(df):
    df['Volatility'] = df['Daily Return'].rolling(window=20).std()
    return df

# ----------------------------
# PRINT ANALYSIS
# ----------------------------
def print_analysis(df):
    print("\n===== RETURNS & RISK ANALYSIS =====")

    avg_return = df['Daily Return'].mean()
    volatility = df['Volatility'].mean()

    print(f"Average Daily Return: {avg_return:.5f}")
    print(f"Average Volatility: {volatility:.5f}")

    if volatility > 0.02:
        print("Risk Level: High ⚠️")
    else:
        print("Risk Level: Moderate/Low ✅")

# ----------------------------
# PLOT RETURNS DISTRIBUTION
# ----------------------------
def plot_returns(df, ticker):
    plt.figure(figsize=(10,5))
    sns.histplot(df['Daily Return'].dropna(), bins=50, kde=True)

    plt.title(f"{ticker} Daily Returns Distribution")
    plt.xlabel("Returns")

    file_path = f"images/{ticker}_returns_distribution.png"
    plt.savefig(file_path)
    plt.close()

    print(f"Saved: {file_path}")

# ----------------------------
# PLOT VOLATILITY
# ----------------------------
def plot_volatility(df, ticker):
    plt.figure(figsize=(12,6))
    plt.plot(df['Volatility'], color='red')

    plt.title(f"{ticker} Volatility Over Time")
    plt.xlabel("Date")
    plt.ylabel("Volatility")

    file_path = f"images/{ticker}_volatility.png"
    plt.savefig(file_path)
    plt.close()

    print(f"Saved: {file_path}")

# ----------------------------
# RUN ANALYSIS
# ----------------------------
def run_returns_analysis(df, ticker):
    print("\nRunning Returns & Volatility Analysis...\n")

    df = calculate_returns(df)
    df = calculate_volatility(df)

    print_analysis(df)
    plot_returns(df, ticker)
    plot_volatility(df, ticker)

    print("\nReturns Analysis Completed!")

    return df