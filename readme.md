# Walmart Sales Data Analysis

This project analyzes Walmart sales data to identify trends, seasonal patterns, and customer preferences. The analysis includes the impact of holidays, external factors like temperature and fuel prices, and a sales forecasting model.

## Project Structure

- **`requirements.txt`**: Contains the list of Python packages required to run the project.
- **`main.py`**: The main source code file that performs the data analysis and visualization.
- **`walmart_sales_data.csv`**: The dataset used for the analysis.

## Installation

1. **Clone the repository**:
   
   git clone https://github.com/ambarkr21/walmart-sales-analysis.git
   
   cd walmart-sales-analysis
   
Create a virtual environment (optional but recommended):

python -m venv env

Activate the virtual environment:

On Windows:

env\Scripts\activate


pip install -r requirements.txt

Usage

Ensure the dataset (walmart_sales_data.csv) is in the same directory as main.py.

Run the analysis:

python main.py

The script will generate visualizations for the sales trends, holiday impacts, store-wise sales, and the correlation between sales and external factors. It also includes a sales forecasting model.

Features
Sales Trends Over Time: Visualization of total weekly sales over time.
Impact of Holidays on Sales: Analysis of how holidays affect sales.
Sales by Store: Analysis of sales distribution across different stores.
Correlation Analysis: Exploration of correlations between sales and external factors like temperature, fuel price, CPI, and unemployment.
Sales Forecasting: A simple ARIMA model to forecast future sales.
Dataset
The dataset walmart_sales_data.csv contains the following columns:

Store: The store number.
Date: The week ending date.
Weekly_Sales: The sales for the given store in that week.
Holiday_Flag: Indicates whether the week is a special holiday week (1) or not (0).
Temperature: The average temperature in the region.
Fuel_Price: The cost of fuel in the region.
CPI: The consumer price index.
Unemployment: The unemployment rate.
License
This project is licensed under the MIT License.

Contributing
If you want to contribute to this project, please fork the repository and create a pull request. Feel free to open issues for any bugs or feature requests.
