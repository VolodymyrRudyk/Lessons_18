L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
print(L1 == L2)                             #в послідовностях порядок має значення

print(set(L1) == set(L2))                   #перевірка на рівність, нейтральна до порядку

print(sorted(L1) == sorted(L2))             #схожа перевірка, но результати упорядковані

print('spam' == 'asmp', set('spam') == set('asmp'), sorted('spam') == sorted('asmp'))