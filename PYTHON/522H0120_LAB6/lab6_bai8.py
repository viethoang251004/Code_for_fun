import numpy as np


def encode_message(message, matrix):
    # Xac dinh bang tra cuu
    lookup_table = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
        'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
        'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
    }
    # Chuyen doi thong diep thanh chu hoa va xoa moi ky tu khong phai chu cai
    message = ''.join(c for c in message if c.isalpha()).upper()
    # Dem thong diep bang X neu do dai cua no khong chia het cho 3
    padding_length = 3 - (len(message) % 3)
    message += 'X' * padding_length
    # Tao ma tran E tu thong diep duoc ma hoa
    E = np.zeros((3, len(message) // 3), dtype=int)
    for i in range(len(message) // 3):
        for j in range(3):
            E[j][i] = lookup_table[message[3*i+j]]
    # Tinh toan thong diep duoc ma hoa bang AE
    encoded_message = np.dot(matrix, E)
    return encoded_message


# Xac dinh thong diep va ma tran A
message1 = 'ATTACK'
message2 = 'LINEAR ALGEBRA LABORATORY'
A = np.array([
    [3, 4, 5],
    [1, 3, 1],
    [1, 1, 2]
])

# Ma hoa thong diep
encoded_message1 = encode_message(message1, A)
encoded_message2 = encode_message(message2, A)
print(encoded_message1)
print(encoded_message2)