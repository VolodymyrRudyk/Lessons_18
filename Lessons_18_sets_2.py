L = [1, 2, 1, 3, 2, 4, 5]
print(set(L))

L = list(set(L))                                        #видалення дублікатів
print(L)

print(list(set(['yy', 'cc', 'aa', 'xx', 'dd', 'aa'])))  #но порядок може змінитися