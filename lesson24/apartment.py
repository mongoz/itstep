class Apartment:
    def __init__(self, number, livers, floor, square):
        self._number = number
        self._livers = livers
        self._floor = floor
        self._square = square

    def __str__(self):
        return f"{self._number}, {self._livers}, {self._floor}, {self._square}"

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, new_number):
        self._number = new_number

    @number.deleter
    def number(self):
        del self._number

    @property
    def livers(self):
        return self._livers

    @livers.setter
    def livers(self, updated_livers):
        if type(updated_livers) == int:
            self._livers = updated_livers
        else:
            print("Not correct input")

    @livers.deleter
    def livers(self):
        del self._livers

    @property
    def floor(self):
        return self._floor
    @floor.setter
    def floor(self, new_floor):
        if type(new_floor) == int:
            self._floor = new_floor
        else:
            print("Not correct input")
    @floor.deleter
    def floor(self):
        del self._floor

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


if __name__ == "__main__":
    num_57 = Apartment(57, 2, 2, 75)
    print(num_57)
    num_57.floor = 4
    print(num_57)
    num_57.livers = 3
    print(num_57)
    num_57.square = 87
    print(num_57)