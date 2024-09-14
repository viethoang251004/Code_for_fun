import numpy as np
import sympy as sp
import math as m
import matplotlib.pyplot as plt
f = lambda x: x ** 2
def fibonacci(a, b, e):
    f1 = 2
    f2 = 3
    while b - a >= e:
        d = b - a
        x1 = b - d * ((f1 / f2))
        x2 = a + d * ((f1 / f2))
        if f(x1) <= f(x2):
            b = x2
        else:
            a = x1
        temp = f1 + f2
        f1 = f2
        f2 = temp
    print("Min: ", (f(a) + f(b)) / 2)
fibonacci(-2, 1, 0.3)