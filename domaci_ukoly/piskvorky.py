# 1-D piskvorky, hraji se na radku s dvaceti policky. 
# Hrac clovek ma krizky, pocitac ma kolecka. Kdo da tri sve symboly vedle sebe, vyhral.

from random import randrange

def vyhodnot(pole):
    'Dostane retezec 20 policek piskvorek a vrati retezec podle stavu hry.'
    if 'xxx' in pole:    # vyhral x
        return 'x'
    elif 'ooo' in pole:    # vyhral o
        return 'o'
    elif '-' not in pole:   # remiza
        return '!'
    else:   # hra neskoncila
        return '-'

def tah(pole, pozice, symbol):
    'Vrati herni pole se symbolem umistenym na danou pozici'
    seznam = list(pole)     # Zapis do retezce pres seznam
    seznam[pozice] = symbol
    pole = ''.join(seznam)
    return pole

def tah_hrace(pole):
    'Zapise do pole tah hrace - vrati pole se zapsanym tahem.'
    symbol = 'x'
    while True:
        vklad = input('Zadej pozici, na kterou chces hrat: ')
        try:
            pozice = int(vklad)
        except ValueError:
            print('To neni cislo, zkus to znova.')
            continue
        if pozice not in range(0,20):
            print('Zadej cele cislo od 0 do 19: ')
            continue
        elif pole[pozice] != '-':
            print('Pozice je obsazena, vyber si jinou: ')
            continue
        else:
            break
    return tah(pole, pozice, symbol)
    
def nahodna_pozice(pole):
    'Vrati nahodnou neobsazenou pozici v poli'
    pozice = randrange(20)  
    while pole[pozice] != '-':
        pozice = randrange(20)
    return pozice

def strategie(pole, n):
    'Strategie, podle ktere pocitac vybira pozici pro sve znaky vedle svych existujicich znaku.'    # Rekurzivne, juhu!
    if n == pole.index('o') and pole[pole.index('o') + 1] != '-' and pole[pole.index('o') - 1] != '-':  
        pozice = nahodna_pozice(pole)
    else:   # Jinak jedeme odzadu pole a zkousime, jestli je na indexu 'o' a jestli vedle nej je volne misto 
        if pole[n] == 'o':
            try:
                if pole[n + 1] == '-':
                    pozice = pole.index('-', n)
                elif pole[n - 1] == '-':
                    pozice = pole.index('-', n - 1)    
                else:
                    return strategie(pole, n - 1)   # Pokud neni vedle 'o' volno, znova zavolame f. strategie s n - 1
            except IndexError:
                pozice = nahodna_pozice(pole)
        else:
            return strategie(pole, n - 1)   # Totez, pokud na indexu n neni 'o'
    return pozice

def tah_pocitace(pole):
    symbol = 'o'
    if 'o' not in pole:     # prvni tah je nahodne cislo, jen nesmi pocitac slapnout na hracuv krizek
        pozice = randrange(20)
        while pole[pozice] != '-':
            pozice = randrange(20)
    else:
        pozice = strategie(pole, 19)    # Pak jede podle strategie, pocitame s 19 policky
    print('Tah pocitace: ', pozice)
    return tah(pole, pozice, symbol)

def piskvorky1d():
    pole = '-' * 20
    print('Zacinaji piskvorky!')
    stav = '-'
    while stav == '-':
        pole = tah_hrace(pole)
        print(pole)
        stav = vyhodnot(pole)
        pole = tah_pocitace(pole)
        print(pole)
        stav = vyhodnot(pole)
    if stav == 'x':
        print('Konec hry, clovek vyhral.')
    elif stav == 'o':
        print('Konec hry, pocitac vyhral.')
    elif stav == '!':
        print('Konec hry, remiza.')

piskvorky1d()
