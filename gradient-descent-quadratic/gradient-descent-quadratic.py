def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code her
    x = x0
    for i in range(steps):
        df = 2 * a * x + b
        x = x - lr * df 
    return x