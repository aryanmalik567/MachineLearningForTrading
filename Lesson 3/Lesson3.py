import pandas as pd
import os

os.chdir("C:/Users/aryan/PycharmProjects/MachineLearningForTrading/")


def test_run():
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date, end_date)

    # create an empty data frame
    df1 = pd.DataFrame(index=dates)

    # create another temporary data frame
    dfSPY = pd.read_csv('Data\SPY.csv', index_col="Date", parse_dates=True,
                        usecols=['Date', 'Adj Close'], na_values=['nan'])

    # Rename 'Adj Close' column to SPY to prevent clash with other stocks
    dfSPY = dfSPY.rename(columns={'Adj Close': 'SPY'})

    # Join the two data frames
    df1 = df1.join(dfSPY, how='inner')

    # Generalised method to add more stocks
    symbols = ['GOOG', 'IBM', 'GLD']
    for symbol in symbols:
        df_temp = pd.read_csv('Data/{}.csv'.format(symbol), index_col="Date", parse_dates=True,
                              usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df1 = df1.join(df_temp)

    print(df1)


if __name__ == "__main__":
    test_run()


