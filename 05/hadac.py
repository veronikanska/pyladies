def pohlavi(prijmeni):
    if prijmeni.endswith('a') or prijmeni.endswith('á'):
        return True
    else:
        return False

prijmeni = input('Napis prijmeni: ')
if pohlavi(prijmeni) == True:
    p = 'zena'
else:
    p = 'muz'

print('{} je pravdepodone {}'.format(prijmeni, p))