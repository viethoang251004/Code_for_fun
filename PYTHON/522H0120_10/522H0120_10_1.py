import random
import matplotlib.pyplot as plt
import numpy as np

def flip_two_dice(num_flips):
    x = []
    for _ in range(num_flips):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        x.append(dice1 + dice2)
    return x
def calculate_probability_distribution(x):
    total_flips = len(x)
    probabilities = [x.count(i) / total_flips for i in range(2, 13)]
    return probabilities
def calculate_characteristic_parameters(x):
    expectation = np.mean(x)
    variance = np.var(x, ddof=1)
    standard_deviation = np.sqrt(variance)
    return expectation, variance, standard_deviation

# (a) Tung hai con xuc xac 10000 lan va luu ket qua vao bien x
num_flips = 10000
x = flip_two_dice(num_flips)
# (b) Tim cac gia tri cua bien ngau nhien X
X = list(set(x))  # Cac gia tri duy nhat cua bien ngau nhien X
# (c) Tinh ham phan phoi xac suat cua bien ngau nhien X
P = calculate_probability_distribution(x)
# (d) Tinh cac tham so dac trung cua bien ngau nhien X
expectation, variance, standard_deviation = calculate_characteristic_parameters(x)
# Hien thi ket qua
print("Random variable X:", X)
print("Probability distribution function P:", P)
print("Expectation (Mean):", expectation)
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)
# Ve ham phan phoi xac suat
plt.bar(X, P)
plt.xlabel("Sum of Dice Faces (X)")
plt.ylabel("Probability")
plt.title("Probability Distribution of X")
plt.xticks(np.arange(2, 13))
plt.show()
