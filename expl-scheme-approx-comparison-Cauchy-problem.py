import numpy as np
import math
import matplotlib.pyplot as plt

b = 1

a = 1

def f(t):
    return 0
    #return (t**2)
    #return 0

start = 0
stop = 1
tau_1 = 0.1
#tau_2 = 0.05
tau_3 = 0.3
def an_solution(t):
    #return (t**3)/3 + b
    return b*np.exp(-a*t)
    #return t**2 - 2*t + 2 - np.exp(-t) + (b-1)*np.exp(-t)

TIME = np.linspace(start, stop + tau_1, 1000)
TIME_1 = np.arange(start, stop + tau_1, tau_1)
#TIME_2 = np.arange(start, stop + tau_2, tau_2)
TIME_3 = np.arange(start, stop + tau_3, tau_3)

u_0 = b
A_2_1 = []
A_3_1 = []
A_2_2 = []
A_3_2 = []
u = u_0

U_analytical = an_solution(TIME)

for t in TIME_1:
    u_n = u
    A_2_1.append(u_n)
    u = (f(t) - a*u_n)*tau_1 + u_n

u = u_0
for t in TIME_3:
    u_n = u
    A_2_2.append(u_n)
    u = (f(t) - a*u_n)*tau_3 + u_n

u = u_0
for t in TIME_1:
    u_n = u # u_(n) - текущее
    A_3_1.append(u_n)
    if len(A_3_1) <= 1:
        u = (f(t) - a * u_0 / 2 + u_0 / tau_1)/(a/2 + 1/tau_1)
    else:
        u_n_1 = A_3_1[-2] #u_(n-1)
        u = (f(t) - a*u_n)*2*tau_1 + u_n_1 #U_(n+1)

u = u_0
for t in TIME_3:
    u_n = u
    A_3_2.append(u_n)
    if len(A_3_2) <= 1:
        u = (f(t) - a * u_0 / 2 + u_0 / tau_3) / (a / 2 + 1 / tau_3)
    else:
        u_n_1 = A_3_2[-2]
        u = (f(t) - a*u_n)*2*tau_3 + u_n_1

plt.figure(figsize=(12, 40))
plt.plot(TIME, U_analytical, label='analytical solution')
plt.scatter(TIME_1, A_2_1, s=5, c='red', label='A_2 for step '+str(tau_1))
plt.scatter(TIME_1, A_3_1, s=8, c='green', label='A_3 for step '+str(tau_1))
plt.plot(TIME_3, A_2_2, c='red', label='A_2 for step '+str(tau_3))
plt.plot(TIME_3, A_3_2, c='green', label='A_3 for step '+str(tau_3))
plt.legend()
plt.title("for a = "+str(a) + ", b = " + str(b) + ", f(t) = 0")
plt.show()