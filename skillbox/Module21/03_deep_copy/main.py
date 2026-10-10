import copy


def find_key(struct, key, name):
    if key in struct:
        struct[key] = name
    for subsctruct in struct.values():
        if isinstance(subsctruct, dict):
            result = find_key(subsctruct, key, name)
            if result:
                return struct


clients = []

for _ in range(int(input('Сколько сайтов: '))):

    product = input('\nВведите название для нового сайта: ')
    site = {
        'html': {
            'head': {
                'title': 'Куплю/продам телефон недорого'
            },
            'body': {
                'h2': 'У нас самая низкая цена на iphone',
                'div': 'Купить',
                'p': 'продать'
            }
        }
    }

    for info in site:
        find_key(site, info, site[info])

    clients.append((f'\nСайт для {product}:',
                    f'{copy.deepcopy(site)}'))

    for client in clients:
        print('\n'.join(client))
