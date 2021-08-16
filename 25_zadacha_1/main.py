from property import Apartment, Car, CountryHouse

total_tax = 0

money = int(input('Введите ваше количество денег: '))

apartment_price = int(input('Введите стоимость вашей квартиры: '))
car_price = int(input('Введите стоимость вашей машины: '))
country_house_price = int(input('Введите стоимость вашей дачи: '))

property_list = [Apartment(apartment_price), Car(car_price), CountryHouse(country_house_price)]

for items in property_list:
    print('Налог на {} составит {}'.format(
        items.name,
        items.tax_calc()
    ))
    total_tax += items.tax_calc()

print('\nСумма налога составила', total_tax)

if total_tax > money:
    print('Вам не хватает', total_tax - money, 'что бы расчитаться с налоговой')
else:
    print('Вы успешно расчитались с налоговой и у вас осталось', money - total_tax,'денег')
