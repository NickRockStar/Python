first_line = input('Первая строка: ')
second_line = input('Вторая строка: ')
sum = 0
step = 1
test = False
while step < len(first_line):
    variable = first_line[-step:] + first_line[:-step]
    sum += 1
    if variable == second_line:
        test = True
        break
    step += 1
if test == True:
    print(f'Первая строка получается из второй со сдвигом {sum}.')
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
