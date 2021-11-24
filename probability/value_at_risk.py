"""
Suppose you're given a portfolio of equities and asked to calculate the 'value at risk' (VaR) via the
variance-covariance method.

The VaR is a statistical risk management technique measuring the maximum loss that an investment portfolio is likely to
face within a specified time frame with a certain degree of confidence. The VaR is a commonly calculated metric used
within a suite of financial metrics and models to help aid in investment decisions.

In order to calculate the VaR of your portfolio, you can follow the steps below:

Calculate periodic returns of the stocks in your portfolio
Create a covariance matrix based on (1)
Calculate the portfolio mean and standard deviation (weighted based on investment levels of each stock in portfolio)
Calculate the inverse of the normal cumulative distribution with a specified probability, standard deviation, and mean
Estimate the value at risk for the portfolio by subtracting the initial investment from the calculation in step 4
"""
import numpy as np
import datetime as dt
import yfinance as yf
from scipy.stats import norm

if __name__ == '__main__':

    # Create our portfolio of equities
    tickers = ['AAPL', 'FB', 'C', 'DIS']

    # Set the investment weights (I arbitrarily picked for example)
    weights = np.array([.25, .3, .15, .3])

    # Set an initial investment level
    initial_investment = 1_000_000

    # Download closing prices
    data = yf.download(" ".join(tickers), start="2021-01-01", end=dt.date.today())['Close']

    # From the closing prices, calculate periodic returns
    returns = data.pct_change()

    # Create a covariance matrix
    cov = returns.cov()

    # Calculate the portfolio mean and standard deviation (weighted based on investment levels of each stock in the
    # portfolio)
    mean_return = (returns.mean()[tickers] * weights).mean()
    sigma_return = np.sqrt(weights.dot(cov).dot(weights))
    portfolio_mean = (1 + mean_return) * initial_investment
    portfolio_sigma = sigma_return * initial_investment

    # Calculate the inverse of the normal cumulative distribution with a specified probability, standard deviation, and
    # mean
    cutoff = norm.ppf(0.95, loc=portfolio_mean, scale=portfolio_sigma)

    # Estimate the value at risk for the portfolio by subtracting the initial investment from the cutoff
    print(f"VaR for the next day is: {initial_investment - cutoff}")
