import pandas as pd
import matplotlib.pyplot as plt

# Doc file company_sales_data.csv file
df = pd.read_csv('company_sales_data.csv')

# Bai 1
# Trích xuất dữ liệu cho months va total profit
months = df['month_number']
total_profit = df['total_profit']

# Tạo biểu đồ đường thẳng
plt.plot(months, total_profit)

# Đặt nhãn cho trục X và Y
plt.xlabel('Month')
plt.ylabel('Total Profit')

# Đặt tiêu đề cho biểu đồ
plt.title('Total Profit of All Months')

# Hiển thị biểu đồ
plt.show()

# Bai 2
# Trích xuất dữ liệu cho months và toothpaste sales
toothpaste_sales = df['toothpaste']

# Tạo biểu đồ phân tán
plt.scatter(months, toothpaste_sales)

# Đặt nhãn cho trục X và Y
plt.xlabel('Month')
plt.ylabel('Toothpaste Sales')

# Đặt tiêu đề cho biểu đồ
plt.title('Toothpaste Sales of All Months')

# Hiển thị biểu đồ
plt.show()

# Bai 3
# Trích xuất dữ liệu cho months, facecream sales, và facewash sales
facecream_sales = df['facecream']
facewash_sales = df['facewash']

# Tạo biểu đồ cột
plt.bar(months, facecream_sales, label='Facecream', width=0.4)
plt.bar(months, facewash_sales, label='Facewash', width=0.4, align='edge')

# Đặt nhãn cho trục X và Y
plt.xlabel('Month')
plt.ylabel('Sales')

# Đặt tiêu đề cho biểu đồ
plt.title('Facecream and Facewash Sales of All Months')

# Thêm chú thích
plt.legend()

# Hiển thị biểu đồ
plt.show()
