def partition(arr):
    pivot = arr[-1]  # Выбираем крайний правый элемент как опорный
    less = []
    equal = []
    greater = []

    for num in arr:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)

    return less, equal, greater


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    less, equal, greater = partition(arr)

    return quicksort(less) + equal + quicksort(greater)


# Пример работы вспомогательной функции
numbers = [4, 9, 2, 7, 5]
less_nums, equal_nums, greater_nums = partition(numbers)
print(less_nums, equal_nums, greater_nums)  # Вывод: [4, 2] [5] [9, 7]

# Пример работы основной функции быстрой сортировки
unsorted_list = [5, 3, 7, 2, 8, 4]
sorted_list = quicksort(unsorted_list)
print(sorted_list)  # Вывод отсортированного списка
