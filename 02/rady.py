# Tento program rozdává naivní rady do života.

print('Odpovídej "ano" nebo "ne".')
stastna_retezec = input('Jsi šťastná? ')
if stastna_retezec == 'ano':
    stastna = True
elif stastna_retezec == 'ne':
    stastna = False
else:
    print('Nerozumím!')

bohata_retezec = input('Jsi bohatá? ')
if bohata_retezec == 'ano':
    bohata = True
elif bohata_retezec == 'ne':
    bohata = False
else:
    print('Nerozumím!')

# Prepisovala jsem to jen odsud:

if bohata:
    if stastna:
        print('Gratuluji!')
    else:
        print('Zkus se víc usmívat.')
elif stastna:
    print('Zkus míň utrácet.')
else:
    print('To je mi líto.')