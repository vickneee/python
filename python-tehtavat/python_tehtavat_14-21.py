# Victoria V
print("Tehtävä 14")
luku = int(input("Anna luku: "))
if luku % 2 == 0:
    print(f"Luku on parillinen: {luku}")
else:
    print(f"Luku on pariton: {luku}")
print("Tehtävä 15, 16, 17")
luku = int(input("Anna luku: "))
if luku <= 0:
    print("Anna positiivinen luku, kiitos!")
elif luku < 10:
    print("Luku on alle 10")
elif luku > 10:
    print("Luku on suurempi kuin 10")
elif luku == 10:
    print("Täysi kymppi!")
print("Tehtävä 18")
luku1 = int(input("Anna luku 1: "))
luku2 = int(input("Anna luku 2: "))
luku3 = int(input("Anna luku 3: "))
avg = (luku1 + luku2 + luku3) / 3
print(f"Keskiarvo on: {avg}")
print("Tehtävä 19")
luku = int(input("Anna luku: "))
if luku < 0:
    print("Luku on negatiivinen!")
elif luku > 0:
    print("Luku on positiivinen!")
elif luku == 0:
    print("Luku on 0!")
print("20")
luku1 = int(input("Anna luku 1: "))
luku2 = int(input("Anna luku 2: "))
luku3 = int(input("Anna luku 3: "))
if luku1 < luku2 and luku1 < luku3:
    print(f"Luku {luku1} on pienin!")
elif luku2 < luku1 and luku2 < luku3:
    print(f"Luku {luku2} on pienin!")
elif luku3 < luku1 and luku3 < luku2:
    print(f"Luku {luku3} on pienin!")
elif luku1 == luku2:
    print(f"Luvut {luku1} ja {luku2} ovat yhtä suuria!")
elif luku2 == luku3:
    print(f"Luvut {luku2} ja {luku3} ovat yhtä suuria!")
elif luku1 == luku3:
    print(f"Luvut {luku1} ja {luku3} ovat yhtä suuria!")
elif luku1 == luku2 == luku3:
    print("Kaikki luvut ovat yhtä suuria!")
print("Tehtävä 21")
user_choice = input("Haluatko kahvia tai teetä?: ")
sugar = int(input("Kuinka monta sokeripalaa?: "))
if user_choice == "kahvia" or "Kahvia":
    if sugar <= 2:
        print("Kahvi kyllä piristää!")
    elif sugar >= 3:
        print("Kahvi voi olla aika vahva maku...")
elif user_choice == "teetä" or "Teetä":
    if sugar <= 2:
        print("Tee usein rauhoittaa!")
    elif sugar >= 3:
        print("Taidat pitää teestäsi makeana?")
else:
    print("Ohjelmassa tapahtunut virhe!")
