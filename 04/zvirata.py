zvirata = ['pes', 'kocka', 'kralik', 'had', 'andulka']
kratci = []
kacka = []

for zvire in zvirata:
    if len(zvire) < 5:
        kratci.append(zvire)

for zvire in zvirata:
    if zvire[0] == 'k':
        kacka.append(zvire)

slovo = input('Napis nazev zvirete: ')

print('Je ', slovo, 'domaci zvire? ', slovo in zvirata)
print('Zvirata: ', zvirata)
print('Zvirata kratsi nez 5 pismen: ', kratci)
print('Zvirata zacinajici na K: ', kacka)

zvirata.sort()
print(zvirata)

seznam_dvojic = []
serazeno = []
for zvire in zvirata:
    klic = zvire[1]
    dvojice = [klic, zvire] 
    seznam_dvojic.append(dvojice)
seznam_dvojic.sort()
for dvojice in seznam_dvojic:
    serazeno.append(dvojice[1])
print(serazeno)
    
