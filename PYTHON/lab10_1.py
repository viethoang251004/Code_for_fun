import sympy as sp
x = sp.symbols("x")
#(a)
f = x ** 3 + 2 * x ** 2 + 3
fin = sp.integrate(f, (x, 1, 2))
print("Antiderivative of f(x) =", fin)
print("Define integral of f(x) from 1 to 2 =", fin.evalf())
#(b)
f = 1 / x ** 3 + 1 / x ** 2 + x * x ** 1 / 2
fin = sp.integrate(f, (x, 1, 4))
print("Antiderivative of f(x) =", fin)
print("Define integral of f(x) from 1 to 4 =", fin.evalf())
#(c)
f = (x**3 + x*x**1/2 + x)/x**2
fin = sp.integrate(f, (x, 1, 4))
print("Antiderivative of f(x) =", fin)
print("Define integral of f(x) from 1 to 4 =", fin.evalf())
#(d)
f = 2/x + x**3
fin = sp.integrate(f, (x, 1, 2))
print("Antiderivative of f(x) =", fin)
print("Define integral of f(x) from 1 to 2 =", fin.evalf())