original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result = list(zip(original_list[::2], original_list[1::2]))
print('Оригинальный список:', original_list)
print(f"Новый список: {result} ")
