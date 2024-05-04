import tkinter as tk
from tkinter import ttk
import requests
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
import numpy as np
import pandas as pd

def get_stock_data(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

def plot_chart():
    symbol = symbol_entry.get()
    api_key = api_key_entry.get()

    data = get_stock_data(symbol, api_key)

    df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace=True)
    df['4. close'] = df['4. close'].astype(float)

    high = df['4. close'].max()
    low = df['4. close'].min()
    fib_levels = [0, 0.236, 0.382, 0.5, 0.618, 1]
    fib_prices = [low + level * (high - low) for level in fib_levels]

    buy_dates = df[df['4. close'] > high * 0.618].index
    sell_dates = df[df['4. close'] < low * 0.382].index

    plt.clf()
    plt.plot(df.index, df['4. close'], label='DAX')

    for price in fib_prices:
        plt.axhline(y=price, color='r', linestyle='--', label=f'Fib')

    plt.scatter(buy_dates, df.loc[buy_dates, '4. close'], color='g', marker='^', s=100, label='Buy Position')
    plt.scatter(sell_dates, df.loc[sell_dates, '4. close'], color='r', marker='v', s=100, label='Sell Position')

    plt.title('DAX Price Chart with Fibonacci Levels and Buy/Sell Positions')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    canvas.draw()

app = tk.Tk()
app.title("Stock Price Analysis")

symbol_label = ttk.Label(app, text="Symbol:")
symbol_label.grid(row=0, column=0, padx=5, pady=5)
symbol_entry = ttk.Entry(app)
symbol_entry.grid(row=0, column=1, padx=5, pady=5)

api_key_label = ttk.Label(app, text="API Key:")
api_key_label.grid(row=1, column=0, padx=5, pady=5)
api_key_entry = ttk.Entry(app)
api_key_entry.grid(row=1, column=1, padx=5, pady=5)

plot_button = ttk.Button(app, text="Plot Chart", command=plot_chart)
plot_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

fig = plt.figure(figsize=(10, 6))
plt.tight_layout()
canvas = FigureCanvasTkAgg(fig, master=app)
canvas.get_tk_widget().grid(row=3, column=0, columnspan=2, padx=5, pady=5)

app.mainloop()
