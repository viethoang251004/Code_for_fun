import numpy as np

# Khai báo và khởi tạo biến ngẫu nhiên X
x = np.random.choice([0, 1, 2, 3, 4, 5], 3650, p=[0.1, 0.2, 0.3, 0.2, 0.15, 0.05])

# (a)
X = np.unique(x)
print("Các giá trị của biến ngẫu nhiên X:", X)

# (b)
P = []
for value in X:
    probability = np.count_nonzero(x == value) / len(x)
    P.append(probability)
print("Hàm phân phối xác suất của biến ngẫu nhiên X:", P)

# (c)
expectation = np.mean(x)
variance = np.var(x)
standard_deviation = np.std(x)
print("Kỳ vọng của biến ngẫu nhiên X:", expectation)
print("Phương sai của biến ngẫu nhiên X:", variance)
print("Độ lệch chuẩn của biến ngẫu nhiên X:", standard_deviation)

# (d)
prob_3_or_more = np.count_nonzero(x >= 3) / len(x)
print("Xác suất để có 3 ca cấp cứu trở lên:", prob_3_or_more)
