from math import pi

def obsah_elipsy(a, b):
    'Vypocita obsah elipsy, a a  jsou osy elipsy'
    return a * b * pi

def obsah_valce(a, b, vyska):
    'Vypocita obsa eliptickeho valce'
    return a * b * pi * vyska

osa_1 = float(input('Zadej delku osy 1: '))
osa_2 = float(input('Zadej delku osy 2: '))
vyska = float(input('Zadej vysku valce: '))

print(obsah_elipsy(osa_1, osa_2))
print(obsah_valce(osa_1, osa_2, vyska))