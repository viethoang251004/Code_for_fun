import pandas as pd
import matplotlib.pyplot as plt

# Doc file iris.csv
df = pd.read_csv('iris.csv')

# Bai 1
# Trích xuất dữ liệu cho sepal_length và sepal_width
sepal_length = df['sepal_length']
sepal_width = df['sepal_width']

# Tao bieu do phan tan
plt.scatter(sepal_length, sepal_width)

# Dat nhan cho truc X va Y
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')

# Hien thi bieu do
plt.show()

#Bai 2
# Tao bieu do tan suat cho sepal_length voi bin = 20
plt.hist(sepal_length, bins=20)

# Dat nhan cho truc X va Y
plt.xlabel('sepal_length')
plt.ylabel('Frequency')

# Hien thi bieu do
plt.show()
