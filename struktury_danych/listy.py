# -*- coding: utf-8 -*-

#listy sa zmienne, uporzadkowana struktura elementow, moga byc elementami 
#zduplikowanymi, ktore byc zmienne

empty_list = list()
print(empty_list)

#%%

techs = ['python', 'java', 'c++', 'go', 'sql']
techs[0] = 'python 3.8'
print(techs)

#%%

numbers = [3, 5, 3, 5, 23]
print(numbers)
#%%

mixed = ['python', 3.8, 4, True]
print(mixed)
#%%

empty = []
nested = [[1, 2, [3, 'sql']], ['python', 'java', 'go'], 3]

#%%

first = ['mleko', 'ziemniaki', 'makaron']
second = ['woda', 'jajka']
bucket = [first, second]
len(bucket)
#%%

techs = ['python', 'java', 'c++', 'go', 'sql']
techs += ['javascript']
print(techs)

#%%
print(dir(list))



