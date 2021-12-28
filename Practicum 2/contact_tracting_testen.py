from contact_tracing_SKELET import *


def main():
    print("#############")
    print("VOORBEELD 1")
    print("#############")

    print("-- ontmoetingen registreren --")

    contact_tracing_datastructuur = initialiseer_contacttracing()

    registreer_ontmoeting(contact_tracing_datastructuur,("Pieter","Koen"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Bart","Koen", "Kim"))

    print("-- vraag ontmoetingen op --")

    if geef_alle_namen(contact_tracing_datastructuur) != {'Bart', 'Kim', 'Koen', 'Pieter'}:
        print("geef_alle_namen(contact_tracing_datastructuur) :", "expected: ","{'Bart', 'Kim', 'Koen', 'Pieter'}",
              "- Returned: ", geef_alle_namen(contact_tracing_datastructuur))

    if sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Koen")) != ['Bart', 'Kim', 'Pieter']:
        print("sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, Koen)):",
              "expected: ","['Bart', 'Kim', 'Pieter']",
              "- Returned: ", sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Koen")))

    print("-- contact gehad --")

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Pieter", 0): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Pieter", 0)!=True')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Koen", 0): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Koen", 0)!=True')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Kim", "Pieter", 1): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Kim", "Pieter", 1)!=True')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Pieter", "Kim", 1): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Pieter", "Kim", 1)!=True')

    if heeft_contact_gehad_met(contact_tracing_datastructuur, "Pieter", "Kim", 0): #False
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Pieter", "Kim", 0)!=True')

    # UITBREIDING 1

    print("## UITBREIDING 1: groter netwerk ##")
    print("-- extra ontmoetingen registreren --")

    registreer_ontmoeting(contact_tracing_datastructuur,("Pieter","Tom"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Bart", "Yana"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Yana","Wouter"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Wouter", "Bert"))
    registreer_ontmoeting(contact_tracing_datastructuur,("Koen", "Koen")) #ontmoeting met zichzelf

    print("-- vraag ontmoetingen op --")

    if geef_alle_namen(contact_tracing_datastructuur) != {'Bart', 'Bert', 'Kim', 'Koen', 'Pieter', 'Tom', 'Wouter', 'Yana'}:
        print("geef_alle_namen(contact_tracing_datastructuur) :",
              "expected: ","{'Bart', 'Bert', 'Kim', 'Koen', 'Pieter', 'Tom', 'Wouter', 'Yana'}",
              "- Returned: ", geef_alle_namen(contact_tracing_datastructuur))

    if sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Koen")) != ['Bart', 'Kim', 'Pieter']: #geen rechtstreekse contacten bijgekomen voor Koen
        print("sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, 'Koen')):",
              "expected: ","['Bart', 'Kim', 'Pieter']",
              "- Returned: ", sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Koen")))

    if sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Pieter")) != ['Koen', 'Tom']: #geen rechtstreekse contacten bijgekomen voor Koen
        print("sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, 'Pieter')):",
              "expected: ","['Koen', 'Tom']",
              "- Returned: ", sorted(geef_rechtstreekse_contacten(contact_tracing_datastructuur, "Pieter")))

    print("-- contact gehad --")

    if heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Wouter", 1): #False
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Wouter", 1)!=False')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Wouter",2): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Wouter", 2)!=True')

    if heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Bert", 2): #False
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Bert", 2)!=False')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Bert", 3): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Bert", 3)!=True')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Bert"): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Bert")!=True')

    if heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Beyonce"): #False
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Beyonce")!=False')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Koen", 0): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Koen")!=True')

    print("-- rechtstreekse besmettingen --")

    if kan_iedereen_rechtstreeks_besmetten(contact_tracing_datastructuur,["Koen", "Wouter"]): #False
        print('kan_iedereen_rechtstreeks_besmetten(contact_tracing_datastructuur,["Koen", "Wouter"])!=False')

    if not kan_iedereen_rechtstreeks_besmetten(contact_tracing_datastructuur,["Tom", "Bart", "Bert"]): #True
        print('kan_iedereen_rechtstreeks_besmetten(contact_tracing_datastructuur,["Tom", "Bart", "Bert"])!=True')

    print("-- hops --")

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Koen"])!=3:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Koen"])!=3',
              ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Koen"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Kim"])!=3:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Kim"])!=3',
              ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Kim"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Tom"])!=5:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Tom"])!=5',
              ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Tom"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bart"])!=2:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bart"])==2',
              ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bart"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bert"])!=5:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bert"])!=5',
              ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bert"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Yana"])!=3:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Yana"])!=3',
              ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Yana"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Pieter"])!=4:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Pieter"])!=4',
              ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Pieter"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter"])!=4:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter"])!=4',
              ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter", "Pieter"])!=1:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter", "Pieter])!=1',
              ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter", "Pieter"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter", "Tom"])!=2:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter", "Tom"])!=2',
              ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Wouter", "Tom"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bert", "Pieter"])!=1:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bert", "Pieter"])!=1',
              ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bert", "Pieter"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bert", "Tom"])!=2:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bert", "Tom"])!=2',
              ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Bert", "Tom"]))

    (hops, superspreaders)=hops_nodig_voor_volledig_geinfecteerde_populatie(contact_tracing_datastructuur) #(2,{'Bart'})
    if hops != 2:
        print('hops!=2', ' - output: ', hops)

    if superspreaders!={'Bart'}:
        print("superspreaders!={'Bart'}", ' - output: ', superspreaders)

    ## UITBREIDING 2 ##

    print("## UITBREIDING 2: vrijstaande ontmoeting ##")
    print("-- extra ontmoeting registreren --")
    registreer_ontmoeting(contact_tracing_datastructuur,("Ronald", "Stefan"))

    print("-- vraag ontmoetingen op --")

    if heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Ronald"): #False
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Koen", "Ronald")!=False')

    if not heeft_contact_gehad_met(contact_tracing_datastructuur, "Stefan", "Ronald"): #True
        print('heeft_contact_gehad_met(contact_tracing_datastructuur, "Stefan", "Ronald")!=True')

    print("-- hops --")
    # geen volledige infectie mogelijk

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Koen"])!=-1:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Koen"])!=-1',
              ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Koen"]))

    if hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Koen", "Stefan"])!=3:
        print('hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Koen", "Stefan])!=3',
              ' - output: ', hops_nodig_voor_geinfecteerde_populatie(contact_tracing_datastructuur,["Koen", "Stefan"]))

    (hops, superspreaders)=hops_nodig_voor_volledig_geinfecteerde_populatie(contact_tracing_datastructuur)
    if hops != -1:
        print('hops!= -1', ' - output: ', hops)

    if superspreaders!= set():
        print("superspreaders!=set()", ' - output: ', superspreaders)





# VOEG EVENTUELE EXTRA TESTEN TOE BOVEN DEZE LIJN
if __name__ == "__main__":
    main()
