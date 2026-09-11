# EXO 1 : Ok

# EXO 2
classDict = {
 "class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}

print(classDict["class"]["student"]["name"])
classDict["class"]["student"]["marks"]["physics"] = 89
classDict["class"]["student"]["average"] = (classDict["class"]["student"]["marks"]["physics"] + classDict["class"]["student"]["marks"]["history"])/2
classDict["class"]["student"] = [classDict["class"]["student"]]
classDict["class"]["student"].append({"name":"Ted", "marks" : {"physics": 34, "history":99}})
classDict["class"]["student"][1]["average"] = (classDict["class"]["student"][1]["marks"]["physics"] + classDict["class"]["student"][1]["marks"]["history"])/2
classDict["class"]["average_grade"] = (classDict["class"]["student"][0]["average"] + classDict["class"]["student"][1]["average"] )/ len(classDict["class"]["student"])
print(classDict)

# Exo 3
import random 

def dooble(n):
    assert 2 < n < 100, "n incorrect"
    tab = [random.randint(0, 500) for _ in range(n)]
    for i in range(1, len(tab)):
        for j in range(i, 0, -1):
            if tab[j] < tab[j - 1]:
                tab[j], tab[j - 1] = tab[j - 1], tab[j]
            else:
                break
    for i in range(1, len(tab)):
        if tab[i] == tab[i-1]:
            return "double trouvé"
    return "pas de double"

print(dooble(50))

# Exo 4

def calculScore(p):
    score = []

    for i in p:
        if i == "C":
            score.pop()
        elif i == "D":
            score.append(score[-1] * 2)
        elif i == "+":
            score.append(score[-1] + score[-2])
        else:
            score.append(int(i))

    return sum(score)

print(calculScore(["10","2","C","D","+"]))

