from orcarmy import Army
from orcarmy import Ork
from orcarmy import Elf


class Gnome(Army):
    def receive_damage(self, damage_per_warrior: int):
        riped_gnomes = (self.warrior_amount * self.warrior_health / damage_per_warrior)
        if self.warrior_amount > riped_gnomes:
            self.warrior_amount = self.warrior_amount - riped_gnomes
            return riped_gnomes
        else:
            return self.warrior_amount


ork_army = Ork(500, 100, 100)
elf_army = Elf(700, 90, 90, 10)
gnome_army = Gnome(400, 110, 110)
list_of_armies = [ork_army, elf_army, gnome_army]


def army_damage():
    num_of_dam = int(input("Enter damage: "))
    print(f"Lost of Orcks: {ork_army.receive_damage(num_of_dam)};\n Remaining amount of orks:  {ork_army.warrior_amount}")
    print(f"Lost of Elfs: {elf_army.receive_damage(num_of_dam)};\n Remaining amount of elfs:  {elf_army.warrior_amount}")
    print(f"Lost of Gnomes: {gnome_army.receive_damage(num_of_dam)};"
          f"\n Remaining amount of gnomes:{gnome_army.warrior_amount}")


army_damage()
