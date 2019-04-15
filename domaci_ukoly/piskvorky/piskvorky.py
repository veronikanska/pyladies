# Obsahuje funkce pro hru piskvorky: vyhodnot, tah_hrace, piskvorky1d

import util
import ai

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

# Tah hrace se kvli inputu netestuje, je osekany o podminky, ty jsou ve funkci vklad nize. Ta se testuje.
def tah_hrace(pole):
    'Zapise do pole tah hrace - vrati pole se zapsanym tahem.'
    symbol = 'x'
    cislo = input('Zadej pozici, na kterou chces hrat: ')
    while vklad(pole, cislo) != True:
        cislo = input('Zadej pozici, na kterou chces hrat: ')
    pozice = int(cislo)
    return util.tah(pole, pozice, symbol)

def vklad(pole, cislo):
    'Vyhodnoti vklad od hrace - jestli je to cislo v danem rozmezi a jestli je zadana pozice volna'
    try:
        pozice = int(cislo)
    except ValueError:
        print('To neni cislo, zkus to znova.')
        return False
    if pozice not in range(0,20):
        print('Zadej cele cislo od 0 do 19: ')
        return False
    elif pole[pozice] != '-':
        print('Pozice je obsazena, vyber si jinou: ')
        return False
    else:
        return True

def piskvorky1d():
    pole = '-' * 20
    print('Zacinaji piskvorky!')
    stav = '-'
    while stav == '-':
        pole = tah_hrace(pole)
        print(pole)
        stav = vyhodnot(pole)
        pole = ai.tah_pocitace(pole)
        print(pole)
        stav = vyhodnot(pole)
    if stav == 'x':
        print('Konec hry, clovek vyhral.')
    elif stav == 'o':
        print('Konec hry, pocitac vyhral.')
    elif stav == '!':
        print('Konec hry, remiza.')
