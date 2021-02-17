list_with_strings = [(1, 2, "pocket_money"), (4, 5), ()]
for (tuple) in list_with_strings:
    if len(tuple) == 0:
        list_with_strings.remove(tuple)
print(list_with_strings)
