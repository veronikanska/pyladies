# Uzivatel zada dve cisla a operaci a program operaci s cislz provede

cislo_1 = int(input('Zadej prvni cislo: '))
cislo_2 = int(input('Zadej druhe cislo: '))
operace = str(input('Vyber operaci: +, -, * nebo /: '))

if operace != '+' and operace != '-' and operace != '*' and operace != '/':
    print('Nerozumim')
else:    
    print('Prvni cislo: ', cislo_1)
    print('Druhe cislo: ', cislo_2)
    print('Operace: ', operace)

    if operace == '+':
        print(cislo_1, ' + ', cislo_2, ' = ', cislo_1 + cislo_2)
    elif operace == '-':
        print(cislo_1, ' - ', cislo_2, ' = ', cislo_1 - cislo_2)
    elif operace == '*':
        print(cislo_1, ' * ', cislo_2, ' = ', cislo_1 * cislo_2)
    elif operace == '/':
        print(cislo_1, ' / ', cislo_2, ' = ', cislo_1 / cislo_2)    