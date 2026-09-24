A = [1,
     2,
     3]
B = []
C = []

def deplacer(dep, arr, n=1):
    global A, B, C
    try:
        for _ in range(n):
            x = dep.pop()
            arr.append(x)
    except KeyError as e:
        print(e)
        
def algo(n):
    global A, B, C
    afficher(n)
    deplacer(A, B, n-1)
    afficher(n)
    deplacer(A, C)
    afficher(n)
    deplacer(B, A)
    afficher(n)
    deplacer(B, C)
    afficher(n)
    deplacer(A, C)
    afficher(n)

def afficher(n):
    global A, B, C
    c = ""
    for i in range(n):
        try:
            a = A[i]
        except IndexError:
            a = " "
        try:
            b = B[i]
        except IndexError:
            b = " "
        try:
            d = C[i]
        except IndexError:
            d = " "
        c += f'{a} | {b} | {d}\n'
    print(c)

algo(3)