from Exos import *

choix = int(input("selectionner un choix d'exo entre 1 et 7"))
assert 0 < choix < 8, "tu le fais exprès ?" 

if choix == 1:
    p = int(input("Entrer poids"))
    t = int(input("Entrer taille"))
    print(imc(p, t))

elif choix == 2:
    print(N_entiers())

elif choix == 3:
    age = int(input("Entrer l'âge réel du chien"))
    print(age_canine(age))

elif choix == 4:
    print(f"approximation de pi : {pi()}")

elif choix == 5:
    print("entier à convertir :")

elif choix == 6:
    print(Exo6())

elif choix == 7:
    print(plaques())


# Exo 2

def FizzBuzz(n):
    c = ""
    if n % 3 == 0:
        c += "Fizz"
    if n % 5 == 0:
        c += "Buzz"
    if n % 3 != 0 and n % 5 != 0:
        c += str(n)
    return c

tab = [random.randint(1, 500) for _ in range(10)] + [15]
print(tab)
for i in tab:
    print(FizzBuzz(i)) 

# Exo 3

def Jeu():
    score = [0, 0]
    valeur = ["As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "V", "D", "R"]
    couleur = ["♠", "♣", "♦", "♥"]
    for _ in range(10):
        r1 = random.choice(valeur)
        print(f"carte piochée : {r1} {random.choice(couleur)}")
        choix = input("+ ou - ?")
        r2 = random.choice(valeur)
        print(f"Nouvelle Carte : {r2} {random.choice(couleur)}")
        if valeur.index(r2) < valeur.index(r1):
            if choix == "-":
                score[0] += 1
            else:
                score[1] += 1
        if valeur.index(r2) > valeur.index(r1):
            if choix == "+":
                score[1] += 1
            else:
                score[0] += 1
        print(f"score : Ordi = {score[0]} et Joueur = {score[1]}")
    print(f"score finaux : Ordi = {score[0]} et Joueur = {score[1]}")
    c = input("rejouer ? (oui/non)")
    if c.lower() == "oui":
        Jeu()

Jeu()