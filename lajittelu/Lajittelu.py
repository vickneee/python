# Victoria V
luku1 = input("Anna luku 1: ")
luku2 = input("Anna luku 2: ")
luku3 = input("Anna luku 3: ")
lajittelu = input("Anna lajittelu tyyppi N tai L: ")
print(f"Input: {luku1}, {luku2}, {luku3}")
if lajittelu == "N":
    print("Lajittelu: N")
elif lajittelu == "L":
    print("Lajittelu: L")
if lajittelu == "N" or lajittelu == "n":
    lista = [luku1, luku2, luku3]
    lista.sort()
    listaStr = ", ".join(lista)
    print(f"Tulos: {listaStr}")
elif lajittelu == "L" or lajittelu == "l":
    lista = [luku1, luku2, luku3]
    lista.sort(reverse=True)
    listaStr = ", ".join(lista)
    print(f"Tulos: {listaStr}")
