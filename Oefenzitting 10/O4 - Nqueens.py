# Het N Queens probleem is een heel bekend probleem in computerwetenschap- pen. 
# Gegeven een bord met dimensie NxN, geef een lijst terug met alle mogelijke
#  configuraties van de bord met N queens zonder dat de N queens elkaar kunnen aanvallen.

# Een queen kan een andere queen aanvallen als en slechts als: 
#• ze zich in dezelfde rij bevinden
#• ze zich in dezelfde kolom bevinden
#• ze zich in dezelfde diagonaal bevinden

# Hint: Aangezien dat de rijen en kolommen van de queens moeten verschillen van elkaar
# kunnen wij deze informatie gebruiken om ons te helpen met de voorstelling van onze oplossing.
# In plaats van onze oplossing voor te stellen als bijvoorbeeld een lijst van
# tuples (rijnummer, kolomnummer) kunnen wij een lijst gebruiken van lengte N met de posities
# van de lijst als kolomnummer en waarde in de lijst als rijnummer. [3,1,4,2] kan een oplossing
# voorstellen waar er een queen is op posities (3,1), (1,2), (4,3) en (2,4).

def examine():
    # Schrijf hier je functie die nakijkt of je partiële oplossing:
    # - Een acceptabele oplossing is voor het probleem (ACCEPT)
    # - Nog geen oplossing is, maar er wel nog een kan worden na uitbreiding (CONTINUE)
    # - Nooit nog een correcte oplossing kan worden voor het probleem (ABANDON)
    pass


def extend():
    # Schrijf hier je functie die een partiële oplossing uitbreidt
    pass


def solve():
    # Schrijf hier je functie die het probleem in z'n geheel oplost. Deze maakt gebruik van de examine-functie, van de
    # extend-functie en tenslotte ook van zichzelf (om de gegenereerde extensies op te lossen)
    pass
