list_begin = [
    'в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5',
    'градусов'
]
#print(list_begin)
list_new = []
for i in range(len(list_begin)):
    x = True
    c = False
    number = ''
    for z in range(len(list_begin[i])):
        if 57 >= ord(list_begin[i][z]) >= 48 and x == True:
            x = True
        elif z == 0 and ord(list_begin[i][z]) == 43:
            x = True
            c = True
        else:
            x = False
    if x == True and c == True:
        number = '+{0:02d}'.format(int(list_begin[i]))
        list_new.extend(['"', number, '"'])
    elif x == True:
        number = '{0:02d}'.format(int(list_begin[i]))
        list_new.extend(['"', number, '"'])
    else:
        list_new.append(list_begin[i])
final_str = ''
print(list_new)
print()
for i in range(len(list_new)):
  final_str = final_str+list_new[i]+' '
print(final_str) 