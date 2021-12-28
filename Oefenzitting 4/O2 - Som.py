"""
Schrijf een iteratieve functie som_iteratief die de som van alle natuurlijke
getallen tot en met een gegeven getal berekent: som_iteratief(n) = 1 + 2 + 3 + ... + n.

Schrijf ook een recursieve functie som_recursief die dezelfde som berekent door
gebruik te maken van recursie.

Maak gebruik van assert statements om te controleren of je functies goed werken en
schrijf er documentatie bij.
"""


def som_iteratief(n):
    som = 0
    # voor elke waarde kleiner of gelijk aan n gaan we deze toevoegen aan de som
    for i in range(n + 1):
        som += i
    return som

def som_recursief(n):
    # Vergeet ook bij deze functie geen documentatie te schrijven
    # als n gelijk is aan 1 dan is de de som ook 1
    if n == 1:
        return 1
    else:
        # als n niet gelijk is aan 1 zullen we n toevoegen met dezelfde functie maar dan van n-1, en deze zal op zijn
        # beurt hetzelfde doen tot n = 1
        return n + som_recursief(n - 1)

def main():
    #we checken of de functies werken voor de som tot en met 15
    assert som_recursief(15) == 120
    assert som_iteratief(15) == 120
    print(som_recursief(15), som_iteratief(15))

main()


# Schrijf zelf enkele assert statements om je functies te testen
