Ron = {"Accio", "Wingardium Leviosa", "Alohomora"}
Harry = {"Accio", "Wingardium Leviosa", "Expelliarmus", "Expecto patronum"}


# Вторая функция уникальные значение, которые не пересекаются
def unique_spells_0(ron_spells: set, harry_spells: set) -> set:
    unique_spells_1 = ron_spells.symmetric_difference(harry_spells)
    return unique_spells_1


print(f"Заклинания которые знают Рон или Гарри {unique_spells_0(Ron, Harry)}")