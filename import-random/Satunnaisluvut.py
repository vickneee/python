import random

# Ensimmäinen kokonaisluku väliltä 30-100
luku_1 = random.randint(30, 100)
# Tarkastetaan tulostetavien lukujen määrä
# print(luku_1)

# Lista satunnaisluvuille
satunnaisluvut = []

# Arvotaan ja lisätään satunnaisluvut listaan
for satunnaisluku in range(luku_1):
    random_satunnaisluku = random.randint(1, 100)
    satunnaisluvut.append(random_satunnaisluku)

# Tulostetaan satunnaisluvut lista
print("Satunnaisluvut:", satunnaisluvut)

# Lasketaan lukujen määrä, summa ja keskiarvo
lukujen_lukumaara = len(satunnaisluvut)
lukujen_summa = sum(satunnaisluvut)
lukujen_keskiarvo = lukujen_summa / lukujen_lukumaara

# Tulostetaan lukujen määrä, summa ja keskiarvo
print("Lukujen lukumäärä:", lukujen_lukumaara)
print("Lukujen summa:", lukujen_summa)
print("Lukujen keskiarvo:", lukujen_keskiarvo)
