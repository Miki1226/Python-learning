# -*- coding: utf-8 -*-

print(2+2)

#%%

print(3 * 3)

#%%

a = 3
b = 5

c = a ** b - (a - b) / b

print(c)

#%%

print('love python')
print("love python")

#%%
print("It's the best!")

#%%

print('It\'s the best!')

#%%
print('Python 3.7')
#%%
print('Python \n3.7')
#%%
print("""Python
3.7""")
#%%
print('\tPython')
print('\t\t\tPython')
#%%

print('C:path\path\to\something\new')
print(r'C:path\path\to\something\new')
#%%
import os
os.getcwd()
#%%

print("""Instrukcja uruchamiania pliku przyklad.py:
    
    --file [nazwa pliku]
        zapisuje output do pliku
        
    --quiet
        wycisza logi w kosoli
        
Koniec.""")

#%%

text = 'I love python. '

print(text)
print(text * 3)
print('hau...' * 8)
print('*' * 30)
#%%

'Python'
print('Py' 'thon')

#%%

url = 'https://docs.cypress.io/guides/references/best-practices.html#Creating-%E2%80%9Ctiny%E2%80%9D-tests-with-a-single-assertion'
url_2 = ('https://docs.cypress.io/guides/references/best-practices.'
        'html#Creating-%E2%80%9Ctiny%E2%80%9D-tests-with-a-single-assertion')
print(url_2)

#%%
name = 'Python'
print(name + ' 3.7')
print(name, '3.7')

#%%
age = 26
imie = 'Mikołaj'

print(imie + ' ' + str(age))
print(imie, age)
print('{} ma {} lat.'.format(imie, age))

#%%

saldo = 40
saldo += 30
saldo -=10
print(saldo)

#%%
lokata = 1000
czynnik_akumulacyjny = 1 + 0.04
lokata_po_roku = lokata * czynnik_akumulacyjny
print('Wartosc lokaty po roku:', lokata_po_roku)
#%%

pixel = 150
pixel /= 255
print(pixel)
#%%

base = 2
base **= 5
print(base)
#%%

x = 103
x %= 10
print(x)
#%%

imie = 'Mikołaj '
nazwisko = 'Kozłowski'
imie += nazwisko
print(imie)
#%%

name = 'Python '
version = '3.8'
name += version
print(name)








