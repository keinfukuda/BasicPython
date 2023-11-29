# TODO
a, b =0, 1

def kein(f, a, b, n):
    h = (b - a) / n
    s = 0
    k = 1
    while True:
        s = s + (h/2) * (f(a + (k-1) * h) + f(a + k * h))
        if k == n:
            print(s)
            break
        k = k + 1

#(1)
def f(x):
    return math.sin(x)

kein(f, 0, math.pi / 2, 50)
#0.9999177519437218

#(2)
def f(x):
    return 4/(1 + x**2)

kein(f, 0, 1, 100)
#3.141575986923131

#(3)
def f(x):
    return math.pi**(1/2) * math.exp(-x**2)

kein(f, -100, 100, 1000)
#3.1415926535897944