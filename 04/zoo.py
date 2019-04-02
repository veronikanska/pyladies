afrika = ['lev', 'antilopa', 'slon', 'zirafa', 'pstros', 'gorila', 'buvol', 'nosorozec']
asie = ['slon', 'buvol', 'tygr', 'panda', 'nosorozec', 'orangutan']
vse = afrika + asie

spolecni = []
jen_afrika = []
jen_asie = []

for zvire in vse:
    if zvire in asie and zvire in afrika:
        if zvire not in spolecni:
            spolecni.append(zvire)
    elif zvire in afrika and not zvire in asie:
        jen_afrika.append(zvire)
    elif zvire in asie and not zvire in afrika:
        jen_asie.append(zvire)    

print(spolecni)
print(jen_afrika)
print(jen_asie)
