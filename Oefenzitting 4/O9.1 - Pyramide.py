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
    middle_position = 1
    while (height - middle_position) >= 0:
        string = (height - middle_position) * " " + (1 + 2*(middle_position-1)) * symbol
        print(string)
        middle_position += 1

def main():
    pyramid(int(input('Pyramid height: ')), str(input('Symbol: ')))

main()