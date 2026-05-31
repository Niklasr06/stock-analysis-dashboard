import matplotlib.pyplot as plt

def plot_price(data, ticker):

    data["MA50"] = data["Close"].rolling(50).mean()
    data["MA200"] = data["Close"].rolling(200).mean()

    plt.figure(figsize=(12, 6))

    plt.plot(data.index, data["Close"], label=ticker)
    plt.plot(data.index, data["MA50"], label="MA50")
    plt.plot(data.index, data["MA200"], label="MA200")

    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.title(f"{ticker} Price with Moving Averages")

    plt.legend()

    plt.savefig(f"images/{ticker.lower()}_analysis.png")

    plt.show()