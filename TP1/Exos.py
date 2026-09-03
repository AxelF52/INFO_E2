# Exos d'avant trop simple 

def pi()->float:
    approx = 3
    signe = 1
    for i in range(2, 17*3, 2):
        approx += 4/(i*(i+1)*(i+2)) * signe
        signe *= -1
        print(i)
    return approx

print(pi())

def dectobin(q:int)->str:
    bin = ""
    while q != 0:
        r = q%2
        q //= 2
        bin += str(r)
    return bin[::-1]

print(dectobin(128))
import random

def plaques():
    alphabet="abcdefghjklmnpqrstvwxyz"
    plaque = alphabet[random.randint(0, 22)].upper() + alphabet[random.randint(0, 22)].upper() + "-" + str(random.randint(000, 1000)).zfill(3) + "-" + alphabet[random.randint(0, 22)].upper() + alphabet[random.randint(0, 22)].upper()
    return plaque if "SS" not in plaque else plaques()

print(plaques())