# TODO
import math

def kein(f, a = 0, b = 1, n = 100):
    h = (b - a) / n
    s = 0
    k = 1
    for i in range(n):
        s = s + (h/2) * (f(a + (k-1) * h) + f(a + k * h))
        k = k + 1
    return s



#(1)
def f1(x):
    return math.sin(x)

kein(f1, 0, math.pi / 2, 50)
#0.9999177519437218

#(2)
def f2(x):
    return 4/(1 + x**2)

kein(f2, 0, 1, 100)
#3.141575986923131

#(3)
def f3(x):
    return math.pi**(1/2) * math.exp(-x**2)

kein(f3, -100, 100, 1000)
#3.1415926535897944