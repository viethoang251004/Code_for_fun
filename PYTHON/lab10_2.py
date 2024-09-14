import sympy as sp
x, y = sp.symbols("x, y")
#(a)
f = x**3 - 3*sp.sin(x)*sp.cos(x)
fin = sp.integrate(f, (x, 0, sp.pi/2))
print = ("Definitive integral of f(x) =", fin.evalf())
#(b)
f = (sp.sin(x**2))**2
fin = sp.integrate(f, (x, 0, 1))
print = ("Definitive integral of f(x) =", fin.evalf())
#(c)
g = x + 1
f = (1 + g**2 + g**2)**1/2
fin = sp.integrate(f, (x, 0, 3))
fin = sp.integrate(g, (x, 0, 3))
print = ("Definitive integral of f(x) =", fin.evalf())
#(d)
f = x**2*y
fin = sp.integrate(f, (x, 1, 2), (y, 0, 3))
print = ("Definitive integral of f(x), f(y) =", fin.evalf())