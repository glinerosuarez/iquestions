# -*- coding: utf-8 -*-

"""
Using Monte Carlo methods, simulate future stock price outcomes for Apple ($AAPL) using Python. You can read more about
Monte Carlo simulation (in a finance context) here.

Below is code using Python to grab the initial stock price data for Apple, to help get you started:
"""

# Import required libraries
import datetime
import numpy as np
import yfinance as yahooFinance


if __name__ == '__main__':

  start_date = datetime.datetime(2009, 1, 1)
  end_date = datetime.datetime(2021, 1, 26)
  apple_data = yahooFinance.Ticker("AAPL")
  data = apple_data.history(start=start_date, end=end_date)

  data["PDR"] = np.log(data["Close"] / data["Close"].shift(1))

  drift = data["PDR"].mean() - data["PDR"].var()/2
  std = data["PDR"].std()

  def next_day_price(price):
    return price*np.exp(drift + np.random.normal(scale=std))

  def generate_trajectory(price):
    T = 254
    returns = np.zeros(T)
    returns[0] = price
    for i in range(1, T):
      returns[i] = next_day_price(returns[i - 1])

    return returns[-1]

  def mc_simulation(n):
    x = np.zeros(n)
    for i in range(n):
      x[i] = generate_trajectory(data["Close"][-1])

    return x

  mc_result = mc_simulation(10_000)

  print(mc_result.mean(), mc_result.std())

