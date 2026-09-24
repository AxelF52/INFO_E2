def Syraccus(n):
    if n == 1:
        print(1)
        return None
    print(n)
    if n % 2 == 1:
        return Syraccus(n*3 + 1)
    else:
        return Syraccus(n//2)


n = 100
assert (type(n) == int and n > 0), "non"
Syraccus(n)