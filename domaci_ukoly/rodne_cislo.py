# Program, ktery overi spravnost rodneho cisla a vypocita datum narozeni a pohlavi

def format(rodne_cislo):
    'Vyhodnoti, je-li rodne cislo napsano ve spravnem formatu: 11 znaku, 6 cislic, lomitko, 4 cislice'
    if len(rodne_cislo) != 11:
        return False
    elif rodne_cislo[6] != '/':
        return False
    rc = ''.join(rodne_cislo.split('/'))
    for n in range(0,9):
        if ord(rc[n]) in range(48,58):
            return True
        else:
            return False

def delitelnost(rodne_cislo):
    'Vyhodnoti, je-li rodne cislo delitelne 11'
    rc = int(''.join(rodne_cislo.split('/')))
    if rc % 11 == 0:
        return True
    else:
        return False

def datum_narozeni(rodne_cislo):
    'Vrati z rodneho cisla tuple tri cisel: den, mesic a rok narozeni'
    rok = rodne_cislo[:2]
    den = rodne_cislo[4:6]
    kod_mesic = rodne_cislo[2:4]
    if kod_mesic[0] == '5':
        mesic = '0' + kod_mesic[1]
    elif kod_mesic[0] == '6':
        mesic = '1' + kod_mesic[1]
    else:
        mesic = kod_mesic
    return den, mesic, rok

def pohlavi(rodne_cislo):
    'Vyhodnoti z rodneho cisla pohlavi a vrati retezec muz nebo zena'
    if rodne_cislo[2] == '0' or rodne_cislo[2] == '1':
        pohlavi = 'muz'
    else:
        pohlavi = 'zena'
    return pohlavi

# Tady zacina kod samotneho programu s vyuzitim funkci definovanych vyse
rodne_cislo = input('Napis rodne cislo: ')
while format(rodne_cislo) == False or delitelnost(rodne_cislo) == False:
    print('Rodne cislo ma spatny format.')
    rodne_cislo = input('Napis rodne cislo: ')

print('{} je skutecne rodne cislo.'.format(rodne_cislo))  

data = datum_narozeni(rodne_cislo)
gender = pohlavi(rodne_cislo)
print('Datum narozeni: {} {} 19{}'.format(*data))
print('Pohlavi: {}'.format(gender))
