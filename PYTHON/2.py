import numpy as np
import sympy as sp
#2a
d = 15
a1 = 5
f_n = lambda n: a1 + (n - 1) * d
a55 = f_n(55)
print(a55)
for i in np.arange(0, 101):
    if f_n(i) == 230:
        print ("Tai vi tri n = ", i , "thi f(n) = 230")
        break
    if f_n(i) > 230: break
#2b
r = 1/2
a1 = 120
f_n = lambda n: a1 * (r) ** (n - 1)
a10 = f_n(10)
print(a10)
for i in np.arange(0, 101):
    if f_n(i) == 15 / 32:
        print ("Tai vi tri n = ", i , "thi f(n) = 15 / 32")
        break
    if f_n(i) < 15 / 32: break