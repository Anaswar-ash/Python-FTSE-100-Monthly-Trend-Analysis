import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_monthly_trends():
    """
    Loads FTSE 100 data, analyzes the performance for each month of the year,
    and saves visualizations to identify any seasonal trends.
    """
    # --- Load and Prepare Data ---
    try:
        df = pd.read_csv("chart (1).csv")
        df.columns = ['Date', 'FTSE_100']
        df['Date'] = pd.to_datetime(df['Date'], format='%m/%Y')
        df.set_index('Date', inplace=True)
    except FileNotFoundError:
        print("Error: 'chart (1).csv' not found. Make sure it's in the same directory.")
        return
    except Exception as e:
        print(f"An error occurred during data loading: {e}")
        return

    # --- Monthly Analysis ---
    
    # Calculate monthly percentage returns
    df['monthly_return'] = df['FTSE_100'].pct_change() * 100
    
    # Add a 'Month' column for grouping
    df['Month'] = df.index.month_name()
    
    # Order the months chronologically for plotting
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    
    # --- Visualization & Summary ---
    
    sns.set_theme(style="whitegrid")
    
    # 1. Box Plot of Monthly Returns
    plt.figure(figsize=(14, 7))
    sns.boxplot(x='Month', y='monthly_return', data=df, order=month_order)
    plt.title('Distribution of FTSE 100 Monthly Returns (2000-2025)', fontsize=16)
    plt.xlabel('Month')
    plt.ylabel('Monthly Return (%)')
    plt.xticks(rotation=45)
    plt.axhline(0, color='black', linestyle='--', linewidth=0.8) # Add a zero line
    plt.savefig('ftse_100_monthly_distribution.png')
    print("Saved monthly return distribution plot.")

    # 2. Bar Chart of Average Monthly Returns
    # Calculate summary statistics
    monthly_stats = df.groupby('Month')['monthly_return'].agg(['mean', 'median']).reindex(month_order)

    plt.figure(figsize=(14, 7))
    colors = ['green' if x > 0 else 'red' for x in monthly_stats['mean']]
    monthly_stats['mean'].plot(kind='bar', color=colors)
    plt.title('Average FTSE 100 Monthly Return (2000-2025)', fontsize=16)
    plt.xlabel('Month')
    plt.ylabel('Average Monthly Return (%)')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.savefig('ftse_100_average_monthly_return.png')
    print("Saved average monthly return plot.")

    # --- Print a summary to the console ---
    print("\n--- Monthly Trend Analysis Summary ---")
    print("This analysis looks at historical data to see if certain months have, on average, performed better than others.")
    
    # Calculate the probability of a positive return for each month
    positive_month_prob = df.groupby('Month')['monthly_return'].apply(lambda x: (x > 0).mean()).reindex(month_order)
    monthly_stats['positive_prob'] = positive_month_prob
    
    print("\nMonthly Performance Statistics (2000-2025):")
    print(monthly_stats.round(2))

    best_month_avg = monthly_stats['mean'].idxmax()
    worst_month_avg = monthly_stats['mean'].idxmin()

    print(f"\nHistorically, the best performing month on average has been {best_month_avg}.")
    print(f"Historically, the worst performing month on average has been {worst_month_avg}.")
    
    print("\nIMPORTANT DISCLAIMER:")
    print("This analysis is based on historical data and is for informational purposes only. Past performance is not an indicator of future results. This is not financial advice.")

    plt.show()

if __name__ == '__main__':
    analyze_monthly_trends()
