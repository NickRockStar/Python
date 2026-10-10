import re

print(re.sub('(^|\s)(.)', lambda x: x[0].upper(), input('Введите строку: ').lower()))
