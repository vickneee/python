Min = int(input("Eka luku: "))
Max = int(input("Toka luku: "))
Limit = int(input("Raja: "))
Step = int(input("Askel: "))
Oe = int(input("1 = Pariton, 2 = Parillinen: "))

Sum = 0

for i in range(Min, Max+1, Step):
	if Sum >= Limit:
		break
	if (Oe == 1) and (i % 2 != 0):
		Sum = Sum + i
	if (Oe == 2) and (i % 2 == 0):
		Sum = Sum + i
	print(i)

print("Sum is " + str(Sum))
