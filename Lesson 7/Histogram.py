import pandas as pd
import matplotlib.pyplot as plt
import sys

sys.path.append("C:/Users/aryan/PycharmProjects/MachineLearningForTrading/Lesson 3")
# noinspection PyUnresolvedReferences
from Utility_Functions import get_data, plot_data


def compute_daily_returns(df):
    pd_daily_returns = (df / df.shift(1)) - 1
    pd_daily_returns.iloc[0, :] = 0  # Pandas will set values at this row as NaN by default, so wont show on graph
    return pd_daily_returns


def test_run():
    dates = pd.date_range('2010-01-01', '2012-12-31')
    symbols = ['SPY']
    df = get_data(symbols, dates)
    # plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    # plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

    plt.hist(daily_returns, bins=3)


test_run()
