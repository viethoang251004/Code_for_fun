import numpy as np
import sympy as sp

A2 = sp.Matrix([[1, 0, 2, 3], [4, -1, 0, 2], [0, -1, -8, -10]])

# cau 4a
# find a basis for the null-space of A2
basis = A2.nullspace()

# extract basis vectors as column vectors
v1 = np.array(basis[0].tolist()).reshape(-1, 1)
v2 = np.array(basis[1].tolist()).reshape(-1, 1)

# print basis vectors
print("(a) Basis for null-space of A2:")
print(v1)
print(v2)