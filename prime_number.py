

# TODO
def primenumber(x):
    count = 2
    while True:
        if (x / count).is_integer():
            print("素数じゃない")
            break
        elif count == x-1:
            print("素数である")
            break
        else:
            count = count + 1
#xがある数で割り切れる、countがx - 1になるでbreak
primenumber(61)
#素数である

primenumber(10)
#素数じゃない


