import numpy as np
import sympy as sp
import math as m
x = sp.symbols('x')
#3a
f = sp.cos(x)
taylor_poly = f.series(x, m.pi / 3, 6)
print('Taylor series of f(x) at pi / 3: ', taylor_poly)
#3b
f = sp.log(x)
taylor_poly = f.series(x, 2, 10)
print('Taylor series of f(x) at 2: ', taylor_poly)
#3c
f = sp.exp(x)
taylor_poly = f.series(x, 3, 12)
print('Taylor series of f(x) at 3: ', taylor_poly)