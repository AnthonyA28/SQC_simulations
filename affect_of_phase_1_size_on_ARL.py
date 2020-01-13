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


""" Input parameters  """
mean = 0 # the known mean
stdDev = 5  # the known stdDev
size_phase_2 = 10000
sims = 50 # the amount of simulations to run
c = 3.00 # the spread of the control limits
max_size_phase_1 = 5000
min_size_phase_1 = 50
skip = 10 # increment of phase_1 size

print("size, ARL_0")
for size_phase_1 in range(min_size_phase_1, max_size_phase_1, skip):

    sumTotal_OCL = 0 # total number of points out of control limits
    n = 0  # total number of  points
    for sim in range(sims):

        X = np.random.normal(mean, stdDev, size_phase_1 + size_phase_2) #generate random normal data with known mean and stdDev
        Xp1 = X[:size_phase_1]
        Xp2 = X[size_phase_1:]
        # mean_est = get_mean(Xp1) # estimate the mean with only phase 1 data
        # stdDev_est = get_sample_std_dev(Xp1) # estimate the standard deviation with only phase 1 data
        stdDev_est = get_sample_stdDev(Xp1)
        mean_est = get_mean(Xp1)
        ucl = mean_est+c*stdDev_est
        lcl = mean_est-c*stdDev_est
        assert(Xp2.size == size_phase_2)
        assert(Xp1.size == size_phase_1)
        n = n + size_phase_2
        sumTotal_OCL = sumTotal_OCL + get_num_OCL(Xp2, ucl, lcl) # only include phase 2 data
    print("%.4f,%.4f" % ( size_phase_1, n/sumTotal_OCL))