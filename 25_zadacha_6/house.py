class House:

    def __init__(self, nightstand=100, refrigerator=50, food_for_animals=30, dirt=0, resident_list=[]):
        self.__nightstand = nightstand
        self.__refrigerator = refrigerator
        self.__food_for_animals = food_for_animals
        self.__dirt = dirt
        self.__resident_list = resident_list
        self.__wardrobe = 0
        self.final_results = {
            'total_money': 0,
            'total_human_food_buy': 0,
            'total_animal_food_buy': 0,
            'total_fur_coat': 0
            }

    def new_fur_coat(self):
        self.__wardrobe += 1
        self.final_results['total_fur_coat'] += 1

    def destruction_of_wallpaper(self):
        self.__dirt -= 5

    def piss_in_the_corner(self):
        self.__dirt -= 5

    def take_from_bowl(self):
        self.__food_for_animals -= 10

    def take_from_refrigerator(self, food):
        self.__refrigerator -= food

    def human_food_added(self, food):
        self.__refrigerator += food
        self.final_results['total_human_food_buy'] += food

    def animal_food_added(self, food):
        self.__food_for_animals += food
        self.final_results['total_animal_food_buy'] += food

    def money_earned(self, amount):
        self.__nightstand += amount
        self.final_results['total_money'] += amount

    def money_taken(self, amount):
        self.__nightstand -= amount

    def registration(self, some_human):
        self.__resident_list.append(some_human)

    def cleaning(self):
        self.__dirt -= 100

    def dirt_added(self):
        self.__dirt += 5

    def departed_removing(self, someone):
        self.__resident_list.remove(someone)

    def get_home_dirt(self):
        return self.__dirt

    def get_resident_list(self):
        return self.__resident_list

    def get_refrigerator(self):
        return self.__refrigerator

    def get_bowl(self):
        return self.__food_for_animals

    def get_money_quantity(self):
        return self.__nightstand

    def get_wardrobe(self):
        return self.__wardrobe

    def info(self):
        return '???????????? ?? ???????? ??????????: {money}, ?????? ?????? ??????????: {food}, ?????? ?????? ????????????????: {anymal_food}, ??????????: {dirt} ?????????? ?????????????? ??????: {furs}'.format(
            money=self.get_money_quantity(),
            food=self.get_refrigerator(),
            anymal_food=self.get_bowl(),
            dirt=self.get_home_dirt(),
            furs=self.get_wardrobe()
        )




