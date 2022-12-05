def sumDivision():
    data = input().split()

    try:
        data = [int(item) for item in data]
    except ValueError:
        print("Chyba v typu vstupní hodnoty.")
        print("Konec programu.")
        return

    try:
        soucet = data[0] / sum(data[1:])
    except IndexError:
        print("Špatné indexování.")
        print("Konec programu.")
        return
    except ZeroDivisionError:
        print("Dělení nulou.")
        print("Konec programu.")
        return

    print(f'Výsledek je {round(soucet, 2)}.')
    print("Program proběhl v pořádku.")
    print("Konec programu.")


sumDivision()