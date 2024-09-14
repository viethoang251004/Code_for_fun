import numpy as np
import sympy as sp
import math as m
import matplotlib.pyplot as plt
x, y = sp.symbols('x, y')
f_xy = x ** 2 - x * y + y ** 2 * 1 / 2 + 3
dfx = sp.diff(f_xy, x)
dfy = sp.diff(f_xy, y)
x0 = 3
y0 = 2
z0 = f_xy.subs(x, x0).subs(y, y0)
z = z0 + dfx.subs(x, x0).subs(y, y0) * (x - x0) + dfy.subs(x, x0).subs(y, y0) * (y - y0)
fxy = lambda x, y: x ** 2 - x * y + y ** 2 * 1 / 2 + 3
f_tangent = lambda x, y: 4 * x - y - 2
x = np.arange(-10, 10.1, 0.1)
y = x.copy()
X, Y = np.meshgrid(x, y)
Z = fxy(X, Y)
Z_tangent = f_tangent(X, Y)
ax = plt.axes(projection = '3d')
ax.plot_surface(X, Y, Z, cmap = 'hot', linewidth = 0)
ax.plot_surface(X, Y, Z_tangent, cmap = 'Blues', linewidth = 0)
plt.show()