string = input('Введите строку: ')

i_h = [i for i in range(len(string)) if string[i] == 'h']

print('Развёрнутая последовательность между первым и последним h:', string[i_h[len(i_h) - 1] - 1:i_h[0]:-1])
