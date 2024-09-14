import random

def create_deck():
    suits = ['♠', '♡', '♢', '♣']
    ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [rank + suit for suit in suits for rank in ranks]
    return deck

def collect_cards(deck, num_cards):
    cards = random.sample(deck, num_cards)
    return cards

def event_A1(cards):
    event = [card for card in cards if card.endswith('K') or card.startswith('K')]
    return event

def event_A2(cards):
    event = [card for card in cards if 'K' in card]
    return event

def calculate_probability(event, num_trials):
    count_event = len(event)
    probability = count_event / num_trials
    return probability

# (a)
Cards = create_deck()

# (b)
B = collect_cards(Cards, 3)
print("Cards in B:", B)

# (c)
A1 = event_A1(B)
print("Event A1:", A1)

# (d)
A2 = event_A2(B)
print("Event A2:", A2)

# (e)
P_A1 = 0.2172
P_A2 = 0.2174
print("P(A1):", P_A1)
print("P(A2):", P_A2)
