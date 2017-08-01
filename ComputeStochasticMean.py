"""
Functions in this file are used to create ensemble averaged quantities from time-traces where the variable of interest
is time-displacement-invariant. An important example is the *mean square displacement* <r(t)^2>, where <r(t)>=0

"""

import numpy as np

__author__ = 'C.A. Miermans (Arnold-Sommerfeld-Center for Theoretical Physics, LMU Munich)'
__date__ = '31-07-2017'
__credits__ = 'C.A. Miermans, C.P. Broedersz'
__license__ = 'GPL'
__version__ = '1.0.0'
__email__ = "c.miermans@lmu.de"
__status__ = "Production"


def stoch_mean_func_identity(y_1, y_2):
    """
    For computing the mean displacement using the stochastic mean.
    :param y_1: Stochastic variable at an earlier time-point.
    :param y_2: Stochastic variable at a later time-point.
    :return: displacement
    """
    return y_2 - y_1

def stoch_mean_func_square(y_1, y_2):
    """
    For computing the MSD using the stochastic mean.
    :param y_1: Stochastic variable at an earlier time-point.
    :param y_2: Stochastic variable at a later time-point.
    :return: squared displacement
    """
    return (y_2 - y_1) ** 2

def stoch_mean_func_autocorrelator(y_1, y_2):
    """
    For computing the autocorrelator <y(t)y(0)> using the stochastic mean.
    :param y_1: Stochastic variable at an earlier time-point.
    :param y_2: Stochastic variable at a later time-point.
    :return: 'autocorrelated' y-variable
    """
    return y_2 * y_1

def compute_stochastic_mean(x, y, bins, func=stoch_mean_func_square):
    """
    Returns the windowed average of the function :param func applied to the stochastic
    variables :param x and :param y.
    :param x: Time-like variable
    :param y: Value of the stochastic variable at the 'time' :param x
    :param bins: Array of bins
    :param func: Function that takes two arguments that is mapped onto the stochastic variable :param y.
    :return: Bins and the windowed average.
    """
    def add_mean_at_bin(bin_nr):
        """ Adds the stochastic mean at the i-th bin of the time-like variable.
        :param bin_nr: Integer that specifies time-interval over which to compute the stochastic mean.
         """
        select_times = (delta >= bins[bin_nr]) & (delta < bins[bin_nr+1])
        if not select_times.any(): # no suitable bins were found, apparently
            return
        select_Y_1 = Y_1[select_times]
        select_Y_2 = Y_2[select_times]
        mapped_vals = func(select_Y_1, select_Y_2)
        result[bin_nr] = np.mean(mapped_vals[(~np.isnan(mapped_vals)) & (~np.isinf(mapped_vals))])

    assert (np.sort(x) == x).all() # time-like variable has to be sorte
    assert (np.sort(bins) == bins).all() # since "bins" is also a time-like variable, it has to be sorted
    try:
        func(np.ones(10), np.ones(10))
    except TypeError as e:
        print(f'Error message: {e}')
        exit('Please supply a function that can take two numpy arrays as arguments.')

    n_bins = len(bins)
    result = np.zeros(n_bins)
    X_1, X_2 = np.meshgrid(x, x)
    Y_1, Y_2 = np.meshgrid(y, y)
    delta = X_2 - X_1 # all the possible time-differences

    for i in range(n_bins-1): # fill up all the bins
        add_mean_at_bin(i)
    return bins[:-1], result[:-1] # the last bin does not have a right-edge, so its value is undefined

if __name__ == '__main__':
    print("Let's run a test of the stochastic mean!")
    x = np.arange(0, 1_000)
    y = np.cumsum(np.random.randint(0, 3, size=len(x)) - 1)
    bins = np.arange(10)
    bins, Y = compute_stochastic_mean(x, y, bins=bins, func=stoch_mean_func_square)
    import matplotlib.pyplot as plt
    plt.xlabel(r'$t$')
    plt.ylabel(r'$\langle ( x(t)-x(0) )^2 \rangle$')
    plt.loglog(bins, Y, 'ok', label=r'Measured using $\mathtt{compute_stochastic_mean}$')
    plt.loglog(bins, bins**1, ':k', label=r'$\mathrm{MSD} \sim t$')
    plt.legend(loc='upper left')
    plt.show()