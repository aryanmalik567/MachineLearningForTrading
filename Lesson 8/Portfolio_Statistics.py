import pandas as pd
import sys
import math

sys.path.append("C:/Users/aryan/PycharmProjects/MachineLearningForTrading/Lesson 3")
# noinspection PyUnresolvedReferences
from Utility_Functions import get_data, plot_data


def cumulative_return(df):
    return (df.iloc[-1] / df.iloc[0]) - 1


def compute_daily_returns(df):
    pd_daily_returns = (df / df.shift(1)) - 1
    pd_daily_returns.iloc[0, :] = 0  # Pandas will set values at this row as NaN by default, so wont show on graph
    return pd_daily_returns


def avg_daily_return(df):
    return df.mean()


def std_daily_return(df):
    return df.std()


def compute_sharpe_ratio(avg_daily_return, daily_risk_free, std_dev):
    return math.sqrt(252) * (avg_daily_return - daily_risk_free) / std_dev


def test_run():
    dates = pd.date_range('2012-01-01', '2012-12-31')
    symbols = ['GOOG']
    df = get_data(symbols, dates)
    plot_data(df)

    daily_returns = compute_daily_returns(df)

    print("Cumulative Return:", cumulative_return(df).values)
    print("Average Daily Return:", avg_daily_return(daily_returns).values)
    print("Std Dev Daily Return:", std_daily_return(daily_returns).values)

    sharpeRatio = compute_sharpe_ratio(avg_daily_return(daily_returns), 0.000562, std_daily_return(daily_returns))

    print("Sharpe Ratio:", sharpeRatio)


test_run()
