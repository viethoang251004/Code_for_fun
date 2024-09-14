import itertools

# (a)
suits = ['♠', '♣', '♦', '♥']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

deck = list(itertools.product(ranks, suits))
poker_5 = list(itertools.combinations(deck, 5))

len_poker_5 = len(poker_5)

print("Danh sách tất cả các bài xì phé 5 lá có thể có:")
for hand in poker_5:
    print(hand)

print("Số lượng bài xì phé 5 lá có thể có:", len_poker_5)

# (b)
three_of_a_kind = []

for hand in poker_5:
    ranks_in_hand = [card[0] for card in hand]
    unique_ranks = set(ranks_in_hand)

    if len(unique_ranks) == 2 and ranks_in_hand.count(ranks_in_hand[0]) == 3:
        three_of_a_kind.append(hand)

len_three_of_a_kind = len(three_of_a_kind)

print("Danh sách bộ ba giống nhau:")
for hand in three_of_a_kind:
    print(hand)

print("Số lượng bộ ba giống nhau:", len_three_of_a_kind)
