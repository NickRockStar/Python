text = input('Введите строку: ').split()

clone = [len(i) for i in text]
biggest = text[clone.index(max(clone))]

print('Самое длинное слово: {}'.format(biggest))
print('Длина этого слова: {}'.format(len(biggest)))
