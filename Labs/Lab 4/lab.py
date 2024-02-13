from fixedpt import fixedpt
import numpy as np

# Prelab
# 1.

p = 1.3652300134140976

g = lambda x: (10/(x+4))**(1/2)

Nmax = 100
tol = 1e-10
x0 = 1.5
[xstar,ier] = fixedpt(g,x0,tol,Nmax)
print('the approximate fixed point is:',xstar[-1])
print('found in',len(xstar),'iterations')

def convergence(xstar, p, alpharange=5):
    abserror = np.abs(xstar - p)
    for alpha in range(1,alpharange):
        l = [np.abs(abserror[i+1] / abserror[i]**alpha) for i in range(len(abserror)-1)]
        print('alpha =',alpha,':',l)
        if l[-1] < 1:
            print('Converges for alpha =',alpha)
            return alpha
    print('Does not converge for any alpha below the limit range of', alpharange)
    return None

alpha = convergence(xstar, p)