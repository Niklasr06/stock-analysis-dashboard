import pandas as pd
from metrics import analyze_ticker
from data_loader import load_data
from visualization import plot_price, plot_comparison


qqq_data = load_data("QQQ")
spy_data = load_data("SPY")

qqq_data["Ticker"] = "QQQ"
spy_data["Ticker"] = "SPY"

historical_prices = pd.concat([qqq_data, spy_data])

qqq_metrics = analyze_ticker(qqq_data)
spy_metrics = analyze_ticker(spy_data)



comparison = pd.DataFrame({
    "Metric": [
        "Annual Return",
        "Annual Volatility",
        "Maximum Drawdown",
        "Sharpe Ratio"
    ],
    "QQQ": [
        qqq_metrics["annual_return"],
        qqq_metrics["annual_volatility"],
        qqq_metrics["max_drawdown"],
        qqq_metrics["sharpe_ratio"]
    ],
    "SPY": [
        spy_metrics["annual_return"],
        spy_metrics["annual_volatility"],
        spy_metrics["max_drawdown"],
        spy_metrics["sharpe_ratio"]
    ]
})

print(comparison)

comparison.to_csv(
    "data/comparison_metrics.csv",
    index=False
)

historical_prices.to_csv("data/historical_prices", index=False)
plot_price(qqq_data, "QQQ")
plot_comparison(qqq_data, "QQQ", spy_data, "SPY")

