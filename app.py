
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Retail Sales Insights",
    page_icon="📊",
    layout="wide"
)

st.title("Retail Sales & Business Insights")
st.write("Analyze sales, profit, product performance, and monthly trends.")


@st.cache_data
def load_data():
    df = pd.read_csv("data/sales.csv", encoding="cp1252")
    df.columns = df.columns.str.strip()

    required_columns = [
        "Order Date", "Sales", "Profit", "Order ID",
        "Region", "Category", "Product Name"
    ]

    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"CSV is missing these columns: {missing}")

    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
    df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
    df = df.dropna(subset=["Order Date", "Sales", "Profit"])

    return df


try:
    df = load_data()
except Exception as error:
    st.error(f"Could not load dataset: {error}")
    st.stop()


st.sidebar.header("Filter the data")

regions = sorted(df["Region"].dropna().unique())
categories = sorted(df["Category"].dropna().unique())

selected_regions = st.sidebar.multiselect(
    "Select Region", regions, default=regions
)
selected_categories = st.sidebar.multiselect(
    "Select Category", categories, default=categories
)

filtered = df[
    df["Region"].isin(selected_regions)
    & df["Category"].isin(selected_categories)
].copy()

if filtered.empty:
    st.warning("No records match your filters.")
    st.stop()


total_sales = filtered["Sales"].sum()
total_profit = filtered["Profit"].sum()
total_orders = filtered["Order ID"].nunique()

profit_margin = (
    total_profit / total_sales * 100
    if total_sales != 0 else 0
)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Unique Orders", f"{total_orders:,}")
col4.metric("Profit Margin", f"{profit_margin:.1f}%")


filtered["Month"] = filtered["Order Date"].dt.to_period("M").astype(str)

monthly_sales = (
    filtered.groupby("Month", as_index=False)["Sales"]
    .sum()
    .sort_values("Month")
)

st.subheader("Monthly Sales Trend")
fig_month = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    markers=True,
    title="Sales by Month"
)
st.plotly_chart(fig_month, use_container_width=True)


category_summary = (
    filtered.groupby("Category", as_index=False)
    .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
)

st.subheader("Category Performance")
fig_category = px.bar(
    category_summary,
    x="Category",
    y=["Sales", "Profit"],
    barmode="group",
    title="Sales and Profit by Category"
)
st.plotly_chart(fig_category, use_container_width=True)


top_products = (
    filtered.groupby("Product Name", as_index=False)["Sales"]
    .sum()
    .nlargest(10, "Sales")
    .sort_values("Sales")
)

st.subheader("Top 10 Products by Sales")
fig_products = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top Products"
)
st.plotly_chart(fig_products, use_container_width=True)


st.subheader("Filtered Sales Records")
st.dataframe(filtered, use_container_width=True)

download_data = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download filtered CSV",
    data=download_data,
    file_name="filtered_sales.csv",
    mime="text/csv"
)
