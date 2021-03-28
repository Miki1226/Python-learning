# -*- coding: utf-8 -*-

name = 'Python'

#%%

print(name[5])
print(name[::-1])

#%%

#name[start:stop] indexu 'stop' nie wycina, lewostronnie domkniety
# name[start:]
# name[:stop]
# name[start:stop:step]

print(name[1:4])
print(name[1:])
print(name[:2])

print(name[:])

#%%

print(name[-3:])
print(name[-3:-1])

#%%
full = "Python Programming"
print(full[7:])
print(full[::2])

#%%

sample = '#stop#this#flow'
print(sample[::5])

#%%

numbers = '8,9,7,4'
print(numbers[::2])

#%%

print(numbers[::-1])

#%%

name = 'kajak'
print(name[::-2])

#%%

name = 'Python'

'P' in name 
