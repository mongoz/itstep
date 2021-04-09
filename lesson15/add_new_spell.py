Ron = {"Accio", "Wingardium Leviosa", "Alohomora"}
Harry = {"Accio", "Wingardium Leviosa", "Expelliarmus", "Expecto patronum"}


# Задание 3 добавляю заклинание, которое не знает один из героев
def add_new_spell(spells_list: set, new_spell: str) -> bool:
    if new_spell in spells_list:
        return False
    if new_spell not in spells_list:
        spells_list.add(new_spell)
        return True


print(f"""'Expelliarmus' это новые заклинания для Рона {add_new_spell(Ron, 'Expelliarmus',)}=>>>>""")
print(f"""'Expecto Patronum' это новые заклинания для Рона {add_new_spell(Ron, 'Expecto patronum',)}=>>>>""")
print(f"""'Alohomora' это новые заклинания для Harry {add_new_spell(Harry, 'Alohomora',)}=>>>>""")


