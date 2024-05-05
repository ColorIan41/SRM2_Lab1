import numpy as np


def f(x): return np.log(x + 2) - x ** 4 + 0.5


def bisection(func, a, b, tol):  ##tol-tolerance
    if np.sign(func(a)) == np.sign(func(b)):
        raise Exception("The scalars a and b do not bound a root")
    m = (a + b) / 2
    if np.abs(func(m)) < tol:
        return m
    elif np.sign(func(a)) == np.sign(func(m)):
        return bisection(func, m, b, tol)
    elif np.sign(func(b)) == np.sign(func(m)):
        return bisection(func, a, m, tol)


root1 = bisection(f, -0.9999, -0.45, 0.1)
root2 = bisection(f, 1.099, 1.45, 0.1)
print(root1)
print(root2)
