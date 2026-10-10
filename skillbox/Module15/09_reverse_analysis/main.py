numbers = [int(number) for number in input('Напишите числа, через пробел: ').split()]
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] % 2 == 0:
        print(numbers[i], end=' ')

# Список чисел для работы (итоговый алгоритм проверьте на разных списках, придуманных самостоятельно):
# numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]
