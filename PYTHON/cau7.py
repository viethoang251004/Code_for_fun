import sympy as sp
import math as m

t, x, y, w, z = sp.symbols('t, x, y, w, z')

#(a)
w = x ** 2 + y ** 2
x = sp.cos(t)
y = sp.sin(t)
dwt = sp.diff(w, t)
print("Derivate of w(t) with regard to t = ", dwt)
print("Derivate of w(t) (with regard to t) at t = pi", dwt.subs(t, m.pi))
print(y.subs(t, 3).evalf())
#(b)
w = x ** 2 + y ** 2
x = sp.cos(t) + sp.sin(t)
y = sp.cos(t) - sp.sin(t)
dwt = sp.diff(w, t)
print("Derivate of w(t) with regard to t = ", dwt)
print("Derivate of w(t) (with regard to t) at t = 0", dwt.subs(t, 0))
print(y.subs(t, 3).evalf())
#(c)
w = x / z + y / z
x = (sp.cos(t)) ** 2
y = (sp.sin(t)) ** 2
z = 1 / t
dwt = sp.diff(w, t)
print("Derivate of w(t) with regard to t = ", dwt)
print("Derivate of w(t) (with regard to t) at t = 3", dwt.subs(t, 3))
print(y.subs(t, 3).evalf())
#(d)
w = 2 * y * sp.exp(x) - sp.log(z)
x = sp.log(t ** 2 + 1)
y = sp.tan(-1) * t
z = sp.exp(t)
dwt = sp.diff(w, t)
print("Derivate of w(t) with regard to t = ", dwt)
print("Derivate of w(t) (with regard to t) at t = 1", dwt.subs(t, 1))
print(y.subs(t, 3).evalf())
#(e)
w = z - sp.sin(x * y)
x = t
y = sp.log(t)
z = sp.exp(t - 1)
dwt = sp.diff(w, t)
print("Derivate of w(t) with regard to t = ", dwt)
print("Derivate of w(t) (with regard to t) at t = 1", dwt.subs(t, 1))
print(y.subs(t, 3).evalf())