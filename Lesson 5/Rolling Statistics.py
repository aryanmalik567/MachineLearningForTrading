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
    rm_SPY = pd.rolling_mean(df['SPY'], window=20)
    # Add rolling mean to same plot
    rm_SPY.plot(label='Rolling mean', ax=ax)

    # Axis labels
    ax.setxlabel("Date")
    ax.setylabel("Price")
    ax.legend(loc='upper left')
    plt.show()


test_run()
