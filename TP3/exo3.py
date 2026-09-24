import sys

try:
    mode = sys.argv[1]
    nombre = int(sys.argv[2])
    fichier = sys.argv[3]

    if mode != "head" and mode != "tail":
        raise ValueError("Le premier paramètre doit être head ou tail")

    if nombre <= 0:
        raise ValueError("Le nombre doit être un entier positif")

    with open(fichier, "r") as f:
        lignes = f.readlines()

    if mode == "head":
        print("".join(lignes[:nombre]))
    else:
        print("".join(lignes[-nombre:]))

except ValueError as e:
    print("Erreur :", e)

except IOError:
    print("Erreur : fichier introuvable")