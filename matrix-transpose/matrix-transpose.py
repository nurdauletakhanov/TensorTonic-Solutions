import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.array(A)
    m,n = A.shape
    At = np.zeros((n, m))
    for i in range(m):
        for j in range(n):
            At[j][i] = A[i][j]
    return At
