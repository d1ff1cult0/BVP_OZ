"""
Een n * n-matrix is een magisch vierkant als de som van de elementen in elke
rij, elke kolom en over de twee diagonalen hetzelfde is. Schrijf een programma
dat, gegeven een matrix met 16 getallen, berekent of het om een magisch vierkant
gaat of niet. Je mag de matrix hier direct in een variabele plaatsen en hoeft
deze dus niet op te vragen aan de gebruiker.

Hint: Gebruik aparte for-lussen om na te kijken of alle kolommen, rijen en diagonalen tot hetzelfde getal sommeren.
"""

geen_magisch_vierkant = [[16, 3, 2, 13],
                        [5, 10, 8, 11],
                        [9, 6, 7, 12],
                        [4, 15, 14, 1]]

magisch_vierkant = [[16, 3, 2, 13],
                    [5, 10, 11, 8],
                    [9, 6, 7, 12],
                    [4, 15, 14, 1]]

# Schrijf je code hieronder
column0 = []
column1 = []
column2 = []
column3 = []
column4 = []
diagonal1 = []
diagonal2 = []

if sum(magisch_vierkant[0]) == sum(magisch_vierkant[1]) == sum(magisch_vierkant[2]) == sum(magisch_vierkant[3]) == sum(magisch_vierkant[4]):
    for i in range(0,5):
        column0.append(magisch_vierkant[i][0])
        column1.append(magisch_vierkant[i][1])
        column2.append(magisch_vierkant[i][2])
        column3.append(magisch_vierkant[i][3])
        column4.append(magisch_vierkant[i][4])
    if sum(column0) == sum(column1) == sum(column2) == sum(column3) == sum(column4) == sum(magisch_vierkant[0]):
        for i in range(0,5):
            diagonal1.append(magisch_vierkant[i][i])
            diagonal2.append(magisch_vierkant[i][(-i-1)])
            if sum(diagonal1) == sum(diagonal2) == sum(column0):
                print('Dit is een magisch vierkant!')

else:
    print('Dit is geen magisch vierkant :(')


