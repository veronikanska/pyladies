# Caesarova sifra, jupi!!!

k = input('Klic: ')                                              # Zadame klic
while len(k) != 1 or ord(k) not in range(48,58):                 # Pro zjednoduseni beru jen jednociferna cisla, jinak bych z toho delala seznam a projizdela for cyklem, jestli jsou vsechny prvky cislice
    print('Klic je prirozene jedniciferne cislo: ')
    k = input('Klic: ')
k = int(k)                                                       # Pokud je k cislice, prevedeme z retezce na cislo

plaintext = input('plaintext: ')                                 # Zadame plaintext a prevedeme na seznam
p = list(plaintext)
c = []                                                           # Nachystany seznam pro ciphertext

# A ted projedeme seznam znaku plaintextu for cyklem - nalozi s nimy podle toho, jestli je to diakriticky znak, velke nebo male pismeno

for sign in p:
    pi = ord(sign)
    if (pi >= 32 and pi <= 64) or (pi >=91 and pi <= 96) or (pi >= 123 and pi < 127):
        c.append(sign)       # Diakritiku nezmenenou prida do seznamu c
    elif pi in range(65,91):
        c.append(chr(((pi - 65 + k) % 26) + 65))     # Pismena posune o k, 65 nebo 97 se odecita, aby mela pismena indexy 0-25, 
    elif pi in range(97,123):                        # a bylo mozno vyuzit deleni se zbytkem (jinak by byl zbytek jiny, nez k)
        c.append(chr(((pi - 97 + k) % 26) + 97))     # Pak se pricte 65 nebo 97 zpet, abychom dostali pismeno a ne znaky ze zacatku ASCII tabulky.

ciphertext = ''.join(c)                          # Spojeni seznamu do retezce
print('Ciphertext: {}'.format(ciphertext))