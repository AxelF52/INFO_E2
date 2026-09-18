import random

historique = []

def actualiser(m, coords, type):
    for i in range(5):
        for j in range(5):
            if [i, j] == coords:
                m[i][j] = type
    return m

def save():
    global historique, m
    historique.append([ligne[:] for ligne in m])

def UNDO():
    global historique, m
    if historique:
        m = historique.pop()
    return m

def afficher(m):
    c = "\n"
    for i in m:
        c += str(i) + "\n"
    print(c)

def voisin(coords):
    voisins = []
    d_xy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for x, y in d_xy:
        nx = coords[0] + x
        ny = coords[1] + y
        if 0 <= nx < 5 and 0 <= ny < 5:
            voisins.append([nx, ny])
    return voisins

def verif_fin(m):
    for i in m:
        for j in i:
            if j != 2:
                return False
    return True

def verif_5(m):
    cases = []
    for i in range(5):
        if all(m[i][j] == 1 for j in range(5)):
            for j in range(5):
                cases.append([i, j])
    for j in range(5):
        if all(m[i][j] == 1 for i in range(5)):
            for i in range(5):
                cases.append([i, j])
    if all(m[i][i] == 1 for i in range(5)):
        for i in range(5):
            cases.append([i, i])
    if all(m[i][4-i] == 1 for i in range(5)):
        for i in range(5):
            cases.append([i, 4-i])
    for case in cases:
        actualiser(m, case, 2)

def init():
    global m
    m = [[0 for _ in range(5)] for _ in range(5)]

    case_m = []
    while len(case_m) < 2:
        case = [random.randint(0, 4), random.randint(0, 4)]
        if case not in case_m:
            case_m.append(case)

    for i in case_m:
        actualiser(m, i, 1)
        v = voisin(i)
        for j in v:
            actualiser(m, j, 1)

def Game():
    choix = input("Choisi de Marquer une case (m), Undo (u), Reset la partie (r) : ")
    if choix == "a":
        afficher(m)
    if choix == "r":
        init()
    if choix == "u":
        UNDO()
    if choix == "m":
        save()
        x = int(input("numéro de ligne (1 - 5) ? "))
        y = int(input("numéro de colonne (1 - 5) ? "))
        actualiser(m, [x-1, y-1], 1)
        print("case marquée avec succès !")
        verif_5(m)
    if not verif_fin(m):
        Game()
    else:
        afficher(m)
        print("fin du jeu")

init()
Game()
