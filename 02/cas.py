cas = int(input('Kolik je hodin? Napis cele cislo a ja ti reknu, co je vhodne delat: '))
spravne = (cas >= 0 and cas <= 24)

if spravne:
    if cas < 5:
        print('Je noc a vsichni slusni lide spi - nebo programuji')
    elif cas < 7:
        print('Vstavat a cvicit! Ranni ptace dal doskace.')
    elif cas < 10:
        print('Prace kvapna malo platna! S chuti do toho, pul je hotovo.')
    elif cas < 12:
        print('Tesime se na obed, jak k dilu, tak k jidlu.')
    elif cas < 16:
        print('Uz se to krati, za chvili se jde domu')
    elif cas < 19:
        print('Dej si kafe nebo caj, mas volno.')
    elif cas < 23:
        print('Noc je jeste mlada! Bez se bavit')
    elif cas < 24:
        print('Cas jit pomalu na kute')
else:
    print('Nerozumim')