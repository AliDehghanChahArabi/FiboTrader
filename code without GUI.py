import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import pandas as pd

def get_stock_data(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

# Settings
api_key = 'YOUR_API_KEY'
symbol = 'DAX'

# received data‌
data = get_stock_data(symbol, api_key)

# Convert data to DataFrame
df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
df.index = pd.to_datetime(df.index)
df.sort_index(inplace=True)
df['4. close'] = df['4. close'].astype(float)

# Calculation of Fibonacci levels
high = df['4. close'].max()
low = df['4. close'].min()
fib_levels = [0, 0.236, 0.382, 0.5, 0.618, 1]
fib_prices = [low + level * (high - low) for level in fib_levels]

# Determining buying and selling times
buy_dates = df[df['4. close'] > high * 0.618].index
sell_dates = df[df['4. close'] < low * 0.382].index

# Charts
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['4. close'], label='DAX')

# Add Fibonacci levels 
for price in fib_prices:
    plt.axhline(y=price, color='r', linestyle='--', label=f'Fib')

# Add points for input time 
plt.scatter(buy_dates, df.loc[buy_dates, '4. close'], color='g', marker='^', s=100, label='Buy Position')
plt.scatter(sell_dates, df.loc[sell_dates, '4. close'], color='r', marker='v', s=100, label='Sell Position')

plt.title('DAX Price Chart with Fibonacci Levels and Buy/Sell Positions')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()
