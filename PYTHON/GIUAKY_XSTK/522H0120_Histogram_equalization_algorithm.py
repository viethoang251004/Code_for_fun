# Cách 2:
# Import thư viện cv2 (OpenCV) và numpy để làm việc với mảng và tính toán số học.
import cv2
import numpy as np
# Hàm histogram_equalization(image): Đây là hàm thực hiện thuật toán cân bằng lược đồ cho ảnh đầu vào.
def histogram_equalization(image):
    # Dùng mảng histogram để tính số lần xuất hiện của mỗi mức xám trong ảnh.
    histogram = np.zeros(256, dtype=int)
    # Hàm image.shape trả về kích thước ảnh (chiều cao và chiều rộng).
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            histogram[image[i, j]] += 1
    # Tính toán hàm phân phối tích lũy (CDF) từ lược đồ. CDF là tổng lũy thừa của lược đồ và đại diện cho phân phối tổng lũy thừa của mức xám trong ảnh.
    cdf = np.zeros(256, dtype=int)
    cdf[0] = histogram[0]
    for i in range(1, 256):
        cdf[i] = cdf[i-1] + histogram[i]
    # Chuẩn hóa CDF sao cho giá trị của CDF nằm trong khoảng [0, 255], để đảm bảo rằng giá trị của ảnh sau khi cân bằng sẽ nằm trong khoảng này.
    cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
    # Tạo một mảng trống có cùng kích thước với ảnh đầu vào để chứa ảnh sau khi cân bằng lược đồ.
    equalized_image = np.zeros_like(image)
    # Sử dụng mảng cdf_normalized để ánh xạ giá trị mức xám của ảnh gốc sang giá trị mới dựa trên CDF đã chuẩn hóa.
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            equalized_image[i, j] = cdf_normalized[image[i, j]]

    return equalized_image
# Đọc ảnh đầu vào và chuyển đổi sang ảnh xám bằng cách sử dụng cv2.imread với cờ cv2.IMREAD_GRAYSCALE.
image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)
# Thực hiện cân bằng lược đồ bằng cách áp dụng hàm cân bằng lược đồ lên ảnh xám.
equalized_image = histogram_equalization(image)
# Hiển thị hai cửa sổ hiển thị gồm ảnh gốc và ảnh sau khi cân bằng lược đồ sử dụng cv2.imshow().
# Hàm cv2.waitKey() dùng để chờ một sự kiện từ bàn phím trước khi đóng cửa sổ.
cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
