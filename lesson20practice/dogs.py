class Dog:
    name = 'Layka'
    age = 2
    legs = 4
    breed = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self, steps):
        print(f"{self.name} are walking {steps} steps")

    def sleep(self):
        print(f"{self.name} are sleeping")

    def eat(self, food):
        print(f"{self.name} are eating {food}")


# Dog -> Bulldog наследование
class Bulldog(Dog):
    breed = "Bulldog"  # Полиморфизм это возможность переопределить какой-то
    # атрибут или метод

    def eat(self, food):
        print(f"{self.name} are eating {food} aloud")


class Labrador(Dog):
    breed = "Labrador"


layka = Dog('Layka', 2)
print(layka.breed)
layka.walk(steps=10)
layka.sleep()
layka.eat('meat')
print(30*"-")
gretta = Bulldog("Gretta", 5)
print(gretta.breed)
gretta.walk(steps=10)
gretta.walk(steps=20)
gretta.walk(steps=30)
gretta.eat('meat')
gretta.sleep()