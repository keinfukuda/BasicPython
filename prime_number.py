a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
count = 2
while True:
     if (a / count).is_integer():
         print("素数じゃない")
         break
     elif count == a-1:
         print("素数である")
         break
     else:
         count = count + 1
#aがある数で割り切れる、countがa - 1になるでbreak
#b = 61のとき
b = 61
count = 2
while True:
     if (b / count).is_integer():
         print("素数じゃない")
         break
     elif count == b-1:
         print("素数である")
         break
     else:
         count = count + 1

"素数である"

#a = 10の時
a = 10
count = 2
while True:
     if (a / count).is_integer():
         print("素数じゃない")
         break
     elif count == a-1:
         print("素数である")
         break
     else:
         count = count + 1

"素数である"
