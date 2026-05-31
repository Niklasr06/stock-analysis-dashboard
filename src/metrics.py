import pandas as pd
import numpy as np

def analyze_ticker(data):

    data["Daily Return"] = data["Close"].pct_change()
    average_return = data["Daily Return"].mean()
    daily_volatility = data["Daily Return"].std()
    annual_volatility = daily_volatility * np.sqrt(252)
    annual_return = average_return * 252
    data["Peak"] = data["Close"].cummax()
    data["Drawdown"] = (data["Close"] - data["Peak"]) / data["Peak"]
    max_drawdown = data["Drawdown"].min()
    sharpe_ratio = annual_return / annual_volatility
    
    return {
        "annual_return": annual_return,
        "annual_volatility": annual_volatility,
        "max_drawdown": max_drawdown,
        "sharpe_ratio": sharpe_ratio
    }