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


def plot_comparison(data1, ticker1, data2, ticker2):

    data1["MA50"] = data1["Close"].rolling(50).mean()
    data1["MA200"] = data1["Close"].rolling(200).mean()
    data2["MA50"] = data2["Close"].rolling(50).mean()
    data2["MA200"] = data2["Close"].rolling(200).mean()

    plt.figure(figsize=(12, 6))

    plt.plot(data1.index, data1["Close"], label=ticker1)
    plt.plot(data2.index, data2["Close"], label=ticker2)
    plt.plot(data1.index, data1["MA50"], label=f"{ticker1} MA50")
    plt.plot(data1.index, data1["MA200"], label=f"{ticker1} MA200")
    plt.plot(data2.index, data2["MA50"], label=f"{ticker2} MA50")
    plt.plot(data2.index, data2["MA200"], label=f"{ticker2} MA200")

    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.title(f"{ticker1} vs {ticker2} Price Comparison")

    plt.legend()

    plt.savefig(f"images/{ticker1.lower()}_vs_{ticker2.lower()}_comparison.png")

    plt.show()