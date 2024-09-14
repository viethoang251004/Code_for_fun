import numpy as np
import sympy as sp
import math as m
import matplotlib.pyplot as plt
from prettytable import PrettyTable
f = lambda x: x ** 2
mytable = PrettyTable()
mytable.field_names = ['i', 'a', 'b']
def GoldenSearch(a, b, e):
    d = b - a
    i = 1
    while b - a >= e:
        d = 0.618 * d
        x1 = b - d
        x2 = a + d
        if f(x1) <= f(x2):
            b = x2
        else:
            a = x1
        mytable.add_row([i, a, b])
        i = i + 1
        print(mytable)
    print("Min = ", (f(a) + f(b)) / 2)
GoldenSearch(-2, 1, 0.3)