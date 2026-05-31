import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

ticker = "QQQ"

data = yf.download(ticker, start="2020-01-01")
data.columns = data.columns.droplevel(1)

print(data.head())
print(data.shape)
print(data.columns)

print(data.isnull().sum())
print(data.describe())

data["Daily Return"] = data["Close"].pct_change()
print(data.head())

average_return = data["Daily Return"].mean()
print(f"Average Return: {average_return:.2%}")

best_day = data["Daily Return"].max()
print(f"Best day: {best_day:.2%}")

worst_day = data["Daily Return"].min()
print(f"Worst day: {worst_day:.2%}")

daily_volatility = data["Daily Return"].std()
print(f"Daily Volatility: {daily_volatility:.2%}")

annual_volatility = daily_volatility * np.sqrt(252)
print(f"Annual Volatility: {annual_volatility:.2%}")

data["Peak"] = data["Close"].cummax()
data["Drawdown"] = (data["Close"] - data["Peak"]) / data["Peak"]
max_drawdown = data["Drawdown"].min()
print(f"Maximum Drawdown: {max_drawdown:.2%}")

data["MA50"] = data["Close"].rolling(50).mean()
data["MA200"] = data["Close"].rolling(200).mean()
print(data[["Close", "MA50", "MA200"]].tail())


plt.figure(figsize=(12, 6))

plt.plot(data.index, data["Close"], label = "QQQ")
plt.plot(data.index, data["MA50"], label = "MA50")
plt.plot(data.index, data["MA200"], label = "MA200")

plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.title("QQQ from 2020-01-01")
plt.legend()

plt.savefig("images/qqq_analysis.png")

plt.show()

