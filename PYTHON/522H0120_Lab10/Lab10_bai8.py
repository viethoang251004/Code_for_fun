import numpy as np

# Define the matrices B1 and B2
B1 = np.array([[-18, 13, -4, 4],
               [2, 19, -4, 12],
               [-14, 11, -12, 8],
               [-2, 21, 4, 8]])

B2 = np.array([[6, -8, -4, 5, -4],
               [2, 7, -5, -6, 4],
               [0, -1, -8, 2, 2],
               [-1, -2, 4, 4, -8]])

# Compute the SVD of B1
U1, Sigma1, Vt1 = np.linalg.svd(B1)

# Compute the SVD of B2
U2, Sigma2, Vt2 = np.linalg.svd(B2)

# Print the results
print("SVD of B1:")
print("U1:\n", U1)
print("Sigma1:\n", Sigma1)
print("Vt1:\n", Vt1)

print("SVD of B2:")
print("U2:\n", U2)
print("Sigma2:\n", Sigma2)
print("Vt2:\n", Vt2)
