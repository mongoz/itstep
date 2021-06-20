from building import Building
from apartment import Apartment


class BuildingExtended(Building):

    def __init__(self, name, floors_number, height, square, city):
        super().__init__(name, floors_number, height, square, city)
        self._flats = []

    def add_flat(self, number, livers, floor, square):
         self._flats.append(Apartment(number, livers, floor, square))

    def sum_flats(self):
        if len(self._flats) > 0:
            return len(self._flats)
        else:
            return f'{self.name} is empty.'

    def number_of_people(self):
        count = 0
        if len(self._flats) > 0:
            for flat in self._flats:
                count += flat.livers
            return count
        else:
            return f'{self.name} is empty.'


if __name__ == "__main__":
    first = BuildingExtended("First", 5, 30, 400, "Kyiv")
    second = BuildingExtended("Second", 7, 40, 500, "Lviv")
    first.add_flat(5, 4, 3, 150)
    first.add_flat(6, 2, 3, 70)
    second.add_flat(7, 3, 3, 110)
    second.add_flat(8, 2, 4, 95)
    print("Flats in First: ", first.sum_flats())
    print("Flats in Second: ", second.sum_flats())
    print("Livers in First: ", first.number_of_people())
    print("Livers in Second: ", second.number_of_people())
    third = BuildingExtended("Third", 7, 40, 500, "Dnepr")
    print("Flats in Third: ", third.sum_flats())
    print("Livers in Third: ", third.number_of_people())