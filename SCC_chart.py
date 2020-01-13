
def get_SSC_LCL_UCL(X, skipLength):
    cols = skipLength
    rows = int(X.size/skipLength)
    scc = np.transpose(X[X.size - rows*cols:].reshape(rows,cols))
    print(scc)
    LCL = np.zeros(scc.shape)
    for row in range(0,np.size(scc,0)):
        LCL[row] = np.mean(scc[row])-3*np.std(scc[row])

    UCL = np.zeros(scc.shape)
    for row in range(0,np.size(scc,0)):
        UCL[row] = np.mean(scc[row])+3*np.std(scc[row])

    return scc, LCL, UCL



mean = 25
stdDev = 5
size = 50
skipLength = 3

X = get_AR(0.0, mean,size)
# X = np.arange(0,size)
t = np.linspace(0,X.size,X.size)
scc, ucl, lcl = get_SSC_LCL_UCL(X, skipLength)

print(scc)
for row in range(0,np.size(scc,0)):
    plt.plot(scc[row])
    plt.plot(ucl[row])
    plt.plot(lcl[row])
plt.show()