import MyFunctions as mF
Luku = input("Anna luku: ")
Luku = int(Luku)

(F, P) = mF.IsPrime(Luku)  # F = Factors, P = Prime
print(F)
if P:
    print("Luku", Luku, "on alkuluku")
else:
    print("Luku", Luku, "ei ole alkuluku")
