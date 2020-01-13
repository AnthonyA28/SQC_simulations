import numpy as np
import matplotlib.pyplot as plt

''' Returns the amount of point in X outisde of the control limits of ucl and lcl '''
def get_num_OCL(X, ucl, lcl):
    n_OCL = 0
    for i in range(X.size):
        if( X[i] >= ucl or X[i] <= lcl ):
            n_OCL = n_OCL + 1
    return n_OCL

def get_mean(X):
    summ = 0
    n = 0
    for x in X:
        summ = summ + x
        n =n + 1
    return (summ/n)

def get_sample_stdDev(X):
    mean = get_mean(X)
    sumSqr = 0
    n = 0
    for x in X:
        sumSqr = sumSqr + (x - mean)*(x - mean)
        n = n + 1
    return (sumSqr/(n-1))**0.5

def get_MR(X):
    MR = np.zeros(X.size-1)
    for i in range(X.size-1):
        MR[i] = abs(X[i+1]- X[i])
    assert(X.size - 1 == MR.size)
    return MR


""" Input parameters  """
sims = 10000 # the amount of simulations to run
c = 3.00 # the spread of the control limits


for size in [30,50,75,100,200,300,500,1000,2000,10000]:
    arl_sum = 0 
    for sim in range(sims):
        rl      = 0 # The run length for this dataset
        Xp1     = np.random.normal(0, 1, size)  # The phase 1 dataset
        X_bar   = get_mean(Xp1)
        MR      = get_MR(Xp1)
        MR_bar  = get_mean(MR)
        ucl     = X_bar + 3*MR_bar/1.128
        lcl     = X_bar - 3*MR_bar/1.128
        while True:
            x   = np.random.normal(0, 1)
            rl  += 1
            if x > ucl or x < lcl:
                break
        arl_sum += rl
    # print(arl_sum/sims)
    print("size: ", size, ", Arl: ", arl_sum/sims)

