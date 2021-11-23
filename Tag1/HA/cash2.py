amount = int(input("Betrag in Cent: "))
munzen = [200, 100, 50, 20, 10, 5, 2, 1]

current = amount
for cents in munzen:
    count = current // cents
    print(f"Wir brauchen {count} mal {cents} Cent.")
    current = current - cents * count
