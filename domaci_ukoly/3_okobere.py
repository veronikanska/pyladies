# Hra oko bere

from random import randrange

pocet = 0
print('Mas ', pocet, ' bodu.')
odpoved = input('Zacina oko bere. Chces hrat? Odpovez ano nebo ne. ')
if odpoved != 'ano' and odpoved != 'ne':        
    print('Nerozumim')

while odpoved == 'ano':
    karta = randrange(2,11)
    print('Karta: ', karta)
    pocet = pocet + karta
    if pocet > 21:
        break
    elif pocet == 21:
        print('Mas 21 bodu. Vyhral jsi. Jupi!!')
        break
    else:
        print('Mas ', pocet, ' bodu.')
        odpoved = input('Chces pokracovat? Odpovez ano nebo ne. ')
        if odpoved != 'ano' and odpoved !='ne':
            print('Nerozumim')
if pocet != 21:
    print('Konec hry. Mas ', pocet, ' bodu.')