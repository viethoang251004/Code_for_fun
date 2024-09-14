import numpy as np

# Define the matrices
A1 = np.array([[1, 0],
               [0, -3]])

A2 = np.array([[-5, 0],
               [0, 0]])

A3 = np.array([[np.sqrt(6), 1],
               [0, np.sqrt(6)]])

A4 = np.array([[np.sqrt(3), 2],
               [0, np.sqrt(3)]])

# Calculate the singular values using SVD
singular_values_A1 = np.linalg.svd(A1, compute_uv=False)
singular_values_A2 = np.linalg.svd(A2, compute_uv=False)
singular_values_A3 = np.linalg.svd(A3, compute_uv=False)
singular_values_A4 = np.linalg.svd(A4, compute_uv=False)

# Print the singular values
print("Singular values of A1:", singular_values_A1)
print("Singular values of A2:", singular_values_A2)
print("Singular values of A3:", singular_values_A3)
print("Singular values of A4:", singular_values_A4)
