num = int(input("Enter the number of rows:\n"))
for x in range(0, num):
    for y in range(0, num - x - 1):
        print(end=" ")
    for y in range(0, x + 1):
        print("*", end=" ")
    print()
