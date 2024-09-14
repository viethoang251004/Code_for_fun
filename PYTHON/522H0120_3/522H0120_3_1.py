def build_probability_space():
    genders = ['M', 'F']
    probability_space = []
    for g1 in genders:
        for g2 in genders:
            for g3 in genders:
                probability_space.append(g1 + g2 + g3)
    return probability_space

def count_elements(probability_space):
    return len(probability_space)

def event_has_at_least_one_female(probability_space):
    event = [outcome for outcome in probability_space if 'F' in outcome]
    return event

def event_all_females(probability_space):
    event = [outcome for outcome in probability_space if outcome == 'FFF']
    return event

def calculate_conditional_probability(event_a, event_b):
    return len(event_a) / len(event_b)

# (a)
probability_space = build_probability_space()
print("Không gian xác suất hiệu suất:", probability_space)

# (b)
num_elements = count_elements(probability_space)
print("Số phần tử trong không gian xác suất:", num_elements)

# (c)
event_b = event_has_at_least_one_female(probability_space)
print("Sự kiện B:", event_b)

# (d)
event_a = event_all_females(probability_space)
print("Sự kiện A:", event_a)

# (e)
conditional_probability = calculate_conditional_probability(event_a, event_b)
print("Xác suất cả ba con mèo đều là con cái trong điều kiện ít nhất một con mèo là con cái:", conditional_probability)
