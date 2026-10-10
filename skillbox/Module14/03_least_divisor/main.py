def min_div(n):
  i = 2
  while i * i <= n:
    if n % i == 0: return i
    i += 1
  return n

print('Наименьший делитель равен:', min_div(int(input('Введите число: '))))