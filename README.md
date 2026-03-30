# Sales Analytics Project

A complete end-to-end data analytics pipeline built with Python and Power BI Desktop.

## Project Overview
This project loads raw sales data, cleans it, analyses key metrics, generates charts and exports everything to Power BI for interactive dashboards.

## Tech Stack
- Python 3.12
- pandas
- matplotlib
- seaborn
- openpyxl
- Power BI Desktop

## Project Structure
```
sales-analytics/
├── data/
│   └── sales_data.csv        # Raw sales data
├── src/
│   ├── data_loader.py        # Load and validate CSV
│   ├── data_cleaner.py       # Clean and transform data
│   ├── analysis.py           # KPIs and summaries
│   ├── visualizer.py         # Generate charts
│   └── export_for_powerbi.py # Export Excel for Power BI
├── powerbi/
│   └── sales_dashboard.pbix  # Power BI dashboard
├── main.py                   # Run this first
├── requirements.txt
└── .gitignore
```

## Setup
```bash
# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Install packages
pip install -r requirements.txt
```

## How to Run
```bash
# Step 1 - Run analytics pipeline
python main.py

# Step 2 - Export data for Power BI
python src/export_for_powerbi.py
```

## Output
Running the scripts generates these files in `outputs/`:
- `monthly_revenue.png`
- `revenue_by_product.png`
- `revenue_by_region.png`
- `rep_performance.png`
- `sales_clean.csv`
- `sales_powerbi.xlsx`

## Power BI Dashboard
1. Open Power BI Desktop
2. Click `Home → Get Data → Excel Workbook`
3. Open `outputs/sales_powerbi.xlsx`
4. Load all 5 sheets
5. Build visuals using the loaded tables

## Key Metrics
| Metric | Value |
|---|---|
| Total Revenue | $37,550 |
| Total Units Sold | 91 |
| Top Product | Laptop |
| Top Region | North |
| Top Sales Rep | Bob |

## Author
GitHub: [Jit23456](https://github.com/Jit23456)