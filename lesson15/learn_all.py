Ron = {"Accio", "Wingardium Leviosa", "Alohomora"}
Harry = {"Accio", "Wingardium Leviosa", "Expelliarmus", "Expecto patronum"}


# Task 5 Обьединить множества
def learn_all(my_spells: set, teacher_spells: set) -> set:
    my_spells.union(teacher_spells)
    return my_spells


print(f"Все заклинания, которые будут знать ребята после обучения друг друга{learn_all(Harry, Ron)}")