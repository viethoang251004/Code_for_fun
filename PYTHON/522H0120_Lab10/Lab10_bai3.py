import numpy as np

# Matrix M
M = np.array([[-3, -5, -7],
              [-2, 1, 0],
              [1, 5, 5]])

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(M)

# Print eigenvalues
print("Eigenvalues of Matrix M:")
print(eigenvalues)
print()

# Find eigenvectors
eigenvector_dict = {}
for i in range(len(eigenvalues)):
    eigenvalue = eigenvalues[i]
    eigenvector = eigenvectors[:, i]
    eigenvector_dict[eigenvalue] = eigenvector

# Print eigenvectors
print("Eigenvectors of Matrix M:")
for eigenvalue, eigenvector in eigenvector_dict.items():
    print(f"Eigenvalue: {eigenvalue}")
    print(f"Eigenvector:\n{eigenvector}\n")
