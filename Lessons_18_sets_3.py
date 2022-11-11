print(set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6]))         #знайти різницю у списках
print(set('abcdef') - set('abdghij'))                   #знайти різницю у строках
print(set('spam') - set(['h', 'a', 'm']))               #знайти різницю, різні типи
print(set(dir(bytes)) - set(dir(bytearray)))            #в bytes, но не в bytearrey
print(set(dir(bytearray)) - set(dir(bytes)))