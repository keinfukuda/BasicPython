

# TODO
#問3
def euclid(a, b):
    while True:
        if b < a:
            b, a = a, b
        elif b % a == 0:
            return a
            break
        else :
            b, a =a, b % a


#問4
def euclid2(a, b):
    while True:
        if b < a:
            b, a = a, b
        elif b % a == 0:
            if a == 1:
                return True
                break
            else:
                return False
                break
        else :
            b, a =a, b % a
