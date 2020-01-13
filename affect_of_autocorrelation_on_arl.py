import numpy as np
import matplotlib.pyplot as plt

''' Returns the amount of point in X outisde of the control limits of ucl and lcl '''
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
                    
def get_AR(phi,_mean, _size):
    X = np.random.normal(0, 1, _size)
    X[0] = _mean/(1-phi) + X[0]
    for i in range(1,_size):
        X[i] = X[i-1]*phi + _mean + X[i]
    return X

def get_next_AR(phi, _mean, prev):
    return prev*phi + _mean + np.random.normal(0,1)


""" Input parameters  """
sims = 1000 # the amount of simulations to run
c = 3.00 # the spread of the control limits

for phi in np.linspace(0, 0.9, 5):
    for size in [30,50,75,100,200,300,500,1000,2000,10000]:
        arl_sum = 0 
        for sim in range(sims):
            rl      = 0 # The run length for this dataset
            Xp1     = get_AR(phi, 0, size)  # The phase 1 dataset
            X_bar   = get_mean(Xp1)
            MR      = get_MR(Xp1)
            MR_bar  = get_mean(MR)
            ucl     = X_bar + 3*MR_bar/1.128
            lcl     = X_bar - 3*MR_bar/1.128
            # plt.plot(Xp1)
            # plt.plot(np.ones(Xp1.size)*ucl)
            # plt.plot(np.ones(Xp1.size)*lcl)
            # plt.show()
            x = Xp1[-1] # set x to the last item in the phase 1 dataset
            while True:
                x   = get_next_AR(phi, 0, x)
                rl  += 1
                if x > ucl or x < lcl:
                    break
            arl_sum += rl
        # print(arl_sum/sims)
        print("phi: %.4f, size: %.1f, ARL: %.4f" % (phi, size, arl_sum/sims))
