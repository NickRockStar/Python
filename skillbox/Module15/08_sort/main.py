namber_list = []
namber = int(input('Введите кол-во чисел для сортировки: '))
for i in range(namber):
    k = int(input('Введите число> '))
    namber_list.append(k)
print(sorted(namber_list))
