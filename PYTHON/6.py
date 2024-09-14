import numpy as np
import sympy as sp
import math as m
n = sp.symbols('n')
#6a
a_n = 1 - 0.2 ** n
print("Limit of the sequence a_n = ", sp.limit_seq(a_n, n))
#6b
a_n = n ** 3 / (n ** 3 + 1)
print("Limit of the sequence a_n = ", sp.limit_seq(a_n, n))
#6c
a_n = (3 + 5 * n ** 2) / (n + n ** 2)
print("Limit of the sequence a_n = ", sp.limit_seq(a_n, n))
#6d
a_n = (n ** 3) / (n + 1)
print("Limit of the sequence a_n = ", sp.limit_seq(a_n, n))
#6e
a_n = sp.exp(1 / n)
print("Limit of the sequence a_n = ", sp.limit_seq(a_n, n))
#6f
a_n = ((n + 1) / (9 * n + 1)) ** 1/2
print("Limit of the sequence a_n = ", sp.limit_seq(a_n, n))
#6g
a_n = ((-1) ** (n + 1) * n) / (n + n ** 1/2)
print("Limit of the sequence a_n = ", sp.limit_seq(a_n, n))
#6h
a_n = sp.tan((2 * n * sp.pi) / (1 + 8 * n))
print("Limit of the sequence a_n = ", sp.limit_seq(a_n, n))
#6i
a_n = sp.factorial(2 * n - 1) / sp.factorial(2 * n + 1)
print("Limit of the sequence a_n = ", sp.limit_seq(a_n, n))
#6j
a_n = sp.log(2 * n ** 2 + 1) - sp.log(n ** 2 + 1)
print("Limit of the sequence a_n = ", sp.limit_seq(a_n, n))