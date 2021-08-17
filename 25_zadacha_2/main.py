import random
from errors import KillError, DrunkError, CarCrashError, GluttonyError, DepressionError

day = [0]
karma = [0]
exception_list = [KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()]


def errors_saver(file_name, some_data):
    errors_file = open(file_name, 'a')
    errors_file.write(some_data + '\n')


def one_day():
    day[0] += 1
    random_number = random.randint(0, 10)
    if random_number != 5:
        carma_points_temp = random.randint(0, 7)
        print('{current_day} день: к вашим {total_carma} будет добавлено {carma} очков кармы'.format(
            current_day=day[0],
            carma=carma_points_temp,
            total_carma=karma[0]
        ))
        return carma_points_temp
    else:
        errors_saver('karma.log', '{current_day} день: {error}'.format(
            current_day=day[0],
            error=random.choice(exception_list).text
        ))
        return 0


def errors_file_cleaner(file_name):
    errors_file = open(file_name, 'w')
    errors_file.write('')


errors_file_cleaner('karma.log')

while karma[0] < 500:
    karma[0] += one_day()

print('Вы успешно набрали 500 кармы')
