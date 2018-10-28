# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 09:57:13 2018

@author: fsk16

Computational Physics Assignment Matrix Methods
"""

import matrixMethods as m
import numpy as np

def LU_decomposition(matrix):
    """ Returns two matrices: lower , upper (L,U) 
    assert matrix.shape[0] == matrix.shape[1] , " Matrix is not NxN"""
    N = matrix.shape[0]                         # Setting dimensions of L and U
    lower = np.zeros([N,N])                        # Initialize L, U and result
    upper = np.zeros([N,N])
    decomposed = np.zeros([N,N])
    
    for j in range(N):                              # Go over a_1j and B_1j
        lower[j][j] = 1                             # Diagonals a_ii = 1
        for i in range(N):                          # Looping over all rows for given j
            
            if i <= j:                              # Upper elements
                sumForBeta = 0
                upper[0][j] = matrix[0][j]          # i=1, B_1j element always a_1j
                if i > 0:                           # Summation part of equation
                    for k in range(i):
                        sumForBeta += lower[i][k] * upper[k][j]
                    upper[i][j] = matrix[i][j] - sumForBeta
                    
            if i > j:                               # Lower elements
                sumForAlpha = 0
                for k in range(j):                  # Summation in equation
                    sumForAlpha += lower[i][k] * upper[k][j]
                lower[i][j] = 1/upper[j][j] * (matrix[i][j] - sumForAlpha)
                
    decomposed = lower + upper - np.identity(N)     # Combine L and U
    return lower , upper                            # Returning them seperately is more convenient

def determinant(LU_matrix):
    det = 1
    for i in range(LU_matrix.shape[0]):
        det *= LU_matrix[i][i]
    return det

def forwardSubst(L , b):
    """ L is NxN matrix, lower part of decomposition, b is a vector sized 1xN
        Function returns N sized vector for y  """
    N = b.size
    y = np.zeros([N])
    assert L[0][0] > 0.001 , "Div by zero"
    y[0] = b[0] / L[0][0]                              # Setting first element
    for i in np.linspace(1, N-1, N-1):
        i = int(i)
        summation = 0
        for j in range(i):
            j = int(j)
            summation += L[i][j] * y[j]
            
        y[i] = 1/L[i][i] * (b[i] - summation)
    return y

def backwardSubst(U , y):
    """ U is NxN matrix, upper part of decomposition, y is a vector sized 1xN
        Function returns N sized vector for x  """
    N = y.shape[0]
    x = np.zeros([N])
    N = N-1                                         # Shift N down for indexing
    x[N] = y[N] / U[N][N]                              # Setting first element
    for i in np.linspace(N-1, 0, N):
        i = int(i)
        summation = 0
        for j in np.linspace(i+1, N, N-i):
            j = int(j)
            summation += U[i][j] * x[j]
        x[i] = 1/U[i][i] * (y[i] - summation)
    return x
    
def solveEquation(A , b):
    """ Equation is Ax = b ,  A is a matrix, x and b are vectors"""
    lower, upper = LU_decomposition(A)
    y = forwardSubst(lower , b)
    x = backwardSubst(upper , y)
    return x

def inverse(matrix):
    N = matrix.shape[0]                         # Number of rows in A, columns in inv(A)
    M = matrix.shape[1]  
    invMatrix = np.zeros([M,N])
    for j in range(N):
        identity_j = np.zeros([N])
        identity_j[j] = 1
        invMatrix[j] = solveEquation(matrix , identity_j)
    invMatrix = np.transpose(invMatrix)             # Vertical vectors are used horizontally, 
    return invMatrix                                # so the resulting matrix needs to be transposed

if __name__ == "__main__":

    matrixAssignment = np.array([[3. , 1. , 0. , 0. , 0. ],
                                 [3. , 9. , 4. , 0. , 0. ],
                                 [0. , 9. , 20., 10., 0. ],
                                 [0. , 0. ,-22., 31.,-25.],
                                 [0. , 0. , 0. ,-55., 60.] ])
    b = np.array([ 2. , 5., -4., 8. , 9.])
    c = np.array([[ 2.] ,[ 5.],[ -4.],[ 8.] , [9.]])
    d = m.MatrixMultiplication(c,b)
    print(d)
    x = solveEquation(matrixAssignment , b)
    bVectorCheck = m.MatrixMultiplication(matrixAssignment , x)
  #  print(bVectorCheck)                 # WORKS HERE
  #  print(inverse(matrixAssignment))    # WORKS HERE

    """
    print("x is: ", x)
    b_new = np.identity(5)
    y = forwardSubst(lower , b_new)
    x = backwardSubst(upper , y)
    bVectorCheck = m.MatrixMultiplication(matrixAssignment , x)
    print("x is: ", x)
    print("identity: ", bVectorCheck)"""