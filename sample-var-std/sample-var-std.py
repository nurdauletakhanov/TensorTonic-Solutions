import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    n = len(x)
    sum = 0
    for i in range(n):
        sum += x[i]
    x_hat = sum / n
    var = 0
    for i in range(n):
        var += (x[i] - x_hat) ** 2
    var = var / (n - 1)
    std = var ** (0.5)
    return (var,std)