# Fibbonaciho posloupnost

n1 = 0
n2 = 1

def fibbonaci(x):
    x = n1 + n2
    n1 = n2
    n2 = fibbonaci(x)
    return nx 

cislo = input('Zadej pocet clenu F. posloupnosti: ')
posloupnost = fibbonaci(cislo)
print(posloupnost)

