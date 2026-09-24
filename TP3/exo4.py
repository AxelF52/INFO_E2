import sys
import random
from erreur import LettreDejaProposee

mot = None
r = random.randint(0, 22739)

try:
    fichier = sys.argv[1]
    with open(fichier, "r") as f:
        lignes = f.readlines()
    mot = lignes[r].strip()

except ValueError as e:
    print(e)

# python .\exo4.py dic.txt

mot_joueur = ["_"] * len(mot)
mot = mot.upper()
lettres = []
vie = 10

while "_" in mot_joueur:
    if vie == 0:
        print("perdu", mot)
        exit()
    choix = input("Choisi une lettre (A-Z) : ")
    choix = choix.upper()
    try:
        if choix in lettres:
            raise LettreDejaProposee("ERREUR : cette lettre a déjà été proposée !")

        if not choix.isalpha() or len(choix) != 1:
            print("ERREUR")
            continue

        lettres.append(choix)

        replace = 0

        for i in range(len(mot)):
            if choix == mot[i]:
                mot_joueur[i] = choix
                replace += 1

        if replace == 0:
            vie -= 1
            print(f"FAUX ! vie restante : {vie}/10")

        print("Voici le mot :", mot_joueur)
        print("Lettres déjà proposées :", lettres)

    except LettreDejaProposee as e:
        print(e)

print("Bravo tu as gagné !")