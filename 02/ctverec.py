strana = float(input('Zadej cislo: '))
cislo_je_spravne = strana > 0

if cislo_je_spravne:
    print('obvod ctverce o strane', strana, 'cm je', 4 * strana, 'cm')
    print('obsah ctverce o strane', strana, '356 cm je', strana * strana, 'cm2')
else:
    print('strana musi byt kladna')