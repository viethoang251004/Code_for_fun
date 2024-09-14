import random

def card_experiment_probability(n):
    total_experiments = n
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    count_e = 0
    count_f = 0

    for _ in range(total_experiments):
        deck = ["2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC",
                "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD",
                "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH",
                "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS"]

        drawn_cards = random.sample(deck, 4)

        suits = [card[-1] for card in drawn_cards]
        ranks = [card[:-1] for card in drawn_cards]

        if len(set(suits)) == 1:
            count_a += 1

        if len(set(suits)) == 4:
            count_b += 1

        if len(set([suit for suit in suits if suit != "C"])) == 1 or len(set([suit for suit in suits if suit != "D"])) == 1 or len(set([suit for suit in suits if suit != "H"])) == 1 or len(set([suit for suit in suits if suit != "S"])) == 1:
            count_c += 1

        if len(set(ranks)) == 1:
            count_d += 1

        if all(rank.isdigit() for rank in ranks) or all(rank.isdigit() for rank in ranks[1:]) or all(rank.isdigit() for rank in ranks[2:]) or all(rank.isdigit() for rank in ranks[3:]):
            count_e += 1

        if all(not rank.isdigit() for rank in ranks) or all(not rank.isdigit() for rank in ranks[1:]) or all(not rank.isdigit() for rank in ranks[2:]) or all(not rank.isdigit() for rank in ranks[3:]):
            count_f += 1

    probability_a = count_a / total_experiments
    probability_b = count_b / total_experiments
    probability_c = count_c / total_experiments
    probability_d = count_d / total_experiments
    probability_e = count_e / total_experiments
    probability_f = count_f / total_experiments

    print("Xác suất thực nghiệm sau", total_experiments, "lần rút bài:")
    print("a) Bốn lá cùng chất:", probability_a)
    print("b) Bốn lá đôi một khác chất:", probability_b)
    print("c) Bốn lá cùng màu:", probability_c)
    print("d) Bốn lá cùng chỉ số (tứ quý):", probability_d)
    print("e) Bốn lá cùng là loại số:", probability_e)
    print("f) Bốn lá cùng là loại hình:", probability_f)

card_experiment_probability(500)