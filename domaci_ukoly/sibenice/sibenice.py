from random import choice
from zadani import seznam_slov, obrazky

def tah(slovo, pole, pismeno):
    'Vrati herni pole s pismenem umistenym na danou pozici'
    seznam = list(pole) 
    seznam[slovo.index(pismeno)] = pismeno
    pole = ''.join(seznam)
    return pole

def overeni(pismeno, pole):
    if len(pismeno) != 1:
        return False
    elif ord(pismeno) not in range(97, 123) and ord(pismeno) not in range(65, 91):
        print('To neni pismeno!')
        return False
    elif pismeno in pole:
        print('Zvol jine pismeno.')
        return False
    else:
        return True

def vklad(pole):
    pismeno = input('Zadej pismeno: ')
    while overeni(pismeno, pole) != True:
        pismeno = input('Zadej pismeno: ')
    pismeno = pismeno.lower()
    return pismeno

def kolo(skore, slovo, pole, pismeno):
    if pismeno in slovo:
        pole = tah(slovo, pole, pismeno)
        skore = skore
        obrazek = obrazky[skore]
    else:
        pole = pole
        skore = skore + 1
        try:
            obrazek = obrazky[skore]
        except IndexError:
            obrazek = obrazky[- 1]
    return pole, skore, obrazek

def sibenice():
    skore = 0
    slovo = choice(seznam_slov)
    pole = len(slovo) * '-'
    while '-' in pole:
        pismeno = vklad(pole)
        stav = kolo(skore, slovo, pole, pismeno)
        pole = stav[0]
        obrazek = stav[2]
        print(obrazek)
        print(pole)
        skore = stav[1]
        if skore >= len(obrazky):
            break
    if '-' not in pole:
        print('Gratuluji, vyhral jsi!')
    else:
        print('Prohral jsi. Priste to snad vyjde.')

sibenice()
