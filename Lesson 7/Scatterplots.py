import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
    symbols = ['SPY', 'XOM', 'GLD']
    df = get_data(symbols, dates)
    plot_data(df)

    daily_returns = compute_daily_returns(df)
    # plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

    # Scatterplot SPY vs XOM
    daily_returns.plot(kind='scatter', x='SPY', y='XOM')
    betaXOM, alphaXOM = np.polyfit(daily_returns['SPY'], daily_returns['XOM'], 1)  # X axis, Y axis, degree of line (1)
    plt.plot(daily_returns['SPY'], betaXOM * daily_returns['SPY'] + alphaXOM, '-', color='r')
    plt.show()
    print("Beta XOM", betaXOM)
    print("Alpha XOM", alphaXOM)

    # Scatterplot SPY vs GLD
    daily_returns.plot(kind='scatter', x='SPY', y='GLD')
    betaGLD, alphaGLD = np.polyfit(daily_returns['SPY'], daily_returns['GLD'], 1)
    plt.plot(daily_returns['SPY'], betaGLD * daily_returns['SPY'] + alphaGLD, '-', color='r')
    plt.show()
    print("Beta GLD", betaGLD)
    print("Alpha GLD", alphaGLD)

    # Calculate correlation coefficient
    print(daily_returns.corr(method='pearson'))


test_run()
