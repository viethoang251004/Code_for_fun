import numpy as np
import sympy as sp
import math as m
n = sp.symbols('n')
#9a
series = sp.Sum(4 ** n, (n, 1, sp.oo))
converged = series.is_convergent()
if converged:
    print("Chuoi so hoi tu.")
else:
    print("Chuoi so khong hoi tu.")
#9b
series = sp.Sum(5 / (2 ** n), (n, 1, sp.oo))
converged = series.is_convergent()
if converged:
    print("Chuoi so hoi tu.")
else:
    print("Chuoi so khong hoi tu.")