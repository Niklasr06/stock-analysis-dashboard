import yfinance as yf
import pandas as pd

def load_data(ticker):

    data = yf.download(ticker, start="2020-01-01")

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.droplevel(1)

    return data