import numpy as np
import matplotlib.pyplot as plt

x = np.logspace(-16, 1, endpoint=False, num=100)

def f1(x,d):
    return np.cos(x+d) - np.cos(x)
def f2(x,d):
    return -2*np.sin(x+d/2)*np.sin(d/2)

plt.plot(x, np.abs(f1(x, np.pi) - f2(x, np.pi)), label='d=pi')
plt.plot(x, np.abs(f1(x, 10**6) - f2(x, 10**6)), label='d=10^6')
plt.legend()
plt.xlabel('log(x)')
plt.ylabel('error')
plt.xscale('log')
plt.title('f1(x, d) - f2(x, d)')
plt.show()