import numpy as np

# Xac dinh vi tri cua cac ve tinh
v1 = np.array([1, 2, 3])
s2 = np.array([7, 4, 3])
s3 = np.array([2, 1, 9])

# Tinh toan khoang cach theo cap giua cac vecto
dist_v1_s2 = np.linalg.norm(v1 - s2)
dist_v1_s3 = np.linalg.norm(v1 - s3)
dist_s2_s3 = np.linalg.norm(s2 - s3)

# In khoang cach
print("The Euclidean distance between v1 and s2 is", dist_v1_s2)
print("The Euclidean distance between v1 and s3 is", dist_v1_s3)
print("The Euclidean distance between s2 and s3 is", dist_s2_s3)