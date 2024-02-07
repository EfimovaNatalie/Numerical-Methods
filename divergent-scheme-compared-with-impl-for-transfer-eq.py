import time
import numpy as np
import matplotlib.pyplot as plt
import math

a = -3 #m/s

def u_0(x):
    return np.sin(2 * math.pi * x)
    #return (10*x) * np.exp(-((10*x - 0.9) ** 2))

t_start = 0
t_stop = 1
tau_1 = 0.001
N = int(1/tau_1)

x_start = 0
x_stop = 1
h = 0.01
M = int(1/h)

TIME_1 = np.arange(t_start, t_stop + tau_1, tau_1)
X_list = np.arange(x_start, x_stop + h, h)

an_sol = np.zeros((len(TIME_1), len(X_list)))

for i in range(len(TIME_1)):
    for j in range(len(X_list)):
        an_sol[i][j] = u_0(X_list[j] - a*TIME_1[i])

num_sol = np.zeros((len(TIME_1), len(X_list)))
implisit_scheme = []
u_0_num = u_0(X_list)
implisit_scheme.append(u_0_num)

b = np.zeros(len(u_0_num))
for i in range(len(X_list)-1):
    b[i] = u_0_num[i]
b[-1] = 0
#matrix for the system
A = np.zeros((len(X_list), len(X_list)))
for i in range(len(X_list)-1):
    A[i][i+1] = a/h
    A[i][i] = (-a/h + 1/tau_1)
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
    implisit_scheme.append(x)
    for i in range(len(X_list)-1):
        b[i] = x[i]
    b[-1] = 0
    #implisit_scheme.append(b)

for i in range(len(TIME_1)):
    num_sol[i][-1] = u_0(X_list[-1] - a*TIME_1[i])
    num_sol[i][0] = num_sol[i][-1]

for i in range(len(X_list)-1):
    num_sol[0][i] = u_0(X_list[i])

for i in range(1, len(TIME_1)):
    for j in range(1, len(X_list)-1):
        num_sol[i][-(j+1)] = num_sol[i-1][-(j+1)] - (a*tau_1/h)*(num_sol[i-1][-j] - num_sol[i-1][-(j+1)])

'''plt.figure(figsize=(10,15))
plt.plot(X_list, an_sol[1])
plt.scatter(X_list, num_sol[1], c='red', s=10)
plt.show()'''
plt.ion()
for i in range(len(TIME_1)):
    plt.clf()
    '''plt.plot(X_list[0:700], an_sol[i][0:700])
    plt.scatter(X_list[0:700], num_sol[i][0:700], c='red', s=10)'''
    plt.plot(X_list, an_sol[i])
    plt.scatter(X_list, num_sol[i], c='red', s=10, label="divergent scheme")
    plt.scatter(X_list, implisit_scheme[i], c='green', s=10, label="implicit scheme")
    plt.legend()
    plt.draw()
    plt.gcf().canvas.flush_events()
    time.sleep(0.02)
plt.ioff()
plt.show()