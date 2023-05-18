Cars = ["Toyota", "Tesla", "Hundai"]
print(Cars)
length = len(Cars)  # Listan pituus
print("Listassa on " + str(length) + " autoa")

print("Lisätään Honda listaan")
Cars.append("Honda")
print(Cars)

print("Otetaan pois " + Cars[1])
Cars.pop(1)
print(Cars)

print("Käydän listaa läpi for-loopilla")
for x in Cars:
    print(x)
print(Cars[1])

SekaLista = [1, "Pekka", "Banaani", 7.0, 1, 1, [56, "Tiina", "Toyota"]]
print(SekaLista)

y = SekaLista[1]
print(y)
