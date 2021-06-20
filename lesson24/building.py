class Building:
    def __init__(self, name, floors_number, height, square, city):
        self._name = name
        self._floors_number = floors_number
        self._height = height
        self._square = square
        self._city = city

    def __str__(self):
        return f"{self._name}, {self._floors_number}, {self._height}, {self._square}, {self._city}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @name.deleter
    def name(self):
        del self._name

    @property
    def floors(self):
        return self._floors_number

    @floors.setter
    def floors(self, new_floors_number):
        if type(new_floors_number) == int:
            self._floors_number = new_floors_number
        else:
            print("Not correct input")

    @floors.deleter
    def floors(self):
        del self._floors_number

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, new_height):
        if type(new_height) == int:
            self._height = new_height
        else:
            print("Not correct input")
    @height.deleter
    def height(self):
        del self._height

    @property
    def square(self):
        return self._square
    @square.setter
    def square(self, new_square):
        if type(new_square) == int:
            self._square = new_square
        else:
            print("Not correct input")
    @square.deleter
    def square(self):
        del self._square

    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, new_city):
        if type(new_city) == str:
            self._city = new_city
        else:
            print("Not correct input")
    @city.deleter
    def city(self):
        del self._city

if __name__ == "__main__":
    church = Building("Church", 5, 30, 400, "Kyiv")
    print(church)
    church.name = "Super Church"
    print(church)
    church.floors = 7
    print(church)
    church.height = 40
    print(church)
    church.square = 500
    print(church)
    church.city = "Lviv"
    print(church)