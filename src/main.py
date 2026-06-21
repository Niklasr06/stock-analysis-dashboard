import pandas as pd
from metrics import add_derived_columns, analyze_ticker
from data_loader import load_data
from visualization import plot_price, plot_combined_returns

TICKERS = ["AAPL", "MSFT", "NVDA", "SPY"]

data_by_ticker = {}
metrics_rows = []

for ticker in TICKERS:
    data = load_data(ticker)
    data["Ticker"] = ticker
    data = add_derived_columns(data)
    data_by_ticker[ticker] = data

    metrics = analyze_ticker(data)
    metrics_rows.append({"Ticker": ticker, **metrics})

comparison = pd.DataFrame(metrics_rows).rename(columns={
    "annual_return": "Annual Return",
    "annual_volatility": "Annual Volatility",
    "max_drawdown": "Maximum Drawdown",
    "sharpe_ratio": "Sharpe Ratio"
})

print(comparison)

comparison.to_csv("data/comparison_metrics.csv", index=False)

historical_prices = pd.concat(
    [data.reset_index() for data in data_by_ticker.values()],
    ignore_index=True
)
historical_prices = historical_prices.rename(columns={"index": "Date"})
historical_prices.to_csv("data/historical_prices.csv", index=False)

daily_returns = pd.DataFrame({
    ticker: data["Daily Return"] for ticker, data in data_by_ticker.items()
})
correlation_matrix = daily_returns.corr()
correlation_matrix.to_csv("data/correlation_matrix.csv")

for ticker, data in data_by_ticker.items():
    plot_price(data, ticker)

plot_combined_returns(data_by_ticker)
