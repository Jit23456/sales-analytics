import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(__file__))
from data_loader import load_data
from data_cleaner import clean_data

def export_for_powerbi():
    os.makedirs("outputs", exist_ok=True)
    df = clean_data(load_data("data/sales_data.csv"))

    df.to_csv("outputs/sales_clean.csv", index=False)

    with pd.ExcelWriter("outputs/sales_powerbi.xlsx", engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Sales", index=False)

        df.groupby("month")["revenue"].sum().reset_index().to_excel(
            writer, sheet_name="Monthly", index=False)

        df.groupby("product").agg(
            Units=("quantity","sum"), Revenue=("revenue","sum")
        ).reset_index().to_excel(writer, sheet_name="By Product", index=False)

        df.groupby("region").agg(
            Units=("quantity","sum"), Revenue=("revenue","sum")
        ).reset_index().to_excel(writer, sheet_name="By Region", index=False)

        df.groupby("sales_rep").agg(
            Units=("quantity","sum"), Revenue=("revenue","sum")
        ).reset_index().to_excel(writer, sheet_name="By Rep", index=False)

    print("✅ Power BI files ready in outputs/")

if __name__ == "__main__":
    export_for_powerbi()