import numpy as np

# (a)
C1 = [[5, -4, 2], [-1, 2, 3], [-2, 1, 0]]
frobenius_norm = (sum(sum(pow(x, 2) for x in row) for row in C1)) ** 0.5
print("Frobenius norm of C1 is: ", frobenius_norm)

# (b)
C2 = [[1, 7, 3], [4, -2, -2], [-2, -1, 1]]
frobenius_norm1 = (sum(sum(pow(x, 2) for x in row) for row in C2)) ** 0.5
print("Frobenius norm of C2 is: ", frobenius_norm1)

# (c)
C3 = [[2, 3], [1, -1]]
frobenius_norm2 = (sum(sum(pow(x, 2) for x in row) for row in C3)) ** 0.5
print("Frobenius norm of C3 is: ", frobenius_norm2)