# Assignment 1
# 1
import pandas as pd
file_path = r'C:\Users\Jannuss\Downloads\Day_10_banking_data.csv'
banking_data = pd.read_csv(file_path)
filtered_data_1 = banking_data[banking_data['Transaction_Amount'] > 2000]
print("\nRows where Transaction_Amount is greater than 2000:")
print(filtered_data_1)

# 2
filtered_data_2 = banking_data[(banking_data['Transaction_Type'] == 'Loan Payment') & (banking_data['Account_Balance'] > 5000)]
print("\nRows where Transaction_Type is 'Loan Payment' and Account_Balance is greater than 5000:")
print(filtered_data_2)

# 3
uptown_transactions = banking_data[banking_data['Branch'] == 'Uptown']
print("\nTransactions made in the 'Uptown' branch:")
print(uptown_transactions)

# Assginment 2
# 1
banking_data['Transaction_Fee'] = banking_data['Transaction_Amount'] * 0.02
print("\nData with new column 'Transaction_Fee':")
print(banking_data[['Transaction_Amount', 'Transaction_Fee']])

# 2
banking_data['Balance_Status'] = banking_data['Account_Balance'].apply(lambda x: 'High Balance' if x > 5000 else 'Low Balance')
print("\nData with new column 'Balance_Status':")
print(banking_data[['Account_Balance', 'Balance_Status']])