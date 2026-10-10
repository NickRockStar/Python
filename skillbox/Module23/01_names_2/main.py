def count_characters():
    total_sum = 0
    line_number = 1
    with open('people.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if len(line) >= 3:
                total_sum += len(line)
            else:
                error_message = f"Ошибка в строке {line_number}: {line}\n"
                with open('errors.log', 'a') as error_file:
                    error_file.write(error_message)
            line_number += 1
    return total_sum


sum_of_characters = count_characters()
print(f"Общая сумма символов: {sum_of_characters}")
