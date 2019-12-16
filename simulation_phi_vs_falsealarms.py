import statistics as stat
import numpy as np 
import matplotlib.pyplot as plt
import scipy

## Input parameters 
mean = 25
stdDev = 5
size = 1000
sims = 1000

## Simulated measurements 
n_OCL = 0.0 # number of values out of control limits 
FalseAlarmRate = np.ndarray(sims)

def get_AR(phi_,mean_, size_):
	ar_ = np.random.normal(0, stdDev, size_)
	ar_[0] = mean_ + ar_[0]
	for i in range(1,size):
		ar_[i] = ar_[i-1]*phi_ + mean_ + ar_[i]
	return ar_


UCL = mean+3*stdDev
LCL = mean-3*stdDev

for sims_ in range(sims):

	n_OCL = 0
	T = np.arange(size)
	# X = np.random.normal(mean, stdDev, size)
	X = get_AR(0.00, mean, size)

	for i_ in range(size):
		if( X[i_] > UCL or X[i_] < LCL ):
			# print("index ", i_ , " is OCL\n")
			n_OCL = n_OCL + 1.0 

	FalseAlarmRate[sims_] = n_OCL/(size*1.0)
	
	UCL_arr = np.ndarray(size) 
	UCL_arr.fill(UCL)
	LCL_arr = np.ndarray(size)
	LCL_arr.fill(LCL)
	if(sims_==0):
		plt.plot(T,LCL_arr)
		plt.plot(T,UCL_arr)
		plt.plot(T,X)
		plt.show()

meanFalseAlarmRate = np.mean(FalseAlarmRate)
print(meanFalseAlarmRate)

hist, bin_edges = scipy.histogram(FalseAlarmRate, bins = 100)
# plotting the histogram 
plt.bar(bin_edges[:-1], hist, width = 0.0001) 
plt.xlim(min(bin_edges), max(bin_edges)) 
plt.show() 
# print(FalseAlarmRate)
plt.show()


# plt.show()

