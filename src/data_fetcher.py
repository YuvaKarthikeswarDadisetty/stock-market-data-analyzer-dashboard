import yfinance as yf
import pandas as pd
import os

def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch stock market data using Yahoo Finance API
    """

    print(f"\nFetching data for {ticker}...")

    try:
        # Download stock data
        stock_data = yf.download(
            ticker,
            start=start_date,
            end=end_date
        )

        # Check if data exists
        if stock_data.empty:
            print("No data found. Please check ticker symbol.")
            return None

        # Create data folder if not exists
        os.makedirs("data", exist_ok=True)

        # Save CSV
        file_path = f"data/{ticker}.csv"
        stock_data.to_csv(file_path)

        print(f"\nData saved successfully to: {file_path}")

        return stock_data

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None