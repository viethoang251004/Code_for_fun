import numpy as np

def is_orthogonal(vectors):
    n = len(vectors)
    for i in range(n):
        for j in range(i+1, n):
            if np.dot(vectors[i], vectors[j]) != 0:
                return False
    return True

u1 = np.array([3, 1, 1])
u2 = np.array([-1, 2, 1])
u3 = np.array([-1/2, 2, 7/2])
vectors = [u1, u2, u3]

if is_orthogonal(vectors):
    print("The set of vectors is orthogonal.")
else:
    print("The set of vectors is not orthogonal.")