import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo


def error(line, data):
    ''' Compute error between given line model and observed data

    Parameters
    ----------
    line: tuple/list/array (C0, C1) where C0 is slope and C1 is y intercept
    data: 2D array where each row is a point (x, y)

    Returns error as a single real value
    '''

    err = np.sum((data[:, 1] - (line[0] * data[:, 0] + line[1])) ** 2)  # (Actual data point - (C0 * X + C1))^2
    return err


def fit_line(data, error_func):
    '''Fit a line to given data, using a supplied error function

    Parameters
    ----------
    data: 2D array where each row is a point (X0, Y)
    error_func: function that computes the error between a line and observed data

    Returns line that minimizes the error function
    '''

    # Generate initial guess for line model
    line = np.float32([0, np.mean(data[:, 1])])  # C0 = 0, C1 = mean(y values of all data points)

    # Plot initial guess
    x_ends = np.float32([-5, 5])  # Limiting domain of X
    plt.plot(x_ends, line[0] * x_ends + line[1], 'm--', linewidth=2.0, label="Initial guess")

    # Call optimizer to minimize err func
    result = spo.minimize(error_func, line, args=(data,), method='SLSQP', options={'disp': True})
    return result.x


def test_run():
    # Create original line
    l_orig = np.float32([4, 2])  # C0 = 4, C1 = 2
    print("Original line: C0 = {}, C1 = {}".format(l_orig[0], l_orig[1]))
    Xorig = np.linspace(0, 10, 21)
    Yorig = l_orig[0] * Xorig + l_orig[1]
    plt.plot(Xorig, Yorig, 'b--', linewidth=2.0, label="Original line")

    # Generate noisy data points
    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma, Yorig.shape)
    data = np.asarray([Xorig, Yorig + noise]).T
    plt.plot(data[:, 0], data[:, 1], 'go', label="Data points")

    # Try to fit line to this data
    l_fit = fit_line(data, error)
    print("Fitted line: C0 = {}, C1 = {}".format(l_fit[0], l_fit[1]))
    plt.plot(data[:, 0], l_fit[0] * data[:, 0] + l_fit[1], 'r--', linewidth=2.0, label="Fitted line")

    # Add legend and show plot
    plt.legend(loc="upper left")
    plt.show()


test_run()
