import itertools

urn = ['W'] * 8 + ['B'] * 6 + ['R'] * 9

# (a)
U3 = list(itertools.combinations(urn, 3))
len_U3 = len(U3)

print("Danh sách tất cả các bộ 3 quả bóng có thể có:")
for combo in U3:
    print(combo)

print("Số lượng bộ 3 quả bóng có thể có:", len_U3)

# (b)
diff_colors = [combo for combo in U3 if len(set(combo)) == 3]

print("Các trường hợp có thể xảy ra của ba quả bóng khác màu:")
for combo in diff_colors:
    print(combo)

# (c)
first_white_second_red = [combo for combo in U3 if combo[0] == 'W' and combo[1] == 'R']

print("Các trường hợp có thể xảy ra của quả bóng thứ nhất màu trắng và quả bóng thứ hai màu đỏ:")
for combo in first_white_second_red:
    print(combo)
