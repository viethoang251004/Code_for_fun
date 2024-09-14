import numpy as np
import math
import matplotlib.pyplot as plt
import sympy as sp
x = sp.symbols("x")
#(a)
f = abs(x * x * sp.cos(x))
fin = sp.integrate(f,(x, -4, 9))
print("Dien tich cua f(x) =", fin.evalf())
f_a = lambda x: x * x * sp.cos(x)
x_array = np.arange(-4, 9.1, 0.1)
y_array = list(map(f_a, x_array))
plt.plot(x_array, y_array)
plt.grid()
plt.title("4a")
plt.show()
#(b)
f = abs(sp.exp(-(1/2) * (x**2)))
fin = sp.integrate(f, (x, -sp.oo, sp.oo))
print("Dien tich cua f(x) =", fin.evalf())
f_b = lambda x: sp.exp(-(1/2) * (x**2))
x_array = np.arange(-100, 100.1, 0.1)
y_array = list(map(f_b, x_array))
plt.plot(x_array, y_array)
plt.grid()
plt.title("4b")
plt.show()