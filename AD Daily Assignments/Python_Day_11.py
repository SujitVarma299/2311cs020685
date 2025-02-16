import pandas as pd
path = r'C:\Users\tanke\Downloads\Day_11_banking_data.csv'
data = pd.read_csv(path)

# Task 1
sorted_data = data.sort_values(by='Account_Balance', ascending=False)
print("Top 10 rows sorted by Account_Balance:")
print(sorted_data.head(10))

# Task 2:
data['Rank'] = data.groupby('Branch')['Transaction_Amount'].rank(ascending=False)
print("\nData with ranking based on Transaction_Amount within each Branch:")
print(data.head(10))  # Display the first 10 rows for a quick check