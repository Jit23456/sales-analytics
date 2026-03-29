import pandas as pd

def clean_data(df):
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    df["quantity"] = df["quantity"].astype(int)
    df["unit_price"] = df["unit_price"].astype(float)
    df["revenue"] = df["quantity"] * df["unit_price"]
    df["month"] = df["date"].dt.to_period("M").astype(str)
    df["year"] = df["date"].dt.year
    print(f"✅ Cleaned: {len(df)} rows")
    return df