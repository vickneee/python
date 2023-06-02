import MyFunctions as mF

Name = input("Name: ")
Luku1 = int(input("Anna luku 1: "))
Luku2 = int(input("Anna luku 2: "))

Tervehdys = mF.Greeting(Name)
Summa = mF.LaskeYhteen(Luku1, Luku2)
print(Tervehdys, Summa)
