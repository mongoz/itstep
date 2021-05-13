class Army:
    def __init__(self, warrior_amount, damage_per_warrior, warrior_health):
        self.warrior_amount = warrior_amount
        self.damage = damage
        self.health = health

    def __str__(self):
        return f"{self.amount}, {self.damage}, {self.health}"

    def __add__(self, other):
        return Army(self.amount + other.amount,
                       (self.damage*self.amount + other.damage*other.amount)/(self.amount + other.amount),
                       (self.health*self.amount + other.health*other.amount)/(self.amount + other.amount))

    def __sub__(self, other):
        if self.amount - other.amount > 0:
            return Army(self.amount - other.amount, self.damage, self.health)
        else:
            return Army(0, self.damage, self.health)


class OrkArmy(Army):
    def receive_damage(self, damage: int):
        died_orks = (self.amount * self.health / damage)
        if self.amount > died_orks:
            self.amount = self.amount - died_orks
            return (died_orks)
        else:
            return (self.amount)


class ElfArmy(Army):
    def __init__(self, amount, damage, health, shield):
        Army.__init__(self, amount, damage, health)
        self.shield = shield

    def receive_damage(self, damage: int):
        died_elfs = ((self.amount * (self.health + self.shield)) / damage)
        if self.amount > died_elfs:
            self.amount = self.amount - died_elfs
            return (died_elfs)
        else:
            return (self.amount)