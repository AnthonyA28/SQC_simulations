import numpy as np 
import matplotlib.pyplot as plt

mean = 25
stdDev = 5
size = 500
skipLength = 10
subgroupSize = 4

def get_AR(phi,_mean, _size):
    X = np.random.normal(0, stdDev, _size)
    X[0] = _mean/(1-phi) + X[0]
    for i in range(1,_size):
        X[i] = X[i-1]*phi + _mean + X[i]
    return X

def get_SASmat(X,skipLength,sg_size=4):
    rows = int(X.size/(sg_size*skipLength))*skipLength
    cols = sg_size
    xShew = np.zeros((rows,cols)) #(row,col)
    for row in range(0,rows):
        for c in range(0,cols):
            xShew[rows-row-1,cols-c-1]=X[X.size-(c*skipLength)-row%skipLength-1-int((row)/(skipLength))*skipLength*sg_size] 
    return xShew

def get_X_bar_and_S_SASmat(X,skipLength,sg_size=4):
    xShew = get_SASmat(X,skipLength,sg_size)
    rows = int(X.size/(sg_size*skipLength))*skipLength
    X_bar = np.zeros(rows)
    S = np.zeros(rows)
    for i in range(0,rows):
        X_bar[i]=np.mean(xShew[i])
        S[i] = np.std(xShew[i])
    return X_bar, S



X = get_AR(0.5, mean,size)
t = np.linspace(0,X.size,X.size)

""" Show the original data """
plt.figure(1)
plt.subplot(211)
plt.plot(t, X)

x = get_SASmat(X, skipLength, subgroupSize)
x_bar, s = get_X_bar_and_S_SASmat(X, skipLength, subgroupSize)
ucl_x_bar = np.ones(x_bar.size)*(np.mean(x_bar) + np.std(x_bar)*3)
lcl_x_bar = np.ones(x_bar.size)*(np.mean(x_bar) - np.std(x_bar)*3)
ucl_s = np.ones(s.size)*(np.mean(s) + np.std(s)*3)
lcl_s = np.ones(s.size)*(np.mean(s) - np.std(s)*3)

""" Show the grouped data """ 
plt.subplot(212)
t2 = np.linspace(0,X.size,x_bar.size)
plt.plot(t2,ucl_x_bar)
plt.plot(t2,lcl_x_bar)
plt.plot(t2,ucl_s)
plt.plot(t2,lcl_s)
plt.plot(t2,x_bar)
plt.plot(t2,s)

plt.show()
