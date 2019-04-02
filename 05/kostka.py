from random import randrange

def hod():
    'Vrati pocet hodu kostkou, dokud nepadne sestka'
    n = None
    s = 0
    while n != 6:
        n = randrange(1,7)
        s = s + 1
    return s

def vyhodnoceni(a, b, c, d):
    'Vyhodnoti nejlepsiho hrace - toho, kdo mel nejvice hodu kostkou'
    seznam = [[a, 'prvni hrac'], [b, 'druhy hrac'], [c, 'treti hrac'], [d, 'ctvrty hrac']]
    seznam.sort()
    prvni = seznam[3]
    vitez = prvni[1]
    return vitez
    
# Samotny program
i = 1
s = []
for x in range(1,5):
    x = hod()
    print('Pocet hodu {}. hrace je {}.'.format(i, x))
    s.append(x)
    i = i + 1

v = vyhodnoceni(s[0], s[1], s[2], s[3])
print('Vitezem je {}'.format(v))
