import random

def simulator_dice4(n):
    count_event = 0

    for _ in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        if (dice1 == 1 and dice2 == 6) or (dice1 == 6 and dice2 == 1):
            count_event += 1

    experimental_probability = count_event / n
    return experimental_probability
