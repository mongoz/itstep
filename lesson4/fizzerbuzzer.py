E = "What the hell are you doing?!Repeat!"
try:
    c = input("Your number\t")
    if int(c) in range(0, 100, 3):
        print("Fizz")
    elif int(c) in range(0, 100, 5):
        print("Buzz")
    elif int(c) not in range(0, 100, 3) \
            or range(0, 100, 5):
        print(E)
except ValueError:
    print(E)
