import pandas as pd
file_path = r'C:\Users\tanke\Downloads\Day_8_sales_data.csv'
sales_data = pd.read_csv(file_path)

# 1
# Extract all rows where sales are greater than 1000
high_sales = sales_data[sales_data['Sales'] > 1000]
print("\nRows where sales are greater than 1000:")
print(high_sales)

# Find all sales records for a specific region (e.g., "East")
region_sales = sales_data[sales_data['Region'] == 'East']
print("\nSales records for the region 'East':")
print(region_sales)

# 2
# Add a new column, Profit_Per_Unit, calculated as Profit / Quantity
sales_data['Profit_Per_Unit'] = sales_data['Profit'] / sales_data['Quantity']
print("\nData with new column 'Profit_Per_Unit':")
print(sales_data[['Product', 'Quantity', 'Profit', 'Profit_Per_Unit']])

# Create another column, High_Sales, which labels rows as Yes if Sales > 1000, else No
sales_data['High_Sales'] = sales_data['Sales'].apply(lambda x: 'Yes' if x > 1000 else 'No')
print("\nData with new column 'High_Sales':")
print(sales_data[['Product', 'Sales', 'High_Sales']])