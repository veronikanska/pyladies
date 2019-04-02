from random import randrange
pocitac = randrange(5)

if pocitac == 0:      # uprava podle ukolu c. 8, aby si pocitac taky zahral
    tah_pocitace = 'papir'
elif pocitac == 1:
    tah_pocitace = 'nuzky'
elif pocitac == 2:
    tah_pocitace = 'spok'
elif pocitac == 3:
    tah_pocitace = 'jester'
elif pocitac == 4:
    tah_pocitace = 'kamen' 

tah_cloveka = input('kamen, nuzky,  papir, jester nebo spok? ')

print('tah pocitace: ', tah_pocitace)    # vypise tah pocitace, aby se dalo hned zkontrolovat, jestli nepodvadi :)

if tah_cloveka == 'kamen':             # tahu cloveka se priradi cislo, podle ktereho se bude vzhodnocovat vzsledek klani (obdobne hodnoty jako promenne 'pocitac')
    clovek = 4
elif tah_cloveka == 'jester':
    clovek = 3
elif tah_cloveka == 'spok':
    clovek = 2
elif tah_cloveka == 'nuzky':
    clovek = 1
elif tah_cloveka == 'papir':
    clovek = 0
else:
    print('Nerozumím.')

if ((clovek == 0 or clovek == 2 or clovek == 4) and (pocitac == 0 or pocitac == 2 or pocitac == 4)) or ((clovek == 1 or clovek == 3) and (pocitac == 1 or pocitac == 3)):
    if clovek > pocitac:
        print('Počítač vyhrál.')
    elif clovek == pocitac:
        print('Plichta')
    else:
        print('Pavel vyhral!.')        # Tato podminka osetruje pripady, kdy vyhrava mensi hodnota promenne clovek nebo pocitac nad tou vetsi
elif clovek == pocitac:
    print('Plichta')
elif clovek < pocitac:
    print('Počítač vyhrál.')
elif clovek > pocitac:
    print('Pavel vyhral!.')
