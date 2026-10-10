def weight_check(weight):
    while weight > 200:
        print(f'Вес контейнера превышает максимальный вес в 200 кг!')
        weight = int(input(f'Введите вес контейнера еще раз: '))
    return weight


i = 0
containers = []
number = int(input('Кол-во контейнеров: '))
for cont in range(number):
    container_weight = int(input(f'Введите вес контейнера: '))
    check1 = weight_check(container_weight)
    containers.append(check1)
    # print(containers) 

new_containers = int(input('\nВведите вес нового контейнера: '))
check2 = weight_check(new_containers)
while i < len(containers) and containers[i] >= check2:
    i += 1

containers.insert(i, check2)

print(f'\nНомер, куда встанет контейнер: {i + 1}')
print(f'Контейнеры будут стоять в таком порядке {containers}')

# Своровал код, так как ничерта не понимаю Я с этими задачами
