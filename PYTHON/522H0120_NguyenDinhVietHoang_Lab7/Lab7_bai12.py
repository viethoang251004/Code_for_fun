import numpy as np
from scipy.linalg import orth

A = np.array([[-10, 13, 7, -11],
              [2, 1, -5, 3],
              [-6, 3, 13, -3],
              [16, -16, -2, 5],
              [2, 1, -5, -7]])

orthogonal_basis = orth(A)

print("Orthogonal Basis:")
print(orthogonal_basis)
