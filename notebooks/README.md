
# Retail Sales & Business Insights Dashboard

## About

This project analyzes a public retail Superstore dataset to explore sales, profit, monthly trends, and product performance.

It includes an interactive Streamlit dashboard and a Jupyter Notebook for data analysis.

## Project Features

- Total sales, total profit, and profit margin KPIs
- Monthly sales trend visualization
- Sales and profit comparison by category
- Top 10 products by sales
- Region and category filters
- Downloadable filtered sales records

## Technologies

- Python
- Pandas
- Jupyter Notebook
- Matplotlib
- Plotly
- Streamlit

## Project Structure

```text
Retail_Sales_Insights/
├── data/
│   └── sales.csv
├── notebooks/
│   └── sales_analysis.ipynb
├── reports/
│   └── business_insights.md
├── app.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Install Python.
2. Open a terminal in the project folder.
3. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. Place the dataset file at `data/sales.csv`.
5. Start the dashboard:

   ```bash
   streamlit run app.py
   ```

6. Open the local URL shown in the terminal in your browser.

## Dataset

The project uses a public Superstore dataset obtained from Kaggle.

The dataset contains retail order and sales records. It is sample data, not confidential company data.

## Analysis

The Jupyter Notebook explores the dataset, checks data quality, calculates business metrics, and examines monthly, category, and product performance.

See `reports/business_insights.md` for findings and recommendations based on the actual analysis.

## Dashboard Screenshot

Add a screenshot of your working dashboard here after capturing it.

For example, if you save your screenshot as `dashboard_screenshot.png` in the project root, use:

![Retail Sales Dashboard](dashboard_screenshot.png)

## Limitations

The findings depend on the dataset's quality and coverage. The analysis describes observed patterns and does not establish the causes of sales or profit changes.
