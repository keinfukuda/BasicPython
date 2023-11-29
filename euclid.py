

# TODO
#問3
def euclid(a, b):
    while True:
        if b < a:
            b, a = a, b
        elif b % a == 0:
            print(a)
            break
        else :
            b, a =a, b % a


#問4
def euclid(a, b):
    while True:
        if b < a:
            b, a = a, b
        elif b % a == 0:
            if a == 1:
                print(bool(1))
                break
            else:
                print(bool(0))
                break
        else :
            b, a =a, b % a
