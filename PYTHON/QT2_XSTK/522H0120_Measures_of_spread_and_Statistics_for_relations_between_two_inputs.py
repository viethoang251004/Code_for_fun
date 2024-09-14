# CHƯƠNG 2 - ĐO LƯỜNG SỰ LAN TRUYỀN (SỰ PHÂN TÁN)

# 1. Ví dụ về hàm statistics.pstdev(data, mu)
import statistics
# Dữ liệu của quần thể (population data)
population_data = [10, 12, 14, 16, 18, 20]
# Tính giá trị trung bình của quần thể (population mean)
population_mean = statistics.mean(population_data)
# Tính độ lệch chuẩn của quần thể (population standard deviation)
population_stdev = statistics.pstdev(population_data, mu=population_mean)
# In kết quả
print("Dữ liệu của quần thể:", population_data)
print("Giá trị trung bình của quần thể:", population_mean)
print("Độ lệch chuẩn của quần thể:", population_stdev)

# 2. Ví dụ về hàm statistics.pvariance(data, mu=None)
import statistics
# Dữ liệu của quần thể (population data)
population_data = [10, 12, 14, 16, 18, 20]
# Tính phương sai của quần thể
population_variance = statistics.pvariance(population_data)
# In kết quả
print("Dữ liệu của quần thể:", population_data)
print("Phương sai của quần thể:", population_variance)

# 3. Ví dụ về hàm statistics.stdev(data, xbar=None)
import statistics
# Dữ liệu mẫu (sample data)
sample_data = [10, 12, 14, 16, 18, 20]
# Tính độ lệch chuẩn của mẫu
sample_stdev = statistics.stdev(sample_data)
# In kết quả
print("Dữ liệu mẫu:", sample_data)
print("Độ lệch chuẩn của mẫu:", sample_stdev)

# 4. Ví dụ về hàm statistics.variance(data, xbar=None)
import statistics
# Dữ liệu mẫu (sample data)
sample_data = [10, 12, 14, 16, 18, 20]
# Tính phương sai mẫu
sample_variance = statistics.variance(sample_data)
# In kết quả
print("Dữ liệu mẫu:", sample_data)
print("Phương sai mẫu:", sample_variance)


# CHƯƠNG 3 - THỐNG KÊ VỀ MỐI QUAN HỆ GIỮA HAI ĐẦU VÀO
# 1. Ví dụ về hàm statistics.covariance(x, y, /)
import statistics
# Dữ liệu mẫu
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
# Tính hiệp phương sai mẫu
sample_covariance = statistics.covariance(x, y)
# In kết quả
print("Dữ liệu x:", x)
print("Dữ liệu y:", y)
print("Hiệp phương sai mẫu:", sample_covariance)

# 2. Ví dụ về hàm statistics.correlation(x, y, /)
import statistics
# Dữ liệu mẫu
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
# Tính hệ số tương quan Pearson
correlation_coefficient = statistics.correlation(x, y)
# In kết quả
print("Dữ liệu x:", x)
print("Dữ liệu y:", y)
print("Hệ số tương quan Pearson:", correlation_coefficient)

# 3. Ví dụ về hàm statistics.linear_regression(x, y, /, *, proportional=False)
import statistics
# Dữ liệu mẫu
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
# Tính toán hồi quy tuyến tính đơn giản
slope, intercept = statistics.linear_regression(x, y)
# In kết quả
print("Dữ liệu x:", x)
print("Dữ liệu y:", y)
print("Tham số slope (độ dốc):", slope)
print("Tham số intercept (điểm cắt trục y):", intercept)
