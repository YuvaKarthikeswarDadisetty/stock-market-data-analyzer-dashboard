from src.data_fetcher import fetch_stock_data
from src.data_cleaner import clean_stock_data

def main():

    print("=" * 50)
    print(" STOCK MARKET DATA ANALYZER ")
    print("=" * 50)

    ticker = input("Enter Stock Ticker Symbol: ")

    start_date = "2020-01-01"
    end_date = "2024-01-01"

    # Fetch data
    raw_data = fetch_stock_data(ticker, start_date, end_date)

    if raw_data is not None:

        file_path = f"data/{ticker}.csv"

        # Clean data
        clean_data = clean_stock_data(file_path)

        print("\nCleaned Data Preview:\n")
        print(clean_data.head())

if __name__ == "__main__":
    main()