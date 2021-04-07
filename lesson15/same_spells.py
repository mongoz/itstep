Ron = {"Accio", "Wingardium Leviosa", "Alohomora"}
Harry = {"Accio", "Wingardium Leviosa", "Expelliarmus", "Expecto patronum"}


def same_spells(ron_spells: set, harry_spells: set) -> set:
    same_spell_0 = []
    ron_spells = {'Accio', 'Wingardium Leviosa', 'Alohomora'}
    harry_spells = {'Accio', 'Wingardium Leviosa', 'Expelliarmus', 'Expecto patronum'}
    for i in ron_spells:
        if i in harry_spells:
            same_spell_0.append(i)
    same_spell_1 = set(same_spell_0)
    return same_spell_1


print(f"Заклинание которые знает и Гарри, и Рон {same_spells(Ron, Harry)}")
# можно ещё сделать через .intersection()
