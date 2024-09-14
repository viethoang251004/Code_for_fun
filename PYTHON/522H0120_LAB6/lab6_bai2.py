import numpy as np

#(a)
B1 = [[1, -7], [-2, -3]]
max_row_sum = max(sum(map(abs, row)) for row in B1)
print("Infinity norm of B1 is: ", max_row_sum)

#(b)
B2 = [[3, 6], [1, 0]]
max_row_sum1 = max(sum(map(abs, row)) for row in B2)
print("Infinity norm of B2 is: ", max_row_sum1)

#(c)
B3 = [[5, -4, 2], [-1, 2, 3], [-2, 1, 0]]
max_row_sum2 = max(sum(map(abs, row)) for row in B3)
print("Infinity norm of B3 is: ", max_row_sum2)

#(d)
B4 = [[3, 6 , -1], [3, 1, 0], [2, 4, -7]]
max_row_sum3 = max(sum(map(abs, row)) for row in B4)
print("Infinity norm of B4 is: ", max_row_sum3)

#(e)
B5 = [[-3, 0, 0], [0, 4, 0], [0, 0, 2]]
max_row_sum4 = max(sum(map(abs, row)) for row in B5)
print("Infinity norm of B5 is: ", max_row_sum4)