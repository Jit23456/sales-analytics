import matplotlib.pyplot as plt
import os

OUTPUTS = "outputs"
os.makedirs(OUTPUTS, exist_ok=True)

def _save(fig, name):
    path = os.path.join(OUTPUTS, name)
    fig.savefig(path, bbox_inches="tight", dpi=150)
    plt.close(fig)
    print(f"📊 Saved: {path}")
    return path

def plot_monthly_revenue(df_monthly):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df_monthly["month"], df_monthly["revenue"], marker="o", color="#4F46E5", linewidth=2)
    ax.fill_between(df_monthly["month"], df_monthly["revenue"], alpha=0.1, color="#4F46E5")
    ax.set_title("Monthly Revenue")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue ($)")
    ax.tick_params(axis="x", rotation=45)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    fig.tight_layout()
    return _save(fig, "monthly_revenue.png")

def plot_revenue_by_product(df_product):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(df_product["product"], df_product["revenue"], color=["#4F46E5","#7C3AED","#A78BFA"])
    ax.set_title("Revenue by Product")
    ax.set_ylabel("Revenue ($)")
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    fig.tight_layout()
    return _save(fig, "revenue_by_product.png")

def plot_revenue_by_region(df_region):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.barh(df_region["region"], df_region["revenue"], color="#0EA5E9")
    ax.set_title("Revenue by Region")
    ax.set_xlabel("Revenue ($)")
    ax.grid(axis="x", linestyle="--", alpha=0.4)
    fig.tight_layout()
    return _save(fig, "revenue_by_region.png")

def plot_rep_performance(df_rep):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(df_rep["sales_rep"], df_rep["revenue"], color="#10B981")
    ax.set_title("Sales Rep Performance")
    ax.set_ylabel("Revenue ($)")
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    fig.tight_layout()
    return _save(fig, "rep_performance.png")