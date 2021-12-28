class ScoreBlad:
    def __init__(self, naam):
        self.naam = naam
        self.scoreblad = {}

    def naam_van_student(self):
        return self.naam

    def registreer_vak(self, vak):
        if vak not in self.scoreblad:
            self.scoreblad[vak] = []
        else:
            return False

    def voeg_score_toe_voor(self, vak, punt):
        if vak not in self.scoreblad:
            self.registreer_vak(vak)
        if punt != 'NA':
            self.scoreblad[vak].append(punt)
        else:
            self.scoreblad[vak].append(0)

    def resultaten_voor(self, vak):
        if vak not in self.scoreblad:
            return None
        else:
            return self.scoreblad[vak]

    def alle_vakken(self):
        return self.scoreblad.keys()

    def hoogste_score_voor(self, vak):
        if vak in self.alle_vakken():
            return max(self.resultaten_voor(vak))
        else:
            return None

    def gemiddelde_score(self):
        scores = []
        for vak in self.alle_vakken():
            scores.append(self.hoogste_score_voor(vak))
        if not scores:
            return None
        else:
            return round(sum(scores)/len(scores))

    def aantal_pogingen_voor_gefaalde_vakken(self):
        result = []
        for vak in self.alle_vakken():
            if self.hoogste_score_voor(vak) < 10:
                result.append((vak, len(self.resultaten_voor(vak))))
        return frozenset(result)






# TESTS

resultaten = ScoreBlad("Jan")
assert resultaten.naam_van_student() == "Jan"
resultaten.registreer_vak("Methodiek van de informatica")
assert resultaten.alle_vakken() == {"Methodiek van de informatica"}
assert resultaten.resultaten_voor("Methodiek van de informatica") == []

resultaten.voeg_score_toe_voor("Methodiek van de informatica", 16)
resultaten.voeg_score_toe_voor("Methodiek van de informatica", 14)
resultaten.voeg_score_toe_voor("Toegepaste Mechanica", 10)
assert resultaten.resultaten_voor("Methodiek van de informatica") == [16, 14]
assert resultaten.resultaten_voor("Toegepaste Mechanica") == [10]
assert resultaten.alle_vakken() == {"Methodiek van de informatica", "Toegepaste Mechanica"}

# Een vak dat al geregistreerd is opnieuw toevoegen veranderd niks aan de huidige scores.
resultaten.registreer_vak("Methodiek van de informatica")
assert resultaten.resultaten_voor("Methodiek van de informatica") != []

resultaten.voeg_score_toe_voor("Analyse 2", "NA")
assert resultaten.hoogste_score_voor("Methodiek van de informatica") == 16
assert resultaten.hoogste_score_voor("Analyse 1") is None
assert resultaten.hoogste_score_voor("Analyse 2") == 0
assert resultaten.gemiddelde_score() == 9  # NA wordt als 0 gerekend.
assert resultaten.aantal_pogingen_voor_gefaalde_vakken() == frozenset([("Analyse 2", 1)])