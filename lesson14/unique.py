"""Реалізувати функцію unique(tup1: tuple, tup2: tuple,
tup3: tuple) -> tuple , яка приймає три кортежі з цілими
числами та повертає кортеж з унікальними
значеннями."""


def unique(tup1: tuple, tup2: tuple, tup3: tuple) -> tuple:
    unique_l = []

    for i in tup1:
        if i not in tup2:
            if i not in tup3:
                unique_l.append(i)
    for n in tup2:
        if n not in tup1:
            if n not in tup3:
                unique_l.append(n)
    for m in tup3:
        if m not in tup1:
            if m not in tup2:
                unique_l.append(m)
    unique_tuple = tuple(unique_l)
    return unique_tuple


print(unique((4, 2, 6, 7), (1, 2, 7, 2, 9), (2, 2, 2, 7, 1)))