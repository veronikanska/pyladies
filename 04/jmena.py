zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']

spravne = []
spatne = []
 
for zaznam in zaznamy:
    jmeno, prijmeni = zaznam.split()
    if not jmeno[0].islower() and not prijmeni[0].islower():
        spravne.append(zaznam)
    else:
        spatne.append(zaznam)

print(spravne)
print(spatne)