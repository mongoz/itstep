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
