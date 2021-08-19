import random

from animals import Cat, Dog
from house import House
from people import Wife, Children, Husband

bakery_street_5 = House()

Cat(home=bakery_street_5, name='Кучка', hunger=30)
Dog(home=bakery_street_5, name='Жучка', hunger=30)
Husband(house=bakery_street_5, name='Колян', hunger=30, happyness=100)
Wife(house=bakery_street_5, name='Лера', hunger=30, happyness=100)
Children(house=bakery_street_5, name='ДимДимыч', hunger=30)


current_day = 0
target_day = 365


while current_day < target_day:
    print(bakery_street_5.info())
    current_day += 1
    print('     Начался день номер', current_day)
    bakery_street_5.dirt_added()
    if bakery_street_5.get_home_dirt() > 90:
        for people in bakery_street_5.get_resident_list():
            if isinstance(people, (Husband, Wife)):
                people.dirty_sadness()
                print('Сегодня все очень расстроились из-за того, что в доме грязно')
    dead_list = []
    for anyone in bakery_street_5.get_resident_list():
        if isinstance(anyone, (Husband, Wife)):
            anyone.everyday_despondency()
        if anyone.get_hunger() < 0:
            print(anyone.get_name(), 'погибает от голода')
            dead_list.append(anyone)
        if isinstance(anyone, (Wife, Husband)):
            if anyone.get_happyness() < 10:
                if not anyone in dead_list:
                    print(anyone.get_name(), 'погибает от грусти')
                    dead_list.append(anyone)

    for departed in dead_list:
        print(departed.get_name(), 'сегодня погиб')
        bakery_street_5.departed_removing(departed)
    if len(bakery_street_5.get_resident_list()) == 0:
        print('Все жильцы умерли =((')
        current_day = 365
    for alive in bakery_street_5.get_resident_list():
        if alive.get_hunger() <= 10:
            alive.eat()
            break
        if isinstance(alive, (Wife, Husband)):
            if isinstance(alive, Husband):
                if alive.get_happyness() < 20:
                    alive.rest()
                else:
                    alive.go_work()
            elif isinstance(alive, Wife):
                if alive.get_happyness() < 20:
                    if bakery_street_5.get_money_quantity() > 350:
                        alive.rest()
                    else:
                        alive.pet_animal()
                elif bakery_street_5.get_home_dirt() > 80:
                    alive.cleaning()
                elif bakery_street_5.get_refrigerator() < 40:
                    alive.go_for_food()
                elif bakery_street_5.get_bowl() < 40:
                    alive.get_food_for_animals()
        elif isinstance(alive, Children):
            if random.randint(0, 1):
                alive.inspire()
            else:
                alive.mischievous()
        elif isinstance(alive, (Cat, Dog)):
            if random.randint(0, 1):
                alive.mischievous()
            else:
                alive.sleep()

print(bakery_street_5.info())



