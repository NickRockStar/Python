films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо',
         'Отступники', 'Деревня']
favourites_films = []
films_number = int(input('Сколько фильмов хотите добавить? '))

for i in range(1, films_number + 1):
    print(i, 'фильм: ', end='')
    movie = input()
while movie not in films:
    print('Нет такого фильма!')
    movie = input('Выберете другой фильм: ')
else:
    favourites_films.append(movie)

print('Список любимых фильмов: ', favourites_films)
# Не пойму, почему он добавляет тольк последний фильм
