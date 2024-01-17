import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Financial Analytics data.csv", encoding='unicode_escape')
print("printing rows and col")
print(df.shape)
print("printing first five entries")
print(df.head())

# Drop unnamed columns with all NaN values
df_cleaned = df.dropna(axis=1, how='all')

print("\nchecking null values")
print(pd.isnull(df_cleaned).sum())
print(df_cleaned.shape)

# Convert to numeric
df_cleaned['Mar Cap - Crore'] = pd.to_numeric(df_cleaned['Mar Cap - Crore'], errors='coerce')
df_cleaned['Sales Qtr - Crore'] = pd.to_numeric(df_cleaned['Sales Qtr - Crore'], errors='coerce')

print("describing ")
print(df_cleaned[['Mar Cap - Crore', 'Sales Qtr - Crore']].describe())
print("the columns are")
print(df.columns)

# Assuming df_cleaned has been processed as in your previous code
plt.figure(figsize=(10, 6))
sns.histplot(df_cleaned['Mar Cap - Crore'], bins=30, kde=True, color='blue')
plt.title('Distribution of Mar Cap - Crore')
plt.xlabel('Mar Cap - Crore')
plt.ylabel('Frequency')
plt.show()

# Histogram for 'Sales Qtr - Crore'
plt.figure(figsize=(10, 6))
sns.histplot(df_cleaned['Sales Qtr - Crore'], bins=30, kde=True, color='green')
plt.title('Distribution of Quarterly Sales')
plt.xlabel('Sales (Crore)')
plt.ylabel('Frequency')
plt.show()

# Bar chart for top N companies based on market capitalization
top_n = 10
top_market_cap = df_cleaned.nlargest(top_n, 'Mar Cap - Crore')
plt.figure(figsize=(12, 6))
sns.barplot(x='Mar Cap - Crore', y='Name', data=top_market_cap, palette='viridis')
plt.title(f'Top {top_n} Companies by Market Capitalization')
plt.xlabel('Market Capitalization (Crore)')
plt.ylabel('Company Name')
plt.show()

correlation_matrix = df_cleaned[['Mar Cap - Crore', 'Sales Qtr - Crore']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Matrix')
plt.show()
