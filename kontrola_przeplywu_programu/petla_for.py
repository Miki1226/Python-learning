# -*- coding: utf-8 -*-
#%%
name = 'python'

for character in name:
    print(character)

#%%

name = 'python'
index = 0

for character in name:
    print(index, character)
    index = index + 1
    
#%%

for index in range(len(name)):
    print('Nr indeksu: ', index, ' Litera: ', name[index])
    
#%%

for i in enumerate(name):
    print(i) 

for index, character in enumerate(name):
    print('Nr indeksu: ',index,' Litera: ', character) 
#%%

for i in [4, 5, 6, 7, 8, 9]:
    print(i)
    
#%%
lista = [4, 5, 6, 7, 8, 9]
for i, value in enumerate(lista):
    print(i, value)

#%%
# wartosci start stop - jak 1 wartosc to jest ta na ktorej konczymy,
# jest 2 to od lewej liczby zaczynamy, a prawa nie wchodzi do range
# jak przy wycinaniu
for i in range(10, -1, -1):
    print(i) 
#%%

for i in range(10, 100, 10):
    print(i)

#%%
techs = 'java'
for i in range(len(techs)):
    print(i, techs[i])

#%%

string = 'Python Course'
for char in string[:6]:
    print(char)
#%%

string = 'Python Course'
for char in string[::-1]:
    print(char)

#%%
hashtags = '#sport#gym#fitness#'
for char in hashtags:
    print(char)
#%%
hashtags = '#sport#gym#fitness#'

for char in hashtags:
    if char not in '#':
        print(char)

#%%
# funkcja zip skraca print do elementu o krotszej dlugosci
for char, number in zip('abcde', '1234'):
    print(char, number) 
    
#%%

result = ''
for char in hashtags:
    if char not in '#':
        result = result + char
    else:
        print(result)
        result = ''
        




