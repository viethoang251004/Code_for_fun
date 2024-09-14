import itertools

A = [1, 2, 3, 4, 5]
num_3_digit = list(itertools.permutations(A, 3))

num_3_digit = [int(''.join(map(str, num))) for num in num_3_digit]

num_length = len(num_3_digit)

print("Danh sách các số có 3 chữ số được lập từ tập hợp A mà không lặp lại:")
for num in num_3_digit:
    print(num)

print("Số lượng các số có 3 chữ số:", num_length)
