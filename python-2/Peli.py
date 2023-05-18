from random import randint
VoittoLuku = randint(1, 20)
# print(VoittoLuku)
# quit()

# input tarkistus
while True:
    Lkm = input("Anna arvauksen lukumäärä (1-5): ")
    try:
        Lkm = int(Lkm)
    except ValueError as e:
        print(e)
        continue
    if (Lkm >= 1) and (Lkm <= 5):
        break
    else:
        continue
# user tries
for i in range(Lkm):
    Arvaus = int(input("Anna luku (1 - 20): "))
    if Arvaus > VoittoLuku:
        print("Liian iso")
    elif Arvaus < VoittoLuku:
        print("Liian pieni")
    else:
        print("Okein!!!")
