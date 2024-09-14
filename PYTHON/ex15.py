import sympy as sp
t = sp.symbols('t')
s = 24*t -0.8*t*t
#(a)
v = sp.diff(s, t)
a = sp.diff(s, t, 2)
print('Van toc cua vat tai thoi diem t la: ', v)
print('Gia toc cua vat tai thoi diem t la: ', a)
#(b)
tmax = sp.solve(v)
print('Thoi diem vat dat do cao cuc dai la:', tmax)
#(c)
h = s.subs(t, tmax)
print('Do cao cuc dai ma vat di duoc la:', h)