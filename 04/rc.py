# Program, ktery overi spravnost rodneho cisla a vypocita datum narozeni a pohlavi

cislice = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
pravda = True

# Kontrola formatu a delitelnosti 11 - hozeno do nekonecneho cyklu, ktery pta tak dlouho, dokud uzivatel nenapise rodne cislo spravne
while True:
    vklad = input('Napis rodne cislo ve formatu xxxxxx/xxxx: ')
    rodne_cislo = list(vklad)                                             # Prevedeme retezec na seznam
    if len(rodne_cislo) == 11:                                            # Overime delku 11 znaku
        if rodne_cislo[6] == '/':                                         
            del rodne_cislo[6]                                            # Zjistime, zda je 6. prvek lomitko a smazeme ho
            for prvek in rodne_cislo:
                if prvek not in cislice:
                    pravda = False                                        # Overime, ze zbyle prvky jsou cislice
            if pravda == True:
                rodne_cislo = ''.join(rodne_cislo)                        # Prevedeme zpet na retezec
                cislo = int(rodne_cislo)                                  # A retezec na cislo
                if cislo / 11 == int(cislo / 11):                         # Overime delitelnost 11
                    break                                                 # Pokud vse plati, vypadneme z cyklu s realnym rodnym cislem.

print('{} je skutecne rodne cislo.'.format(vklad))       

# Vypocet data narozeni
rok = rodne_cislo[:2]
den = rodne_cislo[4:6]
kod_mesic = rodne_cislo[2:4]          # S mesicem to neni tak snadne, u zen je nutne odecist 50
cislo_mesic = int(kod_mesic)          # Takze prevod na cislo

if cislo_mesic > 20:                  # A podminky definujici promennou mesic a pohlavi
    mesic = cislo_mesic - 50
    pohlavi = 'zena'
else:
    mesic = cislo_mesic
    pohlavi = 'muz'

print('Datum narozeni: {} {} 19{}'.format(den, mesic, rok))
print('Pohlavi: {}'.format(pohlavi))