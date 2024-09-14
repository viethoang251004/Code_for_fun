import numpy as np

# Matrix A1
A1 = np.array([[4, -5],
               [2, -3]])
eigenvalues_A1, _ = np.linalg.eig(A1)
is_diagonalizable_A1 = np.all(np.isreal(eigenvalues_A1))

# Matrix A2
A2 = np.array([[0, 2],
               [0, 1]])
eigenvalues_A2, _ = np.linalg.eig(A2)
is_diagonalizable_A2 = np.all(np.isreal(eigenvalues_A2))

# Matrix A3
A3 = np.array([[2, 3],
               [1, 4]])
eigenvalues_A3, _ = np.linalg.eig(A3)
is_diagonalizable_A3 = np.all(np.isreal(eigenvalues_A3))

# Matrix A4
A4 = np.array([[1, 2, -2],
               [-2, 5, -2],
               [-6, 6, -3]])
eigenvalues_A4, _ = np.linalg.eig(A4)
is_diagonalizable_A4 = np.all(np.isreal(eigenvalues_A4))

# Matrix A5
A5 = np.array([[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]])
eigenvalues_A5, _ = np.linalg.eig(A5)
is_diagonalizable_A5 = np.all(np.isreal(eigenvalues_A5))

# Print diagonalizability results
print("Diagonalizability results:")
print("Matrix A1 is diagonalizable:", is_diagonalizable_A1)
print("Matrix A2 is diagonalizable:", is_diagonalizable_A2)
print("Matrix A3 is diagonalizable:", is_diagonalizable_A3)
print("Matrix A4 is diagonalizable:", is_diagonalizable_A4)
print("Matrix A5 is diagonalizable:", is_diagonalizable_A5)
