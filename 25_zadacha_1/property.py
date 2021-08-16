class Property:

    __worth = 0

    def __init__(self, worth):
        self.__worth = self.set_worth(worth)

    def set_worth(self, worth):
        if worth > 0:
            return worth
        else:
            raise ValueError('Значение должно быть больше нуля')

    def get_worth(self):
        return self.__worth

    def tax_calc(self):
        return self.__worth


class Apartment(Property):

    name = 'Квартира'

    def __init__(self, worth):
        super().__init__(worth)

    def tax_calc(self):
        return super(Apartment, self).get_worth() / 1000


class Car(Property):

    name = 'Машина'

    def __init__(self, worth):
        super().__init__(worth)

    def tax_calc(self):
        return super(Car, self).get_worth() / 200


class CountryHouse(Property):

    name = 'Дача'

    def __init__(self, worth):
        super().__init__(worth)

    def tax_calc(self):
        return super(CountryHouse, self).get_worth() / 500
