subsequence = []
list_numb = []

quantyNumb = int(input("Количество чисел: "))
for _ in range(quantyNumb):
    numb = int(input("Число: "))
    subsequence.append(numb)

print(f"\nПоследовательность: {subsequence}")
reversSubsequence = list(reversed(subsequence))

for _ in range(len(subsequence)):
    if subsequence == reversSubsequence:
        break
    else:
        x = subsequence.pop(0)
        list_numb.append(x)
        reversSubsequence = list(reversed(subsequence))

print(f"Нужно приписать чисел: {len(list_numb)}")
print(f"Сами числа {list(reversed(list_numb))}")
