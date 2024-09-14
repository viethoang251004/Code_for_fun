import numpy as np

# (a)
x = np.random.choice([0, 1, 2], 10000)

# (b)
X = np.unique(x)
print("Các giá trị của biến ngẫu nhiên X:", X)

# (c)
P = []
for value in X:
    probability = np.count_nonzero(x == value) / len(x)
    P.append(probability)
print("Hàm phân phối xác suất của biến ngẫu nhiên X:", P)

# (d)
expectation = np.mean(x)
variance = np.var(x)
standard_deviation = np.std(x)
print("Kỳ vọng của biến ngẫu nhiên X:", expectation)
print("Phương sai của biến ngẫu nhiên X:", variance)
print("Độ lệch chuẩn của biến ngẫu nhiên X:", standard_deviation)

# (e)
prob_at_least_one_head = np.count_nonzero(x >= 1) / len(x)
print("Xác suất để có ít nhất một mặt ngửa:", prob_at_least_one_head)
