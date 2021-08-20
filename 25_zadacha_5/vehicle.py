import math
import operator

degrees_list = [x for x in range(0, 360)]


class Vehicle:

    def __init__(self, x=0, y=0, a=90):
        self.__x = self.set_x(x)
        self.__y = self.set_y(y)
        self.__alpha = self.set_a(a)

    def set_x(self, x):
        if isinstance(x, int) or isinstance(x, float):
            return x
        else:
            return 0

    def set_y(self, y):
        if isinstance(y, int) or isinstance(y, float):
            return y
        else:
            return 0

    def set_a(self, a):
        if isinstance(a, int) or isinstance(a, float):
            return a
        else:
            return 0

    def set_direciotn(self, direction):
        if direction.lower() == 'влево':
            return direction
        elif direction.lower() == 'вправо':
            return direction
        else:
            raise NameError('Переменная direction принимает только строковые значения влево/вправо')

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_a(self):
        return self.__alpha

    def move(self, distance):
        x = self.get_x() + distance * math.cos(math.radians(self.get_a()))
        y = self.get_y() + distance * math.sin(math.radians(self.get_a()))
        print(f'Автомобиль проехал расстояние: {distance} и теперь находиться на координатах ({x}:{y})')
        self.change_x(x)
        self.change_y(y)

    def change_x(self, new_x):
        self.__x = new_x

    def change_y(self, new_x):
        self.__y = new_x

    def change_a(self, new_a):
        self.__alpha = new_a

    def turn(self, direction, a):
        choosen_direction = self.set_direciotn(direction)
        if choosen_direction.lower() == 'влево':
            if degrees_list.index(self.get_a()) + a > len(degrees_list):
                overflow = degrees_list.index(self.get_a()) + a
                while overflow > len(degrees_list):
                    overflow -= len(degrees_list)
                new_a = overflow
            else:
                new_a = degrees_list.index(self.get_a()) + a
        else:
            if degrees_list.index(self.get_a()) - a < 0:
                overflow = degrees_list.index(self.get_a()) - a
                while overflow < 0:
                    overflow += len(degrees_list)
                new_a = overflow
            else:
                new_a = degrees_list.index(self.get_a()) - a
        self.change_a(new_a)
        print(f'Вы повернули {choosen_direction} текущее направление езды: {new_a} градусов')


class Bus(Vehicle):

    def __init__(self, x, y, a, passengers=0, money=0):
        super(Bus, self).__init__(x, y, a)
        self.__passengers = self.set_passengers_q(passengers)
        self.__money = self.set_money(money)

    def take_passengers(self, quantity):
        self.__passengers = self.set_passengers_q(quantity)
        print(f'Вы взяли {quantity} пассажиров')

    def set_passengers_q(self, quantity):
        if isinstance(quantity, int) and quantity >= 0:
            return quantity
        else:
            raise ValueError('Количество пассажиров должно быть целым, положительным числом')

    def set_money(self, money):
        if isinstance(money, (int, float)):
            return money
        else:
            raise ValueError('Количество денег должно быть числом')

    def add_money(self, money):
        self.__money += money


    def let_passengers_go(self, quantity):
        self.__passengers -= self.set_passengers_to_go(quantity)
        print(f'Вышло {quantity} пассажиров')

    def set_passengers_to_go(self, quantity):
        if isinstance(quantity, int) and 0 < quantity < self.get_passengers_q():
            return quantity
        else:
            raise ValueError('Количество пассажиров должно быть целым числом и быть меньше текущего числа пассажиров')

    def get_passengers_q(self):
        return self.__passengers

    def get_money(self):
        return self.__money

    def move(self, distance):
        x = self.get_x() + distance * math.cos(math.radians(self.get_a()))
        y = self.get_y() + distance * math.sin(math.radians(self.get_a()))

        self.change_x(x)
        self.change_y(y)
        if distance > 0:
            earned_money = round(distance / 5 * self.get_passengers_q(),2)
            self.add_money(earned_money)
            if earned_money == 0:
                end_of_phrase = ' но у нас нет пассажиров, нам никто не заплатит'
            else:
                end_of_phrase = f' за поездку было заработано {earned_money} $'
        if distance < 0:
            end_of_phrase = f' за поездку в обратном направлении нам никто не заплатит =(('
        print(f'Автобус проехал расстояние: {distance} и теперь находиться на координатах ({round(x,2)} : {round(x,2)})'
              + str(end_of_phrase))




