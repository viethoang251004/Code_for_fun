import numpy as np


def decode_message(encoded_message, matrix):
    # Xac dinh bang tra cuu
    lookup_table = {
        1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
        11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S',
        20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
    }
    # Tinh ma tran nghich dao cua A
    inverse_matrix = np.linalg.inv(matrix)
    # Giai ma thu bang A^(-1) va bang tra cuu
    decoded_message = ''
    for column in encoded_message.T:
        result = np.dot(inverse_matrix, column)
        result = np.round(result) % 27  # Mo dun 27 duoc su dung de xu ly tran
        for r in result:
            decoded_message += lookup_table[int(r)]
    return decoded_message


# Xac dinh thong diep duoc ma hoa va ma tran A
E = np.array([
    [80, 98, 99, 85, 106, 94],
    [71, 92, 76, 95, 100, 92],
    [124, 163, 140, 160, 176, 161]
])
A = np.array([
    [1, 2, 3],
    [2, 1, 2],
    [3, 2, 4]
])

# Giai ma thong diep
decoded_message = decode_message(E, A)
print(decoded_message)