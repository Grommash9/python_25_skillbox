class Animal:

    def __init__(self, home, name='Барсик', hunger=30):
        self.__name = self.set_name(name)
        self.__hunger = self.set_hunger(hunger)
        self.__my_home = self.set_home(home)
        self.__my_home.registration(self)

    def set_name(self, name):
        temp_name = ''
        for letters in name:
            if letters.isalpha():
                temp_name += letters
        if len(temp_name) < 3:
            raise NameError('Неверное имя для животного')
        else:
            return temp_name

    def set_hunger(self, hunger):
        if not isinstance(hunger, int) and not hunger > 0:
            raise ValueError('Голод животного должен быть целым числом больше нуля')
        else:
            return hunger

    def get_name(self):
        return self.__name

    def get_hunger(self):
        return self.__hunger

    def get_home(self):
        return self.__my_home

    def set_home(self, house):
        return house

    def eat(self):
        if self.get_home().get_bowl() >= 10:
            self.get_home().take_from_bowl()
            self.__hunger += 20
        else:
            print(self.get_name(), 'хотел поесть, но еды нет')
            self.__hunger -= 10

    def sleep(self):
        print(self.get_name(), 'спит целый день')
        self.__hunger -= 10

    def get_hungry(self):
        self.__hunger -= 10


class Cat(Animal):

    def __init__(self, home, name, hunger):
        super(Cat, self).__init__(home, name, hunger)

    def mischievous(self):
        self.get_hungry()
        self.get_home().destruction_of_wallpaper()
        print('Кот {name} ободрал обои, уровень грязи повышен на 5'.format(
            name=self.get_name()
        ))


class Dog(Animal):

    def __init__(self, home, name, hunger):
        super(Dog, self).__init__(home, name, hunger)

    def mischievous(self):
        self.get_hungry()
        self.get_home().piss_in_the_corner()
        print('Пес {name} написал в угол, уровень грязи повышен на 5'.format(
            name=self.get_name()
        ))

