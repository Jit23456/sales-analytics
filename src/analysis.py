import pandas as pd

def compute_kpis(df):
    return {
        "total_revenue": df["revenue"].sum(),
        "total_units": df["quantity"].sum(),
        "avg_order_value": df["revenue"].mean(),
        "num_transactions": len(df),
        "top_product": df.groupby("product")["revenue"].sum().idxmax(),
        "top_region": df.groupby("region")["revenue"].sum().idxmax(),
        "top_rep": df.groupby("sales_rep")["revenue"].sum().idxmax(),
    }

def monthly_revenue(df):
    return df.groupby("month")["revenue"].sum().reset_index()

def revenue_by_product(df):
    return df.groupby("product")["revenue"].sum().reset_index().sort_values("revenue", ascending=False)

def revenue_by_region(df):
    return df.groupby("region")["revenue"].sum().reset_index().sort_values("revenue", ascending=False)

def revenue_by_rep(df):
    return df.groupby("sales_rep")["revenue"].sum().reset_index().sort_values("revenue", ascending=False)