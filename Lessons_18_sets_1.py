print({x ** 2 for x in [1, 2, 3, 4]})       #включення множин
print({x for x in 'spam'})                  #те ж саме, що і set('spam')

print({c * 4 for c in 'spam'})              #множина накописувальних результатів виразу
print({c * 4 for c in 'spamham'})

S = {c * 4 for c in 'spam'}
print(S | {'xxxx', 'xxxx'})
print(S & {'mmmm', 'xxxx'})