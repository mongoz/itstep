def same_pos(tup1: tuple, tup2: tuple, tup3: tuple):
    new_dict = {}
    for i in range(len(tup1)):
        for j in range(len(tup2)):
            for k in range(len(tup3)):
                if tup1[i] == tup2[j] == tup3[k]:
                    new_dict[tup1[i]] = i
    print(f"Позиции повтора: {new_dict}")


same_pos((4, 2, 6, 7), (1, 2, 7, 7), (2, 2, 2, 7, 1))

