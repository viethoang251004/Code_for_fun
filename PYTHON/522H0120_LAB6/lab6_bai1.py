import numpy as np

#(a)
A1 = [[1, -7], [-2, -3]]
max_col_sum = max(sum(map(abs, col)) for col in zip(*A1))
print("1-norm of A1 is: ", max_col_sum)

#(b)
A2 = [[-2, 8], [3, 1]]
max_col_sum1 = max(sum(map(abs, col)) for col in zip(*A2))
print("1-norm of A2 is: ", max_col_sum1)

#(c)
A3 = [[2, -8], [3, 1]]
max_col_sum2 = max(sum(map(abs, col)) for col in zip(*A3))
print("1-norm of A3 is: ", max_col_sum2)

#(d)
A4 = [[2, 3], [1, -1]]
max_col_sum3 = max(sum(map(abs, col)) for col in zip(*A4))
print("1-norm of A4 is: ", max_col_sum3)

#(e)
A5 = [[5, -4, 2], [-1, 2, 3], [-2, 1, 0]]
max_col_sum4 = max(sum(map(abs, col)) for col in zip(*A5))
print("1-norm of A5 is: ", max_col_sum4)