

# TODO
def primenumber(n):
    count = 2
    if n == 1:
        return False
    elif n == 2:
        return True
    elif not (n).is_integer() or not n > 1:
        return print("error")
    else:
        while True:
            if (n / count).is_integer():
                return False
                break
            elif count > n ** (1/2):
                return True
                break
            else:
                count = count + 1
#nがある数で割り切れる、countがn - 1になるでbreak
primenumber(61)
#True

primenumber(10)
#False

primenumber(1)
#False

primenumber(2)
#True