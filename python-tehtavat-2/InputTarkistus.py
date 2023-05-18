while True:
    n1 = input("1. kokonaisluku ")
    n2 = input("2. kokonaisluku ")
    n3 = input("3. kokonaisluku ")
    try:
        n1 = int(n1)
        n2 = int(n2)
        n3 = int(n3)
        break
    except ValueError:
        print("Anna vain kokonaislukuja")
        continue
