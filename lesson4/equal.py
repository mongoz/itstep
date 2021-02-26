msg = "Am i a Joke to You?"
E = "Equals"
try:
    a = float(input("First number\n"))
    b = float(input("Second number\n"))
    if a == b:
        print(E)
    elif a <= b:
        print(f"{b} > {a}", sep='\t')
    elif b <= a:
        print(f"{a} > {b}", sep='\t')
except ValueError:
    print(msg)

# МОЖНО ЕЩЁ ТАК
# a = int(input("enter:  "))
# b = int(input("enter:   "))
# Проверить условие
# if a == b:
#  print("equal")
# elif a > b:
#  print(f'{a} , {b}')
# elif a < b:
#  print(f'{b}, {a}')
# else:
#  print("Am i Joke to YOU")
