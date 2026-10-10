students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict):
    lst = []
    string = ''
    for i in dict:
        lst += (dict[i]['interests'])
        string += dict[i]['surname']
    cnt = 0
    for s in string:
        cnt += 1
    return lst, cnt


pairs = []
for i in students:
    pairs += (i, students[i]['age'])

my_lst = f(students)[0]
l = f(students)[1]
print(my_lst, l)


def interests_and_length(dict):
    sum = 0
    interests = []
    for i_student, info in students.items():
        sum += len(info.get('surname'))
        interests.extend(info.get('interests'))
        return sum, set(interests)


print('Список пар «ID студента — возраст»: {pair}\n'
      'Полный список интересов всех студентов: {interests}\n'
      'Общая длина всех фамилий студентов: {len}\n'.format(
    pair=[(id, students[id]['age']) for id in students],
    interests=interests_and_length(students)[0],
    len=interests_and_length(students)[1]
))
