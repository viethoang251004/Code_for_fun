import numpy as np
import sympy as sp
import math as m
x = sp.symbols('x')
#4a
f1 = sp.cos(x)
maclaurin_poly1 = f1.series(x, 0, 6)
print('Maclaurin series of f(x): ', maclaurin_poly1)
#4b
f2 = sp.exp(x)
maclaurin_poly2 = f2.series(x, 0, 12)
print('Maclaurin series of f(x): ', maclaurin_poly2)
#4c
f3 = 1 / (1 - x)
maclaurin_poly3 = f3.series(x, 0, 12)
print('Maclaurin series of f(x): ', maclaurin_poly3)
#4d
f4 = sp.tan(x)
maclaurin_poly4 = f4.series(x, 0, 12)
print('Maclaurin series of f(x): ', maclaurin_poly4)