from random import randrange

def tah(pole, pozice, symbol):
    'Vrati herni pole se symbolem umistenym na danou pozici'
    seznam = list(pole)     # Zapis do retezce pres seznam
    seznam[pozice] = symbol
    pole = ''.join(seznam)
    return pole