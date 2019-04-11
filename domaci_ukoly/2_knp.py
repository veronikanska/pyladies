from random import randrange
cislo = randrange(3)

if cislo == 0:      # uprava podle ukolu c. 8, aby si pocitac taky zahral
    tah_pocitace = 'kámen'
elif cislo == 1:
    tah_pocitace = 'nůžky'
elif cislo == 2:
    tah_pocitace = 'papír'

tah_cloveka = input('kámen, nůžky, nebo papír? ')

print('tah pocitace: ', tah_pocitace)    # vypise tah pocitace, aby se dalo zkontrolovat, jestli nepodvadi :)

if tah_cloveka == tah_pocitace:
    print('Plichta')
elif (tah_cloveka == 'kámen' and tah_pocitace == 'papír') or (tah_cloveka == 'nůžky' and tah_pocitace == 'kámen') or (tah_cloveka == 'papír' and tah_pocitace == 'nůžky'):
    print('Počítač vyhrál.')
elif (tah_cloveka == 'kámen' and tah_pocitace == 'nůžky') or (tah_cloveka == 'nůžky' and tah_pocitace == 'papír') or (tah_cloveka == 'papír' and tah_pocitace == 'kámen'):
    print('Vyhrála jsi!.')
else:
    print('Nerozumím.')