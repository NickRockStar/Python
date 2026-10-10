import zipfile
from collections import Counter


def count_letters(file_path):
    with zipfile.ZipFile(file_path, 'r') as zip_file:
        # Получаем список файлов в архиве
        file_list = zip_file.namelist()

        # Инициализируем Counter для подсчета частоты букв
        letter_counter = Counter()

        # Читаем содержимое каждого файла в архиве
        for file_name in file_list:
            with zip_file.open(file_name) as file:
                # Читаем текст из файла и обновляем счетчик букв
                text = file.read().decode('utf-8')
                letter_counter.update(text.lower())  # Приводим к нижнему регистру

    return letter_counter


def print_letter_statistics(letter_counter, order='descending'):
    # Сортируем результат по частоте встречаемости букв
    sorted_stats = sorted(letter_counter.items(), key=lambda x: x[1], reverse=(order == 'descending'))

    # Выводим результат на экран
    for letter, count in sorted_stats:
        print(f'{letter}: {count}')


if __name__ == "__main__":
    archive_path = "voina-i-mir.zip"

    # Подсчет частоты букв
    letter_stats = count_letters(archive_path)

    # Вывод статистики на экран в убывающем порядке
    print_letter_statistics(letter_stats, order='descending')
