# TODO
import math
a = 0
b = math.pi / 2
n = 100
h = (b - a) / n
s = 0
k = 1
while True:
    s = s + (h/2)*(math.sin(a + (k-1) * h) + math.sin(a + k * h))
    if k == n:
        print(s)
        break
    k = k + 1

#0.9999794382396072

#sにk番目の台形の面積を足す
#k = 1000だったらbreak
#kに1を足す