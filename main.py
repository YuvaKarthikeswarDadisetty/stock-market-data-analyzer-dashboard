from src.data_fetcher import fetch_stock_data

def main():

    print("=" * 50)
    print(" STOCK MARKET DATA ANALYZER ")
    print("=" * 50)

    # User input
    ticker = input("Enter Stock Ticker Symbol (Example: AAPL): ")

    # Date range
    start_date = "2020-01-01"
    end_date = "2024-01-01"

    # Fetch stock data
    data = fetch_stock_data(
        ticker,
        start_date,
        end_date
    )

    # Display preview
    if data is not None:
        print("\nFirst 5 Rows:\n")
        print(data.head())

        print("\nDataset Information:\n")
        print(data.info())

if __name__ == "__main__":
    main()