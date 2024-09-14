import numpy as np
import sympy as sp
import math as m
#10a
def findfibo(i):
    if i < 1 : return -1
    if i == 1 : return 0
    if i == 2 : return 1
    x1 = 0
    x2 = 1
    for k in range(3, i + 1):
        x_next = x2 + x1
        x1 = x2
        x2 = x_next
    return x_next
print(findfibo(11))
#10b
def findfibo(i):
    if i < 1 : return -1
    if i == 1 : return 0
    if i == 2 : return 1
    x = 1.618034
    for k in range(3, i + 1):
        x_next = (x ** i - (1 - 1.618034) ** i) / (5 ** 1/2)
    return x_next
print(findfibo(11))
#10c
def findfibo(i):
    if i < 1 : return -1
    if i == 1 : return 0
    if i == 2 : return 1
    x = 1.618034
    for k in range(3, i + 1):
        x_next = abs((x - x ** i) * 1.618034)
    return x_next
print(findfibo(11))