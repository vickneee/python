# Victoria V
while True:
    luku = int(input("Anna luku väliltä 0-10: "))
    if luku < 0 or luku > 10:
        break
    laske = 1
    kertoma = 1
    while laske < luku:
        laske += 1
        kertoma *= laske
    print(f"Luvun {luku} kertoma on {kertoma}.")
    
    
print("Luku ei ollut väliltä 0-10!")
