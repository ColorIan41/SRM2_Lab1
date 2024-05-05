import numpy as np


def f(x): return np.log(x + 2) - x ** 4 + 0.5


def fixed_point(func, x0, tol):
    x1 = func(x0)
    x0 = x1
    if np.abs(x1 - x0) > tol:
        return fixed_point(func, x0, tol)
    else:
        x1 = func(x0)
        return x1


root1 = fixed_point(f, -0.9999, 0.01)
root2 = fixed_point(f, 1.099, 0.01)
print(root1)
print(root2)
