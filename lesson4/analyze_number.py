a: int = int(input("Enter the integer number\n\t"))
if a % 2 == 0 and a >0:
    smile_parity = "Even positive number"
    print(a, "is the", smile_parity)
elif a % 2 != 0 and a >0:
    smile_parity = "Odd positive number"
    print(a, "is the", smile_parity)
elif a % 2 == 0:
    smile_parity = "Even negative number"
    print(a, "is the", smile_parity)
elif a % 2 != 0:
    smile_parity = "Odd negative number"
    print(a, "is the", smile_parity)



