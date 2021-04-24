class Car:
    def __init__(self, model, year, factory,
                 engine, colour, price):
        self._model = model
        self._year = year
        self._factory = factory
        self._engine = engine
        self._colour = colour
        self._price = price

    def set_model(self, model):
        self._model = model

    def set_year(self, year):
        self._year = year

    def set_engine(self, factory):
        self._factory = factory

    def set_colour(self, colour):
        self._colour = colour

    def set_price(self, price):
        self._price = price

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def get_factory(self):
        return self._factory

    def get_engine(self):
        return self._engine

    def get_colour(self):
        return self._colour

    def get_price(self):
        return self._price


def main():

    cart = Car(model='ML250', year='2012', factory='Mersedes-Benz', engine='2.5', colour='black', price='25 000$')

    print(f"Модель: {cart.get_model()}\n"
          f"Год: {cart.get_year()}\n"
          f"Завод: {cart.get_colour()}\n"
          f"Обьм двигателя: {cart.get_engine()}\n"
          f"Цвет: {cart.get_colour()}\n"
          f"Цена: {cart.get_price()}")


main()