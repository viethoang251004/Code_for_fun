import numpy as np

#(a)
# Xac dinh cac vecto u va v
u = np.array([1, 1])
v = np.array([0, 1])

# Tinh tich vo huong giua cac vecto va do dai cua tung vecto
dot_product = np.dot(u, v)
norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)

# Tinh cosin cua goc giua cac vecto
cos_theta = dot_product / (norm_u * norm_v)

# Tinh goc theo radian va chuyen doi sang do
theta = np.arccos(cos_theta)
theta_degrees = np.degrees(theta)

# In ra man hinh
print("(a) The angle between u and v is", theta_degrees, "degrees.")

#(b)
# Xac dinh cac vecto u1 va v1
u1 = np.array([1, 0])
v1 = np.array([0, 1])

# Tinh tich vo huong giua cac vecto va do dai cua tung vecto
dot_product1 = np.dot(u1, v1)
norm_u1 = np.linalg.norm(u1)
norm_v1 = np.linalg.norm(v1)

# Tinh cosin cua goc giua cac vecto
cos_theta1 = dot_product1 / (norm_u1 * norm_v1)

# Tinh goc theo radian va chuyen doi sang do
theta1 = np.arccos(cos_theta1)
theta_degrees1 = np.degrees(theta1)

# In ra man hinh
print("(b) The angle between u and v is", theta_degrees1, "degrees.")

#(c)
# Xac dinh cac vecto u2 va v2
u2 = np.array([-2, 3])
v2 = np.array([1/2, -1/2])

# Tinh tich vo huong giua cac vecto va do dai cua tung vecto
dot_product2 = np.dot(u2, v2)
norm_u2 = np.linalg.norm(u2)
norm_v2 = np.linalg.norm(v2)

# Tinh cosin cua goc giua cac vecto
cos_theta2 = dot_product2 / (norm_u2 * norm_v2)

# Tinh goc theo radian va chuyen doi sang do
theta2 = np.arccos(cos_theta2)
theta_degrees2 = np.degrees(theta2)

# In ra man hinh
print("(c) The angle between u and v is", theta_degrees2, "degrees.")