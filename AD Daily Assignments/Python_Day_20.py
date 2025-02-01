import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Day 20_E-Commerce_Data.csv')
file_path = "C:/Users/hp/Downloads/Day 20_E-Commerce_Data.csv"
# Initial exploration
print(data.head())
print(data.describe())
print(data.info())

# Identify missing values
missing_values = data.isna()
print(missing_values.sum())
missing_percentage = data.isna().mean() * 100
print(missing_percentage)

# Impute missing numerical values (e.g., Customer_Age) using the median
imputer = SimpleImputer(strategy='median')
data['Customer_Age'] = imputer.fit_transform(data[['Customer_Age']])

# Fill missing Review_Text with an empty string
data['Review_Text'] = data['Review_Text'].fillna('')

# Find and remove duplicate reviews
duplicates = data.duplicated()
print(f"Number of duplicate records: {duplicates.sum()}")
data = data.drop_duplicates()

# Ensure ratings are within 1-5
data['Rating'] = data['Rating'].clip(1, 5)

# Standardize category names
data['Product_Category'] = data['Product_Category'].str.lower().str.replace(' ', '_')

# Boxplot for Product_Price
plt.figure(figsize=(10, 6))
sns.boxplot(data['Product_Price'])
plt.title('Boxplot of Product_Price')
plt.show()

# Boxplot for Rating
plt.figure(figsize=(10, 6))
sns.boxplot(data['Rating'])
plt.title('Boxplot of Rating')
plt.show()

# Log transformation to handle skewed data
data['Product_Price'] = data['Product_Price'].apply(lambda x: np.log(x) if x > 0 else 0)

# Convert 'Product_Category' into numerical format using one-hot encoding
data = pd.get_dummies(data, columns=['Product_Category'])

# Save the cleaned dataset
data.to_csv('cleaned_ecommerce_reviews.csv', index=False)
