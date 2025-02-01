# 1
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv('Day_18_Tours_and_Travels.csv')

# 2
missing_values = df.isna().sum()
print(missing_values)
df['Customer_Age'].fillna(df['Customer_Age'].mean(), inplace=True)
df['Rating'].fillna(df['Rating'].median(), inplace=True)
df['Review_Text'].fillna('No review provided', inplace=True)

# 3
duplicates = df.duplicated()
print(df[duplicates])
df = df.drop_duplicates()

# 4
df['Rating'] = df['Rating'].clip(1, 5)
df['Tour_Package'] = df['Tour_Package'].str.strip().str.lower()

# 5
sns.boxplot(df['Package_Price'])
plt.show()
Q1 = df['Package_Price'].quantile(0.25)
Q3 = df['Package_Price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df['Package_Price'] = df['Package_Price'].clip(lower_bound, upper_bound)

# 6
label_encoder = LabelEncoder()
df['Tour_Package'] = label_encoder.fit_transform(df['Tour_Package'])
df.to_csv('Cleaned_Travel_Customer_Reviews.csv', index=False)