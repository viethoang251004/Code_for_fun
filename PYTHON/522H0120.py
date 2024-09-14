import numpy as np
# Task 1
# Tao ma tran A, B va C với cac so nguyen ngau nhien
A = np.random.randint(1, 101, size=(10, 10))
print("Matrix A:\n", A)

B = np.random.randint(1, 21, size=(2, 10))
print("Matrix B:\n", B)

C = np.random.randint(1, 21, size=(10, 2))
print("Matrix C:\n", C)


# Cau a
# Tinh toan theo yeu cau de bai
result1 = A + A.T + np.dot(C, B) + np.dot(B.T, C.T)
# In kết quả ra màn hình
print("Result of a:\n", result1)


# Cau b
# Tinh toan theo yeu cau de bai
result2 = 0
for i in range(11, 18):
    result2 += np.power(A/i, i-9)
result2 += np.power(A/18, 9)
result2 += np.power(A/19, 10)
result2 += np.power(A/10, 1)
# In ket qua ra man hinh
print("Result of b:\n", result2)


# Cau c
# Tao bien mat na de chon cac hang le cua A
mask = np.array([True, False] * 5)
# Chon cac hang le cua A de gan vao bien A_odd
A_odd = A[mask]
# In ket qua ra man hinh
print("The resultant matrix of c:\n", A_odd)


# Cau d
# Khoi tao danh sach trong de luu cac so nguyen le trong A
odd_numbers = []
# Lap qua tung phan tu trong A
for q in range(10):
    for j in range(10):
        if A[q, j] % 2 == 1:
            odd_numbers.append(A[q, j])
# Chuyen doi danh sach thanh mang numpy
odd_numbers = np.array(odd_numbers)
# In ket qua ra man hinh
print("The resultant vector of d:\n", odd_numbers)


# Cau e
# Xac dinh mot ham de kiem tra xem mot so co phai la so nguyen to hay khong
def is_prime(num):
    if num <= 1:
        return False
    for h in range(2, int(np.sqrt(num))+1):
        if num % h == 0:
            return False
    return True


# Tao mot vecto rong de luu tru cac so nguyen to trong ma tran A
prime_vector = []
# Lap qua tung phan tu trong ma tran A va kiem tra xem no co phai la so nguyen to hay khong
for k in range(10):
    for l in range(10):
        if is_prime(A[k, l]):
            prime_vector.append(A[k, l])
# In ket qua ra man hinh
print("The resultant vector of e:\n", prime_vector)


# Cau f
# Tao ma tran F bang cach nhan B voi C su dung phuong thuc dot trong thu vien numpy
F = np.dot(C, B)
# Dao nguoc cac phan tu trong cac hang le cua F bang cach su dung phep cat [::-1]
for y in range(1, F.shape[0], 2):
    F[y, :] = F[y, ::-1]
# In ket qua ra man hinh
print("The resultant matrix of f:\n", F)


# Cau g
# Xac dinh mot ham de kiem tra xem so do co phai la so nguyen to hay khong
def is_prime(number):
    if number < 2:
        return False
    for e in range(2, int(number ** 0.5) + 1):
        if number % e == 0:
            return False
    return True


# Dem so nguyen to trong moi hang cua A
prime_counts = [sum(is_prime(number) for number in row) for row in A]
# Tim cac hang co so luong so nguyen to toi da
max_count = max(prime_counts)
max_rows = [e for e, count in enumerate(prime_counts) if count == max_count]
# In ket qua ra man hinh
print("Rows with maximum count of prime numbers:")
for t in max_rows:
    print(A[t])


# Cau h
# Tim cac hang co day so le lien ke dai nhat
max_len = 0
max_rows = []

for z in range(A.shape[0]):
    row = A[z]
    curr_len = 0
    max_curr_len = 0
    for v in range(A.shape[1]):
        if row[v] % 2 == 1:
            curr_len += 1
            if curr_len > max_curr_len:
                max_curr_len = curr_len
        else:
            curr_len = 0
    if max_curr_len > max_len:
        max_len = max_curr_len
        max_rows = [z]
    elif max_curr_len == max_len:
        max_rows.append(z)

# In ket qua ra man hinh
print("Rows with longest contiguous odd numbers sequence:")
for row in max_rows:
    print(A[row])
