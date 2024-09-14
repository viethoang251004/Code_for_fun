import numpy as np

# Define the user-item matrix
M = np.array([[np.inf, np.inf, 3],
              [2, np.inf, 5],
              [5, 6, 7],
              [np.inf, np.inf, np.inf]])


def recommend_item(M, user):
    # Get the row corresponding to the user
    user_row = M[user-1]

    # Find the columns (items) on the user_row that are not rated
    unrated_items = np.where(user_row == np.inf)[0]

    if len(unrated_items) == 0:
        return "No item left to rate for user", user

    # Return the list of items to be rated
    return "Items to rate for user", user, ": ", unrated_items+1


# Example usage
for user in range(1, M.shape[0]+1):
    result = recommend_item(M, user)
    print(*result)
