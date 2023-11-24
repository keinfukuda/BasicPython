a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
while True:
     if b < a:
         b, a = a, b
     elif b % a == 0:
         print(a)
         break
     b, a = a, b % a


a, b =10, 20
while True:
     if b < a:
         b, a = a, b
     elif b % a == 0:
         print(a)
         break
     b, a = a, b % a

10

a, b =14, 91
while True:
     if b < a:
         b, a = a, b
     elif b % a == 0:
         print(a)
         break
     b, a = a, b % a

7

a, b =91, 14
while True:
     if b < a:
         b, a = a, b
     elif b % a == 0:
         print(a)
         break
     b, a = a, b % a

7