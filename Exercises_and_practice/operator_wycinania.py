# -*- coding: utf-8 -*-

#%% 1. 
filename = 'view.jpg'
print(filename[5:])
print(filename[-3:])
#%% 2. wyciac kod bez liczb
#         0123456789101112
# -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
string = 'PKV-89415-PLN'
code = string[:3] + string[-3:]
print(code)
#%% 3.
string = '1 0 0 1 0 1'
binary = string[::2]
number = int(binary, 2)
print(f'Znaleziona liczba: {number}')
#%% 4. tekst od tylu
text = 'Learning Python'
print(text[::-1])
