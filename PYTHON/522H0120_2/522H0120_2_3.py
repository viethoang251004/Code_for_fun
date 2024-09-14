import random

def simulator_dice3(n):
    count_same_number = 0

    for _ in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        if dice1 == dice2:
            count_same_number += 1

    experimental_probability = count_same_number / n
    return experimental_probability
