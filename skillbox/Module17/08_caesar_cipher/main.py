def get_index(smb, to_right, lst):
    index = lst.index(smb)
    if index + to_right > len(lst) - 1:
        index = index + to_right - len(lst)
    else:
        index += to_right
    return index


text = input('Введите сообщение: ').lower()

shift = int(input('Введите сдвиг: '))

ascii_en = [chr(i) for i in range(ord('a'), ord('z') + 1)]

ascii_ru = [chr(i) for i in range(ord('а'), ord('я') + 1)]

encrypted_string = ''

for symbol in text:

    if symbol in ascii_ru:
        encrypted_string += ascii_ru[get_index(symbol, shift, ascii_ru)]

    elif symbol in ascii_en:
        encrypted_string += ascii_en[get_index(symbol, shift, ascii_en)]
    else:
        encrypted_string += symbol
print('Зашифрованное сообщение: ', encrypted_string)
