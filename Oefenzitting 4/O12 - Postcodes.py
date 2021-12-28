"""
In de USA worden postcodes geschreven in barcodes. Elke postcode bevat vijf cijfers
en een controlecijfer, dat op een specifieke manier berekend wordt. Eerst worden de
vijf cijfers van de postcode opgeteld. Het controlecijfer is dan het cijfer dat je
bij deze som nog zou moeten optellen om tot een veelvoud van 10 te komen. Zo
sommeert de postcode 95104 bijvoorbeeld tot 19 en heeft deze als controlecijfer 1.

CONTROLECIJFER
Schrijf een functie die, gegeven een postcode, het controlecijfer berekent en
teruggeeft. Je functie maakt gebruik van hulpfuncties om het werk overzichtelijker
te houden.

BARCODE
Cijfers kunnen tot een barcode omgevormd worden door gebruik te maken van de tekens
| en :. Schrijf een functie die één cijfer omzet naar een string die de barcode
bevat op basis van de tabel op het opgaveblad.

OMZETTING
Schrijf tenslotte een functie die gebruik maakt van de eerder besproken functies
om alles samen te brengen. Deze functie krijgt als argument een postcode en
genereert een barcode voor de vijf cijfers én voor het controlecijfer. Tussen de
barcodes van de verschillende cijfers staat steeds een spatie.
"""

def controlecijfer(cijfer):
    x = [int(a) for a in str(cijfer)]
    i = 0
    digit_sum = sum(x)
    if digit_sum % 10 == 0:
        return 0
    while digit_sum % 10 != 0:
        digit_sum += i
        if digit_sum % 10 == 0:
            return i
        i += 1


def barcode(cijfer):
    x = [int(a) for a in str(cijfer)]
    for i in range(len(x)):
        if x[i] == 1:
            x.pop(i)
            x.insert(i, ':::||')
        if x[i] == 2:
            x.pop(i)
            x.insert(i, '::|:|')
        if x[i] == 3:
            x.pop(i)
            x.insert(i, '::||:')
        if x[i] == 4:
            x.pop(i)
            x.insert(i, ':|::|')
        if x[i] == 5:
            x.pop(i)
            x.insert(i, ':|:|:')
        if x[i] == 6:
            x.pop(i)
            x.insert(i, ':||::')
        if x[i] == 7:
            x.pop(i)
            x.insert(i, '|:::|')
        if x[i] == 8:
            x.pop(i)
            x.insert(i, '|::|:')
        if x[i] == 9:
            x.pop(i)
            x.insert(i, '|:|::')
        if x[i] == 0:
            x.pop(i)
            x.insert(i, '||:::')
    return x


def main():
    #postcode = input('Geef een postcode: ')
    postcode = 94835
    postcode_controlecijfer = int(str(postcode) + str(controlecijfer(postcode)))
    print(postcode_controlecijfer)
    for i in barcode(postcode_controlecijfer):
        print(i + " ", end="")

main()
