# -*- coding: utf-8 -*-

for i in '0123456789':
    i = int(i)
    print(i)
    if i == 6:
        break

print('Koniec')
#%%
for i in '0123456789':
    i = int(i)
    if i == 6:
        print(i)
        break

print('Koniec')

#%%

sample = 'Python Course'
for char in sample:
    if char == ' ':
        break
    print(char)

print('Koniec')

#%%

for char in 'Kowalskijgmail.com':
    if char == '@':
        print('Adres email zweryfikowany.')
        break
else:
    print('Adres email nie jest poprawny')
    
print('Koniec')




