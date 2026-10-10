def sum(*args, total=0):
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
        elif isinstance(arg, list):
            total += sum(*arg)
        else:
            raise TypeError("unsupported argument type")
    return total


print('sum([[1, 2, [3]], [1], 3])')
print('Ответ в консоли: ', sum([[1, 2, [3]], [1], 3]))
print('sum(1, 2, 3, 4, 5)')
print('Ответ в консоли: ', sum(1, 2, 3, 4, 5))
