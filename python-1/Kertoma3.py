def Factioral(n):
	if n == 0:
		return 1
	else:
		return n * Factioral(n-1)


Luku = int(input("Luku: "))
k = Factioral(Luku)
print(k)
