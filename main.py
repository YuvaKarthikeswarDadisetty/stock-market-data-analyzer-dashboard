from src.data_fetcher import fetch_stock_data
from src.data_cleaner import clean_stock_data
from src.eda import run_eda
from src.trend_analysis import run_trend_analysis
from src.returns_analysis import run_returns_analysis
from src.report_generator import generate_report
def main():

    print("=" * 50)
    print(" STOCK MARKET DATA ANALYZER ")
    print("=" * 50)

    ticker = input("Enter Stock Ticker Symbol: ")

    start_date = "2020-01-01"
    end_date = "2024-01-01"

    raw_data = fetch_stock_data(ticker, start_date, end_date)

    if raw_data is not None:

        file_path = f"data/{ticker}.csv"

        clean_data = clean_stock_data(file_path)

        # EDA
        run_eda(clean_data, ticker)

        # Trend Analysis
        clean_data, trend = run_trend_analysis(clean_data, ticker)

        # After trend analysis

        clean_data, trend = run_trend_analysis(clean_data, ticker)

        # Returns & Volatility
        clean_data = run_returns_analysis(clean_data, ticker)

        # After Phase 6

        clean_data = run_returns_analysis(clean_data, ticker)

        # Generate report
        generate_report(clean_data, ticker, trend)

if __name__ == "__main__":
    main()