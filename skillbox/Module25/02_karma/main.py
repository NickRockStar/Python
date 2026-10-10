import random


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day():
    current_karma = random.randint(1, 7)
    number = random.randint(1, 10)
    if number == 10:
        try:
            error = random.choice([DepressionError, DrunkError, GluttonyError, CarCrashError, KillError])
            raise error
        except (DepressionError, DrunkError, GluttonyError, CarCrashError, KillError):
            with open('karma.log', 'a') as karma_file:
                karma_file.write(str(error) + '\n')

    return current_karma


enlightenment_points = 500
balance = 0
day = 1
while True:
    if balance >= enlightenment_points:
        print('Вы достигли просвещения!')
        break
    print(f'День {day}')
    day += 1
    balance += one_day()
    print(f'Уровень кармы {balance}')
