import math

def pmf_normal(x, mu, sigma):
    coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
    exponent = -((x - mu) ** 2) / (2 * sigma ** 2)
    return coefficient * math.exp(exponent)

def cdf_normal(x, mu, sigma):
    return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))

# Example usage
mean = 3
variance = 16
std_deviation = math.sqrt(variance)

# (a) Graph representing the relationship between X and the function pmf_normal
import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(mean - 4 * std_deviation, mean + 4 * std_deviation, 1000)
pdf_values = [pmf_normal(x, mean, std_deviation) for x in x_values]

plt.plot(x_values, pdf_values)
plt.xlabel('X')
plt.ylabel('PDF')
plt.title('Probability Density Function (PDF) of the Normal Distribution')
plt.show()

# (b) Graph representing the relationship between X and the function cdf_normal
cdf_values = [cdf_normal(x, mean, std_deviation) for x in x_values]

plt.plot(x_values, cdf_values)
plt.xlabel('X')
plt.ylabel('CDF')
plt.title('Cumulative Distribution Function (CDF) of the Normal Distribution')
plt.show()

# (c) Finding P{2 < X < 7}
probability = cdf_normal(7, mean, std_deviation) - cdf_normal(2, mean, std_deviation)
print(f'P{{2 < X < 7}} = {probability:.4f}')
