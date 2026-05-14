import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    result = 0
    total_prob = 0
    for i in range(len(x)):
        total_prob += p[i]
        result += x[i] * p[i]
    if total_prob != 1:
        raise(ValueError)
    return result
