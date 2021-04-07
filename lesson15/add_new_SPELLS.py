Ron = {"Accio", "Wingardium Leviosa", "Alohomora"}
Harry = {"Accio", "Wingardium Leviosa", "Expelliarmus", "Expecto patronum"}


# Задание 4 Добавляем много аргументов
def add_new_spells(spells_list: set, *args) -> bool:
    if args in spells_list:
        return False
    if args not in spells_list:
        spells_list.difference_update(*args)
        return True


print(f"""Доступны новые заклинания для HARRY {add_new_spells(Harry,
                                                                    'Lumos','Epidimenta', 'Levicorpus',
                                                                    'Sectumsempra','Cruciatus', 'Bombarda')}=>>>>""")
print(f"{Harry}")