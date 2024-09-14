import random

# (a)
total_straights = 32
total_combinations = 2598960
probability = total_straights / total_combinations
print("a) Xác suất lý thuyết của 5 lá bài tạo thành một sảnh:", probability)

# (b)
def straight_probability_experiment(n):
    total_experiments = n
    count_success = 0

    for _ in range(total_experiments):
        deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        hand = random.sample(deck, 5)
        hand.sort()

        is_straight = True
        for i in range(1, 5):
            if deck.index(hand[i]) - deck.index(hand[i-1]) != 1:
                is_straight = False
                break

        if is_straight:
            count_success += 1

    probability = count_success / total_experiments

    print("b) Xác suất thực nghiệm của 5 lá bài tạo thành một sảnh sau", total_experiments, "lần thí nghiệm:", probability)

straight_probability_experiment(1000)
