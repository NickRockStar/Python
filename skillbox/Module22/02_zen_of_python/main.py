file = open("zen.txt", "r")

reverse_str = file.readlines()
reverse_str.reverse()
print(''.join(reverse_str).strip('\n'))

file.close()
