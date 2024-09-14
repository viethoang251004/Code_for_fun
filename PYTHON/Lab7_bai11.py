import numpy as np


def check_orthonormal_columns(matrix):
    m, n = matrix.shape
    U = np.transpose(matrix)
    result = np.dot(U, matrix)
    identity = np.eye(n)
    return np.allclose(result, identity)


# Example usage
a = np.pi/2
U = np.array([
    [np.cos(a), -np.sin(a)],
    [np.sin(a), np.cos(a)]
])

print(check_orthonormal_columns(U))
