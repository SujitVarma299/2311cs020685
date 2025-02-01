# 1
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
df = pd.read_csv('Day_16_Healthcare_Data.csv')

# 2
missing_values = df.isna().sum()
print(missing_values)
df['age'].fillna(df['age'].mean(), inplace=True)
df['gender'].fillna(df['gender'].mode()[0], inplace=True)

# 3
duplicates = df.duplicated()
print(df[duplicates])
df = df.drop_duplicates()

# 4
sns.boxplot(df['age'])
plt.show()
Q1 = df['age'].quantile(0.25)
Q3 = df['age'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df['age'] = df['age'].clip(lower_bound, upper_bound)

# 5
df['gender'] = df['gender'].map({'male': 0, 'female': 1})
scaler = MinMaxScaler()  # Or use StandardScaler()
df[['age', 'blood_pressure']] = scaler.fit_transform(df[['age', 'blood_pressure']])

# 6
print(df.isna().sum())
print(df.duplicated().sum())
print(df.dtypes)

# 7
df.to_csv('Cleaned_Healthcare_Data.csv', index=False)