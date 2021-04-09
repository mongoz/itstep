class Human:
    name = None
    surname = None
    birthday = None
    telephone = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name_1(self, name):
        self.name = name
        print(name)

    def surname_1(self, surname):
        self.surname = surname
        print(surname)

    def birthday_1(self, birthday):
        self.birthday = birthday
        print(birthday)

    def telephone_1(self, telephone):
        self.telephone = telephone
        print(telephone)


gregory = Human("Gregory", "19.08.1956")
gregory.name_1("Gregory")
gregory.birthday_1("19.08.1956")
gregory.telephone_1("+3809745132")
