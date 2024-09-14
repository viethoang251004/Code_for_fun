import sympy as sp
x = sp.symbols("x")
dc = 1/(2*x**2)
fin_c = sp.integrate(dc, x)
c100 = dc.subs(x, 100)
c1 = dc.subs(x, 1)
print("c(100) - c(1) =", c100 - c1)