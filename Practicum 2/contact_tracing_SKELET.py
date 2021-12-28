##########################################################
# INITIALISATIE EN REGISTRATIE IN CENTRALE DATASTRUCTUUR #
##########################################################

def initialiseer_contacttracing():
    """
    Geeft een lege datastructuur terug waarin ontmoetingen bijgehouden kunnen worden.
    """
    pass


def registreer_ontmoeting(ontmoetingen, personen):
    """
    Registreert een meeting tussen een aantal (2 of meer) personen.
    """
    pass


################
# HULPFUNCTIES #
################

def geef_rechtstreekse_contacten(ontmoetingen, persoon_X):
    """
    Geeft een lijst terug met daarin de namen van alle mensen die rechtstreeks contact gehad hebben met persoon_X.

    Elke naam komt slechts 1 keer voor.
    De volgorde is onbelangrijk.
    """
    pass


def geef_alle_namen(ontmoetingen):
    """
    Geeft een set terug met daarin alle namen van de huidige populatiegroep.

    Elke naam komt slechts 1 keer voor.
    De volgorde is onbelangrijk.
    """
    pass


def is_lid_van_populatie(ontmoetingen, persoon):
    pass


#####################################
# CONTACT TRACING ANALYSE FUNCTIES #
####################################

def heeft_contact_gehad_met(ontmoetingen, persoon_X, persoon_Y, afstand=-1):
    """
    Onderzoekt of persX in contact is geweest met persY, rechtstreeks of met maximaal 'afstand' aantal hops tussen.

    Indien afstand -1 is (default) is er geen beperking op het aantal hops.
    """
    pass


def kan_iedereen_rechtstreeks_besmetten(ontmoetingen, geinfecteerd_by_start):
    """
    Controleert of iedereen rechtstreeks besmet kan worden indien de gegeven set van personen initieel geinfecteerd bleek te zijn.
    Iedereen uit de populatie heeft met andere woorden dus minstens met 1 iemand uit de geinfecteerde set een ontmoeting gehad.

    geinfecteerd_by_start - Een set-object met de namen van de mensen die initieel geinfecteerd waren.
    """
    pass


def hops_nodig_voor_geinfecteerde_populatie(ontmoetingen, infected):
    """
    Geeft terug hoeveel hops er nodig zijn voordat de eventuele besmetting van de personen in de infected verzameling de volledige populatie hebben besmet.

    Deze functie geeft 0 terug indien de personen in infected rechtstreeks contact hebben gehad met de volledige populatie.
    Wanneer er geen volledige populatie kan geinfecteerd worden, geeft de functie -1 als resultaat.
    """
    pass


def hops_nodig_voor_volledig_geinfecteerde_populatie(ontmoetingen):
    """
    Geeft terug hoeveel hops er minimaal nodig zijn om de volledige populatie te besmetten indien 1 iemand uit de
    populatie besmet zou zijn en welke persoon of personen dit als 'superverspreider' kunnen mogelijk maken.

    De functie geeft een tuppel terug bestaande uit een cijfer dat het aantal hops weergeeft en een set waarin de namen
    van de personen zitten die als initiele verspreider tot een volledige populatiebesmetting kunnen leiden.

    Wanneer er geen volledige populatie kan besmet worden, wordt '-1' als aantal hops teruggeven, en een lege set als
    superverspreider.
    """
    pass
