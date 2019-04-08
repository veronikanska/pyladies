# 1-D piskvorky, hraji se na radku s dvaceti policky. Hrac clovek ma krizky, pocitac ma kolecka. Kdo da tri sve symboly vedle sebe, vyhral.

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

def tah_hrace(pole):
    'Zapise do pole tah hrace - vrati pole se zapsanym tahem.'
    pozice = input('Zadej pozici, na kterou chces hrat: ')
    a = len(pozice)
    # Cyklus, ktery nepusti hrace dal, dokud nezada cislo od 0 do 19
    while True:
        for n in range(-1, a):    # Tady se overuje, jestli hrac pise cislice. Prijde mi to dost nesikovne, ale nevim, jak na to lepe, aby to nehazelo int error, kdyz s tim inputem budu dal pracovat a nebude to cislice.
            if ord(pozice[n]) not in range(48,58):
                pozice = input('Zadej cislo, nerozumim pismenum a znakum: ')
            else:
                break
        cislo = int(pozice)    # Tady uz mam 100% cislice, tak muzu prevest retezec na cislo    
        if cislo not in range(0,20):
            pozice = input('Zadej cele cislo od 0 do 19: ')
        elif pole[cislo] != '-':
            pozice = input('Pozice je obsazena, vyber si jinou: ')
        else:   # Pokud je zadano cislo vyhovujici vsem podminkam vyse, zapise se do pole. Retezce nejdou menit, tak je nutne to udelat pres seznam. Nebo ne?
            seznam = list(pole)
            seznam[cislo] = 'x'
            pole = ''.join(seznam)
            break
    return pole

def strategie(pole, n):
    'Strategie, podle ktere pocitac vybira pozici pro sve znaky vedle svych existujicich znaku.'    # Rekurzivne, juhu!
    if n == pole.index('o') and pole[pole.index('o') + 1] != '-' and pole[pole.index('o') - 1] != '-':  
        pozice = randrange(20)  # Koncovy bod rekurze - pokud neni v poli zadne 'o', vedle ktereho by se dalo hrat, pocitac zvoli nahodne cislo
        while pole[pozice] != '-':
            pozice = randrange(20)
    else:   # Jinak jedeme odzadu pole (n = 18) a zkousime, jestli je na indexu 'o' a jestli vedle nej je volne misto 
        if pole[n] == 'o':
            if pole[n + 1] == '-':
                pozice = pole.index('-', n)
            elif pole[n - 1] == '-':
                pozice = pole.index('-', n - 1)    
            else:
                return strategie(pole, n - 1)   # Pokud neni vedle 'o' volno, znova zavolame f. strategie s n - 1
        else:
            return strategie(pole, n - 1)   # Totez, pokud na indexu n neni 'o'
    return pozice

def tah_pocitace(pole):
    if 'o' not in pole:     # prvni tah je nahodne cislo, jen nesmi pocitac slapnout na hracuv krizek
        pozice = randrange(20)
        while pole[pozice] != '-':
            pozice = randrange(20)
    else:
        pozice = strategie(pole, 18)    # Pak jede podle strategie
    print('Tah pocitace: ', pozice)
    seznam = list(pole)     # Zapis do retezce opet pres seznam
    seznam[pozice] = 'o'
    pole = ''.join(seznam)
    return pole

def piskvorky1d():
    pole = '-' * 20
    print('Zacinaji piskvorky!')
    stav = '-'  # Nevim, jestli je lepsi nastavit pocatecni stav natvrdo nebo tam dat fci vyhodnot. Asi je to fuk
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
        print('Konec hry, pocitac vyhal.')
    elif stav == '!':
        print('Konec hry, remiza.')

# Nakonec zavolame funkci piskvorky, ktera udela vse
piskvorky1d()
