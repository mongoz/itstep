from functools import reduce

seq = [1, 2, 3, 4, 5]
multiply_all = reduce(lambda x, y: x * y, seq)

print(multiply_all)
