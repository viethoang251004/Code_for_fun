import numpy as np
import matplotlib.pyplot as plt

def compute_characteristic_polynomial(a):
    # Matrix A
    A = np.array([[-6, 28, 21],
                  [4, -15, -12],
                  [8, a, 25]])

    # Compute the characteristic polynomial
    char_poly_coeffs = np.poly(A - np.eye(3))
    char_poly = np.poly1d(char_poly_coeffs)

    return char_poly

def plot_characteristic_polynomials(a_values):
    t_values = np.linspace(0, 3, 1000)  # t values for plotting

    plt.figure(figsize=(10, 6))
    for a in a_values:
        char_poly = compute_characteristic_polynomial(a)
        plt.plot(t_values, char_poly(t_values), label=f'a = {a}')

    plt.xlabel('t')
    plt.ylabel('p(t)')
    plt.title('Characteristic Polynomials')
    plt.legend()
    plt.grid(True)
    plt.show()

def compute_eigenvalues(a_values):
    eigenvalues_dict = {}
    for a in a_values:
        char_poly = compute_characteristic_polynomial(a)
        eigenvalues = np.roots(char_poly.coeffs)
        eigenvalues_dict[a] = eigenvalues

    return eigenvalues_dict

# Values of 'a' to evaluate
a_values = [32, 31.9, 31.8, 32.1, 32.2]

# Plot characteristic polynomials
plot_characteristic_polynomials(a_values)

# Compute eigenvalues
eigenvalues_dict = compute_eigenvalues(a_values)
for a, eigenvalues in eigenvalues_dict.items():
    print(f'Eigenvalues for a = {a}:')
    print(eigenvalues)
    print()
