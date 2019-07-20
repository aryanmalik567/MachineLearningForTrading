import os
import matplotlib as plt
import pandas as pd

os.chdir("C:/Users/aryan/PycharmProjects/MachineLearningForTrading/Lesson 3")
print(os.getcwd())
from Utility_Functions import *

os.chdir("C:/Users/aryan/PycharmProjects/MachineLearningForTrading/")

def test_run():
    dates = pd.date_range('2010-01-01', '2012-12-31')
    symbols = ['SPY', 'XOM', 'GOOG', 'GLD']
    df = get_data(symbols, dates)
    plot_data(df)
