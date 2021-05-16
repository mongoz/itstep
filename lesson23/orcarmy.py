class Army:
    def __init__(self, warrior_amount, damage_per_warrior, warrior_health):
        self.warrior_amount = warrior_amount
        self.damage_per_warrior = damage_per_warrior
        self.warrior_health = warrior_health

    def __str__(self):
        return f"{self.warrior_amount}, {self.damage_per_warrior}, {self.warrior_health}"

    def __add__(self, another_parm):
        return Army(self.warrior_amount + another_parm.amount,
                    (self.damage_per_warrior * self.warrior_amount + another_parm.damage_per_warrior *
                     another_parm.warrior_amount) / (
                                self.warrior_amount + another_parm.amount),
                    (self.warrior_health * self.warrior_amount + another_parm.warrior_health *
                     another_parm.warrior_amount) / (
                                self.warrior_amount + another_parm.amount))

    def __sub__(self, another_parm):
        if self.warrior_amount - another_parm.amount > 0:
            return Army(self.warrior_amount - another_parm.amount, self.damage_per_warrior, self.warrior_health)
        else:
            return Army(0, self.damage_per_warrior, self.warrior_health)


class Ork(Army):
    def receive_damage(self, damage_per_warrior: int):
        rip_ork = (self.warrior_amount * self.warrior_health / damage_per_warrior)
        if self.warrior_amount > rip_ork:
            self.warrior_amount = self.warrior_amount - rip_ork
            return rip_ork
        else:
            return self.warrior_amount


class Elf(Army):
    def __init__(self, warrior_amount, damage_per_warrior, warrior_health, shield):
        Army.__init__(self, warrior_amount, damage_per_warrior, warrior_health)
        self.shield = shield

    def receive_damage(self, damage: int):
        rip_elf = ((self.warrior_amount * (self.warrior_health + self.shield)) / damage)
        if self.warrior_amount > rip_elf:
            self.warrior_amount = self.warrior_amount - rip_elf
            return rip_elf
        else:
            return self.warrior_amount
