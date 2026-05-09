import pandas as pd

def clean_stock_data(file_path):
    print("\nLoading data...")

    # Load CSV WITHOUT parsing issues
    df = pd.read_csv(file_path)

    print("\nInitial Data Shape:", df.shape)

    # ----------------------------
    # REMOVE BAD HEADER ROWS
    # ----------------------------
    # Drop rows where Close is not numeric
    df = df[pd.to_numeric(df.iloc[:, 1], errors='coerce').notnull()]

    # ----------------------------
    # RESET COLUMN NAMES
    # ----------------------------
    df.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']

    # ----------------------------
    # CONVERT DATE
    # ----------------------------
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.dropna(subset=['Date'], inplace=True)
    df.set_index('Date', inplace=True)

    # ----------------------------
    # REMOVE DUPLICATES
    # ----------------------------
    duplicates = df.duplicated().sum()
    print(f"\nDuplicate rows found: {duplicates}")
    df.drop_duplicates(inplace=True)

    # ----------------------------
    # HANDLE MISSING VALUES
    # ----------------------------
    print("\nMissing values:\n", df.isnull().sum())

    df = df.ffill()
    df.dropna(inplace=True)

    # ----------------------------
    # ENSURE NUMERIC TYPES
    # ----------------------------
    numeric_cols = ['Close', 'High', 'Low', 'Open', 'Volume']

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df.dropna(inplace=True)

    print("\nCleaned Data Shape:", df.shape)
    print("\nData Types:\n", df.dtypes)

    return df