import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy import linalg
import time
import math

a = 1 #m/s

def u_0(x):
    #return (x) * np.exp(-((5*x - 0.5) ** 2))
    return np.sin(2*math.pi*x)

t_start = 0
t_stop = 1
tau_1 = 0.01
N = int(1/tau_1)

x_start = 0
x_stop = 1
h = 0.01
M = int(1/h)

TIME_1 = np.arange(t_start, t_stop+tau_1, tau_1)
X_list = np.arange(x_start, x_stop+h, h)

an_sol = np.zeros((len(TIME_1), len(X_list)))

for i in range(len(TIME_1)):
    for j in range(len(X_list)):
        an_sol[i][j] = u_0(X_list[j] - a*TIME_1[i])

num_sol = []
u_0_num = u_0(X_list)
num_sol.append(u_0_num)

b = np.zeros(len(u_0_num))
for i in range(1, len(X_list)):
    b[i-1] = u_0_num[i]
b[-1] = 0
#matrix for the system
A = np.zeros((len(X_list), len(X_list)))
for i in range(len(X_list)-1):
    A[i][i] = -a/h
    A[i][i+1] = (a/h + 1/tau_1)
A[-1][0] = 1/h
A[-1][-1] = -1/h #+ 1/tau_1

#print(np.linalg.inv(tau_1*A))
for i in range(int(N)):
    b_old = b[:]
    x = np.linalg.solve(tau_1*A, b_old)
    #print(np.allclose(np.dot(tau_1*A, x), b_old))
    #print(x)
    '''x_new = np.zeros(len(x))
    x_new[0] = x[-1]
    for i in range(len(x)-1):
        x_new[i+1] = x[i]'''
    num_sol.append(x)
    for i in range(1, len(X_list)):
        b[i - 1] = x[i]
    b[-1] = 0

plt.ion()
for i in range(len(TIME_1)):
    plt.clf()
    plt.plot(X_list, an_sol[i])
    plt.scatter(X_list, num_sol[i], c='red', s=10)
    plt.draw()
    plt.gcf().canvas.flush_events()
    time.sleep(0.02)
plt.ioff()
plt.show()