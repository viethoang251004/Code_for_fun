import sympy as sp
t = sp.symbols('t')
b = 10**6 + (10**4)*t - (10**3)*t*t
db = sp.diff(b, t)
#(a)
dda = db.subs(t, 0)
print('Tai thoi diem t = 0 thi toc do tang truong la: ', dda)
#(b)
ddb = db.subs(t, 5)
print('Tai thoi diem t = 5 thi toc do tang truong la: ', ddb)
#(c)
ddc = db.subs(t, 10)
print('Tai thoi diem t = 10 thi toc do tang truong la: ', ddc)