while True:
    operation = input("Type d'opérations : addition 1, soustraction 2, multiplication 3, division 4 : ").lower()

    if operation not in ("1", "2", "3", "4"):
        print("Saisie incorrecte.")
        continue

    try:
        nombre1 = float(input("Saisir un premier nombre : "))
        nombre2 = float(input("Saisir un deuxième nombre : "))
    except ValueError:
        print("Saisie incorrecte.")
        continue

    if operation == "1":
        result = nombre1 + nombre2
        print(f"{nombre1} + {nombre2} = {result}")

    elif operation == "2":
        result = nombre1 - nombre2
        print(f"{nombre1} - {nombre2} = {result}")

    elif operation == "3":
        result = nombre1 * nombre2
        print(f"{nombre1} * {nombre2} = {result}")

    elif operation == "4":
        if nombre2 == 0:
            print("division par 0 impossible, tu le fais exprès ??? Ohhhhh c'est la base ça !!!!")
            continue
        result = nombre1 / nombre2
        print(f"{nombre1} / {nombre2} = {result}")

    continuer = input("Un autre calcul ? oui ou non : ").lower()

    if continuer != "oui":
        break