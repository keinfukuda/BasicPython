

# TODO
def euclid(a, b):
    while True:
        if b < a:
            b, a = a, b
        elif b % a == 0:
            print(a)
            break
        else :
            b, a =a, b % a


euclid(10, 20)
#10

euclid(14, 91)
#7

euclid(91, 14)
#7
