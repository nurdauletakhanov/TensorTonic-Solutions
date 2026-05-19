import numpy as np
def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    X = np.array(X)
    y = np.array(y)
    ridge_matrix = (X.T @ X + lam * np.identity(X.shape[1])) 
    inverse_ridge_matrix = np.linalg.inv(ridge_matrix)
    ridge_beta = inverse_ridge_matrix @ X.T @ y
    return ridge_beta
    # Write code here