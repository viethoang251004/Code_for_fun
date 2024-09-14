import numpy as np
import sympy as sp
import math as m
#1a
f_n1 = lambda n: 4 * n + 1
n_array1 = np.arange(1, 11)
x_n1 = list( map(f_n1, n_array1))
print(x_n1)
#1b
f_n2 = lambda n: 3 ** n
n_array2 = np.arange(1, 11)
x_n2 = list( map(f_n2, n_array2))
print(x_n2)
#1c
f_n3 = lambda n: n ** 3
n_array3 = np.arange(1, 11)
x_n3 = list( map(f_n3, n_array3))
print(x_n3)
#1d
def caud(n):
    if n < 1: return -1
    if n == 1: return 0
    if n == 2: return 1
    x1 = 0
    x2 = 1
    n4_array = []
    for k in range(3, n + 1):
        x_next = x2 + x1
        n4_array.append(x_next)
        x1 = x2
        x2 = x_next
    return n4_array
print(caud(11))