import numpy as np

# Matrix A
A = np.array([[-1, 3.5, 14],
              [0, 5, -26],
              [0, 0, 2]])

eigenvalues_A, _ = np.linalg.eig(A)
det_A = np.prod(eigenvalues_A)

print("Eigenvalues of Matrix A:")
print(eigenvalues_A)
print("Determinant of Matrix A:")
print(det_A)
print()

# Matrix B
B = np.array([[-2, 0, 0],
              [99, 0, 0],
              [10, -4.5, 10]])

eigenvalues_B, _ = np.linalg.eig(B)
det_B = np.prod(eigenvalues_B)

print("Eigenvalues of Matrix B:")
print(eigenvalues_B)
print("Determinant of Matrix B:")
print(det_B)
print()

# Matrix C
C = np.array([[5, 5, 0, 2],
              [0, 2, -3, 6],
              [0, 0, 3, -2],
              [0, 0, 0, 5]])

eigenvalues_C, _ = np.linalg.eig(C)
det_C = np.prod(eigenvalues_C)

print("Eigenvalues of Matrix C:")
print(eigenvalues_C)
print("Determinant of Matrix C:")
print(det_C)
print()

# Matrix D
D = np.array([[3, 0, 0, 0],
              [6, 2, 0, 0],
              [0, 3, 6, 0],
              [2, 3, 3, -5]])

eigenvalues_D, _ = np.linalg.eig(D)
det_D = np.prod(eigenvalues_D)

print("Eigenvalues of Matrix D:")
print(eigenvalues_D)
print("Determinant of Matrix D:")
print(det_D)
print()

# Matrix E
E = np.array([[3, 0, 0, 0, 0],
              [-5, 1, 0, 0, 0],
              [3, 8, 0, 0, 0],
              [0, -7, 2, 1, 0],
              [-4, 1, 9, -2, 3]])

eigenvalues_E, _ = np.linalg.eig(E)
det_E = np.prod(eigenvalues_E)

print("Eigenvalues of Matrix E:")
print(eigenvalues_E)
print("Determinant of Matrix E:")
print(det_E)
print()
