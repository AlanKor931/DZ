duration = input('Введите время в секундах :')
dur = int(duration)
h = dur // 3600
m = dur % 3600 // 60
s = dur % 60
print('Время  ', end='')
print(h, m, s, sep=':')
print()
