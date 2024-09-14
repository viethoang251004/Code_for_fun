import numpy as np
import sympy as sp
import math as m
import matplotlib.pyplot as plt
x = sp.symbols('x')
#(a)
f = 3 * x ** 4 - 16 * x ** 3 + 18 * x ** 2 - 9
df = sp.diff(f, x)
cvals = sp.solve(df, x)
print('Critical values: ', cvals)
#(b)
f = (x + 2) / (2 * x ** 2)
df = sp.diff(f, x)
cvals = sp.solve(df, x)
print('Critical values: ', cvals)
#(c)
f = - x ** 2 / 3 + x ** 2 + 3 * x + 4
df = sp.diff(f, x)
cvals = sp.solve(df, x)
print('Critical values: ', cvals)
#(d)
f = (5 * x ** 2 + 5) / x
df = sp.diff(f, x)
cvals = sp.solve(df, x)
print('Critical values: ', cvals)