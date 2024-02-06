import numpy as np
from bisection_example import bisection
from fixedpt_example import fixedpt

# Q1
print('Q1')

f = lambda x: x**2 * (x-1)
tol = 1e-6
Nmax = 100

# a
astar, ier = bisection(f, .5, 2, tol, Nmax)
print('-- Q1a: astar:', astar, 'ier:', ier)
# b
astar, ier = bisection(f, -1, 0.5, tol, Nmax)
print('-- Q1b: astar:', astar, 'ier:', ier)
# c
astar, ier = bisection(f,-1, 2, tol, Nmax)
print('-- Q1c: astar:', astar, 'ier:', ier)

# Q2
print('Q2')

tol = 1e-5
Nmax = 100

# a
astar, iter = bisection(lambda x: (x-1)*(x-3)*(x-5), 0, 2.4, tol, Nmax)
print('-- Q2a: astar:', astar, 'iter:', iter)
# b
astar, iter = bisection(lambda x: (x-3)*((x-1)**2), 0, 2, tol, Nmax)
print('-- Q2b: astar:', astar, 'iter:', iter)
# c
astar, iter = bisection(lambda x: np.sin(x), 0, 0.1, tol, Nmax)
print('-- Q2c first interval: astar:', astar, 'iter:', iter)
astar, iter = bisection(lambda x: np.sin(x), 0.5, (np.pi*3)/4, tol, Nmax)
print('-- Q2c second interval: astar:', astar, 'iter:', iter)

# Q3
fa = lambda x: x*(1 + (7-x**5)/(x**2))**3
fb = lambda x: x - (x**5 - 7)/(x**2)
fc = lambda x: x - (x**5 - 7)/(5*(x**4))
fd = lambda x: x - (x**5 - 7)/12

print('Q3 Frist part')
