import skimage.io as skio
from skimage.transform import resize
import matplotlib.pyplot as plt

# Nhập tên file hình ảnh từ người dùng
image_path = input("Nhập đường dẫn đến hình ảnh: ")

# Đọc hình ảnh
image = skio.imread(image_path)

# Hiển thị hình ảnh gốc
plt.subplot(1, 2, 1)
plt.title("Hình ảnh gốc")
plt.imshow(image)
plt.axis('off')

# Nén hình ảnh
compressed_image = resize(image, (image.shape[0] // 2, image.shape[1] // 2))

# Hiển thị hình ảnh đã nén
plt.subplot(1, 2, 2)
plt.title("Hình ảnh đã nén")
plt.imshow(compressed_image)
plt.axis('off')

# Lưu hình ảnh đã nén vào file
compressed_image_path = "compressed_image.jpg"
skio.imsave(compressed_image_path, compressed_image)

# Hiển thị cửa sổ đồ thị
plt.show()
