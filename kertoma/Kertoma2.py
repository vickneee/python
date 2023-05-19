def Factioral(n):
    Kertoma = 1
    for i in range(1, n + 1, 1):
        Kertoma = Kertoma * i
    return Kertoma


Luku = int(input("Luku: "))
k = Factioral(Luku)
print(k)
