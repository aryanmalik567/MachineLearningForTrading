import os
import matplotlib as plt
import pandas as pd
import sys

sys.path.append("C:/Users/aryan/PycharmProjects/MachineLearningForTrading/Lesson 3")
# noinspection PyUnresolvedReferences
from Utility_Functions import *
os.chdir("C:/Users/aryan/PycharmProjects/MachineLearningForTrading/")


def test_run():
    dates = pd.date_range('2010-01-01', '2012-12-31')
    symbols = ['SPY', 'XOM', 'GOOG', 'GLD']

    # noinspection PyUnresolvedReferences
    df = get_data(symbols, dates)
    # noinspection PyUnresolvedReferences
    plot_data(df)

    print(df.mean())
    print(df.median())
    print(df.std())


test_run()
