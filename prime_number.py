

# TODO
def primenumber(n):
    count = 2
    if n == 1:
        print(bool(0))
    elif n == 2:
        print(bool(1))
    elif not (n).is_integer() or not n > 1:
        print("error")
    else:
        while True:
            if (n / count).is_integer():
                print(bool(0))
                break
            elif count == n-1:
                print(bool(1))
                break
            else:
                count = count + 1
#nがある数で割り切れる、countがn - 1になるでbreak
primenumber(61)
True

primenumber(10)
False

primenumber(1)
False

primenumber(2)
True