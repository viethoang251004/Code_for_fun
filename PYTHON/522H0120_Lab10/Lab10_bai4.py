import numpy as np

# Matrix A
A = np.array([[-2, 2, -3],
              [2, 1, -6],
              [-1, -2, 0]])

# Find eigenvalues and eigenvectors of A
eigenvalues_A, eigenvectors_A = np.linalg.eig(A)

# Find eigenvalues and eigenvectors of A.T
eigenvalues_A_transpose, eigenvectors_A_transpose = np.linalg.eig(A.T)

# Find eigenvalues and eigenvectors of A^(-1)
A_inverse = np.linalg.inv(A)
eigenvalues_A_inverse, eigenvectors_A_inverse = np.linalg.eig(A_inverse)

# Print eigenvalues and eigenvectors of A
print("Eigenvalues of Matrix A:")
print(eigenvalues_A)
print()
print("Eigenvectors of Matrix A:")
print(eigenvectors_A)
print()

# Print eigenvalues and eigenvectors of A.T
print("Eigenvalues of Matrix A.T:")
print(eigenvalues_A_transpose)
print()
print("Eigenvectors of Matrix A.T:")
print(eigenvectors_A_transpose)
print()

# Print eigenvalues and eigenvectors of A^(-1)
print("Eigenvalues of Matrix A^(-1):")
print(eigenvalues_A_inverse)
print()
print("Eigenvectors of Matrix A^(-1):")
print(eigenvectors_A_inverse)
print()
