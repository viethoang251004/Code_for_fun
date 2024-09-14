import random

def simulator_dice5(n):
    count_event = 0

    for _ in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        if dice1 + dice2 > 6:
            count_event += 1

    experimental_probability = count_event / n
    return experimental_probability
