import itertools

# (a)
URN = ['W1', 'W2', 'B1', 'B2', 'B3', 'R1', 'R2', 'R3', 'R4']

# (b)
U3 = list(itertools.combinations(URN, 3))
print("b) Tap con gom 3 qua banh tu tap hop URN (khong phan biet thu tu):", U3)

# (c)
white1blue1red1 = []
for comb in U3:
    if 'W' in comb and 'B' in comb and 'R' in comb:
        white1blue1red1.append(comb)
    print("c) Truong hop 3 qua banh duoc chon tu tap U3 co mot qua banh mau trang, mot qua banh mau xanh duong va mot qua banh mau do:", comb)

# (d)
P = len(white1blue1red1) / len(U3)
print("d) Xac suat chon ngau nhien 3 qua banh trong do co mot qua banh mau trang, mot qua banh mau xanh duong va mot qua banh mau do:", P)
