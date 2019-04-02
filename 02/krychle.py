strana = float(input('Zadej cislo: '))
spravne = strana > 0

if spravne:
    print('povrch krychle o strane', strana, 'je', 6 * strana**2, 'cm2')
    print('objem krychle o strane', strana, 'je', strana**3, 'cm3')
else:
    print('Zadej kladne cislo')