# Задача 2. Почта 2
# На почте немного поменялись правила: теперь в почтовом извещении нужно указывать
# фамилию, имя, страну проживания, город, улицу, номер дома и номер квартиры.
# Реализуйте функцию, которая получает все эти данные и выводит на экран.
# В программе вызовите функцию три раза с разными значениями аргументов.
# Подсказка: семь аргументов.

def print_all_info(surname, name, country, city, street, house, flat):
    print("Фамилия:", surname)
    print("Имя:", name)
    print("Страна проживания:", country)
    print("Город:", city)
    print("Улица:", street)
    print("Номер дома:", house)
    print("Номер квартиры:", flat)


# Вариант с форматированием строк (форматирование будет изучено позже)
def print_all_info_hard(surname, name, country, city, street, house, flat):
    print(f"Фамилия: {surname}\n"
          f"Имя: {name}\n"
          f"Страна проживания: {country}\n"
          f"Город: {city}\n"
          f"Улица: {street}\n"
          f"Номер дома: {house}\n"
          f"Номер квартиры: {flat}")


user_surname = input("Введите фамилию: ")
user_name = input("Введите имя: ")
user_street = input("Введите улицу: ")
user_house = input("Введите номер дома: ")

for _ in range(3):
    user_surname = input("Введите фамилию: ")
    user_name = input("Введите имя: ")
    user_country = input("Введите страну проживания: ")
    user_city = input("Введите город: ")
    user_street = input("Введите улицу: ")
    user_house = input("Введите номер дома: ")
    user_flat = input("Введите номер квартиры: ")

    print_all_info(user_surname, user_name, user_country, user_city, user_street, user_house, user_flat)