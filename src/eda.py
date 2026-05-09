import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create images folder if not exists
os.makedirs("images", exist_ok=True)

# ----------------------------
# Closing Price Trend
# ----------------------------
def plot_closing_price(df, ticker):
    plt.figure(figsize=(12,6))
    plt.plot(df['Close'], label='Closing Price')
    plt.title(f"{ticker} Closing Price Trend")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid()

    file_path = f"images/{ticker}_closing_price.png"
    plt.savefig(file_path)
    plt.close()

    print(f"Saved: {file_path}")

# ----------------------------
# Volume Analysis
# ----------------------------
def plot_volume(df, ticker):
    plt.figure(figsize=(12,6))
    plt.plot(df['Volume'], color='orange')
    plt.title(f"{ticker} Trading Volume")
    plt.xlabel("Date")
    plt.ylabel("Volume")
    plt.grid()

    file_path = f"images/{ticker}_volume.png"
    plt.savefig(file_path)
    plt.close()

    print(f"Saved: {file_path}")

# ----------------------------
# Price Distribution
# ----------------------------
def plot_price_distribution(df, ticker):
    plt.figure(figsize=(10,5))
    sns.histplot(df['Close'], bins=50, kde=True)
    plt.title(f"{ticker} Price Distribution")

    file_path = f"images/{ticker}_price_distribution.png"
    plt.savefig(file_path)
    plt.close()

    print(f"Saved: {file_path}")

# ----------------------------
# Correlation Heatmap
# ----------------------------
def plot_correlation(df, ticker):
    plt.figure(figsize=(8,6))
    corr = df.corr()

    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title(f"{ticker} Correlation Heatmap")

    file_path = f"images/{ticker}_correlation.png"
    plt.savefig(file_path)
    plt.close()

    print(f"Saved: {file_path}")

# ----------------------------
# Run All EDA
# ----------------------------
def run_eda(df, ticker):
    print("\nRunning Exploratory Data Analysis...\n")

    plot_closing_price(df, ticker)
    plot_volume(df, ticker)
    plot_price_distribution(df, ticker)
    plot_correlation(df, ticker)

    print("\nEDA Completed Successfully!")