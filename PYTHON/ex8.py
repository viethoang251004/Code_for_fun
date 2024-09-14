import sympy as sp
#(a)
x = sp.symbols('x')
f = x ** 3 - 3 * x + 1
df = sp.diff (f, x)
slope = df.subs(x, 3)
y_8a = slope *  (x - 3) + f.subs(x, 3)
sp.plot(f, y_8a, (x, -5, 5))
#(b)
x, y = sp.symbols('x, y')
f = x ** 3 - 3 * x + 1
y = 9 * x + 2
df = sp.diff (f, x)
slope = df.subs(x, 3)
y_tangentline = slope * (y - 2) + 5
sp.plot(f, y_tangentline, (x, -5, 5))
#(c)
x, y = sp.symbols('x, y')
f = x ** 3 - 3 * x + 1
A = x = 2/3; y = -1
df = sp.diff (f, x, A)
slope = df.subs(x, 3)
y_tangentline = slope * (y - 2) + 5
sp.plot(f, y_tangentline, (x, -5, 5))