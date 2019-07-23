import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo


def error_poly(curve, data):
    err = np.sum((data[:, 1] - np.polyval(curve, data[:, 0]))**2)
    return err


def fit_poly(data, error_func, degree=4):
    Cguess = np.poly1d(np.ones(degree+1, dtype=np.float32))

    x = np.linspace(-5, 5, 21)
    plt.plot(x, np.polyval(Cguess, x), 'm--', linewidth=2.0, label="Initial guess")

    result = spo.minimize(error_func, Cguess, args=(data,), method='SLSQP', options={'disp': True})
    return np.poly1d(result.x)


def test_run():
    # Create original curve
    Corig = np.poly1d(np.array([1, -10, -5, 60, 50], dtype=np.float32))
    print("Original polynomial: {}x^4 + {}x^3 + {}x^2 + {}x + {}".format(Corig[0], Corig[1], Corig[2], Corig[3], Corig[4]))
    Xorig = np.linspace(-5, 5, 21)
    Yorig = np.polyval(Corig, Xorig)
    plt.plot(Xorig, Yorig, 'b--', linewidth=2.0, label="Original line")

    # Generate noisy data points
    noise_sigma = 50.0
    noise = np.random.normal(0, noise_sigma, Yorig.shape)
    data = np.asarray([Xorig, Yorig + noise]).T
    plt.plot(data[:, 0], data[:, 1], 'go', label="Data points")

    # Try to fit line to this data
    c_fit = fit_poly(data, error_poly)
    print("Fitted polynomial: {}x^4 + {}x^3 + {}x^2 + {}X + {}".format(c_fit[0], c_fit[1], c_fit[2], c_fit[3], c_fit[4]))
    plt.plot(data[:, 0], np.polyval(c_fit, data[:, 0]), 'r--', linewidth=2.0, label="Fitted line")

    # Add legend and show plot
    plt.legend(loc="upper left")
    plt.show()


test_run()
