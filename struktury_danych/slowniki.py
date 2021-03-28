# -*- coding: utf-8 -*-

empty_dict = dict()
print(empty_dict)

d = {}
print(type(d))

#zbiory definuje sie set
e = set()
print(type(e))

# klucze nie moga sie w slowniku powtarzac
#w slowniku uporzadkowanie nie jest istotne, i nie jest uporzadkowane

pol_to_eng = {'jeden':'one', 'dwa':'two', 'trzy': 'three'}

name_to_digit = {'Jeden':1, 'dwa':2, 'trzy':3}

#%%

len(name_to_digit)

#dict = {'key1'='value1,'key2'='value2'...}

#%%
#dodawanie kolejnych danych, nie trzeba sie martwic na ktore miejsce, bo
#nie ma uporzadkowania

pol_to_eng['cztery'] = 'four'

#%%

pol_to_eng.clear()

#%%

pol_to_eng_copied = pol_to_eng.copy()
#%%
#wydobycie kluczy ze slownika
pol_to_eng.keys()
#przekonwertowanie kluczy slownika na liste
list(pol_to_eng.keys())

#%%
#wydobycie wartosci ze slownika
pol_to_eng.values()
#przekonwertowanie wartosci slownika na liste
list(pol_to_eng.values())

#%%
# dostaje liste tupli, nie moge zmienic pary "klucz - wartosc"
pol_to_eng.items()

list(pol_to_eng.items())

#%%

pol_to_eng['jeden']
#pol_to_eng['zero']
#%% 
#drugi argument podaje to, co jezeli nie ma danego klucza w slowniku
pol_to_eng.get('zero', 'NaN')

#%%
# wartosc usuwana ze struktury
#pol_to_eng.pop('dwa')
pol_to_eng.popitem()
#%%
#aktualizacje danych ktore moga zmieniac sie w czasie
pol_to_eng.update({'jeden':1})
