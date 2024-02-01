import numpy as np
import numpy.linalg as la
import math
import time


def driver():
    n = 100
    x = np.linspace(0,np.pi,n)
    # this is a function handle. You can use it to define
    # functions instead of using a subroutine like you
    # have to in a true low level language.

    f = lambda x: x**2 + 4*x + 2*np.exp(x)
    g = lambda x: 6*x**3 + 2*np.sin(x)
    # y = f(x)
    # w = g(x)

    # exercise 1
    n = 2
    y = np.array([1,0])
    w = np.array([0,1])

    # evaluate the dot product of y and w
    dp = dotProduct(y,w,n)
    # print the output
    print('the dot product for exercise 1 is : ', dp)

    # exercise 2
    n = 3
    y = np.array([[1,0,0],[0,1,0],[0,0,2]])
    w = np.array([[0,1,0],[0,0,1],[1,0,0]])

    # evaluate the matrix product of y and w
    mp = matrixProduct(y,w,n)
    # print the output
    print('the matrix product for exercise 2 is : ', mp)

    # exercise 3
    n = 2
    y = np.array([1,0])
    w = np.array([0,1])
    print('the dot product for exercise 3 is : ', np.dot(y,w))
    n = 3
    y = np.array([[1,0,0],[0,1,0],[0,0,2]])
    w = np.array([[0,1,0],[0,0,1],[1,0,0]])
    print('the matrix product for exercise 3 is : ', np.dot(y,w)) 

    print('======= Timing Results =======')
    n = 2
    y = np.array([1,0])
    w = np.array([0,1])
    st = time.time()
    for _ in range(1000):
        # evaluate the dot product of y and w
        dp = dotProduct(y,w,n)
    print('the dot product for exercise 1 1000 times took : ', time.time()-st)
    st = time.time()
    for _ in range(1000):
        # evaluate the dot product of y and w
        dp = np.dot(y,w)
    print('the dot product for exercise 3 1000 times took : ', time.time()-st)

    n = 3
    y = np.array([[1,0,0],[0,1,0],[0,0,2]])
    w = np.array([[0,1,0],[0,0,1],[1,0,0]])
    st = time.time()
    for _ in range(1000):
        # evaluate the matrix product of y and w
        mp = matrixProduct(y,w,n)
    print('the matrix product for exercise 2 1000 times took : ', time.time()-st)
    st = time.time()
    for _ in range(1000):
        # evaluate the matrix product of y and w
        mp = np.dot(y,w)
    print('the matrix product for exercise 3 1000 times took : ', time.time()-st)
    return


def dotProduct(x,y,n):
    # Computes the dot product of the n x 1 vectors x and y
    dp = 0.
    for j in range(n):
        dp = dp + x[j]*y[j]
    return dp

def matrixProduct(x,y,n):
    # Computes the matrix product of the n x n matrices x and y
    z = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                z[i,j] = z[i,j] + x[i,k]*y[k,j]
    return z


driver()