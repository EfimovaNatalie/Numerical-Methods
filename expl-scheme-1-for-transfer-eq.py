import time
import numpy as np
import matplotlib.pyplot as plt

'''def a(x):
    return x'''

a = 10 #m/s

def u_0(x):
    #return np.sin(x - x_stop)
    return (x)*np.exp(-(x - 30)**2)

t_start = 0
t_stop = 0.6
tau_1 = 0.001

x_start = 0
x_stop = 100
h = 0.1

TIME_1 = np.arange(t_start, t_stop + tau_1, tau_1)
X_list = np.arange(x_start, x_stop + h, h)

an_sol = np.zeros((len(TIME_1), len(X_list)))

for i in range(len(TIME_1)):
    for j in range(len(X_list)):
        an_sol[i][j] = u_0(X_list[j] - a*TIME_1[i])

num_sol = np.zeros((len(TIME_1), len(X_list)))

for i in range(len(TIME_1)):
    num_sol[i][-1] = 0

for i in range(len(X_list)-1):
    num_sol[0][i] = u_0(X_list[i])

for i in range(1, len(TIME_1)):
    for j in range(len(X_list) - 1):
        num_sol[i][j] = -a*(num_sol[i-1][j+1] - num_sol[i-1][j])*tau_1/h + num_sol[i-1][j]

'''plt.figure(figsize=(10,15))
plt.plot(X_list, an_sol[1])
plt.scatter(X_list, num_sol[1], c='red', s=10)
plt.show()'''
plt.ion()
for i in range(len(TIME_1)):
    plt.clf()
    '''plt.plot(X_list[0:700], an_sol[i][0:700])
    plt.scatter(X_list[0:700], num_sol[i][0:700], c='red', s=10)'''
    plt.plot(X_list[0:700], an_sol[i][0:700])
    plt.scatter(X_list[0:700], num_sol[i][0:700], c='red', s=10)
    plt.draw()
    plt.gcf().canvas.flush_events()
    time.sleep(0.02)
plt.ioff()
plt.show()