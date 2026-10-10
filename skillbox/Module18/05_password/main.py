import re

while True:
    password = input('Придумайте пароль: ')
    up_count, dig_count = 0, 0

    for i in password:
        if i.isupper():
            up_count += 1
        if i.isdigit():
            dig_count += 1
    if len(password) >= 8 and up_count >= 1 and dig_count >= 3 and re.match(r'^[a-zA-Z0-9]+$', password):
        print('Это надёжный пароль!')
        break
    elif not re.match(r'^[a-zA-Z0-9]+$', password):
        print('Для ввода пароля используется латиница.')
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
