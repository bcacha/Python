import numpy as np
import matplotlib.pyplot as plt

r = 1.5
rf = 4
dr = 0.001
dt = 0.01
x = .2
N = 1000
M = round((rf-r)/dr)
O = round((1-.01)/dt)
plotx = np.zeros(M)
plotx1 = np.zeros(N)
plotx2 = np.zeros(M)
time = np.arange(M)*dr+1.5
time2 = np.arange(M)*dr+1.5


for a in range(1,O):
    x = a * dt
    r = 1.5
    for z in range (M):
        k = round(N - (N / 5) * np.random.rand()-1)
        for y in range(N):
            x = r*x*(1-x)
            plotx1[y] = x
        plotx[z] = plotx1[k]
        r = r + dr
    plotx2 = np.append(plotx2,plotx)
    time2 = np.append(time2,time)


plotx2 = np.delete(plotx2,np.arange(M))
time2 = np.delete(time2,np.arange(M))
np.save('bifurX2',plotx2)
np.save('bifurT2',time2)


plt.scatter(time2,plotx2,s=.1)
plt.show()


