import numpy as np
import sympy as sp
import math as m
import matplotlib.pyplot as plt
x = sp.symbols('x')
#(a)
f = x ** 2 - 2 * x - 5
df = sp.diff(f, x)
cvals = sp.solve(df,x)
for x_c in cvals:
    if x_c < 0 or x_c > 2: cvals.remove(x_c)
cvals.extend([0, 2])
yvals = [f.subs(x, v) for v in cvals]
x1 = np.arange(0, 2.1, 0.1)
f1 = lambda x: x ** 2 - 2 * x - 5
y = list(map(f1, x1))
plt.plot(x1, y)
plt.plot(cvals, yvals)
plt.title('4a')
plt.show
#(b)
f = 3 * x + x ** 3 + 5
df = sp.diff(f, x)
cvals = sp.solve(df,x)
for x_c in cvals:
    if x_c < - 4 or x_c > 4: cvals.remove(x_c)
cvals.extend([-4, 4])
yvals = [f.subs(x, v) for v in cvals]
x1 = np.arange(-4.1, 4.1, 0.1)
f1 = lambda x: 3 * x + x ** 3 + 5
y = list(map(f1, x1))
plt.plot(x1, y)
plt.plot(cvals, yvals)
plt.title('4b')
plt.show
#(c)
f = sp.sin(x) + 3 * x ** 2
df = sp.diff(f, x)
cvals = sp.solve(df,x)
for x_c in cvals:
    if x_c < - 2 or x_c > 2: cvals.remove(x_c)
cvals.extend([- 2, 2])
yvals = [f.subs(x, v) for v in cvals]
x1 = np.arange(- 4.1, 4.1, 0.1)
f1 = lambda x: sp.sin(x) + 3 * x ** 2
y = list(map(f1, x1))
plt.plot(x1, y)
plt.plot(cvals, yvals)
plt.title('4c')
plt.show
#(d)
f = sp.exp(x ** 2) + 3 * x
df = sp.diff(f, x)
cvals = sp.solve(df,x)
for x_c in cvals:
    if x_c < - 1 or x_c > 1: cvals.remove(x_c)
cvals.extend([- 1, 1])
yvals = [f.subs(x, v) for v in cvals]
x1 = np.arange(- 4.1, 4.1, 0.1)
f1 = lambda x: sp.exp(x ** 2) + 3 * x
y = list(map(f1, x1))
plt.plot(x1, y)
plt.plot(cvals, yvals)
plt.title('4d')
plt.show