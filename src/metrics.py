import numpy as np

def add_derived_columns(data):

    data["Daily Return"] = data["Close"].pct_change()
    data["Cumulative Return"] = (1 + data["Daily Return"]).cumprod() - 1
    data["MA50"] = data["Close"].rolling(50).mean()
    data["MA200"] = data["Close"].rolling(200).mean()
    data["Peak"] = data["Close"].cummax()
    data["Drawdown"] = (data["Close"] - data["Peak"]) / data["Peak"]

    return data


def analyze_ticker(data):

    average_return = data["Daily Return"].mean()
    daily_volatility = data["Daily Return"].std()
    annual_volatility = daily_volatility * np.sqrt(252)
    annual_return = average_return * 252
    max_drawdown = data["Drawdown"].min()
    sharpe_ratio = annual_return / annual_volatility

    return {
        "annual_return": annual_return,
        "annual_volatility": annual_volatility,
        "max_drawdown": max_drawdown,
        "sharpe_ratio": sharpe_ratio
    }