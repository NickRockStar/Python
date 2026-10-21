# Задача 1. Доска
# Используя новые знания с циклами и оператором end, выведете на экран “доску”, которую вы делали в первом модуле
# Альтернативный вариант с вложенным циклом:
print("-" * 10)
for _ in range(4):
    for i in range(10):
        if i == 0 or i == 9:
            print("|", end="")
        else:
            print("0", end="")
    print()
print("-" * 10)

print("-" * 10)
for i in range(10):
    if i == 0 or i == 9:
        print("|", end="")
    else:
        print("0", end="")
print()
for i in range(10):
    if i == 0 or i == 9:
        print("|", end="")
    else:
        print("0", end="")
print()
for i in range(10):
    if i == 0 or i == 9:
        print("|", end="")
    else:
        print("0", end="")
print()
for i in range(10):
    if i == 0 or i == 9:
        print("|", end="")
    else:
        print("0", end="")
print()
print("-" * 10)