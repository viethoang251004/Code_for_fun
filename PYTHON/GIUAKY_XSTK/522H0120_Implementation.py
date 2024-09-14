# Cách 1:
# Import thư viện và modules
# Đây là việc import thư viện numpy để làm việc với mảng và tính toán số học, và pyplot từ thư viện matplotlib để hiển thị ảnh và biểu đồ.
import numpy as np
from matplotlib import pyplot as plt
# Hàm thuattoancanbangluocdo(image): Đây là hàm thực hiện thuật toán cân bằng lược đồ cho ảnh đầu vào.
def thuattoancanbangluocdo(image):
    # Tính toán lược đồ của ảnh gốc
    # Dùng mảng luocdo để tính số lần xuất hiện của mỗi mức xám trong ảnh. Hàm ravel() được sử dụng để duỗi mảng ảnh thành mảng 1D, từ đó dễ dàng duyệt qua từng pixel.
    luocdo = np.zeros(256)
    for pixel in image.ravel():
        luocdo[pixel] += 1
    # Tính toán cdf (cumulative distribution function) của lược đồ
    # Tính toán hàm phân phối tích lũy (CDF) từ lược đồ. CDF là tổng lũy thừa của lược đồ và đại diện cho phân phối tổng lũy thừa của mức xám trong ảnh.
    cdf = np.zeros_like(luocdo)
    cdf[0] = luocdo[0]
    for x in range(1, len(luocdo)):
        cdf[x] = cdf[x-1] + luocdo[x]
    # Chuẩn hóa cdf để có giá trị trong khoảng [0, 255]
    # Chuẩn hóa CDF sao cho giá trị của CDF nằm trong khoảng [0, 255], để đảm bảo rằng giá trị của ảnh sau khi cân bằng sẽ nằm trong khoảng này.
    cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
    # Áp dụng thuật toán cân bằng lược đồ cho từng pixel của ảnh
    # Sử dụng hàm np.interp() để ánh xạ giá trị mức xám của ảnh gốc sang giá trị mới theo CDF đã chuẩn hóa. Điều này giúp cân bằng lược đồ cho ảnh.
    image_equalized = np.interp(image, np.arange(256), cdf_normalized)
    # Trả về ảnh kết quả
    return image_equalized
# Đọc ảnh gốc và chuyển đổi sang ảnh xám
# Sử dụng plt.imread() để đọc ảnh gốc, sau đó tính trung bình của các kênh màu (RGB) để chuyển đổi ảnh màu sang ảnh xám.
image = plt.imread('input.jpg')
gray = np.mean(image, axis=2).astype(np.uint8)
# Áp dụng thuật toán cân bằng lược đồ cho ảnh xám
gray_equalized = thuattoancanbangluocdo(gray)
# Hiển thị kết quả
# Dùng plt.subplot() để tạo cửa sổ hiển thị gồm hai phần: ảnh gốc và ảnh sau khi cân bằng lược đồ.
# plt.imshow() dùng để hiển thị ảnh và plt.title() để đặt tiêu đề.
# Cuối cùng, plt.show() để hiển thị cửa sổ đồ họa.
plt.subplot(121), plt.imshow(gray, cmap='gray')
plt.title('Original Image')
plt.subplot(122), plt.imshow(gray_equalized, cmap='gray')
plt.title('Histogram Equalized Image')
plt.show()
