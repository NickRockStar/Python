nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [num3 for num in nice_list for num2 in num for num3 in num2]

print(new_list)
