# Stock Analysis Dashboard

## Overview

This project analyzes historical market data using Python and compares the performance and risk characteristics of different ETFs.

The current version focuses on the comparison between:

- QQQ (Invesco QQQ Trust)
- SPY (SPDR S&P 500 ETF Trust)

The application retrieves historical price data from Yahoo Finance, calculates key financial metrics, visualizes price trends, and exports comparison results for further analysis in Power BI.

---

## Features

### Data Collection

- Historical market data retrieval using Yahoo Finance
- Automatic data cleaning and preprocessing
- MultiIndex handling for downloaded datasets

### Performance Analysis

- Daily Returns
- Annual Return
- Best Trading Day
- Worst Trading Day

### Risk Analysis

- Daily Volatility
- Annualized Volatility
- Maximum Drawdown
- Sharpe Ratio

### Technical Analysis

- 50-Day Moving Average (MA50)
- 200-Day Moving Average (MA200)

### Visualization

- Historical price chart
- Moving average visualization
- Export of charts as PNG images

### Benchmark Comparison

Comparison of:

- QQQ
- SPY

Metrics included:

- Annual Return
- Annual Volatility
- Maximum Drawdown
- Sharpe Ratio

### Data Export

- CSV export for Power BI integration

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Yahoo Finance (yfinance)
- Git
- GitHub

---

## Project Structure

text stock-analysis-dashboard/ │ ├── data/ │   └── comparison_metrics.csv │ ├── images/ │   └── qqq_analysis.png │ ├── src/ │   ├── main.py │   ├── data_loader.py │   ├── metrics.py │   └── visualization.py │ ├── requirements.txt └── README.md 

---

## Example Metrics

| Metric | QQQ | SPY |
|----------|----------|----------|
| Annual Return | 22.93% | 16.73% |
| Annual Volatility | 24.91% | 20.36% |
| Maximum Drawdown | -35.12% | -33.72% |
| Sharpe Ratio | 0.92 | 0.82 |

---

## Example Visualization

The project generates charts displaying:

- Historical price development
- 50-Day Moving Average
- 200-Day Moving Average

Example output:

QQQ Analysis

---

## Future Improvements

Planned features include:

- Interactive Power BI dashboard
- Portfolio analysis with multiple assets
- Additional benchmark comparisons
- CAGR calculation
- Risk-adjusted performance metrics
- Streamlit web dashboard
- Automated reporting

---

## Installation

Clone the repository:

bash git clone https://github.com/your-username/stock-analysis-dashboard.git cd stock-analysis-dashboard 

Create a virtual environment:

bash python -m venv venv source venv/bin/activate 

Install dependencies:

bash pip install -r requirements.txt 

Run the project:

bash python src/main.py 

---

## Author

Niklas Ringeisen

Digital Business Student  
Hochschule Reutlingen