import random

def simulator_poker1(n):
    count_event = 0

    for _ in range(n):
        deck = create_deck()
        hand = draw_cards(deck, 5)

        if all(card[1] == '♥' for card in hand):
            count_event += 1

    experimental_probability = count_event / n
    return experimental_probability

def create_deck():
    suits = ['♠', '♣', '♦', '♥']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    return deck

def draw_cards(deck, num_cards):
    hand = random.sample(deck, num_cards)
    return hand
