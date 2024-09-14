from sympy import Matrix

C = Matrix([[1, 0, 2, 3], [4, -1, 0, 2], [0, -1, -8, -10]])

# Cau a
# Compute the reduced row echelon form of C
rref_C = C.rref()[0]

# Identify the pivot columns of the rref of C
pivot_cols = rref_C.rref()[1]

# Extract the columns of C corresponding to the pivot columns
col_space_basis = C[:, pivot_cols]

print("(a) A basis for the column space of C is:")
print(col_space_basis)

# Cau b
# Transpose C to get the column echelon form of C
C_T = C.T

# Compute the row echelon form of the transpose of C
rref_C_T = C_T.rref()[0]

# Identify the pivot rows of the rref of the transpose of C
pivot_rows = rref_C_T.rref()[1]

# Extract the rows of the transpose of C corresponding to the pivot rows
row_space_basis_T = C_T[:, pivot_rows]

# Transpose the basis for the row space to get the basis for the row space of C
row_space_basis = row_space_basis_T.T

print("(b) A basis for the row space of C is:")
print(row_space_basis)