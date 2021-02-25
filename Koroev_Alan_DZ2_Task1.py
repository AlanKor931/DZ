list_a = [5 * 3, 15 / 3, 15 // 2, 15 ** 2]
for ind in range(len(list_a)):
  mes = f'Значение : {list_a[ind]:^6}   {type(list_a[ind])}'
  print(mes)
