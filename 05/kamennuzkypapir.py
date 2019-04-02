# Hra kamen, nuzky, papir - vyuziva funkce, pocita skore, ukonci se az prikazem konec

from random import randrange

# Nejdrive vytvoreni tri uzitecnych funkci
def tah_pocitace():
    'Vygeneruje nahodne tah pocitace - kamen, nuzky nebo papir'
    cislo = randrange(3)
    if cislo == 0:
        return 'kamen'
    elif cislo == 1:
        return 'nuzky'
    elif cislo == 2:
        return 'papir'

def tah_cloveka():
    'Vrati tah cloveka - kamen, nuzky nebo papir.'
    a = input('\nKamen, nuzky, nebo papir? ')
    while a != 'kamen' and a != 'nuzky' and a != 'papir':
        print('Nerozumim')
        a = input('\nKamen, nuzky, nebo papir? ')
    else:
        return a
        
        
def vyhodnoceni(x, y):
    'Porovna a vyhodnoti tah x a y'
    if x == y:
        return None
    elif (x == 'kamen' and y == 'papir') or (x == 'nuzky' and y == 'kamen') or (x == 'papir' and y == 'nuzky'):
        return False
    elif (x == 'kamen' and y == 'nuzky') or (x == 'nuzky' and y == 'papir') or (x == 'papir' and y == 'kamen'):
        return True

odpoved = None
skore_clovek = 0
skore_pocitac = 0

# cyklus definujici prubeh hry. Promennou odpoved a to, jak to cele funguje bych chtela napsat lepe, ale nevim..
while odpoved != 'konec':
    pocitac = tah_pocitace()
    clovek = tah_cloveka()
    print('Tah pocitace: ', pocitac)
    if vyhodnoceni(clovek, pocitac) == True:
        skore_clovek = skore_clovek + 1
    elif vyhodnoceni(clovek, pocitac) == False:
        skore_pocitac = skore_pocitac + 1
    else:
        None
    print('Skore clovek: pocitac je {}:{}.'.format(skore_clovek, skore_pocitac))
    odpoved = input('Chces-li ukoncit hru, napis konec. Jinak napis cokoliv a pokracujeme: ')

if skore_clovek > skore_pocitac:
    vitez = 'clovek'
elif skore_pocitac > skore_clovek:
    vitez = 'poctac'
else:
    vitez = 'nikdo'

print('\nKonec hry. Vyhral {}'.format(vitez))