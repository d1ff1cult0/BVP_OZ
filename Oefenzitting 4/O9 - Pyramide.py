"""
Schrijf een functie die een pyramide tekent als ze opgeroepen wordt. Deze functie
verwacht twee argumenten: als eerste de hoogte van de pyramide en als tweede een
optioneel argument dat het karakter meegeeft waarmee de pyramide getekend wordt.
Als er geen karakter wordt meegegeven bij oproep, wordt de pyramide getekend door
gebruik te maken van het + symbool.

Hint: De functie tekent de pyramide zelf en geeft geen resultaat terug.
Hint: Dit hoeft geen recursieve functie te zijn.
"""


def pyramid(height, symbol='+'):
    j = height-1
    for i in range(height):
        for n in range(j):
            print(end=" ")
        j = j-1
        for k in range(i+1):
            print(symbol+ ' ', end="")
        print("\r")


pyramid(int(input('Pyramid height: ')), str(input('Symbol: ')))
