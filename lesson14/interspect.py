def intersect(tup1: tuple, tup2: tuple, tup3: tuple) -> tuple:
    my_list = []
    for i in tup1:
        for m in tup2:
            for n in tup3:
                if i == m == n:
                    my_list.append(i)
                    i += 1
    my_tuple = tuple(my_list)
    return my_tuple


print(intersect((4, 2, 6, 7), (1, 2, 7, 2, 9), (2, 2, 2, 7, 1)))

