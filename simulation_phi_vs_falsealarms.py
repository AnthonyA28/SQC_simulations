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
n_OCL = 0.0 # number fof values out of control limits 
FalseAlarmRate = np.ndarray(sims)

def get_AR(_phi,_mean, _size):
	_ar = np.random.normal(0, stdDev, _size)
	_ar[0] = _mean + _ar[0]
	for i in range(1,_size):
		_ar[i] = _ar[i-1]*_phi + _mean + _ar[i]
	return _ar


ucl = mean+3*stdDev
lcl = mean-3*stdDev

PHI = np.arange(0,1,0.01)
FalseAlarms = np.ndarray(PHI.size)

for phi_ in range(PHI.size):

	for sims_ in range(sims):
		n_OCL = 0
		T = np.arange(size)
		# X = np.random.normal(mean, stdDev, size)
		X = get_AR(PHI[phi_], mean, size)

		for i_ in range(size):
			if( X[i_] > ucl or X[i_] < lcl ):
				# print("index ", i_ , " is OCL\n")
				n_OCL = n_OCL + 1.0 

		FalseAlarmRate[sims_] = n_OCL/(size*1.0)
		
		UCL_arr = np.ndarray(size) 
		UCL_arr.fill(ucl)
		LCL_arr = np.ndarray(size)
		LCL_arr.fill(lcl)
		# if(sims_==0):
		# 	plt.plot(T,LCL_arr)
		# 	plt.plot(T,UCL_arr)
		# 	plt.plot(T,X)
		# 	plt.show()

	meanFalseAlarmRate = np.mean(FalseAlarmRate)
	print(meanFalseAlarmRate)
	FalseAlarms[phi_] = meanFalseAlarmRate

plt.plot(PHI, FalseAlarms)
plt.show()
np.savetxt("phi_falsealarms.csv", np.vstack((PHI,FalseAlarms)).T, delimiter=',')

# hist, bin_edges = scipy.histogram(FalseAlarmRate, bins = 100)
# # plotting the histogram 
# plt.bar(bin_edges[:-1], hist, width = 0.0001) 
# plt.xlim(min(bin_edges), max(bin_edges)) 
# plt.show() 
# # print(FalseAlarmRate)
# plt.show()


# # plt.show()

