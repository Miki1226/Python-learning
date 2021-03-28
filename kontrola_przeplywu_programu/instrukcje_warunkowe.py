# -*- coding: utf-8 -*-

version = 3.8

print(version)
#%%

version > 3
version <= 3

#%%

number = 1200
number > 1000


number == 1200
number == 1000

number != 1200
number != 1199

#%% 4 spacje wciecia przed instrukcja

# if [warunek]:
    # [instrukcje]
    
    #%%

if 8 > 10:
    print('Tak')
    
#%%

a = 51
if a > 10:
    print('a > 10')
else:
    print('a <= 10') 
    
#%%

age = 18

if age < 18:
    print('Nie masz uprawnień')
else:
    print('Dostęp przyznany')

#%%

age = 18

if age == 18:
    print('Masz 18 lat')
elif age < 18:
    print('Nie masz uprawnień')
else:
    print('Dostęp przyznany.')
    
#%%
age = int(input('Podaj swoj wiek: '))

if age == 18:
    print('Masz 18 lat')
elif age < 18:
    print('Nie masz uprawnień')
elif age > 18:
    print('Dostęp przyznany.')

#%%

print('Program uruchomiony...')
print("""Włam się do systemu, zgadując dwucyfrowy pin.
Numer pin składa się z cyfr:0, 1, 2. """)

pin = int(input('Wprowadź numer pin: '))

if pin == 21:
    print('Brawo! Złamałes system.')
elif pin == 20:
    print('Byłes blisko!')
else:
    print('Nie zgadłes')

#%%

string = ' '
if string:
    print('To nie jest pusty ciag znakow')
else:
    print('Pusty ciag znakow')
#%%

number = -1

if number:
    print('Liczba inna od 0')
else: 
    print('Zeroo')

#%%

default_flag = True

if default_flag:
    print('Doszło do defaultu')
else:
    print('Nie doszło')
    
#%%

default_flag = True

if not default_flag:
    print('Nie doszło')
else:
    print('Doszło do defaultu')
    
#%%

saldo = -10000
klient_zweryfikowany = True

if saldo > 0 and klient_zweryfikowany:
    print('Możesz wypłacić gotówkę')
else:
    print('Nie możesz wypłacić gotówki')
    
#%%

saldo = 10000
klient_zweryfikowany = True

amount = int(input('Ile chcesz wypłacić gotówki: '))

if saldo > 0 and klient_zweryfikowany and saldo >= amount:
    print('Możesz wypłacić gotówkę')
else:
    print('Nie możesz wypłacić gotówki.' 
          ' Brak wystarczajacej kwoty {} złotych'.format(abs(saldo - amount)))

#%%

name = 'Python'

if 'p' in name:
    print('Znaleziono p')
else:
    print('Nie znaleziono p')
    
    #%%
    
tech = 'sas'

if tech == 'python':
    flag = 'Dobry wybor'
else:
    flag = 'Poszuka czegos lepszego'

#%%

# x if [warunek] else y
tech = 'sas'
'Dobry wybor' if tech == 'python' else 'Poszukaj czegos lepszego'
