# -*- coding: utf-8 -*-

text = 'Witaj na kursie Pythona. \n Python jest wspanialy'

print(text)

#%%
print(dir(text))

help(str.count)

#%%
# zwraca tekst z duza litera tylko na poczatku tekstu
print(text.capitalize())
#%%
# zwraca tekst z duzymi literami na poczatku kazdego wyrazu
print(text.title())

#%%
# liczy ile wyrazow, czy ciagow znakow jest w tekscie
text.count('Python')

#%%

print(text.startswith('kurs'))
'python'.startswith('py')

print(text.endswith('y.'))

#%%
'sample.py'.endswith('.py')
'image.png'.endswith('.png')

#%%

text.find('Python')
text[text.find('Python'):]

hashtags = '#sport#gym'
idx = hashtags.find('#')
hashtags[:idx]

#%%
# znaki sa alfanumeryczne
'pawel545'.isalnum()

#%%
# czy znaki sa cyframi

'434334fdf'.isdigit()
#%%

'pyThon'.islower()
'MIKOLAJ'.isupper()
#%%

'  '.join(['python', '3.7'])
'#'.join(['sport', 'gym', 'fit'])
','.join(['1', '2', '3', '4'])

#%%

'#good#time#mood'.replace('#', ' ')

#%%

'column name'.replace(' ', '_')

#%%

'     python     '.strip()
'     python     '.rstrip()
'     python     '.lstrip()

#%%
'1,2,3,4,5'.split(',')

'python java php sql sas'.split()

'#gym#fit#mood'.split('#')

#%%

'12'.zfill(5)

'1'.zfill(10)
