import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from metrics import analyze_ticker
from data_loader import load_data


qqq_data = load_data("QQQ")
spy_data = load_data("SPY")

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