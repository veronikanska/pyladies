from random import randrange
import util

def tah_pocitace(pole):
    if pole.count('o') > pole.count('x'):
        symbol = 'x'
    else:
        symbol = 'o'
    if symbol not in pole:     # prvni tah je nahodne cislo, ale od 1 do 18, at pak strategie nehazi chyby
        pozice = randrange(1, 19)
        while pole[pozice] != '-':
            pozice = randrange(1, 19)
    else:
        pozice = util.strategie(pole, 19, symbol)    # Pak jede podle strategie
    print('Tah pocitace: ', pozice)
    return util.tah(pole, pozice, symbol)