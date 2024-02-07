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
print('-- 7**(1/5) =', 7**(1/5))
print('-- fa(7**(1/5)) =', fa(7**(1/5)))
print('-- fb(7**(1/5)) =', fb(7**(1/5)))
print('-- fc(7**(1/5)) =', fc(7**(1/5)))
print('-- fd(7**(1/5)) =', fd(7**(1/5)))

print('Q3 Second part')
x0 = 1
tol = 1e-10
Nmax = 100

# xstar, ier = fixedpt(fa, x0, tol, Nmax)
print('-- Q3a: overflow error')
# xstar, ier = fixedpt(fb, x0, tol, Nmax)
print('-- Q3b: overflow error')
xstar, ier = fixedpt(fc, x0, tol, Nmax)
print('-- Q3c: xstar:', xstar, 'ier:', ier)
xstar, ier = fixedpt(fd, x0, tol, Nmax)
print('-- Q3d: xstar:', xstar, 'ier:', ier)

import matplotlib.pyplot as plt
x = np.linspace(0, 2, 10000)
# plt.plot(x, fa(x), label='fa')
# plt.plot(x, fb(x), label='fb')
# plt.plot(x, fc(x), label='fc')
plt.plot(x, fd(x), label='fd')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.savefig('lab3_q3_fa.png')