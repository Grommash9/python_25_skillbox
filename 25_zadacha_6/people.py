import random
from animals import Animal


class People:

    def __init__(self, house, name='Человек', hunger=30, happyness=100):
        self.__my_home = house
        self.__my_home.registration(self)
        self.__name = self.set_name(name)
        self.__hunger = self.set_hunger(hunger)
        self.__happyness = self.set_happyness(happyness)

    def set_name(self, name):
        temp_name = ''
        for letters in name:
            if letters.isalpha():
                temp_name += letters
        if len(temp_name) < 3:
            raise NameError('Неверное имя для человека')
        else:
            return temp_name

    def set_hunger(self, hunger):
        if not isinstance(hunger, int) and not hunger > 0:
            raise ValueError('Голод должен быть целым числом больше нуля')
        else:
            return hunger

    def food_eaten(self, food):
        self.__hunger += food

    def set_happyness(self, happyness):
        if not isinstance(happyness, int) and not happyness > 0:
            raise ValueError('Щастье должно быть целым числом больше нуля')
        else:
            return happyness

    def dirty_sadness(self):
        self.__happyness -= 10

    def eat(self):
        if self.get_home().get_refrigerator() >= 30:
            self.food_eaten(30)
            self.get_home().take_from_refrigerator(30)
            print('В холодильние было более 30 едениц еды, поэтому {} плотно поел'.format(
                self.get_name()
            ))
        elif self.get_home().get_refrigerator() >= 20:
            self.food_eaten(20)
            self.get_home().take_from_refrigerator(20)
            print('В холодильние было более 20 едениц еды, поэтому {} немного поел'.format(
                self.get_name()
            ))
        elif self.get_home().get_refrigerator() >= 10:
            self.food_eaten(10)
            self.get_home().take_from_refrigerator(10)
            print('В холодильние было более 10 едениц еды, поэтому {} перекусил'.format(
                self.get_name()
            ))
        else:
            print(self.get_name(), 'хотел поесть, но еды в доме нет')
            self.get_hungry()

    def pet_animal(self):
        temp_animals_list = []
        for someone in self.get_home().get_resident_list():
            if isinstance(someone, Animal):
                temp_animals_list.append(someone)
        if len(temp_animals_list) == 0:
            print(self.get_name(), 'хотел поиграться с животным, но животных в доме нет')
        else:
            choosen_one = random.choice(temp_animals_list)
            print(self.get_name(), 'поигрался с', choosen_one.get_name(), 'и теперь чувствет себя счастливее')
            self.__happyness += 5

    def get_name(self):
        return self.__name

    def get_hunger(self):
        return self.__hunger

    def get_happyness(self):
        return self.__happyness

    def get_hungry(self):
        self.__hunger -= 10

    def get_home(self):
        return self.__my_home

    def get_happynnes(self, q):
        self.__happyness += q

    def everyday_despondency(self):
        self.__happyness -= 2


class Husband(People):

    def __init__(self, house, name, hunger, happyness):
        super(Husband, self).__init__(house, name, hunger, happyness)

    def rest(self):
        print(self.get_name(), 'затащил на пудже, теперь он намного счастливее')
        self.get_happynnes(20)
        self.get_hungry()

    def go_work(self):
        print(self.get_name(), 'пошел на работу')
        self.get_hungry()
        self.get_home().money_earned(150)


class Wife(People):

    def __init__(self, house, name, hunger, happyness):
        super(Wife, self).__init__(house, name, hunger, happyness)

    def go_for_food(self):
        if self.get_home().get_money_quantity() > 0:
            self.get_hungry()
            today_budget = self.get_home().get_money_quantity() // 3
            self.get_home().money_taken(today_budget)
            self.get_home().human_food_added(today_budget)
            print(self.get_name(), 'купила еды')
        else:
            self.get_hungry()
            print('Деньги закончились, я не могу купить еды')

    def get_food_for_animals(self):
        self.get_hungry()
        today_budget = self.get_home().get_money_quantity() // 3
        self.get_home().money_taken(today_budget)
        self.get_home().animal_food_added(today_budget)
        print(self.get_name(), 'купила еды для животных')

    def rest(self):
        self.get_hungry()
        self.get_home().money_taken(350)
        self.get_happynnes(60)
        self.get_home().new_fur_coat()
        print(self.get_name(), 'купила шубу, очень рада')

    def cleaning(self):
        self.get_hungry()
        self.get_home().cleaning()
        print(self.get_name(), 'поубиралась')


class Children(People):

    def __init__(self, house, name, hunger):
        super(Children, self).__init__(house, name, hunger)

    def inspire(self):
        self.get_hungry()
        for someone in self.get_home().get_resident_list():
            if isinstance(someone, (Wife, Husband)):
                someone.get_happynnes(1)
                print(someone.get_name(), 'кайфанул что', self.get_name(), 'растет не тиктокером и стал счастливее')

    def mischievous(self):
        self.get_hungry()
        self.get_home().piss_in_the_corner()
        print('Ребенок {name} написал в угол, уровень грязи повышен на 5'.format(
            name=self.get_name()
        ))

