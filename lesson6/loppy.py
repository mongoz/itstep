number = list(range(1, 100))
for x in reversed(number):
    if x < 10:
        print(x)
    elif x > 10:
        if x % 11 == 0:
            print(x)
