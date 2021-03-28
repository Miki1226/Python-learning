# -*- coding: utf-8 -*-

techs = []
print(techs)

techs.append('python')
print(techs)
#%%
techs.append('java')
#%%
#tak dodaje zagniezdzona liste
techs.append(['hadoop', 'spark'])
print(techs)

#%%
# to rozszerza liste
techs.extend(['sql', 'sas'])
print(techs)

#%%
# wymaga 2 argumentow, pierwszy to index na ktore miejsce wstawic i string
techs.insert(0, 'go')
print(techs)

#%%
#usuwa ostatni element z listy 
print(techs)
print(techs.pop())
print(techs)

#%%

techs = ['python', 'java', 'sql', 'php', 'r']
print(techs.pop(3))
print(techs)
#%%
techs = ['python', 'java', 'sql', 'php', 'r']

print(techs.index('java'))
#%%

techs = ['python', 'java', 'sql', 'php', 'r', 'angular']
techs.count('python')
techs.count('ruby')

#%%
techs = ['python', 'java', 'sql', 'php', 'r', 'angular']
techs.sort()
techs.sort(reverse=True)
print(techs)
#%%

techs = ['python', 'java', 'sql', 'php', 'r', 'angular']

#print(techs[::-1])
techs.reverse()
print(techs)

#%%

techs[1] = 'c++'
print(techs)
techs_2 = techs.copy()
print(techs_2)