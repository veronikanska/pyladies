# Modul pro funkci tah pocitace a strategii

from random import randrange
import util

def tah_pocitace(pole, symbol):
    if pole.count('o') > pole.count('x'):   # Symbol si pocitac voli opacny, nez ma protihrac.
        symbol = 'x'
    else:
        symbol = 'o'
    if '-' in pole:
        if symbol not in pole:     # prvni tah je nahodne cislo, ale od 1 do delky pole - 1, at pak strategie nehazi IndexError
            pozice = randrange(1, len(pole) - 1)    # Praujeme s volitelnou delkou pole
            while pole[pozice] != '-':
                pozice = randrange(1, len(pole) - 1)
        else:
            if symbol == 'o':   # Tato cast je prehozeni symbolu, se kterym pracuje strategie - ted brani souperovi a skoro nejde porazit
                znak = 'x'
            else:
                znak = 'o'
            pozice = strategie(pole, len(pole) - 1, znak)    # Strategie bere jako arg. symbol protihrace (znak) a hleda volne pozice vedle nej
    else:
        raise ValueError ('Pole je plne, nelze zapsat dalsi symbol.')
    print('Tah pocitace: ', pozice)
    return util.tah(pole, pozice, symbol)

def strategie(pole, n, symbol):     # Presunuto sem z modulu util
    'Strategie, podle ktere pocitac vybira pozici pro sve znaky vedle existujicich znaku.'    # Rekurzivne, juhu!
    try:
        if n == pole.index(symbol) and pole[pole.index(symbol) + 1] != '-' and pole[pole.index(symbol) - 1] != '-':  
            pozice = randrange(20)  
            while pole[pozice] != '-':
                pozice = randrange(20)
        else:   # Jinak jedeme odzadu pole a zkousime, jestli je na indexu symbol a jestli vedle nej je volne misto 
            if pole[n] == symbol:
                if pole[n + 1] == '-':
                    pozice = pole.index('-', n)
                elif pole[n - 1] == '-':
                    pozice = pole.index('-', n - 1)    
                else:
                    return strategie(pole, n - 1, symbol)   # Pokud neni vedle symbol volno, znova zavolame f. strategie s n - 1
            else:
                return strategie(pole, n - 1, symbol)   # Totez, pokud na indexu n neni symbol
    except IndexError:  # V krajnich pozicich by program hazel tuto chybu
        return strategie(pole, n - 1, symbol)   
    return pozice