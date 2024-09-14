import sympy as sp
x, y, t, z = sp.symbols('x, y, t, z')
#(a)
f = x ** 2 + 1
df = sp.diff(f, x)
slope = df.subs(x, 2)
y_tangentline = slope * (x - 2) + 5
sp.plot(f, y_tangentline, (x, -5, 5))
#(b)
f = x - (2 * x ** 2)
df = sp.diff(f, x)
slope = df.subs(x, 1)
y_tangentline = slope * (x - 1) - 1
sp.plot(f, y_tangentline, (x, -10, 10))
#(c)
f = x / (x - 2)
df = sp.diff(f, x)
slope = df.subs(x, 3)
y_tangentline = slope * (x - 3) + 3
sp.plot(f, y_tangentline, (x, -10, 10))
#(d)
g = 8 / (x ** 2)
dg = sp.diff(g, x)
slope = dg.subs(x, 2)
y_tangentline = slope * (x - 2) + 2
sp.plot(g, y_tangentline, (x, -10, 10))
#(e)
g = x ** (1 / 2)
df = sp.diff(f, x)
slope = df.subs(x, 4)
y_tangentline = slope * (x - 4) + 2
sp.plot(g, y_tangentline, (x, -10, 10))
#(f)
h = (t ** 3) + (3 * t)
df = sp.diff(h, t)
slope = df.subs(t, 1)
y_tangentline = slope * (t - 1) + 4
sp.plot(h, y_tangentline, (t, -10, 10))
#(g)
f = 8 / (x - 2) ** 1/2
df = sp.diff(f, x)
slope = df.subs(x, 1)
y_tangentline = slope * (x - 6) + 4
sp.plot(f, y_tangentline, (x, -10, 10))
#(h)
g = 1 + (4 - z) ** 1/2
df = sp.diff(g, z)
slope = df.subs(z, 1)
y_tangentline = slope * (z - 3) + 2
sp.plot(g, y_tangentline, (z, -10, 10))