# -*- coding: utf-8 -*-

# 3.
name_1 = 'Python'
name_2 = '3.8.5'

print('Uczę się języka {} w wersji {}'.format(name_1, name_2))
print(f'Uczę się języka {name_1} w wersji {name_2}')
#%% 4.
price = 199.99
print('Towar kosztuje', price)

#%% 5.

price = 69.99
print(f'Towar kosztuje {price}')
#%% 6.
# deklaracja zmiennych
price = 34.99
weight = 10
print(f'Cena: {price} PLN. Waga: {weight} kg')


# wydrukowanie tekstu do konsoli
#%% 7.

pi = 3.1415926535
print(f'Przybliżenie liczby pi: {pi:.2f}')
#%% 8.
print('-' * 40)
print('WERSJA: 1.0.1')
print('-' * 40)
#%% 9.
print('=' * 40)
print('autor: jannowak@poczta.com')
print('data: 01-01-2021')
print('=' * 40)
#%% 10.
#sep = '#'
#print(f'summer{sep}time{sep}holiday')
print('summer', 'time', 'holiday', sep=('#'))
#%% 11.
pi = 3.14
r = 5
#print(r**2)
#print(dir(r))
pole_kola = pi * r**2
print(f'Pole koła wynosi: {pole_kola} cm2')
print(f'Pole koła wynosi: {pole_kola:.1f} cm2')
#%% 12.
kwota_poczatkowa = 1000
roczna_stopa_procentowa = 0.03
okres_inwestycji = 5

wartosc_koncowa_inwestycji = kwota_poczatkowa * (1 + roczna_stopa_procentowa) ** 5
print(f'Wartość końcowa inwestycji wynosi:'
      f'{wartosc_koncowa_inwestycji:.2f} PLN')
#pv = 1000
#r = 0.03
#n = 5
#fv = pv * (1 + r) ** n
#print(f'Wartość końcowa inwestycji wynosi: {fv:.2f} PLN')
#%% 13.
#delta - b**2 - 4 * a * c
# 3x^2 - 4x + 1 = 0

delta = (4**2) - (4*3*1) 
print(f'Delta wynosi: {delta}')

a = 3
b = -4
c = 1
delta = b ** 2 - 4 * a * c
print(f'Delta wynosi: {delta}')
#%% 14. suma 10 poczatkowych wartosci ciagu arytmetyczego
a1 = 14
a10 = 50
n = 10
s10 = ((a1 + a10) / 2) * n
print(f'Suma pierwszych 10 wyrazów ciągu wynosi: {s10:.0f}')
#%% 15. suma pierwszych 6 elementow ciagu geometrycznego

a1 = 8
a2 = 8 * 2
n = 6
q = a2 / a1
s6 = a1 * ((1 - q**n) / (1 - q))
print(f'Suma pierwszych {n} wyrazów ciągu wynosi: {s6:.0f}')
#%% 16. x^2 + 5x + 4 = 0 wzory Viete'a
a = 1
b = 5
c = 4
suma = -b / a
iloczyn = c / a
print(f'x1+x2 = {suma}\nx1x2 = {iloczyn}')
#%% 17. wyznaczanie srodka odcinka 
a1 = 2
a2 = 4
b1 = -4
b2 = 6
s1 = (a1 + b1) / 2
s2 = (a2 + b2) / 2
print(f'Środek odcinka AB: ({s1}, {s2})')

#%% 18. odleglosc punktow A i B
a1 = 3
a2 = 2
b1 = -1
b2 = -1
distance = ((b1 - a1) ** 2 + (b2 - a2) ** 2)**(1/2)
print(f'Odległość punktów A i B wynosi: {distance}')
#%% 19. znajdz pierwiastki rownania kwadratowego x^2 + 5x + 4 = 0
a = 1
b = 5
c = 4
delta = b ** 2 - 4 * a * c
delta_sqrt = delta ** (1/2)
x1 = (-b - delta_sqrt) / (2 * a)
x2 = (-b + delta_sqrt) / (2 * a)
print(f'x1 = {x1}')
print(f'x2 = {x2}')
#%% 20. oblicz srednia geometryczna
x1, x2, x3, x4 = 4, 3, 4.5, 5
geo = (x1 * x2 * x3 * x4)**(1/4)
print(f'Średnia geometryczna podanych liczb: {geo:.2f}')
#%% 21. nieskonczony ciag geometryczny 1, 1/2, 1/4, 1/8, 1/16...
a1 = 1
a2 = 1/2
q = a2 / a1
S = a1 / (1 - q)
print(f'Suma ciągu wynosi: {S}')
#%% 22. oblicz odchylenie standardowe z danych 10, 11, 9 
x1, x2, x3 = 10, 11, 9
mean = (x1 + x2 + x3) / 3.0
var = ((x1 - mean)**2 + (x2 - mean)**2 + (x3 - mean)**2) / 3.0
std = var**(1/2)
print(f'Odchylenie standardowe zestawu danych wynosi: {std:.2f}')




