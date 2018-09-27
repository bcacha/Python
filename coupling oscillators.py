import numpy as np
import matplotlib.pyplot as plt

#number of oscillators
N = 200

#time units
T = 100

#time steps
dt = .01

#coupling strength
A = 4

#array of delta distributions, mean = 0, std = 2, N oscillators
s = np.random.normal(0,2,N)
delta = s - np.mean(s) #helps make the average very near zero

#array of starting theta values
theta = np.random.rand(N)*2*np.pi

out_omega = np.zeros(N)

#array for values of omega
omega = np.zeros(N)

#array of r for every T unit
r_save = np.zeros(int(T/dt))

for x in range(int(T/dt)):
    exp = np.mean(np.exp(1j*theta))                 #exponential array of initial thetas
    r = np.abs(exp)                                 #value of r
    psi = np.angle(exp)                             #value of psi
    omega = 1 + delta + A*r*np.sin(psi-theta)       #value of omega (theta dot)
    theta = theta + dt*omega                        #update value of theta
    r_save[x] = r
    if x >= (T - 10) / dt:
        out_omega = out_omega + omega


avg_omega = out_omega/(10/dt)
plt.subplot(131)
plt.scatter(delta,avg_omega,5)
plt.axvline(x=-A*r, color='k',linestyle='--',linewidth=.75)
plt.axvline(x=A*r, color='k',linestyle='--',linewidth=.75)
plt.axhline(y=1, color='k',linestyle='--',linewidth=.75)
plt.xlabel('Natural Frequency')
plt.ylabel('Output Frequency')
plt.title("A="+str(A)+"  "+"N="+str(N))

plt.subplot(132)
plt.axis([0,T/dt,0,1])
plt.plot(np.arange(int(T/dt)),r_save)
plt.xlabel('dt Steps')
plt.ylabel('Order Parameter (r)')
plt.title('r vs dt steps')


plt.show()

