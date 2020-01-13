import numpy as np 
import matplotlib.pyplot as plt

mean = 25
stdDev = 5
size = 100
phi = 0.5

def get_AR(phi,_mean, _size):
    X = np.random.normal(0, stdDev, _size)
    X[0] = _mean/(1-phi) + X[0]
    for i in range(1,_size):
        X[i] = X[i-1]*phi + _mean + X[i]
    return X

def get_ACF(X, lags):
    ACF = np.zeros(lags)
    mean = np.mean(X)
    for k in range(0,ACF.size):
        cov_k = 0.0
        cov_0 = 0.0
        for t in range(0,X.size - k):
            cov_k += (X[t]-mean)*(X[t+k]-mean)
        for t in range(0,X.size):
            cov_0 += (X[t]-mean)*(X[t]-mean)
        ## print("cov_k ", cov_k)
        ## print("cov_0 ", cov_0)
        ACF[k] = cov_k / cov_0
    return ACF

T = np.arange(size)
lags = 10
X = get_AR(phi, mean, size)
ACF = get_ACF(X, lags)

""" It is known that AC at lag k = phi^k """
ACF_theo = np.ndarray(lags)
for i in range(0,ACF_theo.size):
    ACF_theo[i]=phi**(i)
print(ACF)
print(ACF_theo)
