# 1
import pandas as pd
file_path = 'C:/Users/tanke/Downloads/Day_7_sales_data.csv'
sales_data = pd.read_csv(file_path)
print(sales_data.head())
print(sales_data.describe())

# 2
# Calculate total sales for each region
total_sales_per_region = sales_data.groupby('Region')['Sales'].sum()
print("\nTotal sales for each region:")
print(total_sales_per_region)

# Find the most sold product based on quantity
most_sold_product = sales_data.groupby('Product')['Quantity'].sum().idxmax()
print("\nMost sold product based on quantity:")
print(most_sold_product)

# Compute the average profit margin for each product
sales_data['Profit Margin'] = (sales_data['Profit'] / sales_data['Sales']) * 100
average_profit_margin_per_product = sales_data.groupby('Product')['Profit Margin'].mean()
print("\nAverage profit margin for each product:")
print(average_profit_margin_per_product)
