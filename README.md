# Python-FTSE-100-Monthly-Trend-Analysis
Python FTSE 100 Monthly Trend Analysis from 2000-2025
FTSE 100 Monthly Seasonality Analysis
📈 Project Overview
This project investigates the historical performance of the FTSE 100 index to determine if there are any discernible seasonal trends—specifically, whether certain months of the year have historically provided better or worse returns on average. This type of analysis is often used to explore theories like the "Santa Claus Rally" or "Sell in May and Go Away."

Author: Ash

🛠️ Tools and Libraries
Python: The programming language used for the analysis.

Pandas: For data loading, manipulation, and time-series analysis.

Matplotlib & Seaborn: For creating insightful data visualizations.

🚀 How to Run the Project
Prerequisites: Ensure you have a working Python environment and have installed the required packages from requirements.txt.

Run the analysis script: Execute the Python script from your terminal.

python monthly_trend_analysis.py

The script will print a statistical summary to your console and generate two new plots:

ftse_100_monthly_distribution.png: Shows the spread of returns for each month.

ftse_100_average_monthly_return.png: A bar chart of the average monthly returns.

📊 Results and Visualizations
Distribution of Monthly Returns
The box plot is the most important visualization for this analysis. It shows the full range of returns for each month across the entire 25-year period.

The line inside the box is the median return (the "typical" outcome).

The box represents the middle 50% of all returns for that month.

The whiskers show the range of most returns, and the dots are outliers.

This helps us see not only the average performance but also the volatility and risk associated with each month.

(Insert your ftse_100_monthly_distribution.png image here after you run the script)

Average Monthly Returns
This bar chart simplifies the analysis by showing only the average (mean) return for each month. It provides a quick look at which months have been historically positive (green) or negative (red) on average.

(Insert your ftse_100_average_monthly_return.png image here after you run the script)

📜 Conclusion & Disclaimer
The analysis of the FTSE 100 data from 2000-2025 reveals some slight historical tendencies for certain months to outperform others on average. For example, some months in Q4 and Q2 have historically shown stronger average returns, while late summer months have sometimes shown weaker performance.

IMPORTANT DISCLAIMER: This analysis is purely descriptive and based on historical data. Past performance is not a guarantee or reliable indicator of future results. Financial markets are influenced by countless unpredictable factors, and these historical averages are not strong enough to form the basis of a profitable investment strategy. This analysis is for educational purposes only and does not constitute financial advice.