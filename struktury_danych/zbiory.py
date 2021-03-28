# -*- coding: utf-8 -*-

empty_set = set()

print(type(empty_set))

#%%

techs = {'python', 'java', 'c++', 'sql'}
print(techs)
print(type(techs))
print(len(techs))
#%%

set('python')
set('aaaaaaale')

#%%

'python' in techs
'go' in techs

#%%

print(dir(set))
#%%

techs.add('sas')

#%%

techs.remove('sas')

#%% 
# wyrywa dowolny element, zwraca i usuwa z danego zbioru

techs.pop()
#%%
# usuwa wszystkie elementy zbioru

techs.clear()

#%%

A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 6, 7, 8, 9}
C = {5, 6}
# C jest podzbiorem zbioru A, czyli zawiera elementy, ktore sa tez w zbiorze A
C.issubset(A)
C.issubset({5, 7})
# A jest nadzbiorem zbioru C, czyli A zawiera wszystkie elementy zbioru C
A.issuperset(C)
# suma zbiorow
A.union(B)
# przeciecie, czyli zwraca wartosci ktore wystepuja w obydwu zbiorach
A.intersection(B)
#roznica symetryczna, powstaje z 2 zbiorow, wycina elementy ktore sa w obydwu
#zbiorach i tworzy nowy zbior z pozostalych elementow
A.symmetric_difference(B)
#kopiowanie zbioru
D = A.copy()
print(D)
