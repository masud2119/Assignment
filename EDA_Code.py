
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('Customers.csv')

# Convert SignupDate to datetime
data['SignupDate'] = pd.to_datetime(data['SignupDate'])

# Summary of region counts and yearly signup trends
region_counts = data['Region'].value_counts()
signup_yearly = data['SignupDate'].dt.year.value_counts().sort_index()

# Plotting customer distribution by region
plt.figure(figsize=(8, 6))
sns.barplot(x=region_counts.index, y=region_counts.values, palette='viridis')
plt.title('Number of Customers by Region', fontsize=16)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.show()

# Plotting yearly signups
plt.figure(figsize=(8, 6))
sns.lineplot(x=signup_yearly.index, y=signup_yearly.values, marker='o', color='blue')
plt.title('Yearly Customer Signups', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Signups', fontsize=12)
plt.grid(True)
plt.show()
