class Country:

    def __init__(self, name):
        if type(name) == str:
            for i in name:
                if i[0].isupper():
                    self.name = name
                    break
                else:
                    print("Not correct input of the name of the Country")
                    break
        else:
            print("Not correct input of the Country")

    def capital(self, capital):
        if type(capital) == str:
            for i in capital:
                if i[0].isupper():
                    self.capital = capital
                    break
                else:
                    print("Not correct input of the Capital")
                    break
        else:
            print("Not correct input of the Capital")

    def continent(self, continent):
        continents = ["Eurasia", "Africa", "North America", "South America", "Australia", "Antarctica"]
        if type(continent) == str:
            if continent in continents:
                self.continent = continent
            else:
                print("No such continent exists")
        else:
            print("Not correct input of the Continent")

    def population(self, population):
        if type(population) == int:
            self.population = population
        else:
            print("Not correct input of the population")

    def cities(self, *args):
        cities = []
        for i in args:
            if i[0].isupper():
                cities.append(i)
                self.cities = cities
            else:
                print("Not correct input of the cities")
                break


ukr = Country("Ukraine")
print("Correct name: ", ukr.name)

ukr.capital("Kyiv")
print("Correct Capital: ", ukr.capital)

ukr.continent("Eurasia")
print("Correct Continent: ", ukr.continent)

ukr.population(44390000)
print("Correct population: ", ukr.population)

ukr.cities("DnepR", "Donetsk")
print("Correct cities: ", ukr.cities)
