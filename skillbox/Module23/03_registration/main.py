with open("registrations.txt", "r", encoding='utf-8') as reg_file:
    for i_index, i_line in enumerate(reg_file):
        try:
            line_list = i_line.split()
            if len(line_list) < 3:
                raise IndexError
            else:
                for letters in line_list[0]:
                    if not letters.isalpha():
                        raise NameError
                if "@" and "." not in line_list[1]:
                    raise SyntaxError
                if line_list[2].isdigit():
                    if not 10 < int(line_list[2]) < 99:
                        raise ValueError
                else:
                    raise ValueError
        except IndexError:
            with open("registrations_bad.txt", "a", encoding="utf-8") as reg_bad_file:
                reg_bad_file.write(f"Номер строки: {i_index + 1}\n{i_line}     "
                                   f"НЕ присутствуют все три поля\n"
                                   f"______________________________________\n")
        except NameError:
            with open("registrations_bad.txt", "a", encoding="utf-8") as reg_bad_file:
                reg_bad_file.write(f"Номер строки: {i_index + 1}\n{i_line}     "
                                   f"Поле «Имя» содержит НЕ только буквы\n"
                                   f"______________________________________\n")
        except SyntaxError:
            with open("registrations_bad.txt", "a", encoding="utf-8") as reg_bad_file:
                reg_bad_file.write(f"Номер строки: {i_index + 1}\n{i_line}     "
                                   f"Поле «Имейл» НЕ содержит @ и . (точку)\n"
                                   f"______________________________________\n")
        except ValueError:
            with open("registrations_bad.txt", "a", encoding="utf-8") as reg_bad_file:
                reg_bad_file.write(f"Номер строки: {i_index + 1}\n{i_line}     "
                                   f"Поле «Возраст» НЕ является числом от 10 до 99\n"
                                   f"______________________________________\n")
        else:
            with open("registrations_good.txt", "a", encoding="utf-8") as reg_good_file:
                reg_good_file.write(f"{i_line}")
