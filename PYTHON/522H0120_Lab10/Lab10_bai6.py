import numpy as np

# Define matrix A
A = np.array([[1, 2, -2],
              [0, 3, -2],
              [0, 0, 1]])

# Find eigenvalues and eigenvectors of A
eigenvalues, eigenvectors = np.linalg.eig(A)

# Construct matrix P with eigenvectors as columns
P = np.column_stack(eigenvectors)

# Compute inverse of matrix P
P_inv = np.linalg.inv(P)

# Compute diagonal matrix D using eigenvalues
D = np.diag(eigenvalues)

# Compute P^(-1)*A*P
D_transformed = np.matmul(np.matmul(P_inv, A), P)

# Print the results
print("Eigenvectors:")
print(P)
print("Diagonal matrix D:")
print(D)
print("P^(-1)*A*P:")
print(D_transformed)
