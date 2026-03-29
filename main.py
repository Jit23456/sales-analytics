import sys
sys.path.append("src")

from data_loader import load_data
from data_cleaner import clean_data
from analysis import compute_kpis, monthly_revenue, revenue_by_product, revenue_by_region, revenue_by_rep
from visualizer import plot_monthly_revenue, plot_revenue_by_product, plot_revenue_by_region, plot_rep_performance

def main():
    df = clean_data(load_data("data/sales_data.csv"))

    kpis = compute_kpis(df)
    print("\n📈 KPIs:")
    for k, v in kpis.items():
        print(f"  {k}: {v}")

    plot_monthly_revenue(monthly_revenue(df))
    plot_revenue_by_product(revenue_by_product(df))
    plot_revenue_by_region(revenue_by_region(df))
    plot_rep_performance(revenue_by_rep(df))

    print("\n✅ Done! Charts saved to outputs/")

if __name__ == "__main__":
    main()