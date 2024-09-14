import itertools

men = ['M1', 'M2', 'M3', 'M4', 'M5', 'M6']
women = ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9']

num_selections = len(list(itertools.combinations(men, 3))) * len(list(itertools.combinations(women, 2)))
print("Số cách khác nhau:", num_selections)

selections = list(itertools.combinations(men, 3)) + list(itertools.combinations(women, 2))
print("Danh sách các lựa chọn khác nhau:")
for selection in selections:
    print(selection)
