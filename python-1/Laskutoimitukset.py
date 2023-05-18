while True:
	a = input("1. kokonaisluku ")
	b = input("2. kokonaisluku ")
	try:
		a = int(a)
		b = int(b)
		break
	except ValueError:
		print("Anna vain kokonaislukuja")
		continue
s = a+b
e = a-b
k = a*b

print("a + b = " + str(s))
print("a - b = " + str(e))
print("a * b = " + str(k))

j = a/b
kj = a//b
jj = a % b
print("a / b = " + str(j))
print("a // b = " + str(kj))
print("a % b = " + str(jj))

if a > b:
	print(str(a) + " > " + str(b))
elif a < b:
	print(str(a) + " < " + str(b))
else:
	print(str(a) + " = " + str(b))
