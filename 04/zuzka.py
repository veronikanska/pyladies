rodnecislo = input('zadej rodne cislo i s lomitkem:')

cislo = (rodnecislo[0:6]) + (rodnecislo[7:11])

delenec = int(cislo)
delitel = 11

treticislo = rodnecislo[2]

#format rodneho cisla
if (len(rodnecislo) == 11) and (rodnecislo[6] == '/') and (delenec % delitel == 0):
    print('Rodne cislo ma spravny format')
else: print('Zadane rodne cislo je nespravne')

if (rodnecislo[2] > '1'):
    print('Jsi zena')
else:
    print('Jsi muz')

#pro zeny narozene rijen+
for i in treticislo:
    if i == '6':
        treticislo = ('1' + rodnecislo[3])
        print(treticislo)
        break

#pro vygenerovani datumu narozeni
if (rodnecislo[2] == '5'):
    print(rodnecislo [4:6], '/', rodnecislo[3], '/', rodnecislo[0:2])
elif (rodnecislo[2]) == '6':
    print(rodnecislo [4:6], '/', treticislo, '/', rodnecislo[0:2])
else:
    print(rodnecislo [4:6], '/', rodnecislo[2:4], '/', rodnecislo[0:2])