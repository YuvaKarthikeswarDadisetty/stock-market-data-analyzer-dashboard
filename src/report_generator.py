import pandas as pd
import os

# Ensure reports folder exists
os.makedirs("reports", exist_ok=True)

# ----------------------------
# GENERATE SUMMARY REPORT
# ----------------------------
def generate_report(df, ticker, trend):

    print("\nGenerating Final Report...\n")

    # Key metrics
    max_price = df['Close'].max()
    min_price = df['Close'].min()
    avg_price = df['Close'].mean()

    avg_return = df['Daily Return'].mean()
    volatility = df['Volatility'].mean()

    # Risk level logic
    if volatility > 0.02:
        risk_level = "High"
    else:
        risk_level = "Moderate/Low"

    # Create report dictionary
    report_data = {
        "Ticker": ticker,
        "Max Price": max_price,
        "Min Price": min_price,
        "Average Price": avg_price,
        "Average Daily Return": avg_return,
        "Volatility": volatility,
        "Trend": trend,
        "Risk Level": risk_level
    }

    # Convert to DataFrame
    report_df = pd.DataFrame([report_data])

    # Save report
    file_path = f"reports/{ticker}_final_report.csv"
    report_df.to_csv(file_path, index=False)

    print(f"Report saved: {file_path}")

    # Print summary
    print("\n===== FINAL REPORT SUMMARY =====")
    print(report_df.to_string(index=False))

    return report_df