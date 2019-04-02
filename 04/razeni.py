zvirata = ['pes', 'kocka', 'kralik', 'had', 'andulka']
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
    