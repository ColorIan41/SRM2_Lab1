import numpy as np


def f(x): return np.log(x + 2) - x ** 4 + 0.5


def secant(func, x0, x1, tol):
    if x0 == x1:
        raise ZeroDivisionError("Cannot divide by zero")
    xn = x0 - func(x0) * ((x1 - x0) / (func(x1) - func(x0)))
    if np.abs(xn - x1) < tol:
        return xn
    elif np.abs(xn - x1) > tol:
        return secant(func, x1, xn, tol)


root1 = secant(f, -0.9999, -0.45, 0.001)
root2 = secant(f, 1.099, 1.45, 0.001)
print(root1)
print(root2)
