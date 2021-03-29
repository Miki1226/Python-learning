# -*- coding: utf-8 -*-

i = 0
while i < 5:
    print(i)
    i += 1

#%%

n = 0
while True:
    print(n)
    if n >= 10:
        break
    n +=1
#%%

while True:
    name = input('Podaj swoje imie: ')
    if len(name) >=3 and name.isalpha():
        break
print('Czesc {}'.format(name))

#%%
n = 0

while n < 20:
    n = n + 1
    if n % 2 != 0:
        continue
    print(n)
    
#%%
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False
wartosc = 60

idx = 0
while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartosc:
        flaga = True
        break
    idx += 1 
if flaga:
    print('Znaleziono element {}'.format(wartosc))
    
#%%
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False
wartosc = 60

idx = 0
while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartosc:
        flaga = True
        break
    idx += 1 
if not flaga:
    lista_do_przeszukania.append(wartosc)
    
#%%
KOD_PIN = '0000'

pin = input('Podaj kod pin: ')

while pin != KOD_PIN:
    pin = input('Spróbuj ponownie jeszcze raz: ')

print('Jestes zalogowany!')
#%%
KOD_PIN = '0000'

pin = ''
counter = 0

while pin != KOD_PIN and counter < 3:
    pin = input('Wprowadź kod pin: ')
    if pin == KOD_PIN:
        print('Jestes zalogowany!')
        break
    counter += 1
else:
    print('Zbyt dużo prób logowania.')

#%%
age = 20

print(f'Mam {age} lat.')




















