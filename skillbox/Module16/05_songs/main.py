violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

list_song = []
summ = 0
number_of_songs = int(input('Сколько песен выбрать? '))
for i in range(number_of_songs):
    song = input(f'Название {i + 1}-й песни: ')
    list_song.append(song)
for j in violator_songs:
    if j[0] in list_song:
        summ += j[1]
print(f'\nОбщее время звучания песен {round(summ, 2)} минуты')
