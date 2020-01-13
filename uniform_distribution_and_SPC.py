import statistics as stat
import numpy as np 
import matplotlib.pyplot as plt
import scipy
""" Input parameters  """
mean = 25
stdDev = 5
size = 1000
sims = 1000
phi = 0.0

"""Simulated measurements"""
n_OCL = 0 # number of values out of control limits 
FalseAlarmRate = np.ndarray(sims)

def get_AR(_phi,_mean, _size, stdDev):
    low = -5
    high = 5
    _ar = np.random.uniform(low,high, _size)
    _ar[0] = _mean/(1-_phi) # start at the longrun mean 
    # _ar[0] = _mean # start 'mean'
    for i in range(1,_size):
        _ar[i] = _ar[i-1]*_phi + _mean + _ar[i]
    return _ar

def get_num_OCL(_X, _size_, _ucl, _lcl):
    _n_OCL = 0
    for i_ in range(size):
        if( _X[i_] > _ucl or _X[i_] < _lcl ):
            _n_OCL = _n_OCL + 1.0 
    return _n_OCL

for sims_ in range(sims):
    n_OCL = 0
    T = np.arange(size)
    X = get_AR(phi, mean, size, stdDev)
    mean_est = np.mean(X)
    stdDev_est = np.std(X)
    ucl = mean_est+(3**0.5)*stdDev_est
    lcl = mean_est-(3**0.5)*stdDev_est
    print("mean: ", mean_est)
    print("ucl: ", ucl)
    print("lcl: ", lcl)
    print("stdDev_est: ", stdDev_est)
    UCL_arr = np.ndarray(size) 
    UCL_arr.fill(ucl)
    LCL_arr = np.ndarray(size)
    LCL_arr.fill(lcl)
    n_OCL = get_num_OCL(X, size, ucl, lcl)
    FalseAlarmRate[sims_] = n_OCL/(size*1.0)

meanFalseAlarmRate = np.mean(FalseAlarmRate)
print(meanFalseAlarmRate)

plt.plot(T,UCL_arr)
plt.plot(T,LCL_arr)
plt.plot(T,X)
plt.show()