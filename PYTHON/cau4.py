import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math as m
import sympy as sp
#(a)
x, y = sp.symbols('x, y')
f = x + y + x * y

dfx = sp.diff(f, x, 2)
dfy = sp.diff(f, y, 2)

print("second order partial derivative of f(x, y) with regard to x = ", dfx)
print("second order partial derivative of f(x, y) with regard to x = ", dfy)
#(b)
x, y = sp.symbols('x, y')
f = sp.sin(x * y)

dfx = sp.diff(f, x, 2)
dfy = sp.diff(f, y, 2)

print("second order partial derivative of f(x, y) with regard to x = ", dfx)
print("second order partial derivative of f(x, y) with regard to x = ", dfy)
#(c)
x, y = sp.symbols('x, y')
f = x ** 2 * y + sp.cos(y) + y * sp.sin(x)

dfx = sp.diff(f, x, 2)
dfy = sp.diff(f, y, 2)

print("second order partial derivative of f(x, y) with regard to x = ", dfx)
print("second order partial derivative of f(x, y) with regard to x = ", dfy)
#(d)
x, y = sp.symbols('x, y')
f = x * sp.exp(y) + y + 1

dfx = sp.diff(f, x, 2)
dfy = sp.diff(f, y, 2)

print("second order partial derivative of f(x, y) with regard to x = ", dfx)
print("second order partial derivative of f(x, y) with regard to x = ", dfy)