import numpy as np
import sympy as sp
import math as m
import matplotlib.pyplot as plt
x = sp.symbols('x')
#(a)
f = x ** 3 - 27 * x
df = sp.diff(f, x)
cvals = sp.solve(df,x)
print('Critical values: ', cvals)
for x_c in cvals:
    if x_c >= 0 or x_c <=5: cvals.remove(x_c)
cvals.extend([0, 5])
yvals = [f.subs(x, v) for v in cvals]
print('The absolute maximum is ',  max(yvals))
print('The absolute minimum is ',  min(yvals))
#(b)
f = 3 / 2 * x ** 4 - 4 * x ** 3 + 4
df = sp.diff(f, x)
cvals = sp.solve(df,x)
print('Critical values: ', cvals)
for x_c in cvals:
    if x_c >= 0 or x_c <= 3: cvals.remove(x_c)
cvals.extend([0, 3])
yvals = [f.subs(x, v) for v in cvals]
print('The absolute maximum is ',  max(yvals))
print('The absolute minimum is ',  min(yvals))
#(c)
f = 1 / 2 * x ** 4 - 4 * x ** 2 + 5
df = sp.diff(f, x)
cvals = sp.solve(df,x)
print('Critical values: ', cvals)
for x_c in cvals:
    if x_c >= 1 or x_c <= 3: cvals.remove(x_c)
cvals.extend([1, 3])
yvals = [f.subs(x, v) for v in cvals]
print('The absolute maximum is ',  max(yvals))
print('The absolute minimum is ',  min(yvals))
#(d)
f = 5 / 2 * x ** 4 - 20 / 3 * x ** 3 + 6
df = sp.diff(f, x)
cvals = sp.solve(df,x)
print('Critical values: ', cvals)
for x_c in cvals:
    if x_c >= -1 or x_c <= 3: cvals.remove(x_c)
cvals.extend([-1, 3])
yvals = [f.subs(x, v) for v in cvals]
print('The absolute maximum is ',  max(yvals))
print('The absolute minimum is ',  min(yvals))