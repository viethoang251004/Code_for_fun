def build_probability_space():
    probability_space = [('Thanh', 'Nữ'), ('Hồng', 'Nữ'), ('Thương', 'Nữ'), ('Đào', 'Nữ'), ('Yến', 'Nữ'),
                        ('Hạnh', 'Nữ'), ('My', 'Nữ'), ('Vy', 'Nữ'), ('Tiên', 'Nữ'), ('Thanh', 'Nam'),
                        ('Bình', 'Nam'), ('Nhật', 'Nam'), ('Hào', 'Nam'), ('Đạt', 'Nam'), ('Minh', 'Nam')]
    return probability_space

def event_A(probability_space):
    event = [outcome[0] for outcome in probability_space if outcome[0] == 'Thanh']
    return event

def event_B(probability_space):
    event = [outcome[0] for outcome in probability_space if outcome[1] == 'Nữ']
    return event

def event_A_and_B(probability_space):
    event = [outcome[0] for outcome in probability_space if outcome[0] == 'Thanh' and outcome[1] == 'Nữ']
    return event

def calculate_probability(event, probability_space):
    return len(event) / len(probability_space)

# (a)
probability_space = build_probability_space()
A = event_A(probability_space)
print("Event A:", A)

# (b)
B = event_B(probability_space)
print("Event B:", B)

# (c)
A_B = event_A_and_B(probability_space)
print("Event A ∩ B:", A_B)

# (d)
P_A = calculate_probability(A, probability_space)
P_B = calculate_probability(B, probability_space)
P_A_B = calculate_probability(A_B, probability_space)
print("P(A):", P_A)
print("P(B):", P_B)
print("P(A ∩ B):", P_A_B)

# (e)
P_A_given_B = P_A_B / P_B
print("P(A|B):", P_A_given_B)
