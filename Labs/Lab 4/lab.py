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

def convergence(xstar, p, alpharange=2):
    abserror = np.abs(xstar - p)
    for alpha in range(alpharange, 0, -1):
        l = [np.abs(abserror[i+1] / abserror[i]**alpha) for i in range(len(abserror)-1)]
        print('alpha =',alpha,':',l)
        if l[-1] < 1:
            print('Converges for alpha =',alpha)
            return alpha
    print('Does not converge for any alpha below the limit range of', alpharange)
    return None

alpha = convergence(xstar, p)

# Exercises
print('======== Exercises ========')


# q2

def hat(p, tol=1e-10, Nmax=100):
    phat = []
    # prevent out of bounds
    for i in range(len(p)-2):
        # compute Aitken's delta squared
        nexthat = p[i] - (p[i+1]-p[i])**2/(p[i+2]-2*p[i+1]+p[i])

        # tolerance check
        if len(phat) > 0 and np.abs(nexthat - phat[-1]) < tol:
            phat.append(nexthat)
            return np.array(phat)
        phat.append(nexthat)
    return np.array(phat)

# q3
xstarhat = hat(xstar)
print(xstarhat)
alpha = convergence(xstarhat, p)
print('Aitken\'s alpha =',alpha)

