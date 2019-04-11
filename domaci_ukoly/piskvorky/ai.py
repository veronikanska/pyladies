from random import randrange
from util import tah, strategie

def tah_pocitace(pole):
    symbol = 'o'
    if 'o' not in pole:     # prvni tah je nahodne cislo, ale od 1 do 18, at pak strategie nehazi chyby
        pozice = randrange(1, 19)
        while pole[pozice] != '-':
            pozice = randrange(1, 19)
    else:
        pozice = strategie(pole, 19)    # Pak jede podle strategie
    print('Tah pocitace: ', pozice)
    return tah(pole, pozice, symbol)