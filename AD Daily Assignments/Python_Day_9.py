# Assignment 1
# 1
import pandas as pd
file_path = r'C:\Users\tanke\Downloads\Day_9_banking_data.csv'
banking_data = pd.read_csv(file_path)
# 2
print(banking_data.head())
# 3
print(banking_data.describe())
# 4
print(banking_data.isnull().sum())

# Assignment 2
# 1
total_transaction_amount_per_account_type = banking_data.groupby('Account_Type')['Transaction_Amount'].sum()
print("\nTotal sum of Transaction_Amount per Account_Type:")
print(total_transaction_amount_per_account_type)

average_account_balance_per_account_type = banking_data.groupby('Account_Type')['Account_Balance'].mean()
print("\nAverage Account_Balance per Account_Type:")
print(average_account_balance_per_account_type)

# 2
total_transactions_per_branch = banking_data.groupby('Branch').size()
print("\nTotal number of transactions per Branch:")
print(total_transactions_per_branch)

average_transaction_amount_per_branch = banking_data.groupby('Branch')['Transaction_Amount'].mean()
print("\nAverage transaction amount per Branch:")
print(average_transaction_amount_per_branch)