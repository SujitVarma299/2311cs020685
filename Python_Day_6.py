import pandas as pd

data = {
    'Name' : ['John','Manish','Sami','Bob'],
    'Age': [12, 53, 62, 26],
    'Department': ['HR', 'IT', 'Marketing', 'Finance'],
    'Salary': [45000, 60000, 35000, 50000]
}

df = pd.DataFrame(data)
# Display the first 2 rows of the DataFrame 
print("First 2 rows of the DataFrame:")
print(df.head(2)) 
# Add a new column named 'Bonus' where the bonus is 10% of the salary
df['Bonus'] = df['Salary'] * 0.10 
print("\nDataFrame with the 'Bonus' column added:") 
print(df) 
# Calculate the average salary of employees in the DataFrame 
average_salary = df['Salary'].mean() 
print("\nAverage Salary of employees:", average_salary) 
# Filter and display employees who are older than 25 
older_than_25 = df[df['Age'] > 25] 
print("\nEmployees who are older than 25:") 
print(older_than_25)