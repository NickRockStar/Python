class Property:

    def __init__(self, worth): self.worth = worth

    def tax_calculation(self): pass


class Apartment(Property):

    def __init__(self, worth): super().__init__(worth)

    def tax_calculation(self): return self.worth / 1000


class Car(Property):

    def __init__(self, worth): super().__init__(worth)

    def tax_calculation(self): return self.worth / 200


class CountryHouse(Property):

    def __init__(self, worth): super().__init__(worth)

    def tax_calculation(self): return self.worth / 500


def program_interface():
    amount_of_money = float(input('Пожалуйста, укажите имеющуюся у Вас сумму денежных средств: '))

    properties = [
        (Apartment, 'квартиры'),
        (Car, 'автомобиля'),
        (CountryHouse, 'загородного дома')
    ]

    for prop_type, prop_name in properties:
        worth = float(input(f'\nВведите стоимость {prop_name}: '))
        prop = prop_type(worth)
        tax = prop.tax_calculation()
        print(f'Налог составляет: {tax}')
        if tax <= amount_of_money:
            amount_of_money -= tax
            print(f'Осталось денег: {amount_of_money}')
        else:
            difference = amount_of_money - tax
            print(f'Не хватает денег: {abs(difference)}. Придется поработать!')


program_interface()
