import pandas as pd

def clean_stock_data(file_path):
    """
    Load and clean stock data
    """

    print("\nLoading data...")

    # Load CSV
    df = pd.read_csv(file_path)

    print("\nInitial Data Shape:", df.shape)

    # ----------------------------
    # Convert Date column
    # ----------------------------
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)

    # ----------------------------
    # Remove duplicates
    # ----------------------------
    duplicates = df.duplicated().sum()
    print(f"\nDuplicate rows found: {duplicates}")
    df.drop_duplicates(inplace=True)

    # ----------------------------
    # Handle missing values
    # ----------------------------
    missing_values = df.isnull().sum()
    print("\nMissing values:\n", missing_values)

    # Fill missing values using forward fill
    df.fillna(method='ffill', inplace=True)

    # Drop remaining NaNs (if any)
    df.dropna(inplace=True)

    # ----------------------------
    # Ensure numeric types
    # ----------------------------
    numeric_cols = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # ----------------------------
    # Final check
    # ----------------------------
    print("\nCleaned Data Shape:", df.shape)
    print("\nData Types:\n", df.dtypes)

    return df