import os
import pandas as pd
import matplotlib.pyplot as plt


def plot_selected(title, df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    # Your code here
    df = df.loc[start_index:end_index, columns]

    axis = df.plot(title=title)
    axis.set_xlabel("Date")
    axis.set_ylabel("Prices")

    plt.show()


def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        # Read and join data for each symbol

        df_temp = pd.read_csv('data/{}.csv'.format(symbol), index_col="Date", parse_dates=True,
                              usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)

        if symbol == 'SPY':
            df = df.dropna(subset=['SPY'])

    return df


def normalize_data(df):
    return df / df.iloc[0, :]


def plot_data(df):
    axis = df.plot(title="Stock prices")
    axis.set_xlabel("Date")
    axis.set_ylabel("Prices")

    plt.show()


def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']

    # Get stock data
    df = get_data(symbols, dates)

    '''
    # Slice by dates range
    print(df.loc['2010-01-01':'2010-01-31'])  # January

    # Slice by symbols
    print(df['GOOG'])
    print(df[['IBM', 'GLD']])
    

    print(df.loc['2010-01-01':'2010-01-31', ['SPY', 'IBM']])  # Two dimensional slicing
    print(plot_data(df))
    

    # Slice and plot
    plot_selected(df, ['SPY', 'IBM'], '2010-03-01', '2010-04-01')
    '''

    # Displaying normalised data
    df = normalize_data(df)
    plot_selected("Normalized prices", df, ['SPY', 'GOOG', 'IBM', 'GLD'], '2010-01-01', '2010-12-31')


if __name__ == "__main__":
    test_run()
