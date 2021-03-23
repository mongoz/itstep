numbers = [-1, -6, 8, 100, -2.6, -265, 345, 1]

num_filter = filter(lambda number: number < 0, numbers)

print(list(num_filter))
