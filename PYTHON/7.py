import numpy as np
import sympy as sp
import math as m
#7e
a1 = 1
firstfiveterms = [a1]
a_n = a1
for i in range(0, 4):
    a_next = 5 * a_n - 3
    firstfiveterms.append(a_next)
    a_n = a_next
print(firstfiveterms)
#7f
a1 = 2
firstfiveterms = [a1]
a_n = a1
for i in range(0, 4):
    a_next = a_n / (a_n + 1)
    firstfiveterms.append(a_next)
    a_n = a_next
print(firstfiveterms)
n = sp.symbols('n')
#7a
a_n = 1 - (0.2) ** n
firstfiveterms = [a_n]
for n in range(0, 4):
    a_n = 1 - (0.2) ** n
    firstfiveterms.append(a_n)
print(firstfiveterms)
#7b
a_n = (2 * n) / (n ** 2 + 1)
firstfiveterms = [a_n]
for n in range(0, 4):
    a_n = (2 * n) / (n ** 2 + 1)
    firstfiveterms.append(a_n)
print(firstfiveterms)
#7c
a_n = ((-1) ** (n - 1)) / (5 ** n)
firstfiveterms = [a_n]
for n in range(0, 4):
    a_n = (2 * n) / (n ** 2 + 1)
    firstfiveterms.append(a_n)
print(firstfiveterms)
#7d
a_n = 1 / sp.factorial(n + 1)
firstfiveterms = [a_n]
for n in range(0, 4):
    a_n = 1 / sp.factorial(n + 1)
    firstfiveterms.append(a_n)
print(firstfiveterms)