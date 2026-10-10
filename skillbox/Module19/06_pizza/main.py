number_orders = int(input('введите количество заказов: '))
print('введите заказы в формате: фамилия название пиццы кол-во штук')

dict = dict()

for _ in range(number_orders):
    surname, item, count = input(f'\n{_ + 1}-й заказ: ').split()
    dict[surname][item] = dict.setdefault(surname, {}).setdefault(item, 0) + int(count)

for key in sorted(dict):
    print(f'{key}:')
    for i in sorted(dict[key].items()):
        print('--', *i)
