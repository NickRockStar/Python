import os

while True:
    try:
        name_user = input('\nВведите ваше имя: ').title()
        if not name_user.isalpha():
            raise NameError
    except NameError:
        print('\nОшибка при вводе имени')
    name_file = os.path.join('chat_history.txt')
    with open(name_file, 'a', encoding='utf8') as file_user:
        try:
            what_to_do = int(input('Выберите действие(число):\n'
                                   'Посмотреть текущий текст чата - 1\n'
                                   'Отправить сообщение - 2\n'))
            if what_to_do == 1:
                if os.stat(name_file).st_size == 0:
                    raise FileNotFoundError('Чат пуст начните общений')
                else:
                    print('Сообщения чата:')
                    with open(name_file, 'r', encoding='utf8') as file_user:
                        for line in file_user:
                            print(line.rstrip())
            elif what_to_do == 2:
                message = input('Введите сообщение: ')
                if isinstance(message, str):
                    file_user.write(f'{name_user}: {message}\n')
                else:
                    raise ValueError('Ошибка ввода сообщения')
            else:
                raise Exception('Такое действие отсуствует.')
        except (FileNotFoundError, ValueError, Exception) as exc:
            print(exc)
