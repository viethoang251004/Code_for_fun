import numpy as np

# Cau a
A = np.array([[7, 6, -4, 1], [-5, -1, 0, -2], [9, -11, 7, -3], [19, -9, 7, 1]])
w = np.array([[1], [1], [-1], [-3]])

# Check if w is in the column space of A
if np.linalg.matrix_rank(A) == np.linalg.matrix_rank(np.hstack([A, w])):
    print("(a) w is in the column space of A")
else:
    print("(a) w is not in the column space of A")

# Check if w is in the null space of A
if np.allclose(np.dot(A, w), np.zeros_like(w)):
    print("(a) w is in the null space of A")
else:
    print("(a) w is not in the null space of A")

# Cau b
A = np.array([[-8, 5, -2, 0], [-5, 2, 1, -2], [10, -8, 6, -3], [3, -2, 1, 0]])
w = np.array([[1], [2], [1], [0]])

# Check if w is in the column space of A
if np.linalg.matrix_rank(A) == np.linalg.matrix_rank(np.hstack([A, w])):
    print("(b) w is in the column space of A")
else:
    print("(b) w is not in the column space of A")

# Check if w is in the null space of A
if np.allclose(np.dot(A, w), np.zeros_like(w)):
    print("(b) w is in the null space of A")
else:
    print("(b) w is not in the null space of A")
