list = [1, 2, 3, 4, 5]
shift = int(input('Сдвиг: '))

list_with_shift = list[-shift:] + list[:-shift]

print(f'Изначальный список: {list}')
print(f'Сдвинутый список: {list_with_shift}')

# Для второго примера, нужно поменять список )))
