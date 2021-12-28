'''

Het 'handelsreizigersprobleem' (Eng. 'traveling salesman problem') is een probleem dat in allerlei
varianten in de echte wereld (vnl. in de logistiek) voorkomt. We beschouwen hier een eenvoudige versie.

Een handelsreiziger wordt verwacht om een aantal locaties - steden - te bezoeken. Gegeven zijn daarvoor de
afstanden tussen een aantal steden, bv.
    Tussen stad A en stad B is de afstand 12 (een eenheid is niet belangrijk).
    Tussen stad A en stad C is de afstand 24.
    Tussen stad C en stad D is de afstand 42.
    Tussen stad D en stad E is de afstand 17.
    Tussen stad E en stad A is de afstand 9.
    Tussen stad E en stad B is de afstand 15.

- We gaan ervan uit dat de afstand tussen twee steden dezelfde is in beide richtingen, d.w.z. als de afstand tussen
stad A en stad B gelijk is aan 12, dan is ook de afstand tussen stad B en stad A gelijk aan 12.

- Als er geen afstand tussen twee steden is opgegeven, betekent dat dat de handelsreiziger niet
rechtstreeks tussen die steden kan reizen. Zo kan in het voorbeeld hierboven de reiziger die start in A niet
rechtstreeds in stad D geraken, maar bv. wel via C.

- Een 'geldige route' voor de handelsreiziger is een volledige cyclus, d.w.z. een route waarbij elke stad exact één
keer wordt bezocht, behalve de stad waar de route start. De laatste stad in een geldige route moet dus steeds dezelfde
zijn als de eerste. Een geldige route in het voorbeeld van hierboven is bv. A-C-D-E-B-A.

- De lengte van een route is gelijk aan de som van de afstanden tussen de steden in een route. Een route A-C-D zou
in het voorbeeld van hierboven een lengte hebben van 66 (A-C heeft afstand 24, C-D heeft afstand 42).

Schrijf een backtracking-algoritme dat, gegeven een aantal afstanden tussen steden, nagaat of er een geldige
route voor alle steden bestaat, en zoja, de kortste geldige route als resultaat weergeeft.



Je krijgt van ons de hoofding van 1 functie, nl. handelsreizigersprobleem (zie onder). De functies om het
backtracking-algoritme te implementeren (typisch zijn dat: solve, extend, examine) definieer je zelf. Definieer
uiteraard ook andere hulpfuncties waar nuttig.


Zoals gezegd, je mag geen extra import statements aan je programma toevoegen.

'''


def examine():  # vul zelf parameters aan
    pass

def extend():   # vul zelf parameters aan
    pass

def solve():    # vul zelf parameters aan
    pass


# Deze functie is het startpunt voor je implementatie.
# @param afstanden  - een verzameling van tuples, waarbij elk tuple de afstand tussen 2 steden voorstelt
#                   - bv. { ("A", "B", 12), ("A", "C", 24), ("C", "D", 42),
#                           ("D", "E", 17), ("E", "A", 9), ("E", "B", 15) }
#                   - je mag ervan uitgaan dat deze datastructuur correct is, en dus dat elk tuple
#                       bestaat uit exact 2 strings (de steden) en 1 strikt positief geheel getal,
#                       en dat er nooit 2 tuples zullen zijn die voor dezelfde steden een afstand
#                       definiëren
# @return   - indien er geen geldige route bestaat tussen alle steden in de data-structuur 'afstanden'
#               dan geeft de functie None terug
#           - indien er wel een geldige route bestaat, dat geeft de functie de lengte van de kortste geldige route weer
def handelsreizigersprobleem (afstanden):
    pass



#################################################################################################
# Deze main-functie kan je gebruiken om zelf je programma te testen.                            #
# In deze main wordt het algoritme al voor een aantal gevallen getest.                          #
# Pas deze functie aan om functies afzonderlijk te testen, of om andere gevallen te testen.     #
# Er staan geen punten op deze main-functie.                                                    #
#################################################################################################

def main():

    voorbeeld_nr = 1
    # Voorbeeld
    afstanden = { }
    beste_route = handelsreizigersprobleem(afstanden)
    print("Voorbeeld", voorbeeld_nr, ": ", beste_route)
    assert beste_route == 0
    voorbeeld_nr += 1

    # Voorbeeld
    afstanden = { ("A", "B", 2)}
    beste_route = handelsreizigersprobleem(afstanden)
    print("Voorbeeld", voorbeeld_nr, ": ", beste_route)
    assert beste_route == 4
    voorbeeld_nr += 1

    # Voorbeeld
    afstanden = { ("A", "B", 2), ("B", "C", 3)}
    beste_route = handelsreizigersprobleem(afstanden)
    print("Voorbeeld", voorbeeld_nr, ": ", beste_route)
    assert beste_route == None
    voorbeeld_nr += 1

    # Voorbeeld
    afstanden = { ("A", "B", 12), ("A", "C", 24), ("C", "D", 42),
                  ("D", "E", 17), ("E", "A", 9), ("E", "B", 15) }
    beste_route = handelsreizigersprobleem(afstanden)
    print("Voorbeeld", voorbeeld_nr, ": ", beste_route)
    assert beste_route == 110
    voorbeeld_nr += 1

    # Voorbeeld
    afstanden = { ("A", "B", 12), ("A", "C", 24), ("C", "D", 42),
                  ("D", "E", 17), ("E", "A", 9), ("E", "B", 15),
                  ("D", "A", 2) }
    beste_route = handelsreizigersprobleem(afstanden)
    print("Voorbeeld", voorbeeld_nr, ": ", beste_route)
    assert beste_route == 110
    voorbeeld_nr += 1


# WIJZIG NIETS AAN DE LIJNEN HIERONDER
if __name__ == "__main__":
    main()
