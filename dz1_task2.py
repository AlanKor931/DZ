i = 1
list_value = []
new_list = []
while i <= 1000:
  if i % 2 != 0:
    list_value.append(i ** 3)
  i += 1
sum_item = 0
for ind in range(len(list_value)):
  dec_plc = list_value[ind] // 10
  sum_plc = list_value[ind] % 10 
  new_list.append(list_value[ind] + 17)
  while dec_plc > 0 :
    sum_plc = sum_plc + dec_plc %10
    dec_plc = dec_plc // 10
  cnd = sum_plc % 7
  if cnd == 0:
    sum_item += list_value[ind]
print()
print('Сумма элементов списка соответствующих условию = ',sum_item)
for ind in range (len(new_list)):
  dec_plc = new_list[ind] // 10
  sum_plc = new_list[ind] % 10
  while dec_plc > 0 :
    sum_plc = sum_plc + dec_plc % 10
    dec_plc = dec_plc // 10
  cnd = sum_plc % 7 
  if cnd == 0 :
    sum_item += new_list[ind]   
print()
print ('Сумма элементов нового списка соответствующих условию = ',sum_item)



  
  
