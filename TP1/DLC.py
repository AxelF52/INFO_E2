from Exos import *

choix = int(input("selectionner un choix d'exo entre 1 et 7"))

if choix == 1:
    p = int(input("Entrer poids"))
    t = int(input("Entrer taille"))
    print(IMC(p, t))