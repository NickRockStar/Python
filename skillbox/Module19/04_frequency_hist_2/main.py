string = input('Введите текст: ')

hist = {sym: string.count(sym) for sym in string}

print('\nОригинальный словарь частот:')
for key in sorted(hist.keys()):
    print(key, ':', hist[key])

rev_hist = {val: [i_key for i_key in hist.keys() if hist[i_key] == val] for val in set(hist.values())}

print('\nИнвертированный словарь частот:')
for rev_key in rev_hist:
    print(rev_key, ':', rev_hist[rev_key])
