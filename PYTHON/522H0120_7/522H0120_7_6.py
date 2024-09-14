import itertools

E = {0, 1, 2, 3, 4, 5}

# (a)
three_digit_numbers = []
for digit1 in E:
    for digit2 in E:
        for digit3 in E:
            number = digit1 * 100 + digit2 * 10 + digit3
            three_digit_numbers.append(number)

print("a) Các số có 3 chữ số được tạo từ các phần tử trong tập hợp E:", three_digit_numbers)

# (b)
four_digit_numbers = []
permutations = itertools.permutations(E, 4)
for permutation in permutations:
    number = permutation[0] * 1000 + permutation[1] * 100 + permutation[2] * 10 + permutation[3]
    four_digit_numbers.append(number)

print("b) Các số có 4 chữ số (đôi một khác nhau) được tạo từ các phần tử trong tập hợp E:", four_digit_numbers)
