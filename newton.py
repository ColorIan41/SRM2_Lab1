import numpy as np
import sympy as sp


def f(x): return sp.log(x + 2) - x ** 4 + 0.5


x = sp.symbols('x')


def df(x): return sp.diff(f(x), x)


def newton(func, d_func, x0, tol):
    xn = x0
    fxn = func(xn)
    df_xn = df(x).evalf(subs={x: xn})
    if df_xn == 0:
        raise Exception('Zero derivative. No solution found.')
    xn = x0 - fxn / df_xn
    if np.abs(fxn) < tol:
        return xn
    elif np.abs(fxn) > tol:
        return newton(func, d_func, xn, tol)


root1 = newton(f, df, -0.9999, 0.01)
root2 = newton(f, df, 1.099, 0.01)
print(root1)
print(root2)
