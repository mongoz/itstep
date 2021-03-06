class Country:
    def __init__(self, capital, continent, population, city_1, city_2):
        self._capital = capital
        self._continent = continent
        self._population = population
        self._city_1 = city_1
        self._city_2 = city_2

    def set_capital(self, capital):
        if str(capital):
            return self._capital
        else:
            print("Incorrect input."
                  " Right answer is London.")

    def set_continent(self, continent):
        self._continent = continent

    def set_population(self, population):
        self._population = population

    def set_city_1(self, city_1):
        self._city_1 = city_1

    def set_city_2(self, city_2):
        self._city_2 = city_2

    def get_continent(self):
        return self._continent

    def get_population(self):
        return self._population

    def get_city_1(self):
        return self._city_1

    def get_city2(self):
        return self._city_2


def main():
    capital = input("Enter the capital of Great Britain: ")
    if str(capital):
        if capital == 'London':
            return False # как здесь перешагнуть дальше , потому  что ввожу правильно,
    else:
        return True
    continent = input("Enter the continent: ")
    population = float(input("Enter the population of London by 2019: "))
    city_1 = input('Enter random city 1: ')
    city_2 = input('Enter random city 2: ')

    country = Country(capital, continent, population, city_1, city_2)

    print('Your entered Data')
    print()
    print(f"Capital of Great Britain: {country.set_capital(capital)}\n "
          f"Continent: {country.get_continent()}\n"
          f"Population: {country.get_population()}\n"
          f"City 1: {country.get_city_1()}\n"
          f"City 2: {country.get_city2()}")


"""
Валидацию также необходимо выполнять и вовремя выполнения главной функции не только,  когда пишу класс
"""
main()

# Траблы с этой Валидацией не понимаю что нужно как ее правильно описать
