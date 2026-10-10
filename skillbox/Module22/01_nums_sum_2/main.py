list_number = []

with open('numbers.txt', 'r') as whole_numbers:
    print('Содержимое файла numbers.txt:')
    for line in whole_numbers:
        print(line, end='')
        line = line.strip()
        if line:
            list_number.append(int(line))

with open('answer.txt', 'w') as sum_of_numbers:
    sum_result = sum(list_number)
    print(f'\n\nСодержимое файла answer.txt:\n{sum_result}')
    sum_of_numbers.write(str(sum_result))
