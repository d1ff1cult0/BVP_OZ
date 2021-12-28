def faculteit(n):
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac


getal = int(input('Geef een getal: '))
print(faculteit(getal))
