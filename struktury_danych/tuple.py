# -*- coding: utf-8 -*-

#uporządkowana struktura, ktorej nie mozna zmieniac, definuje sie w nawiasach 
#okrągłych, mozna wycinac ale nie mozna zmieniac tych danych

empty_tuple = tuple()
print(empty_tuple)

#%%
#sposób definiowania tupli
amazon = ('Amazon', 'USA', 'Technology', 1)
google = ('Google', 'USA', 'Technology', 2)

#%%
name_google = google[0]
#%%
data = (amazon, google)

#%%
a = ('Mikolaj', 'Kozlowski')
print(a)
#%%
#sposob definiowania tupli
imie = 'Mikolaj'
nazwisko = 'Kozlowski'

imie, nazwisko, user_id = ('Mikolaj', 'Kozlowski', '001')

#%%
# sposob rozpakowywania tupli
amazon_name, country, sector, rank = amazon

#%%
# sposob definiowania tupli
stocks = 'Amazon', 'Apple', 'IBM'
print(type(stocks))
#%%
#sposob zagniezdzania
nested = 'Europa', 'Polska', ('Warszawa', 'Krakow', 'Wroclaw')
print(nested)

#%%
a = 12
b = 14

c = b
b = a
a = c 
print(a, b)

#%%

x, y = 10, 15

x, y = y, x 
print(x, y)




