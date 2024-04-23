import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import scipy.linalg as scila


def driver():

    ''' create  matrix for testing different ways of solving a square 
    linear system'''

    '''' N = size of system'''
    N = 100

    ''' Right hand side'''
    b = np.random.rand(N,1)
    A = np.random.rand(N,N)

    x_scila = scila.solve(A,b)
    x_lu = scila.lu_solve(scila.lu_factor(A),b)

    
    test_scila = np.matmul(A,x_scila)
    test_lu = np.matmul(A,x_lu)
    print(la.norm(test_scila-b))
    print(la.norm(test_lu-b))
    
    ''' Create an ill-conditioned rectangular matrix '''
    N = 10
    M = 5
    A = create_rect(N,M)     
    b = np.random.rand(N,1)


     
def create_rect(N,M):
     ''' this subroutine creates an ill-conditioned rectangular matrix'''
     a = np.linspace(1,10,M)
     d = 10**(-a)
     
     D2 = np.zeros((N,M))
     for j in range(0,M):
        D2[j,j] = d[j]
     
     '''' create matrices needed to manufacture the low rank matrix'''
     A = np.random.rand(N,N)
     Q1, R = la.qr(A)
     test = np.matmul(Q1,R)
     A =    np.random.rand(M,M)
     Q2,R = la.qr(A)
     test = np.matmul(Q2,R)
     
     B = np.matmul(Q1,D2)
     B = np.matmul(B,Q2)
     return B     
          
  
if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()       