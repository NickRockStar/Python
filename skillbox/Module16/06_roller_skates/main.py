skate = []
people = []

skate_count = int(input('Кол-во коньков: '))

for i in range(skate_count):
    print('Размер', i + 1, '- й пары: ', end=' ')
    skate_size = int(input())
    skate.append(skate_size)

people_count = int(input('\nКол-во людей: '))

for j in range(people_count):
    print('Размер ноги', j + 1, '- го человека: ', end=' ')
    foot_size = int(input())
    people.append(foot_size)

pairs = 0

for i_people in people:
    for i_skate in skate:
        if i_people == i_skate:
            pairs += 1
            skate.remove(i_skate)

print('Наибольшее кол-во людей, которые могут взять коньки:', pairs)
