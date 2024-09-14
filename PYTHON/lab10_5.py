import sympy as sp
t = sp.symbols('t')
v_t = 160 - 32 * t
s = sp.integrate(v_t, (t, 0, 8))
print("Khoảng cách mà hòn đá dịch chuyển =", s)