# MODULE 5 - MINI PROJECT: Retail Sales Dashboard using CSV and Matplotlib
# Reads sales.csv, prints a summary, and displays line and bar charts.

import pandas as pd
import matplotlib.pyplot as plt


def main():
    try:
        data = pd.read_csv("sales.csv")
    except FileNotFoundError:
        print("sales.csv not found. Keep the CSV file in the same folder as this program.")
        return

    required_columns = {"Date", "Product", "Sales"}
    if not required_columns.issubset(data.columns):
        print("CSV must contain Date, Product, and Sales columns.")
        return

    if data.empty:
        print("No sales records found.")
        return

    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    data["Sales"] = pd.to_numeric(data["Sales"], errors="coerce")
    data = data.dropna(subset=["Date", "Product", "Sales"])

    if data.empty:
        print("No valid sales records found.")
        return

    print("\n===== RETAIL SALES DATA =====")
    print(data.to_string(index=False))

    total_sales = data["Sales"].sum()
    product_sales = data.groupby("Product")["Sales"].sum().sort_values(ascending=False)
    daily_sales = data.groupby("Date")["Sales"].sum().sort_index()

    print(f"\nTotal Sales: Rs. {total_sales:,.2f}")
    print("\nSales by Product:")
    for product, amount in product_sales.items():
        print(f"{product}: Rs. {amount:,.2f}")

    # Line chart: daily sales trend
    plt.figure(figsize=(9, 5))
    plt.plot(daily_sales.index, daily_sales.values, marker="o")
    plt.title("Daily Retail Sales")
    plt.xlabel("Date")
    plt.ylabel("Sales (Rs.)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    # Bar chart: total sales by product
    plt.figure(figsize=(8, 5))
    product_sales.plot(kind="bar")
    plt.title("Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Sales (Rs.)")
    plt.xticks(rotation=0)
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()
