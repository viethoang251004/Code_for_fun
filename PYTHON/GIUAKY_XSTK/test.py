from PIL import Image # Import thư viện

def histogram_equalization(image):
    # Lấy kích thước ảnh (width, height)
    width, height = image.size # Lấy kích thước của ảnh bằng cách gọi phương thức size
    
    # Tạo histogram cho ảnh gốc
    histogram = [0] * 256 # Tạo một danh sách gồm 256 phần tử, tương ứng vs histogram của ảnh và đều đặt giá trị của histogram = 0
    for y in range(height): # Vòng lặp đầu tiên duyệt qua từng hàng (chiều cao) của ảnh
        for x in range(width): # Vòng lặp đầu tiên duyệt qua từng cột (chiều rộng) của ảnh
            pixel = image.getpixel((x, y)) # Lấy giá trị pixel tại tọa độ (x, y) trên ảnh bằng cách sử dụng bằng cách sử dụng phương thức getpixel((x, y)) của lớp image
            grayscale_value = pixel[0]  # Lấy giá trị mức xám từ tuple "pixel", với giả định rằng ảnh đang xử lý là ảnh xám, do đó chỉ có giá trị đầu tiên trong tuple là giá trị mức xám.
            histogram[grayscale_value] += 1 # Tăng giá trị tương ứng trong histogram cho mức xám lên 1
    
    # Tính tổng tích luỹ của histogram
    cumulative_histogram = [0] * 256 # Tạo danh sách cumulative_histogram có 256 phần tử, khởi tạo tất cả giá trị là 0.
    cumulative_histogram[0] = histogram[0] # Thiết lập giá trị đầu tiên trong cumulative_histogram bằng giá trị histogram của mức xám đầu tiên.
    for i in range(1, 256): # Vòng lặp duyệt qua từng giá trị từ 1 đến 255 (mức xám từ 1 đến 255).
        cumulative_histogram[i] = cumulative_histogram[i - 1] + histogram[i] # Tính giá trị tích luỹ của histogram
    
    # Tính giá trị mới cho từng mức xám
    equalized_values = [0] * 256 # Tạo danh sách equalized_values với 256 phần tử, tương ứng với giá trị mới sau khi cân bằng cho từng mức xám.
    total_pixels = width * height # Tính tổng số pixel trong ảnh.
    for i in range(256): # Vòng lặp duyệt qua từng giá trị mức xám từ 0 đến 255.
        equalized_values[i] = int(255 * cumulative_histogram[i] / total_pixels) # Tính giá trị mới sau khi cân bằng cho mức xám i bằng cách lấy tổng tích luỹ của histogram tại mức xám i, nhân với 255 và chia cho tổng số pixel.
    
    # Tạo ảnh mới với giá trị đã cân bằng
    equalized_image = Image.new("L", (width, height))  # Tạo một ảnh mới với định dạng xám ("L") có kích thước tương tự ảnh gốc.

    # Sử dụng vòng lặp lồng nhau để duyệt qua từng pixel trong ảnh gốc và thực hiện quá trình cân bằng lược đồ.
    # Lấy giá trị mức xám của pixel, ánh xạ sang giá trị mới sau khi cân bằng bằng cách sử dụng equalized_values, và đặt giá trị mới vào pixel tại tọa độ tương ứng trên ảnh đã cân bằng.
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            grayscale_value = pixel[0]
            new_value = equalized_values[grayscale_value]
            equalized_image.putpixel((x, y), new_value)
    
    return equalized_image

# Đọc ảnh đầu vào
input_image = Image.open("input.jpg") # Image.open("input.jpg"): được sử dụng để mở một tệp ảnh từ đường dẫn cung cấp
# Áp dụng thuật toán cân bằng lược đồ bằng cách gọi hàm 'histogram_equalization' với ảnh đầu vào.
output_image = histogram_equalization(input_image)
# Lưu ảnh sau khi cân bằng vào tệp "output.jpg" sử dụng phương thức .save().
output_image.save("output.jpg")
