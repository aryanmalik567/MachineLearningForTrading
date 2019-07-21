import os
import matplotlib as plt
import pandas as pd
import sys

sys.path.append("C:/Users/aryan/PycharmProjects/MachineLearningForTrading/Lesson 3")
# noinspection PyUnresolvedReferences
from Utility_Functions import *
os.chdir("C:/Users/aryan/PycharmProjects/MachineLearningForTrading/")


def test_run():
    dates = pd.date_range('2012-01-01', '2012-12-31')
    symbols = ['SPY']

    # noinspection PyUnresolvedReferences
    df = get_data(symbols, dates)

    # Plot SPY data, retain axis object
    ax = df['SPY'].plot(title="SPY rolling mean", label='SPY')

    # Compute rolling mean using 20 day window
    rm_SPY = df['SPY'].rolling(window=20).mean()
    # Add rolling mean to same plot
    rm_SPY.plot(label='Rolling mean', ax=ax)

    # Axis labels
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()


def get_rolling_mean(values, window):
    return values.rolling(window=window).mean()


def get_rolling_std(values, window):
    return values.rolling(window=window).std()


def get_bollinger_bands(rm, rstd):
    upper_band = rm + 2*rstd
    lower_band = rm - 2*rstd
    return upper_band, lower_band


def compute_daily_returns(df):
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.iloc[0, :] = 0  # Set daily returns for row 0 to 0
    # return daily_returns

    # Computing with pandas instead
    pd_daily_returns = (df / df.shift(1)) - 1
    pd_daily_returns.iloc[0, :] = 0  # Pandas will set values at this row as NaN by default, so wont show on graph
    return pd_daily_returns


def compute_cumulative_return(df):
    return (df.iloc[-1] / df.iloc[0]) - 1

def test_run2():
    # Read data
    dates = pd.date_range('2012-01-01', '2012-12-31')
    symbols = ['SPY']
    df = get_data(symbols, dates)

    # Compute Bollinger Bands
    # 1. Compute rolling mean
    rm_SPY = get_rolling_mean(df['SPY'], window=20)

    # 2. Compute rolling standard deviation
    rstd_SPY = get_rolling_std(df['SPY'], window=20)

    # 3. Compute upper and lower bands
    upper_band, lower_band = get_bollinger_bands(rm_SPY, rstd_SPY)

    # Plot raw SPY values, rolling mean and Bollinger Bands
    ax = df['SPY'].plot(title="Bollinger Bands", label='SPY')
    rm_SPY.plot(label='Rolling mean', ax=ax)
    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)

    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()

    # Axis labels
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()


def test_run3():
    # Read data
    dates = pd.date_range('2012-07-01', '2012-07-31')  # one month only
    symbols = ['SPY', 'XOM']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

    print("\nCumulative return:\n", compute_cumulative_return(df))


test_run3()
