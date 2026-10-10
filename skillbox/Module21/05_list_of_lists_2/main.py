nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def common_list(lst):
    if not lst:
        return []
    if isinstance(lst[-1], list):
        return common_list(lst[:-1]) + common_list(lst[-1])
    else:
        return common_list(lst[:-1]) + [lst[-1]]


print('Ответ: ', common_list(nice_list))
