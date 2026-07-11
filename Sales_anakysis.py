# ==========================================================
# Sales Performance Analysis using Python
# Author: Yogita Patil
# Tools Used: Python, Pandas, Matplotlib
# ==========================================================

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------------
# STEP 1: Load the Dataset
# ----------------------------------------------------------
# Make sure the dataset is inside the Dataset folder.
df = pd.read_csv("../Dataset/sales_dataset_1000_rows.csv")

# ----------------------------------------------------------
# STEP 2: Display Basic Information
# ----------------------------------------------------------
print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# ----------------------------------------------------------
# STEP 3: Check Missing Values
# ----------------------------------------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# ----------------------------------------------------------
# STEP 4: Convert Order_Date to Date Format
# ----------------------------------------------------------
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Create Month column
df["Month"] = df["Order_Date"].dt.month_name()

# ----------------------------------------------------------
# STEP 5: Calculate KPIs
# ----------------------------------------------------------

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].count()
average_sales = df["Sales"].mean()
total_quantity = df["Quantity"].sum()

print("\n========== KPI ==========")
print("Total Sales :", total_sales)
print("Total Profit :", total_profit)
print("Total Orders :", total_orders)
print("Average Sales :", round(average_sales,2))
print("Total Quantity :", total_quantity)

# ----------------------------------------------------------
# STEP 6: Sales by Region
# ----------------------------------------------------------
region_sales = df.groupby("Region")["Sales"].sum()

print("\nSales by Region")
print(region_sales)

# ----------------------------------------------------------
# STEP 7: Profit by Region
# ----------------------------------------------------------
region_profit = df.groupby("Region")["Profit"].sum()

print("\nProfit by Region")
print(region_profit)

# ----------------------------------------------------------
# STEP 8: Sales by Category
# ----------------------------------------------------------
category_sales = df.groupby("Category")["Sales"].sum()

print("\nSales by Category")
print(category_sales)

# ----------------------------------------------------------
# STEP 9: Top 10 Products
# ----------------------------------------------------------
top_products = (
    df.groupby("Product")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\nTop 10 Products")
print(top_products)

# ----------------------------------------------------------
# STEP 10: Top 10 Customers
# ----------------------------------------------------------
top_customers = (
    df.groupby("Customer_Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\nTop 10 Customers")
print(top_customers)

# ----------------------------------------------------------
# STEP 11: Monthly Sales Trend
# ----------------------------------------------------------
monthly_sales = (
    df.groupby(df["Order_Date"].dt.month_name())["Sales"]
      .sum()
)

print("\nMonthly Sales")
print(monthly_sales)

# ----------------------------------------------------------
# STEP 12: Sales by Region Chart
# ----------------------------------------------------------
plt.figure(figsize=(8,5))

region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("../Images/sales_by_region.png")

plt.show()

# ----------------------------------------------------------
# STEP 13: Sales by Category Chart
# ----------------------------------------------------------
plt.figure(figsize=(6,6))

category_sales.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Sales by Category")
plt.ylabel("")

plt.tight_layout()

plt.savefig("../Images/sales_by_category.png")

plt.show()

# ----------------------------------------------------------
# STEP 14: Monthly Sales Trend Chart
# ----------------------------------------------------------
plt.figure(figsize=(10,5))

monthly_sales.plot(
    kind="line",
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("../Images/monthly_sales_trend.png")

plt.show()

# ----------------------------------------------------------
# STEP 15: Top 10 Products Chart
# ----------------------------------------------------------
plt.figure(figsize=(10,5))

top_products.plot(kind="barh")

plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig("../Images/top_products.png")

plt.show()

# ----------------------------------------------------------
# STEP 16: Export Summary Report
# ----------------------------------------------------------

summary = pd.DataFrame({

    "KPI":[
        "Total Sales",
        "Total Profit",
        "Total Orders",
        "Average Sales",
        "Total Quantity"
    ],

    "Value":[
        total_sales,
        total_profit,
        total_orders,
        round(average_sales,2),
        total_quantity
    ]

})

summary.to_csv("../Dataset/sales_summary.csv", index=False)

print("\nSummary Report Saved Successfully!")

# ----------------------------------------------------------
# END OF PROJECT
# ----------------------------------------------------------
print("\nSales Performance Analysis Completed Successfully!")
