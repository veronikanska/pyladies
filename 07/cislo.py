def nacti_cislo():
    while True:
        cislo = input('Zadej cislo: ')
        try:
            x = int(cislo)
        except ValueError:
            print('To neni cislo, zkus to znova.')
        else:
            return x

print(nacti_cislo())
