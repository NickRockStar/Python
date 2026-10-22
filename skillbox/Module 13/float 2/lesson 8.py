# Пример 2:
# Введите первое число: 1e-14
# Введите второе число: 1e-14
# Введите третье число: 3e-14
# False

def eqv(a, b, c):
    return abs((a + b) - c) <= 1e-15


first = float(input("Введите первое число: "))
second = float(input("Введите второе число: "))
third = float(input("Введите третье число: "))
print(eqv(first, second, third))