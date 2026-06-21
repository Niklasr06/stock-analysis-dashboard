import matplotlib.pyplot as plt

def plot_price(data, ticker):

    plt.figure(figsize=(12, 6))

    plt.plot(data.index, data["Close"], label=ticker)
    plt.plot(data.index, data["MA50"], label="MA50")
    plt.plot(data.index, data["MA200"], label="MA200")

    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.title(f"{ticker} Price with Moving Averages")

    plt.legend()

    plt.savefig(f"images/{ticker.lower()}_analysis.png")

    plt.close()


def plot_combined_returns(data_by_ticker):

    plt.figure(figsize=(12, 6))

    for ticker, data in data_by_ticker.items():
        plt.plot(data.index, data["Cumulative Return"], label=ticker)

    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.title("Cumulative Return Comparison")

    plt.legend()

    plt.savefig("images/cumulative_return_comparison.png")

    plt.close()