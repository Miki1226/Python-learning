# -*- coding: utf-8 -*-

val_1 = True
val_2 = False

#%%

print(val_1)
print(type(val_1))

#%%

# koniunkcja 2 wartosci prawdziwych bedzie prawda, czyli 2 musza sie wydarzyc
#zeby bylo True
True and True
True and False
False and True
False and False

#%% alternatywa - 1 wartosci musi byc prawdziwy by bylo true
True or True
True or False
False or True
False or False

#%% negacja

True
not True
False
not False

#%%
# kazdy tekst ktory zawiera choc 1 znak zwroci wartosc True
bool('python')
#pusty string zwraca False
bool('')
#jako liczba 0 zwraca False
bool(0.0)
# tu jest jako tekst
bool('0.0')
#pusty slownik, zbior, lista i tupla zwracaja False
bool({})
bool(set())
bool(list())
bool(tuple())
#bedzie True, bo jest cos zawarte w slowniku
bool({'key':'val'})



