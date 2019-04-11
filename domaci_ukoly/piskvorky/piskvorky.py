from util import tah
from ai import tah_pocitace

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
