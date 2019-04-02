rimske_cislo = input('Napis rimske cislo: ')
seznam_cislo = list(rimske_cislo)
print(seznam_cislo)
seznam_dvojic = []

for prvek in seznam_cislo:
    poradi = seznam_cislo.index(prvek)
    dvojice = [poradi, prvek]
    seznam_dvojic.append(dvojice)
slovnik_cislo = dict(seznam_dvojic)
print(slovnik_cislo)

hodnoty = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

