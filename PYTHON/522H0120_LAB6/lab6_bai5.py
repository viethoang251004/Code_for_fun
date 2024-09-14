import numpy as np

#(a)
# Xac dinh vecto u
u = np.array([2, 3])

# Tinh do dai cua u
norm_u = np.linalg.norm(u)

# Tinh vecto don vi u_hat
u_hat = u / norm_u

# In ket qua
print("(a) The unit vector for u is", u_hat)

#(b)
# Xac dinh vecto u1
u1 = np.array([1, 2, 3])

# Tinh do dai cua u1
norm_u1 = np.linalg.norm(u1)

# Tinh vecto don vi u_hat1
u_hat1 = u1 / norm_u1

# In ket qua
print("(b) The unit vector for u is", u_hat1)

#(c)
# Xac dinh vecto u2
u2 = np.array([1/2, -1/2, 1/4])

# Tinh do dai cua u2
norm_u2 = np.linalg.norm(u2)

# Tinh vecto don vi u_hat2
u_hat2 = u2 / norm_u2

# In ket qua
print("(c) The unit vector for u is", u_hat2)

#(d)
# Xac dinh vecto u3
u3 = np.array([2 ** 1/2, 2, -(2 ** 1/2), 2 ** 1/2])

# Tinh do dai cua u3
norm_u3 = np.linalg.norm(u3)

# Tinh vecto don vi u_hat3
u_hat3 = u3 / norm_u3

# In ket qua
print("(d) The unit vector for u is", u_hat3)