import numpy as np

def cosine_similarity(doc_matrix):
    num_docs = doc_matrix.shape[0]
    sim_matrix = np.zeros((num_docs, num_docs))
    for i in range(num_docs):
        for j in range(i, num_docs):
            dot_product = np.dot(doc_matrix[i], doc_matrix[j])
            norm_i = np.linalg.norm(doc_matrix[i])
            norm_j = np.linalg.norm(doc_matrix[j])
            similarity = dot_product / (norm_i * norm_j)
            sim_matrix[i][j] = similarity
            sim_matrix[j][i] = similarity
    return sim_matrix

# Vi du
doc_matrix = np.array([[0, 4, 0, 0, 0, 2, 1, 3],
                       [3, 1, 4, 3, 1, 2, 0, 1],
                       [3, 0, 0, 0, 3, 0, 3, 0],
                       [0, 1, 0, 3, 0, 0, 2, 0],
                       [2, 2, 2, 3, 1, 4, 0, 2]])
sim_matrix = cosine_similarity(doc_matrix)
print(sim_matrix)