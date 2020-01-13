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

def get_AR(phi,_mean, _size):
    X = np.random.normal(0, stdDev, _size)
    X[0] = _mean/(1-phi) + X[0]
    for i in range(1,_size):
        X[i] = X[i-1]*phi + _mean + X[i]
    return X



""" Input parameters  """
mean = 0
stdDev = 5
size = 10000
sims = 100
c = 3.00
phase_1 = 1000
print("phi, n_OCL, ARL_0")
for phi in np.linspace(-0.95, 0.95, 30):
    n_OCL = 0 # number of values out of control limits 
    n = 0  # total number of data points
    for sims_ in range(sims):
        X = get_AR(phi, stdDev, size)
        mean_est = get_mean(X[:phase_1])
        stdDev_est = get_sample_std_dev(X[:phase_1])
        ucl = mean_est+c*stdDev_est
        lcl = mean_est-c*stdDev_est
        n = n + size
        n_OCL = n_OCL + get_num_OCL(X[phase_1:], ucl, lcl)
    print("%.4f,%.4f,%.4f" % (  phi, n_OCL, n/n_OCL))