import sympy as sp
x = sp.symbols("x")
#(a)
f = x*x - 1
fin_a = sp.integrate(f, x)
avg_a = 1/(3**(1/2) - 0)*fin_a
print("Average of f =", avg_a)
#(b)
f = -x*x/2
fin_b = sp.integrate(f, x)
avg_b = 1/(3 - 0)*fin_b
print("Average of f =", avg_b)
#(c)
f = -3*x*x - 1
fin_c = sp.integrate(f, x)
avg_c = 1/(1 - 0)*fin_c
print("Average of f =", avg_c)
#(d)
f = x*x - x
fin_d = sp.integrate(f, x)
avg_d = 1/(-2 - 1)*fin_d
print("Average of f =", avg_d)