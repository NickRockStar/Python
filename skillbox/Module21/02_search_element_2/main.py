def find_key(struct, key, depth):
    if depth >= 1:
        if key in struct:
            return struct[key]
    else:
        return None
    for subsctruct in struct.values():
        if isinstance(subsctruct, dict):
            result = find_key(subsctruct, key, depth - 1)
            if result:
                break
    else:
        result = None
    return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

while True:
    user_key = input('\nВведите искомый ключ: ')
    ask = input('Хотите ввести максимальную глудину ? Y/N: ').lower()
    some_depth = 1000000
    if ask == 'y':
        max_depth = int(input('Введите максимальную глубину: '))
        value = find_key(site, user_key, max_depth)
    else:
        value = find_key(site, user_key, some_depth)
    print(f'Значение ключа: {value}')
