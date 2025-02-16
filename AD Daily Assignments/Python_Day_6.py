import pandas as pd
# 1
data = {
    'Name': ['John', 'Alice', 'Bob', 'Diana'],
    'Age': [28, 34, 23, 29],
    'Department': ['HR', 'IT', 'Marketing', 'Finance'],
    'Salary': [45000, 60000, 35000, 50000]
}
df = pd.DataFrame(data)

# 2
print("First 2 rows of the DataFrame:")
print(df.head(2))

df['Bonus'] = df['Salary'] * 0.10

average_salary = df['Salary'].mean()
print(f"\nThe average salary of employees: {average_salary}")

filtered_df = df[df['Age'] > 25]
print("\nEmployees who are older than 25:")
print(filtered_df)