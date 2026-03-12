import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    npx = np.asarray(x, dtype=float)
    result = 1 / (1 + np.exp(-npx))
    return result
