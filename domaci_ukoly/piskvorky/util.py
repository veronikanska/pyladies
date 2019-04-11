from random import randrange

def tah(pole, pozice, symbol):
    'Vrati herni pole se symbolem umistenym na danou pozici'
    seznam = list(pole)     # Zapis do retezce pres seznam
    seznam[pozice] = symbol
    pole = ''.join(seznam)
    return pole

def strategie(pole, n):
    'Strategie, podle ktere pocitac vybira pozici pro sve znaky vedle svych existujicich znaku.'    # Rekurzivne, juhu!
    try:
        if n == pole.index('o') and pole[pole.index('o') + 1] != '-' and pole[pole.index('o') - 1] != '-':  
            pozice = randrange(20)  
            while pole[pozice] != '-':
                pozice = randrange(20)
        else:   # Jinak jedeme odzadu pole a zkousime, jestli je na indexu 'o' a jestli vedle nej je volne misto 
            if pole[n] == 'o':
                if pole[n + 1] == '-':
                    pozice = pole.index('-', n)
                elif pole[n - 1] == '-':
                    pozice = pole.index('-', n - 1)    
                else:
                    return strategie(pole, n - 1)   # Pokud neni vedle 'o' volno, znova zavolame f. strategie s n - 1
            else:
                return strategie(pole, n - 1)   # Totez, pokud na indexu n neni 'o'
    except IndexError:
        return strategie(pole, n - 1)
    return pozice