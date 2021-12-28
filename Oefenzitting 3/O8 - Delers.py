"""
Schrijf met behulp van een list comprehension een programma dat alle delers van een gegeven geheel getal als
uitvoer geeft. Dit getal vraag je op aan de gebruiker.
"""
getal = int(input('Geef een getal: '))
delers = []
for i in range(1, getal+1):
    if getal%i == 0:
        delers.append(i)
print(delers)