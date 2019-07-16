import pandas as pd


def test_run():
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date, end_date)

    #create an empty dataframe
    df1 = pd.DataFrame(index = dates)

    #create another temporary dataframe
    dfSPY = pd.read_csv('Data\SPY.csv')


if __name__ == "__main__":
    test_run()

#test changes