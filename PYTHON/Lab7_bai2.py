import sympy as sp

# Cau a
# Define the given vectors
v1 = sp.Matrix([1, -2, 0])
v2 = sp.Matrix([0, -4, 1])
v3 = sp.Matrix([1, -1, 1])

# Create a matrix using the given vectors
A = sp.Matrix.hstack(v1, v2, v3)

# Find the reduced row echelon form of the matrix A
rref_A = A.rref()

# Get the second element of rref_A, which is a list of indices of the linearly independent columns
lin_ind_cols = rref_A[1]

# Check whether the number of linearly independent columns is equal to the number of given vectors
if len(lin_ind_cols) == len([v1, v2, v3]):
    print("(a) The vectors are linearly independent")
else:
    print("(a) The vectors are linearly dependent")

# Cau d
# Create a matrix from the given vectors
A = sp.Matrix([[0, 0, 1, 2, 3],
               [0, 0, 2, 3, 1],
               [1, 2, 3, 4, 5],
               [2, 1, 0, 0, 0],
               [-1, -3, -5, 0, 0]])

# Find the reduced row echelon form of the matrix and the indices of the pivot columns
rref_A, pivot_cols = A.rref()

# If the number of pivot columns is equal to the number of vectors, the vectors are linearly independent
if len(pivot_cols) == A.shape[1]:
    print("(d) The vectors are linearly independent.")
else:
    print("(d) The vectors are linearly dependent.")