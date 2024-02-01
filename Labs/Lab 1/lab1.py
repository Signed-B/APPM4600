# 3.1.1

x = [1, 2, 3]
print('x*3', x*3)

# this imports numpy and renames it to np
import numpy as np

y = np.array([1,2,3])
print('y*3', y*3)

# 3.1.2

# This is a print statement that prints a statement.
print('this is 3y', 3*y)

# 3.1.3

# This is an import statement that imports the matplotlib.pyplot library and renames it to plt
import matplotlib.pyplot as plt

X = np.linspace(0,2*np.pi,100)
Ya = np.sin(X)
Yb = np.cos(X)

plt.plot(X,Ya)
plt.plot(X,Yb)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# this is a print statement that prints the size of X
print('size of X', X.size)
print('linspace works by creating a vector of 100 evenly spaced points between 0 and 2pi')

# 3.2

# 1.

x = np.linspace(0, 10, 100)
y = np.arange(0, 10, 0.1)

# 2 and 3

# this is a print statement that prints the first three entries of x
print('the first three entries of x are', x[0:3])

# 4 

w = 10**(-np.linspace(1,10,10))
print('the entries of w are', w)

x = np.arange(1, len(w)+1, 1)

plt.semilogy(x, w, label='w')
plt.xlabel('x')
plt.ylabel('w')

# 5

s = 3*w

plt.semilogy(x, s, label='s')
plt.legend()

# 6
plt.savefig('semilogy.png')


