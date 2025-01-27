import matplotlib.pyplot as plt
import seaborn as sns

# Business Insight 1: Distribution of Customers by Region
customer_region_distribution = customers_df['Region'].value_counts()

# Business Insight 2: Top 5 Most Purchased Products by Quantity
top_products = (
    transactions_df.groupby('ProductID')['Quantity']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# Map ProductID to ProductName for clarity
top_products_names = top_products.index.map(
    dict(zip(products_df['ProductID'], products_df['ProductName']))
)

# Business Insight 3: Revenue Contribution by Product Category
merged_data = transactions_df.merge(products_df, on='ProductID')
revenue_by_category = merged_data.groupby('Category')['TotalValue'].sum()

# Business Insight 4: Average Spend Per Region
average_spend_by_region = (
    transactions_df.merge(customers_df, on="CustomerID")
    .groupby('Region')['TotalValue']
    .mean()
)

# Business Insight 5: Monthly Sales Trend (from Transaction Dates)
transactions_df['TransactionDate'] = pd.to_datetime(transactions_df['TransactionDate'])
transactions_df['MonthYear'] = transactions_df['TransactionDate'].dt.to_period('M')
monthly_sales = transactions_df.groupby('MonthYear')['TotalValue'].sum()

# Visualization setup
fig, axes = plt.subplots(3, 2, figsize=(16, 12))

# Plot 1: Customer distribution by region
sns.barplot(x=customer_region_distribution.index, y=customer_region_distribution.values, ax=axes[0, 0])
axes[0, 0].set_title("Customer Distribution by Region")
axes[0, 0].set_ylabel("Number of Customers")

# Plot 2: Top 5 most purchased products
sns.barplot(x=top_products_names, y=top_products.values, ax=axes[0, 1])
axes[0, 1].set_title("Top 5 Most Purchased Products")
axes[0, 1].set_ylabel("Quantity")

# Plot 3: Revenue by product category
sns.barplot(x=revenue_by_category.index, y=revenue_by_category.values, ax=axes[1, 0])
axes[1, 0].set_title("Revenue by Product Category")
axes[1, 0].set_ylabel("Total Revenue")

# Plot 4: Average spend per region
sns.barplot(x=average_spend_by_region.index, y=average_spend_by_region.values, ax=axes[1, 1])
axes[1, 1].set_title("Average Spend Per Region")
axes[1, 1].set_ylabel("Average Transaction Value")

# Plot 5: Monthly sales trend
monthly_sales.index = monthly_sales.index.astype(str)  # Convert to string for x-axis labels
axes[2, 0].plot(monthly_sales.index, monthly_sales.values, marker="o")
axes[2, 0].set_title("Monthly Sales Trend")
axes[2, 0].set_ylabel("Total Sales")
axes[2, 0].tick_params(axis='x', rotation=45)

# Remove unused subplot
fig.delaxes(axes[2, 1])

plt.tight_layout()
plt.show()

# Insights Output
customer_region_distribution, top_products_names, revenue_by_category, average_spend_by_region, monthly_sales.tail()
