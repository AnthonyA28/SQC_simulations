
import statistics as stat
import numpy as np 
import matplotlib.pyplot as plt
import scipy
import random

def get_AR(phi,_mean, _size):
    X = np.random.normal(0, stdDev, _size)
    X[0] = _mean/(1-phi) + X[0]
    for i in range(1,_size):
        X[i] = X[i-1]*phi + _mean + X[i]
    return X

def get_num_OCL(_X, _ucl, _lcl):
    _n_OCL = 0
    for i in range(_X.size):
        if( _X[i] >= _ucl or _X[i] <= _lcl ):
            _n_OCL = _n_OCL + 1.0 
    return _n_OCL

def get_mean(_X):
    _sum = 0
    _n = 0
    for x in _X:
        _sum = _sum + x
        _n =_n + 1
    return (_sum/_n)

def get_sample_std_dev(_X):
    _mean = get_mean(_X)
    _sumSqr = 0
    _n = 0
    for x in _X:
        _sumSqr = _sumSqr + (x - _mean)*(x - _mean)
        _n = _n + 1
    return (_sumSqr/(_n-1))**0.5


""" Input parameters  """
mean = 0
stdDev = 5
size = 100000
sims = 1000
c = 3.00

for phi in np.linspace(-0.90,0.90,19):
    print("size, n/n_OCL")
    n_OCL = 0 # number of values out of control limits 
    n = 0  # total number of data points
    for sims_ in range(sims):
        X = get_AR(phi, stdDev, size)
        mean_est = get_mean(X)
        stdDev_est = get_sample_std_dev(X)
        ucl = mean_est+c*stdDev_est
        lcl = mean_est-c*stdDev_est
        n = n + size
        n_OCL = n_OCL + get_num_OCL(X, ucl, lcl) # only include phase 2 data 
    print("%.4f,%.4f" % (  phi, n/n_OCL))