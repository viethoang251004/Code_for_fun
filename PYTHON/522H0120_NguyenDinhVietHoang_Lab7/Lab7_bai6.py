import numpy as np

# Define the matrix A and extract columns a1, a2, a3, a4, and a5
A = np.array([[5, 1, 2, 2, 0], [3, 3, 2, -1, -12], [8, 4, 4, -5, 12], [2, 1, 1, 0, -2]])
a1 = A[:, 0]
a2 = A[:, 1]
a3 = A[:, 2]
a4 = A[:, 3]
a5 = A[:, 4]

# Define the matrix B as [a1 a2 a4]
B = np.array([a1, a2, a4]).T

# Augment B with a3 and compute the ranks
B_a3 = np.hstack((B, a3.reshape(-1, 1)))
rank_B = np.linalg.matrix_rank(B)
rank_B_a3 = np.linalg.matrix_rank(B_a3)

# Print the results for a3
if rank_B == rank_B_a3:
    print("a3 is in the column space of B")
else:
    print("a3 is not in the column space of B")

# Augment B with a5 and compute the ranks
B_a5 = np.hstack((B, a5.reshape(-1, 1)))
rank_B_a5 = np.linalg.matrix_rank(B_a5)

# Print the results for a5
if rank_B == rank_B_a5:
    print("a5 is in the column space of B")
else:
    print("a5 is not in the column space of B")
