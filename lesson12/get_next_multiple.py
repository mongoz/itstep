def get_next_multiple(digit):
    total = 0
    while digit != 0:
        total += digit
        yield total


gen_multiple_of_two = get_next_multiple(2)
print(next(gen_multiple_of_two))
print(next(gen_multiple_of_two))
print(next(gen_multiple_of_two))
print(next(gen_multiple_of_two))

gen_multiple_of_thirteen = get_next_multiple(13)
print(next(gen_multiple_of_thirteen))
print(next(gen_multiple_of_thirteen))
print(next(gen_multiple_of_thirteen))
print(next(gen_multiple_of_thirteen))