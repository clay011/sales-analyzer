import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('sales.csv')

# Clean the data
df['date'] = pd.to_datetime(df['date'])
df = df.dropna()

# Calculate revenue for each row
df['revenue'] = df['quantity'] * df['price']
df['month'] = df['date'].dt.strftime('%Y-%m')

# Analysis
total_revenue = df['revenue'].sum()
by_category = df.groupby('category')['revenue'].sum()
by_month = df.groupby('month')['revenue'].sum()
top_products = df.groupby('product')['revenue'].sum().sort_values(ascending=False).head(3)

print('Total revenue:', total_revenue)
print('\nRevenue by category:\n', by_category)
print('\nRevenue by month:\n', by_month)
print('\nTop 3 products:\n', top_products)

# Charts
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
by_month.plot(kind='bar', ax=axes[0], title='Monthly Revenue')
by_category.plot(kind='pie', ax=axes[1], title='Revenue by Category', autopct='%1.1f%%')
plt.tight_layout()
plt.savefig('report.png')
plt.show()