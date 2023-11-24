# TODO
import math
s = 0
k = 1
while True:
     s = s + (math.pi / 4000) * (math.sin((k-1) * math.pi / 2000) + math.sin(k * math.pi / 2000))
     if k == 1000:
         print(s)
         break
     k = k + 1

0.9999997943832338
#sにk番目の台形の面積を足す
#k = 1000だったらbreak
#kに1を足す