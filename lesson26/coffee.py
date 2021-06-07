from abc import ABCMeta
from abc import abstractmethod


class Coffee(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_cup_size(self, size):
        pass

    @abstractmethod
    def coffee_name(self):
        pass

    @abstractmethod
    def is_have_milk(self, answer):
        pass


class Latte(Coffee):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def get_cup_size(self, size):
        return f"The size of the cup is {size}"

    def coffee_name(self):
        return f"This is {self.name}"

    def is_have_milk(self, answer):
        if answer == "yes":
            return True
        else:
            return False


class Espresso(Coffee):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def get_cup_size(self, size):
        return f"The size of the cup is {size}"

    def coffee_name(self):
        return f"This is {self.name}"

    def is_have_milk(self, answer):
        if answer == "yes":
            return True
        else:
            return False


class Cappuccino(Coffee):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def get_cup_size(self, size):
        return f"The size of the cup is {size}"

    def coffee_name(self):
        return f"This is {self.name}"

    def is_have_milk(self, answer):
        if answer == "yes":
            return True
        else:
            return False