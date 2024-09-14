import numpy as np

# Cau a
# Define the vectors
v1 = np.array([1, 2, 3, 4])
v2 = np.array([-1, 0, 1, 3])
v3 = np.array([0, 5, -6, 8])
w = np.array([3, -6, 17, 11])

# Form the augmented matrix
A = np.column_stack((v1, v2, v3))
B = np.column_stack((A, w))

# Check the rank of the matrices
if np.linalg.matrix_rank(A) == np.linalg.matrix_rank(B):
    print("(a) w is a linear combination of v1, v2, v3")
else:
    print("(a) w is not a linear combination of v1, v2, v3")

# Cau b
# Define the vectors
v1 = np.array([1, 1, 2, 2])
v2 = np.array([2, 3, 5, 6])
v3 = np.array([2, -1, 3, 6])
w = np.array([0, 5, 3, 0])

# Form the augmented matrix
A = np.column_stack((v1, v2, v3))
B = np.column_stack((A, w))

# Check the rank of the matrices
if np.linalg.matrix_rank(A) == np.linalg.matrix_rank(B):
    print("(b) w is a linear combination of v1, v2, v3")
else:
    print("(b) w is not a linear combination of v1, v2, v3")

# Cau c
# Define the vectors
v1 = np.array([1, 1, 2, 2])
v2 = np.array([2, 3, 5, 6])
v3 = np.array([2, -1, 3, 6])
w = np.array([-1, 6, 1, -4])

# Form the augmented matrix
A = np.column_stack((v1, v2, v3))
B = np.column_stack((A, w))

# Check the rank of the matrices
if np.linalg.matrix_rank(A) == np.linalg.matrix_rank(B):
    print("(c) w is a linear combination of v1, v2, v3")
else:
    print("(c) w is not a linear combination of v1, v2, v3")

# Cau d
# Define the vectors
v1 = np.array([1, 2, 3, 4])
v2 = np.array([-1, 0, 1, 3])
v3 = np.array([0, 5, -6, 8])
v4 = np.array([1, 15, -12, 8])
w = np.array([0, -6, 17, 11])

# Form the augmented matrix
A = np.column_stack((v1, v2, v3, v4))
B = np.column_stack((A, w))

# Check the rank of the matrices
if np.linalg.matrix_rank(A) == np.linalg.matrix_rank(B):
    print("(d) w is a linear combination of v1, v2, v3, v4")
else:
    print("(d) w is not a linear combination of v1, v2, v3, v4")