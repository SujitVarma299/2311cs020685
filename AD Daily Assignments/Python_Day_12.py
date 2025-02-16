import pandas as pd
import matplotlib.pyplot as plt
path = r'C:\Users\tanke\Downloads\Day_12_banking_data.csv'
data = pd.read_csv(path)

# Task 1
account_type_sum = data.groupby('Account_Type')['Transaction_Amount'].sum()
account_type_sum.plot(kind='bar', color='skyblue')
plt.title('Total Transaction Amount per Account Type')
plt.xlabel('Account Type')
plt.ylabel('Total Transaction Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Task 2:
branch_counts = data['Branch'].value_counts()
branch_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Percentage of Transactions per Branch')
plt.ylabel('')
plt.show()