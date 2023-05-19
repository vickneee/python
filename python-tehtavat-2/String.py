Merkkijono = "Pekka on poika"
print(Merkkijono)
print(Merkkijono[0])
print("Pekka" in Merkkijono)  # True

print(Merkkijono[3], Merkkijono[-1])  # k a
print(Merkkijono[4], Merkkijono[-2])  # a k

print(Merkkijono[len(Merkkijono)-1])  # a

c = "Hello World!"
print(c[2:5])  # llo
print(c[:5])  # Hello
print(c[2:])  # llo World!

for i in c:
    print(i)
