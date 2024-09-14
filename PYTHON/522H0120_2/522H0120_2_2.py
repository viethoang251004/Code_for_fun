import random

def simulator_dice2(n):
    count_even_odd = 0

    for _ in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        if (dice1 % 2 == 0 and dice2 % 2 != 0) or (dice1 % 2 != 0 and dice2 % 2 == 0):
            count_even_odd += 1

    experimental_probability = count_even_odd / n
    return experimental_probability
