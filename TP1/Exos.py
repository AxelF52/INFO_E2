import random

def imc(poids, taille):
    return poids / taille**2

def N_entiers():
    n_list = []
    n = 0
    while n >= 0:
        n = int(input("ajouter un nombre"))
        n_list.append(n)
    return n_list.sort(), max(n_list), min(n_list), sum(n_list)/len(n_list)

def age_canine(age):
    assert age > 0, "age ne peut pas être négatif !!!"
    age_c = 0
    for i in range(0, age):
        if i <= 1:
            age_c += 10.5
        else:
            age_c += 4
    return age_c

def pi()->float:
    approx = 3
    signe = 1
    for i in range(2, 17*3, 2):
        approx += 4/(i*(i+1)*(i+2)) * signe
        signe *= -1
    return approx

def dectobin(q:int)->str:
    bin = ""
    while q != 0:
        r = q%2
        q //= 2
        bin += str(r)
    return bin[::-1]

def plaques():
    alphabet="abcdefghjklmnpqrstvwxyz"
    plaque = alphabet[random.randint(0, 22)].upper() + alphabet[random.randint(0, 22)].upper() + "-" + str(random.randint(000, 1000)).zfill(3) + "-" + alphabet[random.randint(0, 22)].upper() + alphabet[random.randint(0, 22)].upper()
    return plaque if "SS" not in plaque else plaques()