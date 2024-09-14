import numpy as np

def retrieve_nearest_document(q, doc_matrix):
    num_docs = doc_matrix.shape[0]
    sim_scores = np.zeros(num_docs)
    for i in range(num_docs):
        dot_product = np.dot(q, doc_matrix[i])
        norm_q = np.linalg.norm(q)
        norm_doc_i = np.linalg.norm(doc_matrix[i])
        sim_scores[i] = dot_product / (norm_q * norm_doc_i)
    nearest_doc_index = np.argmax(sim_scores)
    return nearest_doc_index, sim_scores[nearest_doc_index]

# Vi du
doc_matrix = np.array([[1.0, 0.5, 0.3, 0, 0, 0],
                       [0.5, 1.0, 0, 0, 0, 0],
                       [0, 1.0, 0.8, 0.7, 0, 0],
                       [0, 0.9, 1.0, 0.5, 0, 0],
                       [0, 0, 0, 1.0, 0, 1.0],
                       [0, 0, 0, 0, 0.7, 0],
                       [0.5, 0, 0.7, 0, 0, 0.9],
                       [0, 0.6, 0, 1.0, 0.3, 0.2]])
q = np.array([0, 0, 0.7, 0.5, 0, 0.3])
nearest_doc_index, sim_score = retrieve_nearest_document(q, doc_matrix)
print(f"The nearest document is D{nearest_doc_index+1} with a similarity score of {sim_score}")