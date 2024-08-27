import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA

# Load the dataset
file_path = 'walmart_sales_data.csv'  # Replace with your file path
df = pd.read_csv(file_path)

# Convert the date column to datetime with the correct format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# Display the first few rows to confirm the conversion
print(df.head())

# Check the structure of the dataset
print(df.info())

# Summary statistics
print(df.describe())

# Checking for missing values
print(df.isnull().sum())

# Sales Trends Over Time
sales_over_time = df.groupby('Date')['Weekly_Sales'].sum()

# Plotting the sales over time
plt.figure(figsize=(12, 6))
plt.plot(sales_over_time)
plt.title('Total Weekly Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Weekly Sales')
plt.show()

# Impact of Holidays on Sales
holiday_sales = df.groupby('Holiday_Flag')['Weekly_Sales'].mean()

# Plotting the average sales on holidays vs non-holidays
plt.figure(figsize=(8, 5))
sns.barplot(x=holiday_sales.index, y=holiday_sales.values)
plt.title('Average Weekly Sales: Holidays vs Non-Holidays')
plt.xlabel('Holiday Flag (0 = No, 1 = Yes)')
plt.ylabel('Average Weekly Sales')
plt.show()

# Sales by Store
sales_by_store = df.groupby('Store')['Weekly_Sales'].sum()

# Plotting the sales by store
plt.figure(figsize=(12, 6))
sns.barplot(x=sales_by_store.index, y=sales_by_store.values)
plt.title('Total Sales by Store')
plt.xlabel('Store')
plt.ylabel('Total Weekly Sales')
plt.show()

# Correlation Analysis
corr_matrix = df[['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']].corr()

# Plotting the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Analyzing the Impact of External Factors

# Temperature vs Sales
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Temperature', y='Weekly_Sales', data=df)
plt.title('Temperature vs Weekly Sales')
plt.xlabel('Temperature')
plt.ylabel('Weekly Sales')
plt.show()

# Fuel Price vs Sales
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Fuel_Price', y='Weekly_Sales', data=df)
plt.title('Fuel Price vs Weekly Sales')
plt.xlabel('Fuel Price')
plt.ylabel('Weekly Sales')
plt.show()

# CPI vs Sales
plt.figure(figsize=(10, 6))
sns.scatterplot(x='CPI', y='Weekly_Sales', data=df)
plt.title('CPI vs Weekly Sales')
plt.xlabel('CPI')
plt.ylabel('Weekly Sales')
plt.show()

# Unemployment vs Sales
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Unemployment', y='Weekly_Sales', data=df)
plt.title('Unemployment vs Weekly Sales')
plt.xlabel('Unemployment Rate')
plt.ylabel('Weekly Sales')
plt.show()

# Sales Forecasting (Optional)
model = ARIMA(sales_over_time, order=(5, 1, 0))
model_fit = model.fit()

# Make predictions
predictions = model_fit.forecast(steps=12)

# Plotting the predictions
plt.figure(figsize=(12, 6))
plt.plot(sales_over_time, label='Actual Sales')
plt.plot(pd.date_range(start=sales_over_time.index[-1], periods=12, freq='W'), predictions, label='Predicted Sales', linestyle='--')
plt.title('Sales Forecast')
plt.xlabel('Date')
plt.ylabel('Weekly Sales')
plt.legend()
plt.show()
