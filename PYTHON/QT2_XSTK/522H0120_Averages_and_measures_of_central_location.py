# CHƯƠNG 1 - CÁC GIÁ TRỊ TRUNG BÌNH VÀ ĐO LƯỜNG VỊ TRÍ TRUNG TÂM

# 1. Ví dụ về hàm statistics.mean(data)
import statistics
# Danh sách các điểm số của các học sinh
diem_so = [85, 90, 78, 92, 88, 95, 83]
# Tính điểm trung bình của các học sinh
diem_trung_binh = statistics.mean(diem_so)
# In kết quả
print("Danh sách điểm số:", diem_so)
print("Điểm trung bình:", diem_trung_binh)

# 2. Ví dụ về hàm statistics.fmean(data, weights=weights_list)
import statistics
# Danh sách các số cần tính giá trị trung bình có trọng số
data_list = [10, 20, 30, 40, 50]
# Trọng số tương ứng với các giá trị trong data_list
weights_list = [2, 3, 1, 4, 2]
# Tính giá trị trung bình có trọng số của tập dữ liệu
weighted_mean = statistics.fmean(data_list, weights=weights_list)
# In kết quả
print("Dữ liệu:", data_list)
print("Trọng số:", weights_list)
print("Giá trị trung bình có trọng số:", weighted_mean)

# 3. Ví dụ về hàm statistics.geometric_mean(data)
import statistics
# Danh sách các số cần tính trung bình hình học
data_list = [2, 4, 8, 16, 32]
# Tính trung bình hình học của tập dữ liệu
geometric_mean_value = statistics.geometric_mean(data_list)
# In kết quả
print("Dữ liệu:", data_list)
print("Trung bình hình học:", geometric_mean_value)

# 4. Ví dụ về hàm statistics.harmonic_mean(data)
import statistics
data_list = [10, 15, 20, 25]
# Tính giá trị trung bình nghịch đảo
harmonic_mean_value = statistics.harmonic_mean(data_list)
# In kết quả
print("Dữ liệu:", data_list)
print("Giá trị trung bình nghịch đảo:", harmonic_mean_value)

# 5. Ví dụ về hàm statistics.median(data)
import statistics
data_list = [15, 23, 12, 45, 10, 32]
# Tính giá trị trung vị
median_value = statistics.median(data_list)
# In kết quả
print("Dữ liệu:", data_list)
print("Giá trị trung vị:", median_value)

# 6. Ví dụ về hàm statistics.median_low(data)
import statistics
data_list = [5, 8, 12, 15, 20, 25]
# Tính giá trị trung vị (lấy giá trị thấp hơn nếu số lượng phần tử là lẻ)
median_low_value = statistics.median_low(data_list)
# In kết quả
print("Dữ liệu:", data_list)
print("Giá trị trung vị (lấy giá trị thấp hơn):", median_low_value)

# 7. Ví dụ về hàm statistics.median_high(data)
import statistics
data_list = [5, 8, 12, 15, 20, 25]
# Tính giá trị trung vị (lấy giá trị cao hơn nếu số lượng phần tử là lẻ)
median_high_value = statistics.median_high(data_list)
# In kết quả
print("Dữ liệu:", data_list)
print("Giá trị trung vị (lấy giá trị cao hơn):", median_high_value)

# 8. Ví dụ về hàm statistics.median_grouped(data, interval=1)
import statistics
data_list = [15, 20, 25, 30, 35, 40]
interval_size = 5
# Tính giá trị trung vị của tập dữ liệu sau khi được nhóm lại vào các khoảng
median_grouped_value = statistics.median_grouped(data_list, interval=interval_size)
# In kết quả
print("Dữ liệu:", data_list)
print("Giá trị trung vị sau khi nhóm lại vào các khoảng:", median_grouped_value)

# 9. Ví dụ về hàm statistics.mode(data)
import statistics
data_list = [2, 4, 6, 4, 8, 10, 4]
# Tính giá trị mode của tập dữ liệu
mode_value = statistics.mode(data_list)
# In kết quả
print("Dữ liệu:", data_list)
print("Giá trị mode:", mode_value)

# 10. Ví dụ về hàm statistics.multimode(data)
import statistics
data_list = [2, 4, 6, 4, 8, 10, 4]
# Tìm các giá trị mode của tập dữ liệu
mode_values = statistics.multimode(data_list)
# In kết quả
print("Dữ liệu:", data_list)
print("Các giá trị mode:", mode_values)

# 11. Ví dụ về hàm statistics.multimode(data, n = 4) và method không để gì thì mặc định là exclusive
import statistics
data_list = [10, 15, 20, 25, 30, 35, 40, 45]
# Tính các phân vị (25%, 50% và 75%)
quantiles_values = statistics.quantiles(data_list, n=4)
# In kết quả
print("Dữ liệu:", data_list)
print("Các phân vị (25%, 50%, 75%):", quantiles_values)
