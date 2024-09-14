import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math as m
import sympy as sp
#(a)
x, y = sp.symbols('x, y')
f = 2 * x * x - 3 * y - 4

dfx = sp.diff(f, x, 1)
dfy = sp.diff(f, y, 1)

print("first order partial derivative of f(x, y) with regard to x = ", dfx)
print("first order partial derivative of f(x, y) with regard to x = ", dfy)
#(b)
x, y = sp.symbols('x, y')
f = (x ** 2 - 1) * (y + 2)

dfx = sp.diff(f, x, 1)
dfy = sp.diff(f, y, 1)

print("first order partial derivative of f(x, y) with regard to x = ", dfx)
print("first order partial derivative of f(x, y) with regard to x = ", dfy)
#(c)
x, y = sp.symbols('x, y')
f = x ** 2 - x * y + y ** 2

dfx = sp.diff(f, x, 1)
dfy = sp.diff(f, y, 1)

print("first order partial derivative of f(x, y) with regard to x = ", dfx)
print("first order partial derivative of f(x, y) with regard to x = ", dfy)
#(d)
x, y = sp.symbols('x, y')
f = 5 * x * y - 7 * x ** 2 - y ** 2 + 3 * x - 6 * y + 2

dfx = sp.diff(f, x, 1)
dfy = sp.diff(f, y, 1)

print("first order partial derivative of f(x, y) with regard to x = ", dfx)
print("first order partial derivative of f(x, y) with regard to x = ", dfy)