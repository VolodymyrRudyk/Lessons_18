engineers = {'bob', 'sue', 'ann', 'vic'}
manegers = {'tom', 'sue'}

print('bob' in engineers)                               #чи є боб інженером?
print(engineers & manegers)                             #хто одночасно інженер і менеджер?
print(engineers | manegers)                             #всі співробітники в двох категоріях
print(engineers - manegers)                             #інженери які не є менеджерами
print(manegers - engineers)                             #менеджери які не є інженерами
print(engineers > manegers)                             #чи всі менеджери є інженерами?(надмножинність)
print({'bob', 'sue'} < engineers)                       #чи є ці два співробітники інженерами(підмножинність)
print((manegers | engineers) > engineers)               #всі співробітники - надмножинність менеджерів?
print(manegers ^ engineers)                             #хто знаходиться в одній категорії, но не в двох?
print((manegers | engineers) - (manegers ^ engineers))  #пересічення!