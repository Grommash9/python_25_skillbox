def text_check(some_text):
    for symbols in some_text:
        if not symbols.isalpha():
            raise NameError(symbols, 'не являеться буквой')
        if len(some_text) < 3:
            raise NameError('Имя или фамилия не должны быть такими короткими')
    return some_text


class Person:

    def __init__(self, name, surname, age):
        self.__name = self.set_name(name)
        self.__surname = self.set_name(surname)
        self.__age = self.set_age(age)

    def set_name(self, name):
        return text_check(name)

    def set_surname(self, surname):
        return text_check(surname)

    def set_age(self, age):
        if not 18 < int(age) < 99:
            raise ValueError('Возраст должен быть в диапазоне от 18 до 99')
        else:
            return int(age)

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age


class Employee(Person):

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def earnings(self):
        return 0


class Manager(Employee):

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def earnings(self):
        return 13000

    def info(self):
        return 'My name is {name} {surname} i am {work} in this months i will get {money}'.format(
            name=self.get_name(),
            surname=self.get_surname(),
            work='Manager',
            money=self.earnings()
        )


class Agent(Employee):

    def __init__(self, name, surname, age, sales_volume=5000):
        super().__init__(name, surname, age)
        self.__sales_volume = self.set_sales_volume(sales_volume)

    def set_sales_volume(self, sales_volume):
        if sales_volume > 0:
            return sales_volume
        else:
            raise ValueError('Обьем продаж должен быть больше нуля')

    def get_sales_volume(self):
        return self.__sales_volume

    def earnings(self):
        return 5000 + self.__sales_volume * 0.5

    def info(self):
        return 'My name is {name} {surname} i am {work} we made {sales} volume of sales' \
               ' in this months i will get {money}'.format(
            name=self.get_name(),
            surname=self.get_surname(),
            work='Agent',
            sales=self.get_sales_volume(),
            money=self.earnings()
        )


class Worker(Employee):

    def __init__(self, name, surname, age, hours_worked=20):
        super().__init__(name, surname, age)
        self.__hours_worked = self.set_hours_worked(hours_worked)

    def set_hours_worked(self, hours_worked):
        if hours_worked > 0:
            return hours_worked
        else:
            raise ValueError('Отработанные часы не могут быть отрицательным значением')

    def get_hours_worked(self):
        return self.__hours_worked

    def earnings(self):
        return 100 * self.__hours_worked

    def info(self):
        return 'My name is {name} {surname} i am {work} i worked hard for {hours} hours' \
               ' in this months i will get {money}'.format(
            name=self.get_name(),
            surname=self.get_surname(),
            work='Worker',
            hours=self.get_hours_worked(),
            money=self.earnings()
        )
