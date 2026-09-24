def facto(n):
    if n <= 1:
        return 1
    return facto(n-1) * n

for i in range(10):
    print(facto(i))

